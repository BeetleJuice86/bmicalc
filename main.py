height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

regular_bmi = round(int(weight)) / (float(height ** 2))
bmi = round(regular_bmi)

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
else:
    if bmi < 25:
        print(f"Your BMI is {bmi}, you have a normal weight.")
    else:
        if bmi < 30:
            print(f"Your bmi is {bmi}, you are slightly overweight.")
        else:
            if bmi < 35:
                print(f"Your bmi is {bmi}, you are obese.")
            else:
                print(f"Your bmi is {bmi}, you are clinically obese.")
