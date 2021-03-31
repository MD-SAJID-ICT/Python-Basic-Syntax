fruit = ["banana", "apple", "cherry"]
print(fruit)

fruit[0] = "pear"
fruit[-1] = "orange"
print(fruit)
alist = ['a', 'b', 'c', 'd', 'e', 'f']
alist[1:3] = []
print(alist)
greeting = "Hello, world!"
newGreeting = 'J' + greeting[1:]
print(newGreeting)
print(greeting)
phrase = "many moons"
phrase_expanded = phrase + " and many stars"
phrase_larger = phrase_expanded + " litter"
phrase_complete = "M" + phrase_larger[1:] + " the night sky."
excited_phrase_complete = phrase_complete[:-1] + "!"
print(excited_phrase_complete)
a = ['one', 'two', 'three']
del a[1]  #deletion
print(a)

alist = ['a', 'b', 'c', 'd', 'e', 'f']
del alist[1:5]
print(alist)
a = "banana"
b = "banana"

print(a is b) #objects and references

a = [81,82,83]
b = [81,82,83]

print(a is b) #objects and references

print(a == b)

print(id(a))
print(id(b))
a = [81,82,83]
b = [81,82,83]
print(a is b)

a = b #aliasing
print(a == b)
print(a is b)

a[0] = 5
print(b)
print(a is b)
a = [81,82,83]

b = a[:]       # make a clone using slice
print(a == b)
print(a is b)

b[0] = 5

print(a)
print(b)
