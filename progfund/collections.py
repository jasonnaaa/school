#lists
#tuples
#dictionaries
#sets

#arraya

superheros = ["Superman", "Catwoman", "Spiderman"]
print(superheros)
print(superheros[1])
print(superheros[-2])
print(superheros[1:])
print(superheros[0:2])
print(superheros[:3])

superheros = ["Superman", "Catwoman", "Spiderman"]
superheros[0] = "Superwoman"
print(superheros)

#append
superheros = ["Superman", "Catwoman", "Spiderman"]
supervillains = ("Dr. Doom", "Loki", "Green Goblin")
superheros.extend(supervillains)
print(superheros)

superheros.append("Wonder Woman")
print(superheros)

superheros.pop(3)
print(superheros)

superheros.pop()
print(superheros)

superheros.insert(2, "Venom")
print(superheros)

superheros.remove("Venom")
print(superheros)


superheros = ["Dr. Doom", "Loki", "Green Goblin"]
print(superheros.index("Loki"))

superheros.append("Wonder Woman")
superheros.append("Wonder Woman")
print(superheros)

print(superheros.count("Wonder Woman"))




superheros = ["Dr. Doom", "Loki", "Green Goblin"]
superheros.sort()
print(superheros)

superheros_copy = superheros.copy()
print(superheros)


superheros = ["Dr. Doom", "Loki", "Green Goblin"]
print(superheros)
superheros.clear()
print(superheros)


#tuples
dice_rolls = (3, 6, 9)
print(dice_rolls)

# cant change, immutable
# dice_rolls[1] = 8

# cant use pop() with a tuple
# dice_rolls.pop(
# print(dice_rolls)

# list of tuples
dice_rolls_plays = [(3, 6, 9), (8, 9), (3, 4, 10, 2)]
print(dice_rolls_plays)


dice_rolls = (3, "cow", 9)
print(dice_rolls)

monthConversions = {
    "Jan": "January",
    "Feb": "Febuary",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "Novemeber",
    "Dec": "December"
}

print(monthConversions["Nov"])

print(monthConversions.get("Gir", "not a vlue key"))

#set

soft_drinks = {"Coke", "Pepsi", "Root Beer", "Coke"}
print(soft_drinks)

mixed_set = {"Coke", "Pepsi", "Root Beer", "Sunkist", "Coke", 39, False}
print(mixed_set)

soft_drinks.update(mixed_set)
print(soft_drinks)
