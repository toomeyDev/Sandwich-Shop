"""Manages game-flow and sequencing of events."""
from restaurant import Restaurant

test_location = Restaurant('Testing Grounds', 500)
test_location.add_menu_item("p")
test_location.show_info()