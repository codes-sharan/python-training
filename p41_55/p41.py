# OOP in Python
# In OOP first you need to create a class and then an object
# class : blueprint for creating objects

# class Student:
#     def __init__(self, name, grade):
#         self.name = name
#         self.grade = grade
    
#     def get_info(self):
#         return f"Name is {self.name} and grade is {self.grade}"
    
#     def is_passed(self):
#         if self.grade >= 60:
#             return True
#         else:
#             return False


# # Object

# s1 = Student(name='Hari', grade=84)
# s2 = Student(name = 'Ram', grade= 54)
# s3 = Student(name= 'Sita', grade=72)

# print(s1.get_info())
# print(s1.is_passed())


# print(s2.get_info())
# print(s2.is_passed())


# print(s3.get_info())
# print(s3.is_passed())



#################################################

class Laptop:
    def __init__(self, id, name, ram):
        self.id = id
        self.name = name
        self.ram = ram

    def laptop_details(self):
        print (f"Laptop id is {self.id}, Laptop brand is {self.name}. RAM capacity is {self.ram}")

    def is_gaming(self):
        if self.ram >= 8:
            return True
        else:
           return False

laptop1 = Laptop(id = 1, name='DELL', ram = 8)
laptop2 = Laptop(id = 2, name='hp', ram = 4)
laptop3 = Laptop(id = 3, name='acer', ram = 12)


print(laptop1.is_gaming())
print(laptop2.is_gaming())
print(laptop3.laptop_details())