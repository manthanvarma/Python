a = 33
b = 200
if a>b:
    print("a is greater than b")
else:
    print("b is greater than a")

a = 33
b = 33
if a>b:
    print("a is greater than b")
elif(a == b):
    print("a and b are equal")
else:
    print("b is greater than a")

#short hand if else

a = 20
b = 30
print("A greater") if a>b else print("b is greater")

# nester if else

x = 31
if x > 10:
    print("above 10")
    if x > 20:
        print("above 20")
    else:
        print("but not above 20")

a = 20
b = 30
if b > a:
    pass