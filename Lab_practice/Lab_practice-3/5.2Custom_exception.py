try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except ValueError:
    print("Error: Invalid input! Please enter numbers only.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
else:
    print(f"Result: {result}")
finally:
    print("Execution completed.")
