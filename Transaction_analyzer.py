data = [(749.17, "Investment Return"),
  (-11.54, "Utilities"),
  (-247.58, "Online Shopping"),
  (981.17, "Investment Return"),
  (-410.65, "Rent"),
  (310.60, "Rent"),
  (563.70, "Gift"),
  (220.79, "Salary"),
  (-49.85, "Car Maintenance"),
  (308.49, "Salary"),
  (-205.55, "Car Maintenance"),
  (870.64, "Salary"),
  (-881.51, "Utilities"),
  (518.14, "Salary"),
  (-264.66, "Groceries")]

def print_transactions(transactions): #print transactions with format
    for transaction in transactions:
        amount, statement = transaction
        print(f"${amount} - {statement}")
print_transactions(data)

def print_summary(transactions): #function to summarize transactions
    deposits = [transaction[0] for transaction in transactions if transaction[0] >= 0]
    total_deposits = sum(deposits)
    print(f"${total_deposits} deposited")
    withdrawals = [transaction[0] for transaction in transactions if transaction[0] < 0]
    total_withdrawn = sum(withdrawals)
    print(f"${total_withdrawn} withdrawn")
    balance = total_deposits + total_withdrawn
    print(f"Current balance: ${balance}")
print_summary(data)



