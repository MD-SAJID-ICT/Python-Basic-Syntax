#nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nums = range(11)
accum = 0
for w in nums:
	accum = accum + w
	print (accum)
print ("range(0,5): ")
for i in range(0, 5):
	print (i)
print ("range(5): ")
for i in range(5):
        print (i)
print (list(range(5)))
print (list(range(0,5)))
print(range(0,5))
numbers = range(41)
sum1 = 0
for sum in numbers:
    sum1 =sum1 + sum
print (sum1)
str1 = "I like nonsense, it wakes up the brain cells. Fantasy is a necessary ingredient in living."
numbs = 0
for character in str1:
   numbs += 1
print(numbs)
fruits = ['apple', 'pear', 'apricot', 'cherry', 'peach']
for n in range(len(fruits)):
    print(n, fruits[n])

s = input("Enter some text") #The Accumulator Pattern with Strings
ac = ""
for c in s:
    ac = ac + c + "-" + c + "-"

print(ac)