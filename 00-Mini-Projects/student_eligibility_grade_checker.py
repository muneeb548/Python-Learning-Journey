## First, check the student's attendance.
# If the student is eligible for the exam, then check the marks and assign a grade.
name = input("Enter the Name: ")
marks = int(input("Enter the Marks: "))
attendance = int(input("Enter the Attendance:" ))
if(attendance>=75):
    print("Eligible For Exam:")
    if(marks>=80):
        print("Grade A: ")
    elif(marks>=60 and marks<79):
        print("Grade B: ")
    elif(marks>=40 and marks<59):
        print("Grade C: ")
    elif(marks<40):
        print("Fail")
elif(attendance<75):
     print("Not Eligible For Exam")
