# set in python (example uses: coordinates, which donot require changes)

# fruits = {"Apple", "Mango", "Orange"}
# print(fruits)
# print(fruits[0]) #cannot provide index on set / unordered
# fruits[1] = 'Grapes' #cannot change items 
# print(fruits)


fruits = {"Apple", "Mango", "Orange", "Apple"} #donot add another item (apple)
# print(fruits)

# print("Apple" in fruits) #true
fruits.add("banana")    #adds banana 
# print(fruits)

# fruits.remove("Mango") # removes mango
# print(fruits)

for fruit in fruits:
    print(fruit)