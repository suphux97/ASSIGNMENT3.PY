def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_percent = price - (price * discount_percent/100)
        return discount_percent
    else:
        return price
    
    def main():
        original_price = float(input("Enter the original price of the item:"))
        discount_percent = float(input("Enter the discount percentage:"))

        final_price = calculate_discount(original_price, discount_percent)

        if final_price == original_price:
            print("No discount applied. Final price:", final_price)
        else:
            print("Final price after applying discount:", final_price)


            if __name__ == "_ _main_ _":
                main()
