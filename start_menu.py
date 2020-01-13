import os
import sys

from interface_selector import InterfaceSelector

class StartMenu():
    
    def __init__(self):
        self.interface_selector = InterfaceSelector()

    def menu(self):
        choice = input("1: start / 2: quit > ")
        if choice == "start" or choice == "1":
            os.system('clear')
            self.interface_selector.menu()
        
        elif choice == "quit" or choice == "2":
            print("Exiting program, goodbye!")
            sys.exit()
        else:
            print("Sorry, I don't know what that means.")
            self.menu()