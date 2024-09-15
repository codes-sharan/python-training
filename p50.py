# File Handling in Python

# file = open("hello.txt")
# content = file.read()
# print(content)


# file = open("C:\\Users\\shara\\Desktop\\Hi.txt")
# content = file.read()
# print(content)


# file = open("Hi.csv", 'w')
# file.write("Hi, how you doing?")
# file.close()

# file = open("names.csv", 'w')
# file.write("Hari Sharma")
# file.close()


file = open("names.csv", 'a') #append mode 
file.write("\nRam Sharma")
file.close()