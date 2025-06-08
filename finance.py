transaction = []

def transactions():
    type = input("select i/e for income and expense respectively: ").lower()
    amount = float(input("Enter amount: "))
    transaction.append({'type': type ,'amount': amount})

def balance():
    income = sum(item['amount'] for item in transaction if item['type']=='i')
    expense = sum(item['amount'] for item in transaction if item['type']=='e')
    balance = income - expense
    print(f"balance : {balance:.2f}")

def view():
    if not transaction:
        print("No transaction")
    else:
        for item in transaction:
            print(f"Type: {item['type']}, Amount: {item['amount']}")
while True:
    print("==financial tracker==")
    print("1.add transaction")
    print("2.view transaction")
    print("3.view balance")
    print("4.exit")

    choice = input("please insert your choice: ")

    if choice == '1':
        transactions()
    elif choice == '2':
        view()
    elif choice == '3':
        balance()
    else:
        print("good bye")
        break
