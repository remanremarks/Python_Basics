#3 ways to create a string
str1="I am Zeeshan"
str2='I am "Zeeshan"'
str3="""I am Zeeshan"""
print(str1)
print(str2)
print(str3)

#concatenation
print(str1+str2+str3)
print(str1+" "+str2+" "+str3)

name=input("Enter your name: ")
day=input("What day is it today? ")
print("Hello, "+name+" its "+day)


#length of string
print(len(str1))
print(len(str2))
print(len(str3))

name="Remas Navid"
print(name[0])
print(name[2])
print(name[4])
print(name[6])
print(name[8])

#Slicing
print(name[0:4])
print(name[1:7])
print(name[3:])
print(name[:7])
print(name[-4:])
print(name[:-4])