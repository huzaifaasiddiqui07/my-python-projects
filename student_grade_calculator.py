# ============================================
# Student Grade Calculator
# Author: Huzaifa Siddiqui
# Course: Software Engineering - NED Academy
# Description: A simple program that takes student
#              marks as input and calculates
#              percentage and grade.
# ============================================


def get_student_details():
    """
    Takes student name and marks as input.
    Calculates and returns the percentage.
    """
    print("=" * 40)
    print("      STUDENT GRADE CALCULATOR")
    print("=" * 40)

    name = input("Enter student name: ")
    print("\nEnter marks out of 100 for each subject:")
    anatomy    = int(input("  Anatomy    : "))
    physiology = int(input("  Physiology : "))
    kinesiology = int(input("  Kinesiology: "))

    total_marks   = anatomy + physiology + kinesiology
    percentage = (total_marks / 300) * 100

    print(f"\nStudent Name : {name}")
    print(f"Total Marks  : {total_marks} / 300")
    print(f"Percentage   : {percentage:.2f}%")

    return name, percentage


def assign_grade(name, percentage):
    """
    Takes percentage as input and assigns a grade.
    A : 80% and above
    B : 50% to 79%
    F : Below 50%
    """
    print("\n--- Result ---")
    if percentage >= 80:
        print(f"Congratulations {name}! You got Grade A 🎉")
    elif percentage >= 50:
        print(f"Well done {name}! You got Grade B ✅")
    else:
        print(f"Sorry {name}, You got Grade F. Keep working hard! 💪")


# --- Main Program ---
student_name, student_percentage = get_student_details()
assign_grade(student_name, student_percentage)
