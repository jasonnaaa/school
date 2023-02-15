# filtering with list
from itertools import permutations
from itertools import combinations
letter = "J"
friend_list = ["Michael", "Jim", "Pam", "Kelly", "Stanley", "Dwight"]

for i in friend_list:
    index = friend_list(index(i))
    selected = friend_list[index].startswith(letter)
    if selected == True:
        print(friend_list[index])

print(', '.join([i for i in friend_list if i.startswith(letter)]))

actor_list = ['Steve', 'John', 'Jenna', 'Mindy', 'Leslie', 'Rainn']

casting = list(zip(actor_list, friend_list))
print(casting)

# we could insert this list of tuples into a table, likely with keys
# sql = "INSERT INTO casting (actor, role) VALUES (%s, %s)"
# val = casting
# mycursor.executemany(sql, val)
# mydb.commit()

original_list = [1, 2, 3, 4, 5]
reversed_list = original_list[::-1]
print(reversed_list)

if 8 in original_list:
    print("yes")
else:
    print("no")

programs = ['IENG', 'MENG', 'SENG', 'EENG', 'EENG']
majors = set(programs)
print(majors)

programs = ['IENG', 'MENG', 'SENG', 'EENG', 'EENG']
print(max(majors, key=programs.count))

x = [True, True, True]
if any(x):
    print("At least one true")
if all(x):
    print("Not one false")
if any(x) and not all(x):
    print("At least one true and one false")

Dunwoody = ['born', 'to', 'do']
print('born' in Dunwoody)
print('nothing' in Dunwoody)
