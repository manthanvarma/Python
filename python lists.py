thislist = ["apple", "banana", "cherry"]
print(thislist)

# lists allow duplicate values

thislist = ["apple", "banana", "cherry", "apple"]
print(thislist)

print(len(thislist))

# list can contain different data types

thislist = ["a", 1, True, "bcd"]
print(thislist)
print(type(thislist))

print(thislist[1])
print(thislist[-1])
print(thislist[2:5])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[4:])
print(thislist[2:])
print(thislist[-4:-1])

if "apple" in thislist:
    print("yes, 'apple' is in fruits list")

thislist[1] = "blackcurrent"
print(thislist)

thislist[1:3] = ["sugarcane","watermelon"]
print(thislist)

thislist.append("orange")
print(thislist)

thislist.insert(2,"blueberry")
print(thislist)

a = ["apple", "banana"]
b = ["bheem", "chutki"]
a.extend(b)
print(a)

a = ["apple"]
b = ("jaggu", "raju")
a.extend(b)
print(a)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
thislist.remove("apple")
print(thislist)

thislist.pop(2)
print(thislist)

thislist.pop()
print(thislist)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
for x in thislist:
    print(x)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
[print(x) for x in thislist]

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
newlist = []
for x in thislist:
    if "a" in x:
        newlist.append(x)

print(newlist)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
newlist = [x for x in thislist if "a" in x]
print(newlist)

a = [x for x in range(10)]
print(a)

a = [x for x in range(11) if x<5]
print(a)

a = [x.upper() for x in thislist]
print(a)

a = [x if x != "banana" else "orange" for x in thislist]
print(a)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
thislist.sort()
print(thislist)

thislist = [100, 50, 60, 20, 33]
thislist.sort()
print(thislist)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
thislist.sort(reverse=True)
print(thislist)

thislist = [100, 50, 60, 20, 33]
thislist.sort(reverse=True)
print(thislist)

thislist.reverse()
print(thislist)

thislist = [100, 50, 60, 20, 33]
mylist = thislist.copy()
print(mylist)

l1 = [100, 50, 60, 20, 33]
l2 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
l3 = l1 + l2
print(l3)

for x in l2:
    l1.append(x)
print(l1)