def calculate_change(paid, price):
    change=paid-price
    return change
price=100
print("Hello. This snack costs", price, ". These coins are accepted; 1, 5, 10, 25.")

total_inserted=0
coins_inserted=0

while True:
    coin= int(input("Insert a coin (1, 5, 10, 25.)- "))

    if coin !=1 and coin !=5 and coin !=10 and coin !=25:
        print("Invalid coin. Try again.\n")
        continue

    total_inserted+= coin
    coins_inserted+= 1

    print(f"Inserted {coin}. Total so far- {total_inserted}\n")


    if total_inserted>= price:
        print("Enough money inserted.\n")
        break

change_due= calculate_change(total_inserted, price)
print("Dispensing your snack.")

if change_due==0:
    pass
else:
    print(f"Here is you change- {change_due} units")

print("\n===== Purchase Summary =====")
print("Snack Price- ", price,)
print("Coins Inserted- ", coins_inserted,)
print("Total Paid- ", total_inserted,)
print("Change Due- ", change_due,)
print("Thank you for coming and buying something... I guess.")