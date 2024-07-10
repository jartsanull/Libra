import time

book_list = ["Bible", "The Headless Horseman", "The Gospel Driven Life", "On the Incarnation"]

def service(choice: str):
    match (choice):
        case "recommendations":
            print("Oh, I can recommend you these books:")
            print()
            print("\n".join(book_list))

        case "inquire":
            print() #there should another match syntax soon

        case "assistance", "assist":
            print("Sure, how can I assist you?")

        case _:
            print("please try again")

def bot():
    choice = input("How can I help you? ")
    service(choice)
