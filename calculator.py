print("""Please Enter Two Numbers and the Operation You Want to Perform
Available Operators:
+  or 1 for Addition 
-  or 2 for Subtraction
*  or 3 for Multiplication
/  or 4 for Division
// or 5 for Floor Division
%  or 6 for Modulus
** or 7 for Exponentiation
""")

# Function for calculation
def calculate(num1, num2, operator):
    if operator in ["+", "1"]:
        return num1 + num2
    elif operator in ["-", "2"]:
        return num1 - num2
    elif operator in ["*", "3"]:
        return num1 * num2
    elif operator in ["/", "4"]:
        return "Error: Division by zero" if num2 == 0 else num1 / num2
    elif operator in ["//", "5"]:
        return "Error: Division by zero" if num2 == 0 else num1 // num2
    elif operator in ["%", "6"]:
        return "Error: Division by zero" if num2 == 0 else num1 % num2
    elif operator in ["**", "7"]:
        return num1 ** num2
    else:
        return "Invalid operator! Please try again."

# Main loop
while True:
    try:
        number_1 = float(input("\nEnter Number 1: "))
        number_2 = float(input("Enter Number 2: "))
        operator = input("Enter the Operator or Number: ").strip()

        result = calculate(number_1, number_2, operator)
        print("Result is:", result)

        # Ask user to continue or not
        choice = input("\nDo you want to perform another operation? (y/n): ").lower()
        if choice != 'y':
            print("Thank you for using the Mini Calculator!")
            break
    except ValueError:
        print("Invalid input! Please enter numeric values only.")
