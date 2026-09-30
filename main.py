from menu import menu
from display import display_menu
from customer import take_order


display_menu()

total_price = take_order(menu)

print(f"The total price of items you ordered is Rs.{total_price}")
