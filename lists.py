t = [5,6,7,8,9] #lists
s = (1,2,3,4,56) #tuples
print(type(t))
print(type(s))
print(s[2]) #index
print(t[-3])
w = len(s) #length
print(len(t))
print(s[w-1])
r = ("my name is sajid")
print(r[5:7])
print(r[:])
print(r[:4]) #slice operator
print(r * 4)
print (t+[6,7,8,9]) #concatation and repetition
print(r.count("i"))
print(t.count(7)) #count
print(r.index("s"))
print(t.index(7)) #index
print(r.split("i")) #split
y = ['s','a','j','i','d']
glue = ""
print(glue.join(y))
print(" & ".join(y)) #join

