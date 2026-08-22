# ============================================
# Student Login & Fee Concession System
# Author: Huzaifa Siddiqui
# Course: Software Engineering - NED Academy
# Description: A student login system that
#              authenticates users, calculates
#              their percentage, and applies
#              fee concession based on marks.
# ============================================


# --- Student Database ---
student_database = {
    'huzaifa': {'password': 'pass123',  'marks': 435, 'fees': 11000},
    'umaima':  {'password': 'pass456',  'marks': 460, 'fees': 11000},
    'aqsa':    {'password': 'pass789',  'marks': 420, 'fees': 11000},
    'zoha':    {'password': 'pass321',  'marks': 470, 'fees': 11000},
    'umer':    {'password': 'pass654',  'marks': 440, 'fees': 11000},
    'hashir':  {'password': 'pass987',  'marks': 380, 'fees': 11000},
}


def calculate_percentage(name, total_marks):
    """
    Calculates and displays the percentage of a student.
    Total marks are out of 500.
    """
    percentage = (total_marks / 500) * 100
    print(f"\nStudent Name : {name.capitalize()}")
    print(f"Marks        : {total_marks} / 500")
    print(f"Percentage   : {percentage:.2f}%")
    return percentage


def apply_concession(percentage, monthly_fees):
    """
    Applies fee concession based on percentage:
    - 80% and above → 20% discount
    - 50% to 79%    → 10% discount
    - Below 50%     → No discount
    """
    if percentage >= 80:
        discount = 20
    elif percentage >= 50:
        discount = 10
    else:
        discount = 0

    discounted_price = monthly_fees - (monthly_fees * discount / 100)

    print(f"\n--- Fee Concession ---")
    print(f"Original Fees  : Rs. {monthly_fees}")
    print(f"Discount       : {discount}%")
    print(f"Updated Fees   : Rs. {discounted_price:.0f}")


# --- Main Program ---
print("=" * 40)
print("     STUDENT LOGIN SYSTEM")
print("=" * 40)

user_name = input("Enter username: ").lower().strip()
user_password = input("Enter password: ")

if user_name in student_database:
    if student_database[user_name]['password'] == user_password:
        print("\n Login Successful!")
        print("-" * 40)

        student_data = student_database[user_name]
        marks = student_data['marks']
        fees = student_data['fees']

        percentage = calculate_percentage(user_name, marks)
        apply_concession(percentage, fees)

    else:
        print("\n Incorrect password! Access Denied.")
else:
    print("\n Username not found in the system.")
