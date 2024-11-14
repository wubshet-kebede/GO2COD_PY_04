def bmi_calculator():
    """Calculates and categorizes Body Mass Index (BMI)."""

    while True:
        try:
            height = float(input("Enter your height in meters: "))
            weight = float(input("Enter your weight in kilograms: "))
            break
        except ValueError:
            print("Invalid input. Please enter numbers only.")

    bmi = weight / (height * height)

    print(f"Your BMI is: {bmi:.2f}")

    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 25:
        category = "Normal weight"
    elif 25 <= bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"

    print(f"Your BMI category is: {category}")


if __name__ == "__main__":
    bmi_calculator()

