#Question 1

grade= float(input("Please enter your marks "))

if grade<25:
    print("Your final grade is F")
elif grade>=25 and grade<45:
    print("Your final grade is E")
elif grade>=45 and grade<50:
    print("Your final grade is D")
elif grade>=50 and grade<60:
    print("Your final grade is C")
elif grade>=60 and grade<80:
    print("Your final grade is B")
elif grade>=80 and grade<=100:
    print("Your final grade is A")
else:
    print("Error!!")
    
    
#Question 2

yr= int(input("Please enter year: "))

if yr % 100 == 0:
    if yr % 400 == 0:
        print("The year ",yr," is a leap year!")
    else:
        print("The year ",yr," is not a leap year :(")
elif yr % 4 == 0:
    print("The year ",yr," is a leap year!")
else:
    print("The year ",yr," is not a leap year :(")


#Question 3

from random import randint

for loop_variable in range(10):
    n1 = randint(0,10)
    n2 = randint(0,10)
    if int(input('Question: ' + str(n1) + ' x ' + str(n2) + ' = ')) == n1 * n2: print('Right!')
    else: print('Wrong. The answer is ', n1 * n2)


#Question 4

for i in range(200):
    if i % 5 == 2 and i % 6 == 3 and i % 7 == 2:
        print("Answer:",i)

