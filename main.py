# Main file 
# We can demostrate Abstraction here, since we are not showing all the data just the necessary one

from item import Item
from keyboard import Keyboard

item1 = Item("KEY1", 750, 2)

item1.apply_discount()

print(len(str(item1.price)))

print(len(Item.all))

# If we execute this code, we can see the len() funtion in case -
#     1. Gives us the length of the string, outputed by item1.price 
#     2. In second case, len() returns the number of elements in the list Item.all
# This demonstrates Polymorphism, since the same function len() is adapting and doing different jobs according to the condition it is called in






