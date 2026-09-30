from order import add_item


def take_order(menu):
    total_price = 0

    item = input("Enter the name of item you want to order = ")
    total_price = add_item(item, menu, total_price)

    another_order = input(
        "Do you want to add another item to your order? (Yes/No) = "
    )

    while another_order.lower() == "yes":

        item = input("Enter the name of item you want to order = ")
        total_price = add_item(item, menu, total_price)

        another_order = input(
            "Do you want to add another item to your order? (Yes/No) = "
        )

    return total_price
