def add_item(item, menu, total_price):
    if item in menu:
        total_price += menu[item]
        print(f"Your item {item} has been added to your order")
    else:
        print(f"Ordered item {item} is not available in the menu!")

    return total_price
