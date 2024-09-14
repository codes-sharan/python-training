
expenses = [565, 563, 789, 456, 365, 58]

total = 0
for i in expenses:
    total+=i

print(f"The total expenses is {total}")


average = total/len(expenses)


print(f"The average expenses per person is: {average}")