"""Module representing menus (entire menu) and submenus (breakfast, lunch, dinner etc)."""
import sandwich

class Menu :
    """Represents a larger menu (IE restaurants with no specific breakfast/lunch menu)."""
    def __init__(self, name: str='default') :
        """Initialize menu contents with provided values."""
        # create named dictionary to store menu items
        self.contents = {
            name: {}
        }
    
    def add_item(self, item: sandwich.Sandwich, name: str) :
        """Add a new item to the contents of the menu."""
        self.contents[name] = item
        
    def get_contents(self):
        """Retrieve the contents of this menu object."""
        menu_string = ''
        for item in self.contents:
            menu_string += item + '\n'
        return menu_string

class SubMenu(Menu) :
    """Represents a smaller, sub-menu (IE breakfast menu, lunch menu)."""
    # def __init__(self, name: 'str') :
    #     super.__init__(name)
    #     # create named dictionary to store sub-menu items
    #     self.sub_contents = {

    #     }