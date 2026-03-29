#Task 1
name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello,", name,"! You are", age, "years old.")
#########################################################################################################
#Task 2
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
print(number1 + number2, number1 - number2, number1 * number2)
#########################################################################################################
#Task 3
temperature = int(input("Enter the temperature: "))
print(temperature * 9 / 5 + 32)
#########################################################################################################
#Task 4
fnumber = 5
snumber = 10
tnumber = fnumber
fnumber = 10
snumber = tnumber
print(fnumber, snumber)
#########################################################################################################
#Task 5
yournum = int(input("Enter your number: "))
if(yournum % 2 == 0):
    print("Your number is even")
else :
    print("Your number is odd")
#########################################################################################################
#Task 6
yourNum = int(input("Enter your number: "))
if(yourNum >= 0 and yourNum <= 12):
    print("Child")
elif(yourNum >= 13 and yourNum <= 17):
    print("Teenager")
else:
    print("Adult")
#########################################################################################################
#Task 7
a = int(input("Enter your first: "))
b = int(input("Enter your second: "))
c = int(input("Enter your third: "))
print(max(a, b, c))
#########################################################################################################
#Task 8
FIrstNum = int(input("Enter first number: "))
SEcondNum = int(input("Enter second number: "))
operation = input("Choose operation (+, -, *, /): ")
if operation == "+":
    print(FIrstNum + SEcondNum)
elif(operation == "-"):
    print(FIrstNum - SEcondNum)
elif(operation == "*"):
    print(FIrstNum * SEcondNum)
elif(operation == "/"):
    print(FIrstNum / SEcondNum)
else:
    print("Invalid operation")
#########################################################################################################
#Task 9
youryear = int(input("Enter your year: "))
if(youryear % 4 == 0 and youryear % 100 != 0 or youryear % 400 == 0):
    print("Leap year")
else:
    print("Not leap year")
#########################################################################################################
#Task 10
yourgrade = int(input("Enter your grade: "))
if(yourgrade>=90 and yourgrade<=100):
    print("A")
elif(yourgrade>=75 and yourgrade<=89):
    print("B")
elif(yourgrade>=50 and yourgrade<=74):
    print("C")
elif(yourgrade<50):
    print("F")
#########################################################################################################
#Task 11
balance = 1000
deduction = int(input("How much money do you want to get: "))
if(deduction > balance):
    print("Error");
else:
    print("The money was successfully withdrawn. Left money:",balance-deduction)
#########################################################################################################
#Task 12
login = "admin"
password = "1234"
enterlogin = input("Enter your login name: ")
enterpassword = input("Enter your password: ")
if(login==enterlogin and password==enterpassword):
    print("You logged in")
else:
    print("Login failed")
#########################################################################################################
#Task 13
purchase = int(input("Enter purchase amount: "))
if(purchase >= 10000):
    print("You have 10% discount. You have to pay", purchase * 0.9)
elif(purchase >= 5000 and purchase < 10000):
    print("You have 5% discount. You have to pay", purchase * 0.95)
else:
    print("You don't have discount. You have to pay", purchase)
#########################################################################################################
#Task 14
fside = int(input("Enter first side: "))
sside = int(input("Enter second side: "))
tside = int(input("Enter third side: "))
if(max(fside, sside, tside) == fside and fside < sside + tside or max(fside, sside, tside) == sside and sside < fside + tside or max(fside, sside, tside) == tside and tside < fside + sside):
    print("Triangle exists")
    if(fside == sside and tside == sside):
        print("This triangle is equilateral")
    elif(fside == sside or tside == sside or fside == sside):
        print("This triangle is isosceles")
    else:
        print("This triangle is not scalene")
else:
    print("This triangle does not exist")
#########################################################################################################
#Task 15
color = input("What color traffic light shows: ")
if(color == "red"):
    print("Stop")
elif(color == "green"):
    print("Go")
elif(color == "yellow"):
    print("Wait")
#########################################################################################################
#Task 16
NUMber = int(input("Enter a number: "))
if(NUMber > 0):
    print("Positive")
elif(NUMber < 0):
    print("Negative")
else:
    print("Zero")
if(NUMber % 2 == 0):
    print("Even")
else:
    print("Odd")
if(NUMber >= 1 and NUMber <= 100):
    print("The number within range from 1 to 100")
else:
    print("The number outside range from 1 to 100")
#########################################################################################################
#Task 17
FIrstNum = int(input("Enter first number: "))
SEcondNum = int(input("Enter second number: "))
operation = input("Choose operation (+, -, *, /, ^, %): ")
if operation == "+":
    print(FIrstNum + SEcondNum)
elif(operation == "-"):
    print(FIrstNum - SEcondNum)
elif(operation == "*"):
    print(FIrstNum * SEcondNum)
elif(operation == "/" and SEcondNum == 0):
    print("Undefined operation")
elif(operation == "/"):
    print(FIrstNum / SEcondNum)
elif(operation == "^"):
    print(FIrstNum ** SEcondNum)
elif(operation == "%"):
    print(FIrstNum % SEcondNum)
else:
    print("Invalid operation")
#########################################################################################################
#Task 18
Password = input("Enter password: ")
Checking = 0
if(len(Password) >= 8):
    Checking+=1;
if(any(char.isdigit() for char in Password)):
    Checking+=1;
if(any(char.isupper() for char in Password)):
    Checking+=1;
if(Checking == 1 or Checking == 0):
    print("Weak")
elif(Checking == 2):
    print("Medium")
elif(Checking == 3):
    print("Strong")
#########################################################################################################
#Task 19
Balance = 5000
print("Choose:")
print("1.Check your balance")
print("2.Deposit")
print("3.Withdraw")
Choice = int(input("Enter your choice:"))
if(Choice == 1):
    print("Your balance:",Balance)
elif(Choice == 2):
    print("Put the cash")
elif(Choice == 3):
    witHdraw = int(input("How much would you like to withdraw:"))
#########################################################################################################
#Task 20
guess = int(input("Guess a secret number:"))
secret = int(input("Enter a secret number:"))
if(guess == secret):
    print("Correct")
elif(guess > secret):
    print("Too high")
elif(guess < secret):
    print("Too low")
#########################################################################################################
#Task 21
yourattendance = int(input("Enter your attendance:"))
yourgrade = int(input("Enter your grade: "))
if(yourattendance < 60):
    print("F")
elif(yourgrade>=90 and yourgrade<=100):
    print("A")
elif(yourgrade>=75 and yourgrade<=89):
    print("B")
elif(yourgrade>=50 and yourgrade<=74):
    print("C")
elif(yourgrade<50):
    print("F")
#########################################################################################################
#Task 22
order = int(input("Order amount:"))
distance = int(input("Distance:"))
total = 1000
if(distance > 5):
    total+=200
if(order > 15000):
    total=0;
print(total)
#########################################################################################################
#Task 23
salary = int(input("Salary:"))
CreditHistory = input("Credit History:")
if(salary > 200000 and CreditHistory == "Good"):
    print("Approved")
else:
    print("Rejected")
#########################################################################################################
#Task 24
Login = input("Enter Login:")
Pass = input("Enter Password:")
if(Login == "admin" and Pass == "1234"):
    print("Login Successful")
else:
    print("Login Failed, try again");
    Login = input("Enter Login:")
    Pass = input("Enter Password:")
    if(Login == "admin" and Pass == "1234"):
        print("Login Successful")
    else:
        print("Blocked")
#########################################################################################################
#Task 25
print("Menu:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Exit")
ChoiCe = int(input("Your choice: "))
NumBer1 = int(input("First number: "))
NumBer2 = int(input("Second number: "))
if(ChoiCe == 1):
    print(NumBer1 + NumBer2)
elif(ChoiCe == 2):
    print(NumBer1 - NumBer2)
elif(ChoiCe == 3):
    print(NumBer1 * NumBer2)
elif(ChoiCe == 4):
    print("Program closed")