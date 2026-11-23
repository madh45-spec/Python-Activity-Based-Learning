# Case Study 7: Tuple-Based Transaction Audit

## 1. Problem Statement

Financial transactions need to be recorded and analysed to maintain accurate account records. This Python program stores transaction details using tuples, separates credit and debit transactions, and calculates the final balance to generate a transaction audit report.

## 2. Objectives

- To collect transaction details.
- To store transaction records using tuples.
- To display transaction information.
- To calculate total credit and debit amounts.
- To determine the final account balance.

## 3. Assumptions

- The user enters the number of transactions.
- Each transaction contains an ID, customer name, amount, and transaction type.
- Transaction types are Credit or Debit.
- Transaction amounts are entered as positive numerical values.
- The final balance is calculated as total credit minus total debit.
- This is an educational audit program, not a real banking system.

## 4. Algorithm

1. Start the program.
2. Read the number of transactions.
3. Create an empty transaction list.
4. For each transaction:
   - Read transaction ID.
   - Read customer name.
   - Read transaction amount.
   - Read transaction type.
   - Store the details in a tuple.
   - Add the tuple to the transaction list.
5. Display all transaction records.
6. Calculate total credit and debit amounts.
7. Calculate the final balance.
8. Display the transaction audit summary.
9. Stop the program.

## 5. Flowchart

Start  
↓  
Enter number of transactions  
↓  
Collect transaction details  
↓  
Create transaction tuple  
↓  
Store tuple in transaction list  
↓  
Display transaction records  
↓  
Check transaction type  
↓  
Calculate total credit and debit  
↓  
Calculate final balance  
↓  
Display audit summary  
↓  
End

## 6. Pseudocode

BEGIN

INPUT number_of_transactions

CREATE empty transactions list

FOR each transaction

    INPUT transaction_id
    INPUT customer_name
    INPUT amount
    INPUT transaction_type

    CREATE tuple containing transaction details

    ADD tuple to transactions list

END FOR

DISPLAY transaction records

SET total_credit = 0
SET total_debit = 0

FOR each transaction

    IF transaction_type = "credit" THEN
        total_credit = total_credit + amount

    ELSE IF transaction_type = "debit" THEN
        total_debit = total_debit + amount

    END IF

END FOR

balance = total_credit - total_debit

DISPLAY total transactions
DISPLAY total credit
DISPLAY total debit
DISPLAY final balance

END

## 7. Python Source Code

The Python program is saved in `transaction.py`.

It uses variables, tuples, lists, loops, conditional statements, tuple indexing, and arithmetic operators to perform transaction auditing.

## 8. Test Cases

| Test Case | Transaction ID | Customer | Amount | Type |
|---|---|---|---:|---|
| TC01 | T101 | Ravi | 5000 | Credit |
| TC02 | T102 | Priya | 2000 | Debit |
| TC03 | T103 | Arun | 3000 | Credit |
| TC04 | T104 | Sneha | 1000 | Debit |

### Expected Results

- Total Transactions: 4
- Total Credit: ₹8000
- Total Debit: ₹3000
- Final Balance: ₹5000

## 9. Output Screenshots

Add screenshots of the successfully executed Python program in the `screenshots` folder.

## 10. Conclusion

The Tuple-Based Transaction Audit program successfully stores and analyses financial transaction records using tuples. It calculates total credits, total debits, and the final balance. This project demonstrates the practical application of Python tuples, lists, loops, conditional statements, and arithmetic operators.