print(type(2))
print(type(2.5633))
print(type("hi there"))

# string is immutable
a = "test 1"
print(a)
print(id(a))
a = "test 2"
print(a)
print(id(a))

# a list is mutable
b = [1, "banana", 234]
print(b)
print(id(b))
b += [100, "second banana"]
print(b)
print(id(b))

# a tuple is immutable
c = (1, "banana", 345)
print(c)
print(id(c))
c += (100, "second banana")
print(c)
print(id(c))

d = "Dunwoody"
e = "Dunwoody"
print(id(d))
print(id(e))
print(d is e)

d = "Dunwoody"
e = "Dunwoody College of Technology"
print(id(d))
print(id(e))
print(d is e)
