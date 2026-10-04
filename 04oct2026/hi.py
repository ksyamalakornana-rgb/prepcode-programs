buying_price=int(input("enter the buying price:"))
selling_price=int(input("enter the amount you sold for:"))
total_product=int(input("enter the amount of products:"))
storage_price=int(input("storage amount:"))

profit=((selling_price-buying_price)*total_product-storage_price)

print(f"total profit:{profit}")