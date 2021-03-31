mylist = []
mylist.append(5)
mylist.append(27)
mylist.append(3)
mylist.append(12)
print(mylist) #mutator, Adds a new item to the end of a list

mylist.insert(1, 12)
print(mylist) #mutator, Inserts a new item at the position given
print(mylist.count(12)) #Returns the number of occurrences of item

print(mylist.index(3)) #Returns the position of first occurrence of item

print(mylist.count(5))

mylist.reverse() #Modifies a list to be in reverse order
print(mylist)

mylist.sort() #Modifies a list to be sorted
print(mylist)
mylist.sort(reverse=True)
print(mylist)
mylist.remove(5) #Removes the first occurrence of item

print(mylist)

lastitem = mylist.pop() #Removes and returns the last item
print(lastitem)
print(mylist)
item = mylist.pop(1) #Removes and returns the item at position
print(item)
print(mylist)
ss = "    Hello, World    "
print(ss.upper()) #Returns a string in all uppercase
print(ss.lower()) #Returns a string in all lowercase

els = ss.count("l")
print(els)

print("***"+ss.strip()+"***") #Returns a string with the leading and trailing whitespace removed

news = ss.replace("o", "***")
print(news)
origPrice = float(input('Enter the original price: $'))
discount = float(input('Enter discount percentage: '))
newPrice = (1 - discount/100)*origPrice
calculation = '${} discounted by {}% is ${}.'.format(origPrice, discount, newPrice) #format=involve where having {}
print(calculation)
#tuples and strings are immutable