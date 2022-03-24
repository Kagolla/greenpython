#comparison oerator
amount=int(input("Enter amount"))
discount=amount*float(0.05)
if(amount>=1000):
    print("total is:",amount-discount)
else:
    print("no discount")