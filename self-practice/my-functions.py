# Odd or Even: Write a function that takes an integer as input and returns "Odd" if the number is odd and "Even" if it is even.


def odd_or_even(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

# num = int(input("Enter a number to check odd/even: "))
# print(odd_or_even(num))


# Sum of a List: Write a function that takes a list of integers and returns the sum of all the numbers.
lst  = [1, 2, 3, 4, 5]

def sum_of_list(lst):
    return sum(lst)

# print(sum_of_list(lst))


# Count Vowels: Write a function that counts the number of vowels in a given string.

def count_vowels(s):
    return sum(1 for c in s if c.lower() in 'aeiou')
    
    
print(count_vowels("Hello World"))

