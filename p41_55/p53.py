# Create a python program that reads a file containing a list of numbers (one number per line) and writes
# the sum of those numbers to another file called sum.txt

with open("hello.txt", "r") as file:
    content = file.read()
    # print(content)


splitted_content = content.split(sep='\n')
print(splitted_content)

print(type(splitted_content[0]))

sum=0
for x in splitted_content:
    sum += int(x)

print(sum)


file = open("sum.txt", 'w')
file.write(f"The sum is {sum}")
file.close()