"""
Georgia Institute of Technology - CS1301
HW10 - OOP
"""

__author__ = """ Christopher Eckart """
__collab__ = """ I worked on the homework assignment alone, using only this semester's course materials. """

class Food:
    """
    Function name: __init__
    Parameters: str, float, list, str, int
    """
    def __init__(self, name, price, ingredients, food_type, calories):
        self.name = str(name)
        self.price = round(price,2)
        self.ingredients = ingredients
        self.food_type = str(food_type)
        self.calories = int(calories)


    """
    Function name: __eq__
    Parameters: Food object, Food object
    Returns: boolean
    """
    def __eq__(self, other):
        if (self.name == other.name and
            self.price == other.price and
            sorted(self.ingredients) == sorted(other.ingredients) and
            self.food_type == other.food_type and
            self.calories == other.calories):
            return True
        else:
            return False


    """
    Function name: __str__
    Parameters: Food object
    Returns: str
    """
    def __str__(self):
        return "{} is a {} that costs ${}.".format(self.name,self.food_type,self.price)

    """
    Do not modify __repr__ function.
    Leave it in for testing purposes and when
    turning in your HW.
    """
    def __repr__(self):
        return f"{self.name}: {self.price}: {self.food_type}: {self.calories}"

class Menu:
    """
    Function name: __init__
    Parameters: list, list, list
    Remember to also initialize total_items
    """
    def __init__(self, appetizer_list, entree_list, dessert_list):
        self.appetizer_list = appetizer_list
        self.entree_list = entree_list
        self.dessert_list = dessert_list
        self.total_items = int(len(appetizer_list)+len(entree_list)+len(dessert_list))


    """
    Function name: delete_items
    Parameters: list of Food objects
    Returns: tuple in the following format: (int, boolean)
    """
    def delete_items(self, foods):
        # make sure i check later to add a func that checks if "pizza" was in the
        # LIST twice, doesnt just remove it once

        menu = []
        count = 0
        for food in foods:
            
            if food.food_type.lower() == "appetizer":
                menu = self.appetizer_list
            elif food.food_type.lower() == "entree":
                menu = self.entree_list
            elif food.food_type.lower() == "dessert":
                menu = self.dessert_list
            
            if food in menu:            
                index = menu.index(food)
                del menu[index] # should be a reference to self menu, but make sure
                count+=1

        self.total_items = int(len(self.appetizer_list)+len(self.entree_list)+len(self.dessert_list))
        if count == len(menu):
            return (count,True)
        else:
            return (count,False)
        

    """
    Function name: add_items
    Parameters: list of Food objects
    Returns: str
    """
    def add_items(self, foods):
        menu = []
        count = 0
        for food in foods:
            
            if food.food_type.lower() == "appetizer":
                menu = self.appetizer_list
            elif food.food_type.lower() == "entree":
                menu = self.entree_list
            elif food.food_type.lower() == "dessert":
                menu = self.dessert_list

            if food not in menu: # should check __eq__ of every food item, but just be sure
                menu.append(food)
                count+=1

        self.total_items = int(len(self.appetizer_list)+len(self.entree_list)+len(self.dessert_list))
        return "You have added {} items to your menu. Your menu now contains {} total items.".format(count,self.total_items)


    """
    Function name: __str__
    Parameters: Menu object
    Returns: str
    """
    def __str__(self):
        return "There are {} items on the menu. Appetizers are {}. Entrees are {}. Desserts are {}.".format(self.total_items,self.appetizer_list,self.entree_list,self.dessert_list)

    """
    Do not modify __repr__ function.
    Leave it in for testing purposes.
    """
    def __repr__(self):
        return f"Menu: {self.total_items} items"

class Customer:
    """
    Function name: __init__
    Parameters: str, float/int, boolean, list, Server object
    """
    def __init__(self, name, wallet, is_vegetarian, allergies, server):
        self.name = str(name)
        self.wallet = round(wallet,2)
        self.is_vegetarian = bool(is_vegetarian)
        self.allergies = allergies
        self.server = server


    """
    Function name: place_order
    Parameters: list of Food objects, Menu object
    Returns: boolean
    """
    def place_order(self, foods, menu):
        
        for food in foods:
            for allergy in self.allergies:
                if allergy in food.ingredients:
                    return False # am i supposed to return false here or pass
                #else:
            # has cleared allergies, good
            
            if (self.wallet - food.price < 0):
                return False
            else:
                self.wallet = round(self.wallet - food.price,2)

    """
    Function name: change_servers
    Parameters: Server object
    """
    def change_servers(self, new_server):
        self.server.total_tips -= 5
        new_server.total_tips += 5

        self.server.customer_list.remove(self) # should find self w equal attr
        new_server.customer_list.append(self)
        self.server = new_server

    """
    Function name: give_tip
    Parameters: int
    """
    def give_tip(self, tip):
        self.server.total_tips += int(tip)
        self.server.customer_list.remove(self)
        self.wallet = round(self.wallet - tip,2)

    """
    Function name: __str__
    Parameters: Customer object
    Returns: str
    """
    def __str__(self):
        return "{} has ${} and has allergies to {}. Server is {}".format(self.name,self.wallet,self.allergies,self.server.name)

    """
    Do not modify __repr__ function.
    Leave it in for testing purposes.
    """
    def __repr__(self):
        return f"{self.name}: ${self.wallet}, {self.is_vegetarian}, {self.allergies}, {self.server.name}"

class Server:
    """
    Function name: __init__
    Parameters: str, list of Customer objects, int, str
    Remember to also initialize total_tips
    """
    def __init__(self, name, customer_list, restaurant):
        self.name = str(name)
        self.customer_list = customer_list
        self.total_tips = 0
        self.restaurant = str(restaurant)

    """
    Function name: done_serving
    Parameters: list of Customer objects
    Returns: str
    """
    def done_serving(self, customers):
        for customer in customers:
            if customer in self.customer_list:
                index = self.customer_list.index(customer)
                del self.customer_list[index]
            else:
                self.customer_list.append(customer)

        return "{} still has {} customers waiting to be served.".format(self.name,len(self.customer_list))

    """
    Function name: __str__
    Parameters: Server object
    Returns: str
    """
    def __str__(self):
        return "{} is a server.".format(self.name)

    """
    Do not modify __repr__ function.
    Leave it in for testing purposes.
    """
    def __repr__(self):
        return f"server: {self.name}, tips: {self.total_tips}, restaurant: {self.restaurant}"
