import sys

class StartMenu():
    stop_program = False

    def menu(self):
        choice = input("1: start / 2: quit > ")
        if choice == "start" or "1":
            print("Running program")
        
        elif choice == "quit" or "2":
            quit()
            sys.exit()
        else:
            print("Sorry, I don't know what that means.")
            self.menu()

    def quit(self):
        stop_program = True
        return stop_program