from client import Client
from bank import Bank


bank = Bank()
print("Welcome to {}!".format(bank.name))

running = True
while running:
    print("""Choose an option:
    1. Open new bank account
    2. Open existing bank account
    3. Exit
    """.format(bank.name))

    choice = int(input("1, 2 or 3: "))

    if choice == 1:
        client = Client(input("Enter your name: "), int(input("Enter your deposit sum: ")))
        bank.update_db(client)
        print("Account created successfully!")
        print("Your account number is: ", client.acc_number)
    elif choice == 2:
        print("Please enter your account credentials below.")
        current_client = bank.verification(input("Name: "), int(input("Account number: ")))
        print("Welcome {}!".format(current_client.name))
        acc_open = True
        while acc_open:
            print("""Choose an option:
                1. Withdraw
                2. Deposit
                3. Balance
                4. Exit
                """)
            acc_choice = int(input("1, 2, 3 or 4: "))
            if acc_choice == 1:
                current_client.withdraw(int(input("Withdraw amount: ")))
            elif acc_choice == 2:
                current_client.deposit(int(input("Deposit amount: ")))
            elif acc_choice == 3:
                current_client.balance()
            elif acc_choice == 4:
                print("Thank you for visiting!")
                current_client = ''
                acc_open = False
    elif choice == 3:
        print("Goodbye!")
        running = False
