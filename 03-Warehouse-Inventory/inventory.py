print("==========================================")
print("       WAREHOUSE INVENTORY SYSTEM")
print("==========================================")

print("Welcome to the Inventory Reconciliation Program!")

n = int(input("\nEnter number of products: "))

inventory = []

# Collect product details
for i in range(n):

    print("\nEnter details of Product", i + 1)

    name = input("Enter product name: ")

    expected = int(input("Enter expected stock quantity: "))
    actual = int(input("Enter actual stock quantity: "))

    if expected < 0 or actual < 0:
        print("Invalid stock quantity! Please enter positive values.")
        continue

    difference = actual - expected

    if difference == 0:
        status = "Stock Matched"

    elif difference > 0:
        status = "Extra Stock"

    else:
        status = "Stock Shortage"

    inventory.append([name, expected, actual, difference, status])


# Display inventory report
print("\n========== INVENTORY RECONCILIATION REPORT ==========")

for product in inventory:

    print("\nProduct Name:", product[0])
    print("Expected Quantity:", product[1])
    print("Actual Quantity:", product[2])
    print("Difference:", product[3])
    print("Status:", product[4])


# Calculate inventory summary
matched = 0
extra = 0
shortage = 0

for product in inventory:

    if product[4] == "Stock Matched":
        matched += 1

    elif product[4] == "Extra Stock":
        extra += 1

    else:
        shortage += 1


# Display summary
print("\n========== INVENTORY SUMMARY ==========")

print("Total Products Processed:", len(inventory))
print("Products with Matched Stock:", matched)
print("Products with Extra Stock:", extra)
print("Products with Shortage:", shortage)

print("\n==========================================")
print("       INVENTORY CHECK COMPLETED")
print("==========================================")