a = """lorem ipsum,
dolor sit
amet"""
print(a)

a = "hello word"
print(a[1])
print(len(a))

a = "the best things in life are free"
print("free" in a)
print("expensive" not in a)

for x in "banana":
    print(x)

b = "hello world"
print(b[2:5])
print(b[:5])
print(b[5:])
print(b[-5:-2])

a = "helloworld"
print(a.upper())
print(a.lower())

a = " helloworld"
print(a.strip()) #removes whitespace
print(a.replace("h", "j"))

a = " hello, world"
print(a.split(","))

a = "hello"
b = "world"
c = a + b
print(c)

age = 36
k = f"my name is john i am {age}"
print(k)

a = f"the price is {20*59} dollars"
print(a)