# Exception handling in python

# try:
#     num1 = float(input("Enter num 1: "))
#     num2 = float(input("Enter num 2: "))
#     sum = num1 + num2
#     print(f"Total is {sum}")

# except:
#     print("Please enter only number")

# finally:
#     print("Program completed")



# try:
#     result = 10/0
# except ZeroDivisionError:
#     print("Error: Cannot divide by zero.")



# try:
#     value = int(input("Enter a number: "))
#     result = 10/value
#     print(result)
# except ValueError:
#     print("Error: Invalid input. Please enter a number")
# except ZeroDivisionError:
#     print("Error: Cannot divide by zero")


############### raising exceptions manually ########
# age = 15
# if age < 18:
#     raise ValueError("You must be at least 18 years old")

#######################

try:
    num = int(input("Please enter a number: "))
    if num % 2 == 0:
        print(f"{num} is even")
    elif num % 2 == 1:
        print(f"{num} is odd")
    else:
        print("Error occurred")

except:
    print("please enter a valid integer")

finally:
    print("Program completed")


