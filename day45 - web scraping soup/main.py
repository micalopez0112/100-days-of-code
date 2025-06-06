from bs4 import BeautifulSoup

# with open("website.html", encoding="utf-8") as file:
#     contents = file.read()
    
# soup = BeautifulSoup(contents, "html.parser")
# print(soup.title.string)

# all_anchor_tags = soup.find_all("a")
# for tag in all_anchor_tags:
#     print(tag.getText())
#     print(tag.get("href"))
# print(all_anchor_tags)

# heading = soup.find(name="h1", id="name")
# print(heading.getText())

# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.getText())

# class_is_heading = soup.find_all( class_="heading")
# print(class_is_heading)

# h3_heading = soup.find(name="h3", class_="heading")
# print(h3_heading.get("class"))

# name = soup.select_one(selector="#name")
# print(name)

# form_tag = soup.find("input")
# max_length = form_tag.get("maxlength")
# print(max_length)

#########################################

import requests

response = requests.get("https://news.ycombinator.com/")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

# article_tag = soup.select_one('.titleline > a')
# article_text = article_tag.getText()
# article_link = article_tag.get("href")
# article_upvote = soup.select_one('.subtext > span > span').getText()

# print(article_text)
# print(article_link)
# print(article_upvote)

articles = soup.select('.titleline > a')
# article_text = article_tag.getText()
# article_link = article_tag.get("href")
# article_upvote = soup.select_one('.subtext > span > span').getText()

# print(article_text)
# print(article_link)
# print(article_upvote)

# print(articles)

article_texts = [article.getText() for article in articles]
article_links = [article.get("href") for article in articles]

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)

print(article_texts[largest_index])
print(article_links[largest_index])
print(article_upvotes[largest_index])