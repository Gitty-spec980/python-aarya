# def total_calc(bill_amount, tip_perc):
#     tip_amount=bill_amount*tip_perc/100
#     total=bill_amount+tip_amount
#     total = round(total,2)
#     print(f"Please pay ${total}")
# total_calc(100,10)



def factorial(x):
    if x==0 or x == 1:
        return 1
    else:
        return x*factorial(x-1)


print(factorial.__doc__)
print("the factorial of 0:",factorial(0))
print("the factorial of 1:",factorial(1))
print("the factorial of 2:",factorial(2))
print("the factorial of 5:",factorial(5))
print("the factorial of 10:",factorial(10))

    