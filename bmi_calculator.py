# BMI Calculator ⚖️

print("Welcome to the BMI Calculator!")

# Get user input
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

# Calculate BMI
bmi = weight / (height ** 2)

# Show result
print(f"Your BMI is: {bmi:.2f}")

# Interpret BMI
if bmi < 18.5:
    print("You are underweight.")
elif bmi < 25:
    print("You have a normal weight.")
elif bmi < 30:
    print("You are overweight.")
else:
    print("You are obese.")
