from Getters import *
 
def Story3(debug = False):
	if debug: print("Story3 Function")
	
	print("\n")
	Name = getWord("Enter a Name: ", debug)
	Monster = getMonster("Enter a Monster: ", debug)
	Number = getNumber("Enter a number less than 20: ", debug)
	Roll = getWord("Enter a Number more than the last Number: ", debug)
	Name2 = getWord("Enter a female Name: ", debug)
	Magic = getWord("Enter a Magic Spell: ", debug)
	Dude = getWord("Enter a Male Name: ", debug)
	Animal = getAnimal("Enter an Animal: ", debug)
	
	out = "\n"
	out += "Once upon a time there was " + Name + "."
	out += "\n"
	out += Name + " and his friends were playing D&D, they were fighting a " + Monster + "."
	out += "\n"
	out += "On " + Name + "'s turn, to kill the " + Monster + " he needed to roll a " + Number + "."
	out += "\n"
	out += Name + " rolled a " + Roll + " and killed the " + Monster + "."
	out += "\n"
	out += "Next it was " + Name2 + "'s turn and they cast " + Magic + "."
	out += "\n"
	out += "The spell hit " + Dude + " and turned him into a " + Animal + "."
	if Animal == ("newt"):
		  out += "\n"
		  out += "He got better"
	else:
		out += "\n" 
		out += "Then she was put on trial as a witch" 
		out += "\n"
		out += "She was found guilty and burned at the stake"
		out += "\n"
		out += "The End"
		out += "\n"
		out += "(Hint, Think Monty python and the Holy Grail)"
		
		
	return out


	
