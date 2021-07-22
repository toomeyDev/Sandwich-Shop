import menu, sandwich, actors, finance

# test menu and sandwich modules
restauruant_menu = menu.Menu()
breakfast_menu = menu.SubMenu("Breakfast")
ham_egg_cheese = sandwich.Sandwich('sandwich', 'wheat bagel', 4.99, 'ham', 'egg', 'cheese')
cream_cheese_bagel = sandwich.Sandwich('bagel', 'white bagel', 2.49, 'cream cheese spread')
breakfast_menu.add_item(Ham_Egg_Cheese=ham_egg_cheese)
breakfast_menu.add_item(Cream_Cheese_Bagel=cream_cheese_bagel)
restauruant_menu.add_item(Breakfast_Menu=breakfast_menu)
restauruant_menu.print_menu()

# test actors module
test_customer = actors.Customer('John Doe', [ham_egg_cheese])
test_employee = actors.Employee('Worker Name', 'Cook')

# test finance module
restauruant_funds = finance.Wallet(500.00, 'Restaurant')
customer_funds = finance.Wallet(53.25, 'John Doe')
finance.transaction(customer_funds, restauruant_funds, 4.99)