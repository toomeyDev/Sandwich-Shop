import sandwich
"""
Contains classes relevant to menu organization and storage
(menus, submenus).
"""
class Menu:
    def __init__(self, **kwargs):
        """Initialize this menu with any provided items."""
        self.items = {}
        for key, value in kwargs.items():
            self.items[key] = value

    def add_item(self, **kwargs):
        """
        Take any number of keyword arguments and add them to
        the items dictionary, inputs should be dictionary or submenu
        type.
        """
        for key, value in kwargs.items():
            self.items[key] = value

    def print_menu(self):
        """Print the contents of this menu, including any submenus."""
        for key, value in self.items.items():
            if(isinstance(value, SubMenu)):
                value.print_menu()
            elif(isinstance(value, sandwich.Sandwich)):
                value.print_sandwich_details()
            else:
                print(f"{key}: {value}")

class SubMenu(Menu):
    """Represents a specialized menu/section part of the larger menu."""
    def __init__(self, title: str, **kwargs):
        """Initialize this submenu with specified title, items."""
        super().__init__(**kwargs)
        self.title = title.title()


    def print_menu(self):
        """
        Print the contents of this submenu, then print out a line
        break sized to match submenu title.
        """
        print(self.title)
        hr = '' # empty line break
        for i in range(len(self.title)):
            hr += '='
        print(hr + "\n") # print properly sized line break

        for key, value in self.items.items():
            if(isinstance(value, sandwich.Sandwich)):
                value.print_sandwich_details()
            else:
                print(f"{key}: {value}")