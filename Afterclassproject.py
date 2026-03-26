user_input = input("Enter a character: ")
a = user_input.lower()
if not a:
    print("You didn't enter anything!")
elif a >= 'a' and a <= 'z':
    print("It is an alphabet.")
else:
    print("This is not an alphabet.")