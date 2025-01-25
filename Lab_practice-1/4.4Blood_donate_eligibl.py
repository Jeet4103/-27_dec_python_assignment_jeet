
age = int(input("Enter your age: "))
weight = float(input("Enter your weight in kilograms: "))


if age >= 18:
    if weight >= 50:
        print("You are eligible to donate blood.")
    else:
        print("You are not eligible to donate blood. You must weigh at least 50 kg.")
else:
    print("You are not eligible to donate blood. You must be at least 18 years old.")
