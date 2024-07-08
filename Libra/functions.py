#import Libra
import time

book_list = ["Bible", "The Headless Horseman", "The Gospel Driven Life", "On the Incarnation"]

def service(choice: str):
    match (choice):
        case "recommendations":
            print("Oh, I can recommend you these books:")
            print()
            print("\n".join(book_list))

def bot():
    choice = input("How can I help you? ")
    service(choice)
