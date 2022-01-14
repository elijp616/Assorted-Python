"""
Georgia Institute of Technology - CS1301
HW10 - OOP
"""

__author__ = """ Elijah Peterson """
__collab__ = """ I worked on this assignment alone using only this semester's materials. """

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
        if self.name == other.name and
        self.price == other. price and self.food_type == other.food_type and
        self.calories == other.calories and sorted(self.ingredients) == sorted(other.ingredients):
            return True
        else:
            return False
        
        


    """
    Function name: __str__
    Parameters: Food object
    Returns: str
    """
    def __str__(self):
        return ("{} is a {} that costs ${}.".format(self.name,self.food_type,self.price))

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
        self.total_items = int(len(appetizer_list) + len(entree_list) + len(dessert_list))


    """
    Function name: delete_items
    Parameters: list of Food objects
    Returns: tuple in the following format: (int, boolean)
    """
    def delete_items(self, foods):
        count = 0
        newlist = []
        newtup = ()
        newfood = food.food_type.lower()
        for i in foods:
            if newfood == "appetizer":
                newlist = self.appetizer_list
            elif newfood == "entree":
                newlist = self.entree_list
            elif newfood = "dessert":
                newlist = self.dessert_list
            if i in newlist:
                end = newlist.find(i)
                del(newlist[end])
                count += 1
        self.total_items = int(len(appetizer_list) + len(entree_list) + len(dessert_list))
        if count == len(newlist):
            newtup += count,True
            return newtup
        else:
            newtup += (count,False)
            return newtup

    """
    Function name: add_items
    Parameters: list of Food objects
    Returns: str
    """
    def add_items(self, foods):
        newlist = []
        count = 0
        newfood = food.food_type.lower()
        for i in foods:
            if newfood == "appetizer":
                newlist = self.appetizer_list
            elif newfood == "entree":
                newlist = self.entree_list
            elif newfood = "dessert":
                newlist = self.dessert_list
            if i not in newlist:
                newlist.append(i)
                count += 1
        self.total_items = len(appetizer_list) + len(entree_list) + len(dessert_list)
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
        for i in foods:
            for x in self.allergies:
                if x in food.ingredients:
                    return False
        money = self.wallet - food.price
        if money < 0:
            return False
        else:
            self.wallet = round(money,2)

    """
    Function name: change_servers
    Parameters: Server object
    """
    def change_servers(self, new_server):
        self.server.total_tips += -5
        new_server.total_tips += 5

        self.server.cusomer_list.remove(self)
        new_server.customer_list.append(self)
        self.server = new_server

    """
    Function name: give_tip
    Parameters: int
    """
    def give_tip(self, tip):
        self.server.total_tips += int(tip)
        self.server.customer_list.remove(self)
        money = self.wallet-tip
        self.wallet = round(money,2)

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
        self.restaurant = str(restaurant)
        self.total_tips = 0

    """
    Function name: done_serving
    Parameters: list of Customer objects
    Returns: str
    """
    def done_serving(self, customers):
        for i in customers:
            if i in self.customer_list:
                end = self.customer_list.find(i)
                del(self.customer_list[i])
            else:
                self.customer_list.append(i)
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
