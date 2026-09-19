a5="Me"  #STR
a1=2   #INT
a2=3.75   #FLOAT
a3=None   #NULL
a4=True   #Bool

print(a5,a1,a2,a3,a4)
print(type(a1))
print(type(a2))
print(type(a3))
print(type(a4))
print(type(a5))

# Arithmetic Operators
a=5
b=2
print("sum",a+b)
print("difference",a-b)
print("product",a*b)
print("true quotient",a/b)
print("floor quotient",a//b)  #ignores the decimal part of your quotient
print("remainder",a%b)   #10/3  rem=1
print("exponent",a**b)   #power

# Relational Operators
print(a>b)
print(a<b)
print(a==b)
print(a!=b)
print(a>=b)
print(a<=b)


#Assignment Operators
a=10        #10
a+=10    #20  --> a=a+10
print(a)
a-=5     #15
print(a)
a*=2     #30
print(a)
a/=3     #10
print(a)
a%=10
print(a)
a**=10
print(a)


#Input function
age=input("Enter your age: ")
print(age)

name=input("Enter your name: ")
print(name)

a=int(input("Enter 1st number: "))
b=int(input("Enter second number: "))
print(a+b)
