# Case Study 3: Warehouse Inventory Reconciliation

## 1. Problem Statement

Warehouses need to maintain accurate stock records. Sometimes the actual quantity of products differs from the expected quantity due to errors, missing items, or additional stock. This Python program compares expected and actual stock quantities, identifies differences, and generates an inventory reconciliation report.

## 2. Objectives

- To collect product details and stock quantities.
- To compare expected stock with actual stock.
- To identify extra stock and stock shortages.
- To generate an inventory report.
- To calculate a summary of matched, extra, and shortage products.

## 3. Assumptions

- The user enters the number of products.
- Product names are entered as text.
- Expected and actual quantities are non-negative integers.
- Actual stock is compared with expected stock.
- Equal quantities indicate matched stock.

## 4. Algorithm

1. Start the program.
2. Display the Inventory Management System heading.
3. Read the number of products.
4. Create an empty inventory list.
5. Repeat for each product:
   - Read product name.
   - Read expected stock quantity.
   - Read actual stock quantity.
   - Validate the quantities.
   - Calculate the difference.
   - Identify the stock status.
   - Store the product details in the list.
6. Display the inventory reconciliation report.
7. Count matched, extra, and shortage products.
8. Display the inventory summary.
9. Stop the program.

## 5. Flowchart

Start  
↓  
Enter number of products  
↓  
Collect product details  
↓  
Validate stock quantities  
↓  
Calculate difference  
↓  
Is difference equal to zero?
- Yes → Stock Matched
- No → Is difference positive?
  - Yes → Extra Stock
  - No → Stock Shortage

↓  
Store product details  
↓  
Display inventory report  
↓  
Calculate inventory summary  
↓  
Display summary  
↓  
End

## 6. Pseudocode

BEGIN

INPUT number_of_products

CREATE empty inventory list

FOR each product

    INPUT product_name
    INPUT expected_quantity
    INPUT actual_quantity

    IF expected_quantity < 0 OR actual_quantity < 0 THEN
        DISPLAY "Invalid stock quantity"

    ELSE

        difference = actual_quantity - expected_quantity

        IF difference = 0 THEN
            status = "Stock Matched"

        ELSE IF difference > 0 THEN
            status = "Extra Stock"

        ELSE
            status = "Stock Shortage"

        END IF

        ADD product details to inventory list

    END IF

END FOR

DISPLAY inventory report

SET matched = 0
SET extra = 0
SET shortage = 0

FOR each product in inventory

    COUNT its stock status

END FOR

DISPLAY inventory summary

END

## 7. Python Source Code

The Python program is saved in `inventory.py`.

It uses variables, lists, loops, conditional statements, arithmetic operators, and comparison operators to perform inventory reconciliation.

## 8. Test Cases

| Test Case | Product | Expected Stock | Actual Stock | Expected Result |
|---|---|---:|---:|---|
| TC01 | Laptop | 50 | 50 | Stock Matched |
| TC02 | Mouse | 100 | 120 | Extra Stock |
| TC03 | Keyboard | 80 | 65 | Stock Shortage |
| TC04 | Monitor | 40 | 45 | Extra Stock |

### Expected Summary

- Total Products: 4
- Products with Matched Stock: 1
- Products with Extra Stock: 2
- Products with Shortage: 1

## 9. Output Screenshots

Add screenshots of the successfully executed Python program in the `screenshots` folder.

## 10. Conclusion

The Warehouse Inventory Reconciliation program successfully compares expected and actual stock quantities. It identifies matched stock, extra stock, and shortages and generates a summary report. This project demonstrates the practical use of Python lists, loops, conditional statements, and operators.