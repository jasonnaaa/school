'''Strings
numbers
variables
user input
comments
Escaping a character
built-in Python functions
user-defines python functions'''

string_example = "i forgot to capitalize this string!"
# print (string_example.capitalize())

# x = string_example.capitalize()
# print(x)

print(string_example.capitalize().replace("forgot", "remembered"))

new_string_example = "How much wood can a woodchuck chuck if a woodchuck could chuck wood?"

print(new_string_example.count("wood"))
print(new_string_example.count("chuck"))

sentence = "Joel Jones was present when  the crime occurred. Mr. Jones aided and abetted the crime."
# print(sentence.find("Joel"))
# print(sentence.find("Jones"))
# print(sentence.index("Joel"))
# print(sentence.index("Jones"))

# print(sentence.ifnd("banana"))
print(sentence.index("banana"))

days = "We have gone {:^8} days without an accident"
print(days.format(20))

days = "days"
_day = "test"
1_day = "test"