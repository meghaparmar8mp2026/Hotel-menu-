menu={'vegetable fried rice':100,
      'crispy tacos':50,
      'biryani':35,
      'pav bhaji':80,
      'aloo paratha':65,
      'Vegetable fried rice':100,
      'Crispy tacos':50,
      'Biryani':35,
      'Pav bhaji':80,
      'Aloo paratha':65,
    }
print("Welcome to our restaurant")
print("Vegetable fried rice: Rs.100\nCrispy tacos: Rs.50\nBiryani: Rs.35\nPav bhaji: Rs.80\nAloo paratha: Rs.65")

total_price=0
item_1=input("Enter the name of item you want to order=")
if item_1 in menu:
    total_price+=menu[item_1]
    print(f"Your item{item_1} has been added to your order")
else:
    print(f"Ordered item {item_1} is not available in the menu!")
another_order=input("Do you want to add another item to your order?(Yes/No/yes/no)")
while another_order == "Yes" or another_order == "yes":
    item_2=input("Enter the name of second item you want to order=")
    if item_2 in menu:
        total_price+=menu[item_2]
        print("Item {item_2} has been added to your order")
    else:
        print("Ordered item {item_2} is not available in the menu!")
    another_order=input("Do you want to add another item to your order?(Yes/No/yes/no)")

print(f"The total price of items you ordered is {order_total}")
