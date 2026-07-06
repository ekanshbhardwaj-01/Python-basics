# conditional statement syntax :  ie  if->elif->else
name=input("Enter ur name:")
age=int(input("enter ur age :"))
if(age >= 18):
    print(" u r eligible") #indentation : proper spacing 
elif(age==17):
    print("wait till 18")
else:
    print(" u r not eligible")

marks=int(input("Enter ur marks :"))
if(marks>=90):
    print("Grade : A")
elif(marks>=80 and marks<90):
    print("Grade:B")
elif(marks>=70 and marks<80):
    print("Grade :C")
else:
    print("Grade: D")
    