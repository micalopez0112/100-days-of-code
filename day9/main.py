programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again."
}

# empty_list = []

# empty_list.append("Value")
# print(empty_list)

# nested_list = [[1, 2, 3], 4, 5]

print(programming_dictionary["Bug"])

# initialize empty dictionary

empty_dictionary = {}

# add key and value

empty_dictionary["Key"] = "Value"
print(empty_dictionary)

#clear dictionary

programming_dictionary.clear()
programming_dictionary = {}
print(programming_dictionary)

#edit dictionary

programming_dictionary["Bug"] = "A moth in your computer"
print(programming_dictionary)

# loop through dictionary

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

# loop through both key and value

for key, value in programming_dictionary.items():
    print(key)
    print(value)

#nested dictionary

capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

#nesting a dictionaries in a list

travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]

#nesting a dictionary in a dictionary

travel_log = {
    "France": {"visits": 12, "cities": ["Paris", "Lille", "Dijon"]},
    "Germany": {"visits": 5, "cities": ["Berlin", "Hamburg", "Stuttgart"]},
}

#nesting a list in a dictionary

travvel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

print(travvel_log["France"][2]) #print Dijon

country_travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5
    },
}

print(country_travel_log["Germany"]["cities_visited"][2])


fruits = {"Strawberries": 5, "Nectarines": 2, "Apples": 3}

most_fruit = max(fruits.values())
print(most_fruit)

fruits_mayority = max(fruits, key=fruits.get)
print(fruits_mayority)