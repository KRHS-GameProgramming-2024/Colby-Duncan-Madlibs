from Getters import * 

def Story1(debug = False):
    if debug: print("story1 Function")

    print("\n")
    wizardFrogName = getWord("Enter a male name: ", debug)
    shopName = getWord("Enter a shop name: ", debug)
    shadyfrogName = getWord("Enter the name of a shady frog: ", debug)
    frogbuisnessName = getWord("Enter the name of a buisness: ", debug)
    animalName = getAnimal("Enter an animal: ", debug)
    number1 = getNumber("Enter a number thats more than 1: ", debug)
    spellName = getWord("Enter the name of a magic spell: ", debug)
    causeofDeath = getWord("enter the cause of death for the shady frog: ", debug)
    
    out = "\n"
    out += "Once upon a time there was a frog, a wizard frog. his name was " + wizardFrogName + "."
    out += "\n"
    out += "He was living his life selling potions and spellbooks to aspiring young frog mages, his shop was called: " "\n" + wizardFrogName + "'s " + shopName + "."
    out += "\n"
    out += "One day a shady frog entered " + wizardFrogName + "'s " + 'shop. "Two Invisibility potions please." he said as he smacked 5 gold coins down on the counter'
    out += "\n"
    out += '"Coming right up! "' + wizardFrogName + " said."
    out += "\n"
    out += "you don't plan on doing anything shady with these potions do you? said " + wizardFrogName
    out += "\n"
    out += "nope, said the shady frog."
    out += "\n"
    out += "The name's " + shadyfrogName + "."
    out += "\n"
    out += "I work at " + frogbuisnessName + ". I need the potions to scare off some " + animalName + "s that keep stealing from me."
    out += "\n"
    out += "Oh, said " + wizardFrogName
    out += "\n"
    out += "How many are there? "
    out += number1 + " said " + shadyfrogName + "."
    out += "\n"
    out += "you're going to need more than just invisbilty potions to deal with that many."
    out += "\n"
    out += "Let me get you the spellbook for " + spellName + ", " + wizardFrogName + " said as he walked into the back room." 
    out += "\n"
    out += "Thank you! said " + shadyfrogName + "."
    out += "\n"
    out += "Then he died of " + causeofDeath + " from the " + animalName + "s"
    
    return out
