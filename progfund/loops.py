# For loops
'''
for index in range(10):
    print(index)

for index in range(2, 3):
    print(index)

superheroes = ['Superman', 'Batman', 'Catwoman']
for index in range(len(superheroes)):
    print(superheroes[index])


for index in range(5):
    if index == 0:
        print("This is the maiden voyage")
    else:
        print("You are beginning a new flight")

num_list = [1, 2, 3]
alpha_list = ['a', 'b', 'c']

for number in num_list:
    print(number)
    for letter in alpha_list:
        print('------' + letter)


# while loop
# as long as a condition is true, loop

i = 1
while i <= 10:
    print(i)
    i += 1
print("done with loop.")


# guessing game
true_age = "29"
guess = ""

while guess != true_age:
    guess = input("How old do you think I am?")

print("You Win")
'''



# Let's Improve the game with a limit
true_age = "29"
guess = input("How old do you think I am?") # Priming Read
guess_count = 0
guess_limit = 4
out_of_guessing = False

while guess != true_age and not(out_of_guessing):
    if guess_count < guess_limit:
        guess = input("Try again, How old do you think I am? You have " + str(guess_limit) + " more guesses.   ")
        guess_count += 1
    else:
        out_of_guessing = True
        if out_of_guessing:
            print("Out of guesses, You Lose!!!")
            break
else:
    print("You win!!!!!")


# nested while loop
i = 1
while i <= 3:
    print(i, "outer loop is executed")
    j = 1
    while j <= 3:
        print(j, "_____________innder loop is executed")
        j += 1
    i += 1;

number = 0
while True:
    print(number)
    number = number + 1
    if number > 5000:
        print(number)
        break



number_grid = [
    [1,2,3]
    [4,5,6]
    [7,8,9]
    [0]
]


# print(number_grid[2][2])

# for row in number_grid:
    # print(row)

for row in number_grid:
    for col in row:
        print(col)