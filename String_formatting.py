#method 1 - concatination using '+ perator'
companyName ="Ednue Technlogies"
suffix = "Pvt Ltd"
print(companyName+ ""+suffix)

#method2 - '%'or c-style string formatting
# %s for string
# %d for integer
# %f for float
name = "Sai" #string
age = 25 # integer
print("%s age is %d" %(name,age))


# method 3 - .format() method
print(" {} age is {} ".format(name,age))

#method 4- f'string
personName = "Alex"
CompanyName2 = "Google"
print(f"{personName} works in a {CompanyName2}") #output= Alex works in Google