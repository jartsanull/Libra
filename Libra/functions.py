import time
import datetime
from datetime import date

book_list = ["Clean Code", "Bible", "The Headless Horseman", "On the Incarnation"]  #<--- temporary storage
feast = ["Easter", "Christmas", "New Year", "Women's Day", "Men's Day"]
feast_now: str
now = date.today()

def services(choice: str):
    match (choice):
        case 1 if "recommendations" in choice:
            print("Oh, I can recommend you these books:")
            print()
            print("\n".join(book_list))

        case 2 if "inquire" in choice or "inquiry" in choice:
            print("Hmmm... Let me see if we have it\n") #not done yet
            time.sleep(1500)
            print("Please wait...")

        case 3 if "assistance" in choice or "assistance" in choice:
            print("Sure, how can I assist you?")

        case "event":
            print(f"It's ${feast_now} today! This is what we have: ")
            #more coming soon

        case _:
            print("Excuse me? ")

def bot():
    choice = input("How can I help you? ")
    services(choice)

#print(now) # <- nvm that, just testing :)
