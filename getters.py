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
  
  
def getNumber(prompt, debug = False):
    if debug: print("getWord Function")

    goodInput = False
    
    while not goodInput:
       word = input(prompt)
       goodInput = True
       if isSwear(word, debug):
           goodInput = False
           print("Don't say naughty words >:(")
       elif word.lower() not in numberList:
           goodInput = False
           print("Idk that Number")
            
    return word

def isNumber(word, debug = False):
	if debug: print("isNumber Function")
	if word.lower() in numberList:
		return True
	else:
		return False



numberList = ["1",
			  "2",
			  "3",
			  "4",
			  "5",
			  "6",
			  "7",
			  "8",
			  "9",
			  "10",
			  "11",
			  "12",
			  "13",
			  "14",
			  "15",
			  "16",
			  "17",
			  "18",
			  "19",
			  "20",
			  "21",
			  "22",
			  "23",
			  "24",
			  "25",
			  "26",
			  "27",
			  "28",
			  "29",
			  "30",
			  "31",
			  "32",
			  "33",
			  "34",
			  "35",
			  "36",
			  "37",
			  "38",
			  "39",
			  "40",
			  "41",
			  "42",
			  "43",
			  "44",
			  "45",
			  "46",
			  "47",
			  "48",
			  "49",
			  "50",
			  "51",
			  "52",
			  "53",
			  "54",
			  "55",
			  "56",
			  "57",
			  "58",
			  "59",
			  "60",
			  "61",
			  "62",
			  "63",
			  "64",
			  "65",
			  "66",
			  "67",
			  "68",
			  "70",
			  "71",
			  "72",
			  "73",
			  "74",
			  "75",
			  "76",
			  "77",
			  "78",
			  "79",
			  "80",
			  "81",
			  "82",
			  "83",
			  "84",
			  "85",
			  "86",
			  "87",
			  "88",
			  "89",
			  "90",
			  "91",
			  "92",
			  "93",
			  "94",
			  "95",
			  "96",
			  "97",
			  "98",
			  "99",
			  "100",
			  "101",
			  "102",
			  "103",
			  "104",
			  "105",
			  "106",
			  "107",
			  "108",
			  "109",
			  "110",
			  "111",
			  "112",
			  "113",
			  "114",
			  "115",
			  "116",
			  "117",
			  "118",
			  "119",
			  "120",
			  "121",
			  "122",
			  "123",
			  "124",
			  "125",
			  "126",
			  "127",
			  "128",
			  "129",
			  "130",
			  "131",
			  "132",
			  "133",
			  "134",
			  "135",
			  "136",
			  "137",
			  "138",
			  "139",
			  "140",
			  "141",
			  "142",
			  "143",
			  "144",
			  "145",
			  "146",
			  "147",
			  "148",
			  "149",
			  "150",
			  "151",
			  "152",
			  "153",
			  "154",
			  "155",
			  "156",
			  "157",
			  "158",
			  "159",
			  "160",
			  "161",
			  "162",
			  "163",
			  "164",
			  "165",
			  "166",
			  "167",
			  "168",
			  "170",
			  "171",
			  "172",
			  "173",
			  "174",
			  "175",
			  "176",
			  "177",
			  "178",
			  "179",
			  "180",
			  "181",
			  "182",
			  "183",
			  "184",
			  "185",
			  "186",
			  "187",
			  "188",
			  "189",
			  "190",
			  "191",
			  "192",
			  "193",
			  "194",
			  "195",
			  "196",
			  "197",
			  "198",
			  "199",
			  "200",
]
            
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
                   "bob",
                   ]
   
    while not goodInput:
        word = input(prompt)
        goodInput = True
        if isSwear(word, debug):
            goodInput = False
            print("Don't say naughty words >:(")
        elif word.lower() not in goodAnimals:
            goodInput = False
            print("Idk that animal.")
            
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

