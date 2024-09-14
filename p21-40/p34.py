
# set intersection/union/difference/symmetric_difference

course_A_students = {'Alice', 'Charlie', 'Bob'}
course_B_students = {'Charlie', 'David', 'Mary'}

# common_students = course_A_students.intersection(course_B_students)
# print(common_students)

# all_students = course_A_students.union(course_B_students)
# print(all_students)

only_courseA_students = course_A_students.difference(course_B_students)
print(only_courseA_students)