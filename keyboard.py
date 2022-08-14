# File containing sub class 'Keyboard'

from item import Item   # Importing super class

class Keyboard(Item):
     pay_rate = 0.7
     # Constructor 
     def __init__(self, name: str, price: float, quantity=0):
        # Adding a super function to have access to all arguments from parent class
        super().__init__(
            name, price, quantity
        )

