correct_pin = "1234"
balance = 10000
attempts = 3
history = []

while attempts > 0:
    pin = input("Enter your PIN: ")
    if pin == correct_pin:
        print("PIN correct.")
        break
    else:
        attempts = attempts - 1
        if attempts > 0:
            print("Wrong PIN. Attempts left:", attempts)
        else:
            print("Card blocked.")

if attempts > 0:
    while True:
        print("\n----- ATM MENU -----")
        print("1. Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Current balance:", balance)
        elif choice == "2":
            amount = int(input("Enter deposit amount: "))
            if amount > 0:
                balance = balance + amount
                history.append("Deposit " + str(amount))
                print("New balance:", balance)
            else:
                print("Amount must be above 0")
        elif choice == "3":
            amount = int(input("Enter withdrawal amount: "))
            if amount <= 0:
                print("Amount must be above 0")
            elif amount > balance:
                print("Insufficient balance")
            else:
                balance = balance - amount
                history.append("Withdraw " + str(amount))
                print("New balance:", balance)
        elif choice == "4":
            print("Thank you!")
            print("Transaction History:")

            for transaction in history:
                print(transaction)
            break
        else:
            print("Invalid choice")
