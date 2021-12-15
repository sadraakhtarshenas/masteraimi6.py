


username = input()
password = input()

if username == "admin" and password == "asgharsagsibi1@2020":
    print("welcome")

else:
    print("error! try again")


a = int(input("please enter first numer"))
b = int(input("please enter second number"))

op = input()

if op == "+":
    result = a + b

if op == "-":
    result = a - b 

if op == "*":
    result = a * b 

if op == "/":
    result = a / b
    print(result)



a = int(input("please enter first numer"))
b = int(input("please enter second number"))

op = input()

if op == "+":
    result = a + b

if op == "-":
    result = a - b 

if op == "*":
    result = a * b 

if op == "/":
   if b != 0:
        result = a / b
else:
    result = "cannot divide by zero"

print(result)

