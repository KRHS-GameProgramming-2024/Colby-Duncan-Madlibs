from screens import *
from getters import *
from story1 import *
from Story2 import *

def madlibs(debug = False):
    if debug: print("welcome to madlibs debugging")

    print(TitleScreen(debug))
    input('Press "Enter" to continue: ')
    
    done = False
    
    while not done:
        print(MainMenu(debug))
        choice = getMenuOption(debug)
        
        if choice == "q":
            exit();
        elif choice == "1":
            print(story1())
            print("\n")
            input('Press "Enter" to continue.')
        elif choice == "2":
            print(Story2())
            print("\n")
            input('Press "Enter" to continue.')



madlibs(True)
