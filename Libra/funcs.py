import Libra
from Libra.Libra import book_list
import time

def service(choice: str):
    match(choice):
        case "recommendation":
            print("Oh, I can recommend you these books:")
            print(book_list)

def bot():
