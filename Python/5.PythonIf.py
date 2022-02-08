total_marks = int(input("Enter your total marks (out of 100): "))

if total_marks < 35:
    print("FAIL")
elif total_marks > 35 and total_marks < 70:
    print("PASS")
elif total_marks > 70 and total_marks < 75:
    print("FIRST CLASS")
else:
    print("FIRST CLASS WITH DISTINCTION")
