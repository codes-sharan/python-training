# function in python

# def greet(name):
#     print(f"Hello {name}")
    
# # Call function
# greet("Kamal")
# greet("Gopal")


# def findsum(num1, num2):
#     total=num1+num2
#     print(f"Total is {total}")

# findsum(5, 7)


# Function types
# 1. no paramater and no return type

# def prime_minister():
#     print("Current prime minister is Hari")

# prime_minister()


#2. have parameter, but not return
# def full_name(first_name, last_name):
#     print(f"Full name is {first_name} {last_name}")

# full_name('Gopal', 'Sharma')

# 3. parameter and return type 
# def full_name(first_name, last_name):
#     fullname = f"{first_name} {last_name}"
#     return(fullname)

# fn = full_name("Rahul", "Sharma")
# print(fn)

# 4. no parameter, has return

def voter_age():
    return 18

ram_age = 20

if ram_age >= 18:
    print("Ram is a voter")
else:
    print("Ram is not a voter")
