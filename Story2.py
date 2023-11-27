from getters import*

def Story2(debug = False):
    if debug: print("Story2 Function")
    
    print("\n")
    name1 = getWord("Enter a Name: ", debug)
    adj1 = getWord("Enter an Adj: ", debug)
    industry1 = getWord("Enter a Noun plural: ", debug)
    accident1 = getBob("Enter an Adj: ", debug)
    item1 = getWord("Enter a Noun plural: ", debug)
    emotion1 = getWord("Enter an Emotion: ", debug)
    adj2 = getWord("Enter an Adj: ", debug)
    death1 = getWord("Enter a Noun: ", debug)
    
    out = "\n"
    out += "Once upon a time there was " + name1 + "."
    out += "\n"
    out += name1 + " owned a " + adj1 + " buisness, " + name1 + "'s " + industry1 + "."
    out += "\n"
    out += name1 + "'s " + industry1 + " had a " + accident1 + " accident while shipping " + item1 + "."
    out += "\n"
    out += name1 + " recived a phone call about the accident, he was " + emotion1 + "!"
    out += "\n"
    out += name1 + " then made a new policy, no more " + adj2 + " shipping!"
    out += "\n"
    out += name1 + " then died from " + death1 + " a year later."
    out += "\n"
    out += "The End"
    
    return out
