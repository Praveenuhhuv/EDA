def my_discount():
    price=int(input("Enter the Price: "))
    discount=int(input("Enter the discount percentage: "))
    Discount=price*(discount/100)
    total=price-Discount
    return total

print(my_discount())