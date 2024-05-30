# if, elif, multiple if, nested if, operators=> and, or, not, lower(), count()->it counts number of letters in a string
# , its case sensitive
# number = input("Enter a Number")
# if int(number)%2==0:
#     print("The number is Even")
# else:
#     print("The number is Odd")
# Exercise 1- BMI Calculator
# weight = float(input("Enter Your weight in Kg"))
# height = float(input("Enter your Height in M"))
# bmi= weight/height**2
# if bmi<18.5:
#     print("Your are Underweight")
# elif bmi>=18.5 and bmi<25:
#     print(f"Your bmi is {round(bmi,2)}. You have normal weight.")
# elif bmi>=25 and bmi<30:
#     print("You are overweight.")
# elif bmi>=30 and bmi<35:
#     print("You are Obese")
# else:
#     print("You are clinically Obese")
# Exercise 2
number = int(input("Enter a year."))
if number % 4==0:
    if number % 100 == 0:
        if number % 400==0:
            print("Leap year")
        else:
            print("Not leap year")
    else:
        print("Leap year")
else:
    print("Not leap year")
