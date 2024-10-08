import json
import random
import time
import datetime
from datetime import date



'''Tämä tiedosto sisältää botin toimintoja päätiedostolle''' 

#Jotta kirjoja ja päivämääriä voitaisiin näyttää, ne pitää tuoda tänne toisesta tiedostosta
with open("data.json", "r") as file:
    data = json.load(file)

book_list = data["book_list"] 
feast = data["feast"]
feast_now: str
elaborations = data["elaborations"]
now = date.today()

def services(choice: str):
    match (choice):
        case "recommendations" if "recommendations" in choice:
            print("Oh, I can recommend you these books:")
            print()
            print("\n".join(book_list))

        case "inquire" | "inquiry" if "inquire" in choice or "inquiry" in choice:
            print("Hmmm... Let me see if we have it") #not done yet, need to add database and functions
            time.sleep(5)
            print("Please wait...")

        case "assistance" | "assist" if "assistance" in choice or "assist" in choice:
            print("Sure, how can I assist you?")  #this is not the assistance you imagine

        case "event":
            print(f"It's ${feast_now} today! This is what we have thematically: ")
            match (feast_now):        #still unfinished
                case "New Year":
                    print()
                case "Easter":
                    print()
                case "1st May" | "First May" if "1st May" in feast_now or "First May" in feast_now:
                    print()
                case "Mother's Day":
                    print()
                case "Father's Day":
                    print()
                case "Christmas":
                    print()

        case "exit":
            exit()

        case _:
            print(random.choice(elaborations))

def bot():
    choice = input("How can I help you?\n")
    print()
    services(choice)

#print(now) # <- nvm that, just testing :)
