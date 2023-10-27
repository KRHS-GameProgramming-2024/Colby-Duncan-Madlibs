def getMenuOption(debug = False):
    if debug: print("getMenuOption Function")

    goodInput = False
    
    while not goodInput:
        option = input("Please selest an option: ")
        option = option.lower()
        
        
        if (option == "q" or 
        option == "quit" or 
        option == "esc"):
            option = "q" 
            goodInput = True
            
        elif (option == "1" or 
        option == "one" or 
        option == "uno"): 
            option = "1" 
            goodInput = True    
        else: 
            print("please enter a valid choice")
            
        return option

def getWord(prompt, debug = False):
    if debug: print("getWord Function")

    goodInput = False
    
    while not goodInput:
        word = input(prompt)
        goodInput = True
        if isSwear(word, debug):
            goodInput = False
            print("Don't say naughty words >:(")
            
    return word

def getShop(prompt, debug = False):
    if debug: print("getShop Function")

    goodInput = False
    
    while not goodInput:
        word = input(prompt)
        goodInput = True
        if isSwear(word, debug):
            goodInput = False
            print("Don't say naughty words >:(")
            
    return word

def getShady(prompt, debug = False):
    if debug: print("getShady Function")

    goodInput = False
    
    while not goodInput:
        word = input(prompt)
        goodInput = True
        if isSwear(word, debug):
            goodInput = False
            print("Don't say naughty words >:(")
            
    return word

def getBuisness(prompt, debug = False):
    if debug: print("getBuisness Function")

    goodInput = False
    
    while not goodInput:
        word = input(prompt)
        goodInput = True
        if isSwear(word, debug):
            goodInput = False
            print("Don't say naughty words >:(")
            
    return word
    


def getAnimal(prompt, debug = False):
    if debug: print("getAnimal Function")

    goodInput = False
    
    goodAnimals = ["frog",
                   "worm",
                   "slug",
                   "mouse",
                   "racoon",
                   "hedgehog",
                   "squirrel",
                   "salamander",
                   "newt",
                   "opossum",
                   "mole"
                   "shrew",
                   "badger",
                   "rabbit",
                   "bunny",
                   "owl",
                   "duck",
                   "goose",
                   "crow",
                   "raven",
                   "swallow",
                   "woodpecker",
                   "starling",
                   ]
    
    while not goodInput:
        word = input(prompt)
        goodInput = True
        if isSwear(word, debug):
            goodInput = False
            print("Don't say naughty words >:(")
        elif word.lower() not in goodAnimals:
            goodInput = False
            print("Idk that animal. (or its not a small animal that would be found in a european forest)")
            
    return word
    
def getNumber(prompt, debug = False):
    if debug: print("getNumber Function")

    goodInput = False
    
    while not goodInput:
        word = input(prompt)
        goodInput = True
        if isSwear(word, debug):
            goodInput = False
            print("Don't say naughty words >:(")
            
    return word

def getSpell(prompt, debug = False):
    if debug: print("getSpell Function")

    goodInput = False
    
    while not goodInput:
        word = input(prompt)
        goodInput = True
        if isSwear(word, debug):
            goodInput = False
            print("Don't say naughty words >:(")
            
    return word

def getDeath(prompt, debug = False):
    if debug: print("getDeath Function")

    goodInput = False
    
    while not goodInput:
        word = input(prompt)
        goodInput = True
        if isSwear(word, debug):
            goodInput = False
            print("Don't say naughty words >:(")
            
    return word

def isSwear(word, debug = False):
    if debug: print("isSwear Function")
    if word.lower() in swearList:
        return True
    else:
        return False

swearList = ["fuck",
             "shit",
             "damn",
             "ass",
             "bitch",
             "penis",
             "dick",
             "cock",
             "cum",
             "hell",
             "heck",
             "frick",
             "poop",
             "pee",
             "fortnite",
             "roblox",
             "france",
             "french",
             "creeper",
             "piss",
             "retard",
             "fagot",
             "semen",
             "weiner",
             "vagina",
             "butt",
             "pussy",
             "nigger",
             "nigga",
             "porn",
             "hentai",
             "69",
             "420",
]

