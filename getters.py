def getMenuOption(debug = False):
    if debug: print("getMenuOption Function")

    goodInput = False
    
    while not goodInput:
        option = input("Please select an option: ")
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
            
        elif (option == "2" or 
        option == "two" or 
        option == "dos"): 
            option = "2" 
            goodInput = True
        
        elif (option == "3" or 
        option == "three" or 
        option == "tres"): 
            option = "3" 
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
  
def getBob(prompt, debug = False):
	if debug: print("getBob Function")
    
	goodInput = False
    
    
    
	while not goodInput:
		word = input(prompt)
		goodInput = True
		if isBob(word):
			goodInput = False
			print("try something else")
            
        
	return word
    
def isBob(word, debug = False):
    if debug: print("isBob Function")
    if word.lower() in bobList:
        return True
    else: 
        return False   
        
bobList = ["accident",           
           "people",
           "meth",
           "cocaine",
           "weed",
           "cat",
           "dog",          
 ]   

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
                   "cat",
                   "dog",
                   "bird",
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

def getMonster(prompt, debug = False):
    if debug: print("getMonster Function")

    goodInput = False
    
    goodMonsters = ["dragon",
                    "orc",
                    "ogre",
                    "titan",
                    "cyclops",
                    "zombie",
                    "skeleton",
                    "spider",
                    "thief",
                    "guard",
                    "castle guard",
                    "goblin",
                    "gremlin",
                    "mimic",
                    "werewolf",
                    "vampire",
                    "witch",
                    "worlock",
                    "gargoyle",
                    "monster",
                    "minotaur",
                    "mummy",
                    "wyvern",
                    ]
    
    while not goodInput:
        word = input(prompt)
        goodInput = True
        if isSwear(word, debug):
            goodInput = False
            print("Don't say naughty words >:(")
        elif word.lower() not in goodMonsters:
            goodInput = False
            print("Idk that Monster")
            
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
             "jiggaboo",
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

