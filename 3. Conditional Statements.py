#Write a program to allow access to a website if he/she is above 18

user_age = int(input("Enter your age: "))
if(user_age>=18):
    print("Access Provided")
elif(user_age<=0):
    print("Invalid Input! Try again")
else:
    print("Access Denied")
print("End of program")


#Write a program which allows u to sit in exam if your attendance is above 75

student_name = input("Enter Student Name: ")
student_attendence = int(input("Enter Student Attendence: "))
if (student_attendence>= 75):
    print ("Permission To Sit In The Exam: Provided to",student_name,"!")

elif (student_attendence<75):
    print("Permission To Sit In Exam: Not Provided to ",student_name,"!")
 
elif (student_attendence<=0):
   print ("Invalid Input!")