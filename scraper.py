import requests
from bs4 import BeautifulSoup
import random
import re
import textwrap

# Tracks the page of the website.
x = 0
# Stores every unique tag of all quotes.
all_tags = []
# Loops through all websites pages.
for i in range(0,10):
    # The url of the website.
    url = "https://quotes.toscrape.com/page/" + str(x) + "/"
    #  Request the webpage from the internet
    response = requests.get(url)
    # Turn the HTML code of the page into something Python can navigate
    soup = BeautifulSoup(response.text, 'html.parser')
    # Finds the container where the quote text are stored.
    container  =  soup.find_all('div', class_='quote')

    # Loops through the entire quotes found on each page.
    for quote in container:
        # Temporarily stores the tags.
        keywords = []
        # Places each unique tag in the variable all tags.
        for tag in quote.find_all('a'):
            if tag not in all_tags and tag.text != "(about)":
                all_tags.append(tag.text)


    x += 1

print("Menu:")
print("[1] List all tags")
print("[2] Pick how many tags to choose from")
print("[3] Pick random tag")
choice = int(input("Enter your choice: "))

# Prints all tag
if choice == 1:
    # Loops until a valid tag has been entered.
    while True:
        print(all_tags)
        choice = input("Choose a tag: ")
        if choice not in all_tags:
            print("Invalid choice")
        else:
            break
# Prints tag, in ranges that the user chooses
elif choice == 2:
    temp_tags = []
    number = input("How many tags: ")
    # Loops through the number of choice.
    for i in range(0,int(number)):
        tag = random.choice(all_tags)
        if tag not in temp_tags:
            temp_tags.append(tag)
    # Loops until a valid tag has been entered.
    while True:
        print(temp_tags)
        choice = input("Choose a tag: ")
        if choice not in temp_tags:
            print("Invalid choice")
        else:
            break
# Prints a random quote.
elif choice == 3:
    choice = random.choice(all_tags)


# Loops until a quote found within the tag has been selected.
while True:
    url = "https://quotes.toscrape.com/page/" + str(random.randint(1, 10)) + "/"
    #  Request the webpage from the internet
    response = requests.get(url)
    # Turn the HTML code of the page into something Python can navigate
    soup = BeautifulSoup(response.text, 'html.parser')

    # Finds all the tags of the same name chosen by the user.
    text_all = soup.find_all(string=re.compile(choice))
    if text_all:
        break

# Chooses a random quote.
text = random.choice(text_all)
# Finds the parent container of the quote.
container_inc = text.find_parent("div")
# Finds the grandparent of the parent tag of the quote.
container = container_inc.find_parent("div")
# Finds the container of the quote containing text.
quote = container.find("span", class_="text")
# Cleans the text inside the container.
quote = textwrap.fill(quote.text)

print("Quote: ")
print(quote)
print("Author: ")

# Finds the container of the author name.
author = container.find("small", class_="author")
print(author.text)


choice = input("Want to know more about the author [y/n]: ")
if choice == "y":
    link = container.find("a")["href"]

    url ="https://quotes.toscrape.com" + str(link)
    #  Request the webpage from the internet
    response = requests.get(url)
    # Turn the HTML code of the page into something Python can navigate
    soup = BeautifulSoup(response.text, 'html.parser')

    # Finds the container of the author description.
    description = soup.find("div", class_="author-description")
    # Cleans the text inside the container of the author description.
    description = textwrap.fill(description.text)
    print(description)




