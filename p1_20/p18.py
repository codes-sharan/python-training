# string
# str.upper() 
# str.lower()
# str.capitalize() > capitalize first character
# str.title() > capitalize first character of each word
# str.strip() > removes leading or trailing whitespace or special characters (-\n\t)
# str.replace(a,b) > replaces all occurrences of substring a with substring b
# str.split(sep) > splits the string into a list using sep as the delimiter 

#f-string, or formatted string literal > can embed expressions using curly braces {}.
# name = input("Enter your name: ")
# name = name.upper()
# greet = f"Hello {name}, how are you?"
# print(greet)

# name = input("Enter your name: ")
# # name = name.split(' ')[1]
# # name = name.replace('a', 'e')
# name = name.strip('-')
# # name = name.capitalize()
# # name = name.title()
# greet = f"Hello {name}, how are you?"
# print(greet)


names = "hari,gopal,shyam"
lists = names.split(',')
# print(lists)

for n in lists:
    print(n)



