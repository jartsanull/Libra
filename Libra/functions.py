import json
import time
import datetime
from datetime import date

with open("data.json", "r") as file:
    data = json.load(file)

book_list = data["book_list"] 
feast = data["feast"]
feast_now: str
now = date.today()

def services(choice: str):
    match (choice):
        case "recommendations" if "recommendations" in choice:
            print("Oh, I can recommend you these books:")
            print()
            print("\n".join(book_list))

        case "inquire" | "inquiry" if "inquire" in choice or "inquiry" in choice:
            print("Hmmm... Let me see if we have it") #not done yet
            time.sleep(5)
            print("Please wait...")

        case "assistance" | "assist" if "assistance" in choice or "assist" in choice:
            print("Sure, how can I assist you?")

        case "event":
            print(f"It's ${feast_now} today! This is what we have: ")
            #more coming soon

        case _:
            print("Excuse me? Could ")

def bot():
    choice = input("How can I help you? ")
    print()
    services(choice)

#print(now) # <- nvm that, just testing :)
