# randomization

import random

# a = random.random()
# print(a)

# b = random.randint(1 ,100)
# print(b)


# names = ['bimal', 'hari', 'menuka', 'sadikshya']
# random.shuffle(names)
# # print(names)
# print(names[0])



guess = int(input("Enter a number between 1 and 6: "))
random_number = random.randint(1, 6)

if guess == random_number:
    print(f"Your guess is correct, random number was {random_number}")
else:
    print(f"Your guess is not correct, random number was {random_number}")

