amount=int(input("enter the amount:"))
membership=input("does customer have membership? (yes/no):").strip().lower()=="yes"
if (amount >=1000 or membership):
    print(" eligible for free delivery")
else:
    print("not eligible for free delivery")    