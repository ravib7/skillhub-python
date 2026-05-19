marks = 90

# < 35 Fail
# > 35 < 50  D
# > 50 < 60  C
# > 60 < 75  B
# > 75 < 90  A
# > 90  A+


if(marks < 35):
    print("Fail")
elif(marks > 35 and marks <= 50):
    print("D Grade")
elif(marks > 50 and marks <= 60):
    print("C Grade")
elif(marks > 60 and marks <= 75):
    print("B Grade")
elif(marks > 75 and marks <= 90):
    print("A Grade")
elif(marks>90 and marks<=100):
    print("A+")
else:
    print("invalid marks")