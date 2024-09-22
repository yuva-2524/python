#arithmeticoperations (+,-,*,/,%,**,//)
# / will do division and give the quotient
# //
from operator import truediv

num1=2
num2=4
print(num1 * num2)
print(num1**num2) #** is power of

#comparison operator(==,!=,>,<,>=,<=)
num3=10
num4=20
if num3<num4:
    print("condition satisfied")

#logical operator(and,or,not)
flag1= True
flag2= True
flag3=True
flag4=4

if flag1 and flag2:
    print("and passed")

    if flag1 or flag3:
        print("or passed")

        if flag3 or flag4:
            print("or passed")
        else:
            print("or failed")
            if not flag3:
                print("Not passed")

#assignment operator(+=,-=,*=,/=)
number1=10
number1 += 20 # number = number +20
print(number1)

number2=40
number2 -=20 #number = number-20
print(number2)
