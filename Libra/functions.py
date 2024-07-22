import time
import datetime
from datetime import date

book_list = ["Bible", "The Headless Horseman", "The Gospel Driven Life", "On the Incarnation"]
feast = ["Easter", "Christmas", "New Year", "Women's Day", "Men's Day"]
feast_now: str
now = date.today()


def services(choice: str):
    match (choice):
        case "recommendations":
            print("Oh, I can recommend you these books:")
            print()
            print("\n".join(book_list))

        case "inquire":
            print() #there should another match syntax soon

        case "assistance" | "assist":
            print("Sure, how can I assist you?")

        case "event":
            print(f"It's ${feast_now} today! This is what we have: ")
            #more coming soon

        case _:
            print("Excuse me?")

def bot():
    choice = input("How can I help you? ")
    services(choice)

#print(now) # <- nvm that, just testing :)
