"""Module representing menus (entire menu) and submenus (breakfast, lunch, dinner etc)."""
import sandwich

class Menu :
    """Represents a larger menu (IE restaurants with no specific breakfast/lunch menu)."""
    def __init__(self, name: 'str') :
        """Initialize menu contents with provided values."""
        # create named dictionary to store menu items
        self.contents = {
            name: {}
        }
        

class SubMenu(Menu) :
    """Represents a smaller, sub-menu (IE breakfast menu, lunch menu)."""
    # def __init__(self, name: 'str') :
    #     super.__init__(name)
    #     # create named dictionary to store sub-menu items
    #     self.sub_contents = {

    #     }