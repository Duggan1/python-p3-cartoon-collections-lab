def roll_call_dwarves(dwarfs):
    count = 1
    for dwarf in dwarfs:
        print(f"{count}. {dwarf}")
        count += 1

def summon_captain_planet(oldL):
    newL = []
    for word in oldL:
        newS = f"{word.capitalize()}!"
        newL.append(newS)
    return newL

def long_planeteer_calls(daList):
    for daWord in daList:
        if len(daWord) > 4:
            return True
    return False 

def find_the_cheese(daFood):
    daCheeses = ["cheddar", "gouda", "camembert"]

    for item in daFood:
        if item in daCheeses:
            return item 
