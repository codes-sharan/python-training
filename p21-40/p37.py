# dictionary comprehenson in python
# {key_expression: value_expression for item in iterable if condition}



# my_data = {x: x**2 for x in range(1, 6)}
# print(my_data)


student_scores = {"Alice": 85, "Bob": 54, "Charlie": 68, "Mary": 92, "David": 76}
high_scores = {name: val for name, val in student_scores.items() if val>80 }
print(high_scores)
