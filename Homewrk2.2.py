#Task1
#Fix buggy Code:
#if number > 0:
    #print("The number is positive.")
#elif number = 0:
    #print("The number is zero.")
#else number < 0:
    #print("The number is negative.")
number = float(input("Enter a number: "))

if (number > 0):
    print("The number is positive.")
elif (number == 0):
    print("The number is zero.")
else:
    print("The number is negative.")
#Task2
#Identify the Greatest Write a Python program that asks the user to enter three numbers. Your code should then identify and print out the largest number among the three.
num1 = float(input("Enter a number."))
num2 = float(input("Enter a number."))
num3 = float(input("Enter a number."))

if num1 > num2 and num1 > num3:
    largest_num = num1
elif num2 > num1 and num2 > num3:
    largest_num = num2
else:
    largest_num = num3
print(f"The largest number is {largest_num}.")
#Identify the Smallest Improve upon your code from Task 1 to also determine the smallest number among the three and print it out.
if num1 < num2 and num1 < num3:
    smallest_num = num1
elif num2 < num1 and num2 < num3:
    smallest_num = num2
else:
    smallest_num = num3
print(f"The smallest number is {smallest_num}.")
#Task3
#Leap Year Checker: Write a Python program that prompts the user to input a year. The program should determine if the given year is a leap year or not and then display an appropriate message. Please note that this is the definition of a leap year: Every year that is exactly divisible by four is a leap year, except for years that are exactly divisible by 100, but these centurial years are leap years if they are exactly divisible by 400.
year = float(input("Enter a year."))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f"{year} is a leap  year.")
else:
    print(f"{year} is not a leap year.")
