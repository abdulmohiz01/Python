# Datatypes
# "Hello"[4]
# print("hello"[4])
# print("Welcome to the tip calculator.")
# bill = input("What was the total Bill?")

# Integer
# print(123456)
# num=123
# num=str(num)
# print(type(num))
# #float
# print(79 + float("100.5"))

# num = input("Enter two digit number")
# result = int(num[0]) + int(num[1])
# print(result)
# print(2**2) #Exponent>**
#PEMDAS
# ()
# **
# */
# +-
# print(3*3+3/3-3)
# weight= input("Enter your weight in Kg")
# height= input("Enter your height in M")
# weight= float(weight)
# round(x, y) y= rounding to how many decimal places?
# bmi = round(float(weight) / float(height)**2,2)
# print("Your BMI is: " + str(bmi))
# If theres single / then its float, if its double // then its int
# print(8/5)
# print(8//5)
# shorthand
# score=0
# score+=1
# print(score)
# f-string
# print(f"Your score is {score}")

# Exercise 1
# age = input("Enter your age")
# remainingAge = 90 - int(age)
# print(f"You have {remainingAge*365} Days, {remainingAge*56} Weeks, {remainingAge*12} Months left.")

# Exercise 2
print("Welcome to the tip Calculator.")
bill = input("What was the total Bill? $")
tip= input("How much tip percentage you would like to give?")
people =input("How many people are you?")
print(f"Each person should pay: ${(int(bill)+(int(bill) * (int(tip)/100))) /int(people)}")