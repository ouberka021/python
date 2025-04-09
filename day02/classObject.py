"""
in java
class Item{
String ItemName
String ItemPrice

Item(String ItemName, String ItemPrice) {
this.ItemName =ItemName
this.ItemPrice = ItemPrice
}
}

"""

class Item:
    made_in = 'China' # Static variable
    tariffs = "100%"  # Static variable
    def __init__(self, item_name, item_price):
        self.item_name = item_name  # instance variables
        self.item_price = item_price   # instance variables

    def __str__(self):
        return f'{type(self).__name__} {self.__dict__}'

    """@staticmethod
    def static_method():
        print(f"This is a static method of Item")"""

    @classmethod  # is the same of static method of java
    def class_method(cls): ## only accept static variables
        print(f"This is a class method {cls.made_in}")


"""def __str__(self):
    return f'Name Item {self.item_name}, Item Price {self.item_price}'"""





item1 = Item("Apple", 5)
print(item1)

# access static
print(Item.made_in)
print(Item.tariffs)

# call the class method
print(Item.class_method())