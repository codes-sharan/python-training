# list comprehension in python (for, in) (for, in, if) 
# [expression for item in iterable if condition] #syntax

# expression: this is the value that will be added to the list
#  item: each item in the iterable
#  iterable: a collection you are looping over like a list, range etc
# condition (optional): a filter that only includes elements that satisfy the condition


# numbers = [x**2 for x in range (1, 6) ]
# print(numbers)


# scores = [65, 85, 92, 75, 81, 90, 51]
# # filter out scores above 80 using list comprehension
# scores_above_80 = [score for score in scores if score>80]
# print(f"High scores are {scores_above_80}")

# fruits = ['apple', 'mango', 'banana', 'cherry', 'guava', 'grapes', 'plum']
# # filter the fruits with five letters 
# fruits_with_5_letters = [fruit for fruit in fruits if len(fruit)==5]
# print(fruits_with_5_letters)

numbers = [4, 5, 7, 12, 14, 15, 27, 20]
numbers_divisible_by_2 = [number for number in numbers if number % 2 ==0]
print(numbers_divisible_by_2)