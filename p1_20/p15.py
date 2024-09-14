# vowel

userinput = input("Enter word: ")

first_char = userinput.lower()[0]

if first_char == 'a' or first_char == 'e' or first_char == 'i' or first_char == 'o' or first_char == 'u':
    print('Word starts with vowel letter')
else:
    print("Word starts with consonant letter")    