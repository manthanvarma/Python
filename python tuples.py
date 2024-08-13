tup1 = ("apple", "cherry", "banana")
print(tup1)

tup1 = ("apple", "cherry", "banana", "apple", "apple")
print(tup1)

tup1 = ("apple", "cherry", "banana", "apple", "apple")
print(len(tup1))

print(tup1[1])
print(tup1[-1])
print(tup1[-4:-1])

if "apple" in tup1:
    print("yes")

y = list(tup1)
y[1] = "kiwi"
print(y)

tup1 = ("apple", "cherry", "banana", "apple", "apple")
x = list(tup1)
x.append("chickoo")
tup1 = list(x)
print(tup1)

tup1 = ("apple", "cherry", "banana", "apple", "apple", "chickoo")
x = list(tup1)
x.remove("chickoo")
tup1 = list(x)
print(tup1)

tup1 = ("apple", "cherry", "banana", "apple", "apple", "chickoo")
del tup1

tup2 = ("apple", "cherry", "banana")
(green, yellow, red) = tup2
print(green)
print(yellow)
print(red)

