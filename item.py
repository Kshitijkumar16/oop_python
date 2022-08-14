
import csv

# Creating a class called 'Item'
class Item:
     pay_rate = 0.8  # Pay rate after a 20% discount

     all = []  # List containing all items in the shop

     # Construtor in python, syntax as: __init__ [From one ofthe magic methods]
     def __init__(self, name: str, price: float, quantity=0):
          # Validating the received arguments
          assert price >= 0, f"Price {price} should be greater than or equal to zero."
          assert quantity >= 0, f"Price {quantity} should be greater than or equal to zero."

          # Assigning parameters to self object
          self.__name = name
          self.__price = price
          self.quantity = quantity

          # Actions to execute
          Item.all.append(self)

     # Decorator @property to disable change of argument
     @property
     def price(self):
          return self.__price
     
     def apply_discount(self):
         self.__price = self.__price * self.pay_rate
         
     def apply_increment(self, inc_value):
          self.__price = self.__price + self.__price * inc_value
          
     # Argument cannot be changed under this decorator, __ is added before the name of argument   
     @property
     # Property attribute = Read-only attribute
     def name(self):
          return self.__name
     
     # Setter helps to validate any change, if needs to be made 
     @name.setter
     def name(self, value):
          if len(value) > 10:
               raise Exception("The name is too long!")
          else:
               self._name = value

     
     def calc_tot_price(self):
         return self.__price * self.quantity

     # Class methods are used when data to be passed through the method is unique 
     @classmethod
     def instantiate_from_csv(cls):
          with open('items.csv', 'r') as f:
               reader = csv.DictReader(f)
               items = list(reader)
          for item in items:
               Item(
                   name = item.get('name'),
                   price = float(item.get('price')),
                   quantity = int(item.get('quantity')),
               )

     # Static method is used when data is generic [or not unique each time]
     @staticmethod
     def is_integer(num):
          # Not counting floats with zero after the decimal point
          if isinstance(num, float):
              # Counting out the floats that are point zero
              return num.is_integer()
          elif isinstance(num, int):
              return True
          else:
              return False

     # Magic method __repr__  is used to represent a class' object as a string
     def __repr__(self):
         return f"{self.__class__.__name__}{self.name}','{self.price}','{self.quantity}')"
