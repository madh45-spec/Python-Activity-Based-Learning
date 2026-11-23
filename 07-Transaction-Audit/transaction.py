print("==========================================")
print("       TRANSACTION AUDIT SYSTEM")
print("==========================================")

n = int(input("\nEnter number of transactions: "))

transactions = []

# Collect transaction details
for i in range(n):

    print("\nEnter details of Transaction", i + 1)

    transaction_id = input("Enter transaction ID: ")
    name = input("Enter customer name: ")
    amount = float(input("Enter transaction amount: "))
    transaction_type = input("Enter type (Credit/Debit): ").lower()

    transaction = (transaction_id, name, amount, transaction_type)

    transactions.append(transaction)


# Display transaction records
print("\n========== TRANSACTION RECORDS ==========")

for transaction in transactions:

    print("\nTransaction ID:", transaction[0])
    print("Customer Name:", transaction[1])
    print("Amount: Rs.", transaction[2])
    print("Transaction Type:", transaction[3])


# Calculate credit and debit totals
total_credit = 0
total_debit = 0

for transaction in transactions:

    if transaction[3] == "credit":
        total_credit += transaction[2]

    elif transaction[3] == "debit":
        total_debit += transaction[2]


# Calculate balance
balance = total_credit - total_debit


# Display audit summary
print("\n========== TRANSACTION AUDIT SUMMARY ==========")

print("Total Transactions:", len(transactions))
print("Total Credit: Rs.", total_credit)
print("Total Debit: Rs.", total_debit)
print("Final Balance: Rs.", balance)

print("\n==========================================")
print("       AUDIT COMPLETED")
print("==========================================")