print("====================================")
print("   ELECTRICITY BILLING SYSTEM")
print("====================================")

print("Welcome to the Electricity Billing Program!")

n = int(input("\nEnter number of consumers: "))

consumers = []

for i in range(n):

    print("\nEnter details of Consumer", i + 1)

    name = input("Enter consumer name: ")
    units = float(input("Enter electricity units consumed: "))

    if units < 0:
        print("Invalid units! Please enter a positive value.")
        continue

    if units <= 100:
        bill = units * 1.50

    elif units <= 200:
        bill = (100 * 1.50) + ((units - 100) * 2.50)

    elif units <= 300:
        bill = (100 * 1.50) + (100 * 2.50) + ((units - 200) * 4.00)

    else:
        bill = (100 * 1.50) + (100 * 2.50) + (100 * 4.00) + ((units - 300) * 6.00)

    fixed_charge = 50
    total_bill = bill + fixed_charge

    consumers.append([name, units, bill, total_bill])


print("\n========== ELECTRICITY BILL REPORT ==========")

for consumer in consumers:

    print("\nConsumer Name:", consumer[0])
    print("Units Consumed:", consumer[1])
    print("Energy Charges: Rs.", round(consumer[2], 2))
    print("Fixed Charges: Rs. 50")
    print("Total Bill: Rs.", round(consumer[3], 2))

print("\nTotal Consumers Processed:", len(consumers))

print("\n============================================")
print("          BILLING COMPLETED")
print("============================================")