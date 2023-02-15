#lists
#sets
#dictionaries
#tuples

office_supplies = {"Sticky notes", "pens", "pencils", "tape", "staples"}
print(id(office_supplies))
print(office_supplies)
mixed_set = {"100", "erasers", 39, False}
print (mixed_set)
office_supplies = {"Sticky notes", "pens", "pens", "tape", "staples"}
print(office_supplies)
print(id(office_supplies))
office_supplies.update(mixed_set)
print(office_supplies)
print (mixed_set)
print(id(office_supplies))
print(mixed_set)


veggies = ["artichoke", "arugala", "beet"]
print(veggies[1])
print(veggies[-1])
print(veggies[1:])
print(veggies[0:1])
print(veggies[:2])
print(veggies[:3])
print(id(veggies))
veggies[0] = "Bok Choy"
print(veggies)
print(id(veggies))
#fruit = ("banana", "apple", "strawberry")
fruit = ["banana", "apple", "strawberry"]
veggies.extend(fruit)
print(veggies)
veggies.append("grape")
print(veggies)
# veggies.pop()
# veggies.pop()
veggies.pop(3)
print(veggies)
veggies.insert(2, "endive")
print(veggies)
veggies.remove("apple")
print(veggies)
print(veggies.index("Bok Choy"))
print(veggies)
#print(veggies.index("Jason")) will error if not found
veggies.append("Wonder Woman")
veggies.append("Wonder Woman")
print(veggies)
veggies.append("Potato")
veggies.append("Potato")
veggies.append("Potato")
veggies.append("Potato")
print(veggies.count("potato"))
print(veggies)
veggies.sort()
print(veggies)
veggies_copy = veggies.copy()
print(veggies_copy)
veggies.clear()
print(veggies)

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

print(monthConversions.get("Dec", "not a value for this key"))
print(monthConversions.get("Phone", "not a key"))
print(monthConversions["Nov"])

numbers = {
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine"
}

print(numbers[8])

dice_rolls = (3, 6, 9)
print(dice_rolls)

dice_rolls_plays = [(3, 6, 9), (8, 9), (3, 4, 10, 2)]
print(dice_rolls_plays)

dice_rolls_plays.pop()
dice_rolls_plays.pop()
#dice_rolls_plays.pop()
print(dice_rolls_plays)