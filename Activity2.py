a=10
b=12
c=12
print(a != b)
print(b != c)

d="Zanna"
e="Katriel"
if d != e:
    print(d,"and", e, "are different.")
else:
    print(d, "and", e, "are the same.")

f=68
g=23
if (f == 1) != (g == 23):
    print("Hello")
else:
    print("Bye")

h=int(input("Enter a number: "))
if h % 2 != 0:
    print(h, "is an odd number.")
else:
    print(h, "is an even number.")