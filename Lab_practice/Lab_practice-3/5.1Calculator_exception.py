def calculator():
    while True:
        try:
            print("Select operation:")
            print("1. Addition (+)")
            print("2. Subtraction (-)")
            print("3. Multiplication (*)")
            print("4. Division (/)")
            
            choice = input("Enter choice (1/2/3/4): ")
            if choice not in ['1', '2', '3', '4']:
                print("Invalid choice! Please select a valid option.")
                continue
            
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                result = num1 + num2
            elif choice == '2':
                result = num1 - num2
            elif choice == '3':
                result = num1 * num2
            elif choice == '4':
                if num2 == 0:
                    raise ZeroDivisionError("Error: Cannot divide by zero!")
                result = num1 / num2

            print(f"Result: {result}")
        except ValueError:
            print("Invalid input! Please enter numeric values.")
        except ZeroDivisionError as e:
            print(e)
        
        again = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
        if again != 'yes':
            break

calculator()
