# ==============================================================================
# PROJECT: STUDENT REPORT CARD GENERATOR
# ==============================================================================
# User enters name, roll number, and marks in 5 subjects stored in a list. 
# Program calculates total, percentage, highest mark, lowest mark, 
# and prints a formatted report card with grade and result.
#
# Grade rules:
# 90 and above — Grade A
# 75 to 89 — Grade B
# 60 to 74 — Grade C
# 40 to 59 — Grade D
# Below 40 — Grade F (Result Fail, everything else Result Pass)
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. USER INPUT SECTION
# ------------------------------------------------------------------------------
name = input("Enter Student Name: ")
roll_No = input("Enter Student Roll_No: ")
marks = []

print("Enter First Subject Marks of Student: ")
marks.insert(0, int(input("Marks: ")))

print("Enter Second Subject Marks of Student: ")
marks.insert(1, int(input("Marks: ")))

print("Enter Third Subject Marks of Student: ")
marks.insert(2, int(input("Marks: ")))

print("Enter Fourth Subject Marks of Student: ")
marks.insert(3, int(input("Marks: ")))

print("Enter Fifth Subject Marks of Student: ")
marks.insert(4, int(input("Marks: ")))


# ------------------------------------------------------------------------------
# 2. CALCULATIONS SECTION
# ------------------------------------------------------------------------------
total_marks = sum(marks)
percentage = float((total_marks * 100) / 500)



# ------------------------------------------------------------------------------
# 3. CONDITIONAL EVALUATION SECTION (Decision Making)
# ------------------------------------------------------------------------------
if (percentage >= 90):
    grade = "A"
    result = "Pass"

elif (percentage >= 75 and percentage <= 89):
    grade = "B"
    result = "Pass"

elif (percentage >= 60 and percentage <= 74):
    grade = "C"
    result = "Pass"

elif (percentage >= 40 and percentage <= 59):
    grade = "D"
    result = "Pass"

else:
    grade = "F"
    result = "Fail"


# ------------------------------------------------------------------------------
# 4. FINAL FORMATTED REPORT CARD DISPLAY
# ------------------------------------------------------------------------------
print("\n==============================")
print("         REPORT CARD          ")
print("==============================")
print(f"Name      : {name}")
print(f"Roll No   : {roll_No}")
print("------------------------------")
print(f"Subject 1 : {marks[0]}")
print(f"Subject 2 : {marks[1]}")
print(f"Subject 3 : {marks[2]}")
print(f"Subject 4 : {marks[3]}")
print(f"Subject 5 : {marks[4]}")
print("------------------------------")
print(f"Total     : {total_marks} / 500")
print(f"Percentage: {percentage}%")
print(f"Highest   : {max(marks)}")
print(f"Lowest    : {min(marks)}")
print(f"Grade     : {grade}")
print(f"Result    : {result}")

print("==============================")
