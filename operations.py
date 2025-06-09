num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

# Perform calculations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2 if num2 != 0 else "Undefined (division by zero)"

# Display results
print("\nAddition Result =", addition)
print("Subtraction Result =", subtraction)
print("Multiplication Result =", multiplication)
print("Division Result =", division)