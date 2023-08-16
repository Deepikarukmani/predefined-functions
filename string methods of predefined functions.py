# school grade example
# >90-A+, <80- A, >70 -B+, >60 -B, <60 - C

mark = int(input("ENTER YOUR MARK : "))
if mark>=90:
    print("A+")
elif mark<=80:
    print("A")
elif mark>=70:
    print("B+")
elif mark>=60:
    print("B")
else:
    print("C")

#other example

name = input("what is your name: ")
if name== ('Deepika'):
    print("Hi")
    print('Hello')

# find greater number

no1 = int(input("Enter no1 "))   #80
no2 = int(input("Enter no2 "))   #90
no3 = int(input("Enter no3 "))   #100

if no1>no2 and no1>no3:
    print("Num1 is Greatest")
elif no2>no3:
    print("Num2 is Greatest")
else:
    print("Num3 is Greatest")


# find odd or even

n= int(input("Enter no "))
if n%2==0:
    print("even")
else:
    print("odd")


n= int(input("Enter no "))
if n%3==0:
    print("even")
else:
    print("odd")


# iterative statement -----> loope


guess = 5
while True:
    mind = int(input("Enter your choice between 1 and 10: "))
    if guess == mind:
        print("correct")
        break
    elif guess > mind:
        print("your guess is too small")
    elif guess < mind:
        print("your guess is too large")



