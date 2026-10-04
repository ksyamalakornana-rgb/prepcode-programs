no_of_items=int(input("enter the products count:"))
products_count_per_box=int(input("enter the box size/box:"))

total_box_needed=no_of_items // products_count_per_box
remaining_items=no_of_items % products_count_per_box

print(f"total boxes needed{total_box_needed} and remaing items:{remaining_items}")