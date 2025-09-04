# Cashier Change Return System
# Author: A.G. Hasan Zarook
a=int(input("enter the total bill amount"))
b=int(input("enter the paid amount by cutomer"))

print("bill is ",a, "pakistan rupees")
print("paid amount is ",b, "pakistan rupees")
if (b>=a):
    c=(b-a)
    print("your balance is",c)
    
    d=(c//5000)
    c= (c-(d*5000))
    
    e=(c//1000)
    c=(c-(e*1000))
    
    f=(c//500)
    c=(c-(f*500))
    
    g=(c//100)
    c=(c-(g*100))

    h=(c//50)
    c=(c-(h*50))

    i=(c//20)
    c=(c-(i*20))

    j=(c//10)
    c=(c-(j*10))

    k=(c//5)
    c=(c-(k*5))

    l=(c//2)
    c=(c-(l*2))

    p=(c//1)
    c=(c-(p*1))
    print("5000rs:",d)
    print("1000rs:",e)
    print("500rs:",f)
    print("100:",g)
    print("50rs:",h)
    print("20rs:",i)
    print("10rs:",j)
    print("5rs:",k)
    print("2rs:",l)
    print("1rs:",p)
else:
    print("paid amount is less than total bill amount")



#Updated Version of code
# Input bill and payment
bill = int(input("Enter the total bill amount: "))
paid = int(input("Enter the paid amount by customer: "))

print(f"\nBill is {bill} Pakistan Rupees")
print(f"Paid amount is {paid} Pakistan Rupees")

if paid >= bill:
    change = paid - bill
    print(f"\nYour balance is {change} PKR\n")

    # Available Pakistani currency denominations
    denominations = [5000, 1000, 500, 100, 50, 20, 10, 5, 2, 1]

    for note in denominations:
        count = change // note
        change = change % note
        if count > 0:
            print(f"{note}rs: {count}")
else:
    print("Paid amount is less than the total bill amount!")

