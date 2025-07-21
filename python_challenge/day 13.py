def your_vat():
    while True:
        try:
            price = float(input("Input the price of an item: "))
            vat = float(input("Input the VAT (VAT should be a percentage): "))

            if price > 0 and vat > 0:
                percentage = price * (vat / 100)
                total = percentage + price
                print(f"Total price including VAT: {total:.2f}")
                break
            else:
                print("Price and VAT should be positive numbers. Please try again.")
        except ValueError:
            print("Invalid input! Please enter numerical values.")

your_vat()
