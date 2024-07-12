import time
import datetime

book_list = ["Bible", "The Headless Horseman", "The Gospel Driven Life", "On the Incarnation"]
feast: str
now = datetime.datetime.now()

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
            print(f"It's ${feast} today! This is what we have: ")
            #more coming soon

        case _:
            print("please try again")

def bot():
    choice = input("How can I help you? ")
    service(choice)
