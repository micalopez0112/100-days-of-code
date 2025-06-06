from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")

web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")

titles = soup.select(".content_content__i0P3p > h2 > strong")

title_texts = [title.getText() for title in titles]
titles_result = list(reversed(title_texts))
print(titles_result)

with open("output.txt", "w") as f:
    f.write("Titles:\n" + "\n".join(titles_result))