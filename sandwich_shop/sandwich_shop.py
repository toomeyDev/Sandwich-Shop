import menu, sandwich, actors, finance

# test menu and sandwich modules
print("### Testing menu and sandwich modules ###")
restauruant_menu = menu.Menu()
breakfast_menu = menu.SubMenu("Breakfast")
ham_egg_cheese = sandwich.Sandwich('sandwich', 'wheat bagel', 4.99, 'ham', 'egg', 'cheese')
cream_cheese_bagel = sandwich.Sandwich('bagel', 'white bagel', 2.49, 'cream cheese spread')
breakfast_menu.add_item(Ham_Egg_Cheese=ham_egg_cheese)
breakfast_menu.add_item(Cream_Cheese_Bagel=cream_cheese_bagel)
restauruant_menu.add_item(Breakfast_Menu=breakfast_menu)
restauruant_menu.print_menu()

# test actors module
print("### Testing actors module ###")
test_customer = actors.Customer('John Doe', [ham_egg_cheese, cream_cheese_bagel], 100.00)
print(test_customer.balance.format_balance())
test_employee = actors.Employee('Worker Name', 'Cook')

# test finance module
print("### Testing finance module ###")
restauruant_funds = finance.Wallet(500.00, 'Restaurant')
test_funds = finance.Wallet(53.25, 'Testing')
finance.transaction(test_funds, restauruant_funds, 4.99)

# test ordering
print("### Testing ordering process ###")
test_customer.order_food(restauruant_funds)
print("Current restaurant funding:")
print(restauruant_funds.get_balance())