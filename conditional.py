x = 7
if x%2 == 0:
	print(x, "is even")
else:
	print(x, "is odd")
n = 10
m = 10
if n>m:
	print("less")
else:
	if n<m:
		print("greater")
	else:
		print("eqeal") #nested elif= else if
sajid = "i'am sajid and i'am a student"
tot = 0
for f in sajid:
	if f != " ":
		tot = tot + 1
print (tot)
nums = [2,6,1,0,6,10,67,2]
best = 0
for k in nums:
	#k = int(j)
	if k>best:
		best = k
print (type(best))
s = "We are learning!"
x = 0
for i in s:
    if i in ['a', 'b', 'c', 'd', 'e']:
        x += 1
print(x)
