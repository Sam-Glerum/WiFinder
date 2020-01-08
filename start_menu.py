import sys


stop_program = False

def menu():
    choice = input("1: start / 2: quit > ")
    
    if (choice == "start" or "1"):
        print("Running program")
    
    elif(choice == "quit" or "2"):
        sys.exit()
    else:
        print("Sorry, I don't know what that means.")