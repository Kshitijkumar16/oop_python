# Imporing super class 'Item' [Demonstrating inheritance]
from item import Item

# Child/Sub class 'Smartphone' 
class Smartphone(Item):
     # Constructor
    def __init__(self, name: str, price: float, quantity=0, broken_ph=0):
        # Adding a super function to have access to all arguments from parent class
        super().__init__(
            name, price, quantity
        )

        # Validating arguments
        assert broken_ph >= 0, f"Broken {broken_ph} should be greater than or equal to zero!"

        # Assigning parameters to self object
        self.broken_ph = broken_ph
