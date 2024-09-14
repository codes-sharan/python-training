# ATM project

balance = 15000

print("Welcome to SBA[Simple Bank ATM]")

while True:
    input_text = """
   What do you want to do?"
    print("1. Check Balance ")
    print("2. Deposit Amount")
    print("3. Withdraw Amount")
    print("4. Close Program")
    : 
    """

    user_input = int(input(input_text))

    if user_input == 1:
        print(f"Your balance is {balance}")

    elif user_input == 2:
        amount = float(input("Enter amount to deposit: "))
        balance += amount
        print(f"Deposit success. Your new balance is {balance}")

    elif user_input == 3:
        amount = float(input("Enter amount to withdraw: "))
        if balance >= amount:
            balance -= amount
            print(f"Your new balance is {balance}")
        else:
            print("Insufficient balance")
        
    elif user_input ==4:
        print("Thank you for visiting Simple ATM Bank")
        break

    else:
        print("Not valid choice, try again...")
        

    





