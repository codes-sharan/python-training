
# books = ["Book A", "Book B", "Book C", "Book D"]

# for book in books:
#     if book == "Book C":
#         print("Found the book! Stopping search.")
#         break
#     print(f"Checking {book}")
# print("Search ended.")


values = [10, 0, 25, 0, 50, -1, 40]

total = 0
for value in values:
    if value < 0:
        print("negative number found")
        break
    if value == 0:
        print("zero found")
        continue
    total += value
    
print(f"Total is {total}" )
average = total/len(values)
print(f"Average is {average}")


