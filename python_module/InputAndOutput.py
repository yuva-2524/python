
name=input("Enter your name:")
rollNo=input("Enter your roll no:")
print(f"My name is {name} and my roll no is {rollNo}")


#to get multiple inputs in single input command
numbers=input("Enter multiplenumbers using comma separator:")
commaSeperatedNumbers = numbers.split(",")
print(commaSeperatedNumbers)

#to check the type of the input
test = input("Enter something")
print(type(test))

#type conversion/casting
score = input("Enter score:")
print(type(score))
print("my hsc score is :"+score)
print(100+int(score))