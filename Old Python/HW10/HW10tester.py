import unittest
from pathlib import Path
import importlib



"""
HW 10 Student Tester - Fall 2018
"""

__author__ = "1301 TAs"
__version__ = 3.0

class TestMyClass(unittest.TestCase):

    error_messages = {}
    maxDiff = None

    @classmethod
    def set_hw(cls, hw):
        cls.hw = hw

    def test_author(self):
        self.error_messages["author"] = "Missing or empty __author__ global variable."
        self.assertTrue(self.hw.__author__, msg=self.error_messages["author"])
        del self.error_messages["author"]

    def test_collab(self):
        self.error_messages["collab"] = "Missing or empty __collab__ global variable."
        self.assertTrue(self.hw.__collab__, msg=self.error_messages["collab"])
        del self.error_messages["collab"]

    def test_food_init(self):
        func = "Food __init__"
        food1 = self.hw.Food("pasta", 25.777777, ["flour", "salt", "tomatoes", "basil"], "entree", 300)
        student_answer = [food1.name, food1.price, food1.ingredients, food1.food_type, food1.calories]
        ans = ["pasta", 25.78,["flour", "salt", "tomatoes", "basil"], "entree",300]
        message = "Failed {}{} expected '{}'.".format(func, food1, ans)
        self.assertEqual(ans, student_answer,
                         msg=message)


    def test_food_eq(self):
        func = "Food __eq__"
        food1 = self.hw.Food("pasta", 25.777777, ["flour","salt","tomatoes","basil"], "entree", 300)
        food2 = self.hw.Food("pasta", 25.777777, ["flour","salt","tomatoes","basil"], "entree", 300)
        params = food1, food2
        ans = True
        message = "Failed {} {} {} expected '{}'.".format(func, food1, food2, ans)
        self.assertEqual(ans, food1.__eq__(food2),
                         msg=message)

    def test_food_str(self):
        func = "Food __str__"
        params = self.hw.Food("pasta", 25.777777, ["flour","salt","tomatoes","basil"], "entree", 300)
        ans = "pasta is a entree that costs $25.78."
        message = "Failed {}{} expected '{}'.".format(func, params, ans)
        self.assertEqual(ans, self.hw.Food.__str__(params),msg=message)

    def test_menu_init(self):
        func = "Menu __init__"
        food1 = self.hw.Food("guacamole", 7, ["avocado", "tomato", "onion", "cilantro", "green chili"], "appetizer", 400)
        food2 = self.hw.Food("chips&queso", 5.50, ["cheese"], "appetizer", 515)
        food3 = self.hw.Food("ceviche", 11, ["fish", "grapefruit", "lime", "cilantro"], "appetizer", 100)
        food4 = self.hw.Food("pork tamale", 3.50, ["pork", "onion", "corn husk", "cumin", "garlic", "masa harina", "chili"], "entree", 250)
        food5 = self.hw.Food("chile relleno", 6, ["chile", "egg", "queso fresco", "tomato", "flour", "broth"], "entree", 375)
        food6 = self.hw.Food("arroz con leche", 9, ["rice", "cinnamon", "condensed milk", "raisin"], "dessert", 142)
        params = [food1, food2, food3], [food4, food5], [food6]
        menu = self.hw.Menu([food1, food2, food3], [food4, food5], [food6])
        student_answer = [len(menu.appetizer_list), len(menu.entree_list), len(menu.dessert_list), menu.total_items]
        ans = [3,2,1,6]
        message = "Failed {}{}.".format(func, params)
        self.assertEqual(ans, student_answer, msg=message)

    def test_menu_delete_items(self):
        func = "Menu delete_items"
        food1 = self.hw.Food("guacamole", 7, ["avocado", "tomato", "onion", "cilantro", "green chili"], "appetizer", 400)
        food2 = self.hw.Food("chips&queso", 5.50, ["cheese"], "appetizer", 515)
        food3 = self.hw.Food("ceviche", 11, ["fish", "grapefruit", "lime", "cilantro"], "appetizer", 100)
        food4 = self.hw.Food("pork tamale", 3.50, ["pork", "onion", "corn husk", "cumin", "garlic", "masa harina", "chili"], "entree", 250)
        food5 = self.hw.Food("chile relleno", 6, ["chile", "egg", "queso fresco", "tomato", "flour", "broth"], "entree", 375)
        food6 = self.hw.Food("arroz con leche", 9, ["rice", "cinnamon", "condensed milk", "raisin"], "dessert", 142)
        foods = [food1, food2, food3], [food4], [food6]
        menu = self.hw.Menu([food1, food2, food3], [food4], [food6])

        params = [food6,food2,food5]
        ans = (2,False)
        message = "Failed {}{} expected '{}'.".format(func, params, ans)
        self.assertEqual(ans, menu.delete_items(params),msg = message)

        message = "Failed to update total_items with {}{}".format(func,params)
        self.assertEqual(3, menu.total_items, msg = message)

    def test_menu_add_items(self):
        func = "Menu add_items"

        food2 = self.hw.Food("chips&queso", 5.50, ["cheese"], "appetizer", 515)
        menu = self.hw.Menu([food2],[],[])
        food1 = self.hw.Food("guacamole", 7, ["avocado", "tomato", "onion", "cilantro", "green chili"], "appetizer", 400)
        food4 = self.hw.Food("pork tamale", 3.50, ["pork", "onion", "corn husk", "cumin", "garlic", "masa harina", "chili"], "entree", 250)
        food5 = self.hw.Food("chile relleno", 6, ["chile", "egg", "queso fresco", "tomato", "flour", "broth"], "entree", 375)
        food6 = self.hw.Food("arroz con leche", 9, ["rice", "cinnamon", "condensed milk", "raisin"], "dessert", 142)

        params = [food1, food4, food5, food6]
        ans = "You have added 4 items to your menu. Your menu now contains 5 total items."
        message = "Failed {}{} expected '{}'.".format(func, params, ans)
        self.assertEqual(ans, menu.add_items(params),msg = message)

    def test_menu_str(self):
        func = "Menu __str__"

        food1 = self.hw.Food("guacamole", 7, ["avocado", "tomato", "onion", "cilantro", "green chili"], "appetizer", 400)
        food2 = self.hw.Food("chips&queso", 5.50, ["cheese"], "appetizer", 515)
        food3 = self.hw.Food("ceviche", 11, ["fish", "grapefruit", "lime", "cilantro"], "appetizer", 100)
        food4 = self.hw.Food("pork tamale", 3.50, ["pork", "onion", "corn husk", "cumin", "garlic", "masa harina", "chili"], "entree", 250)
        food5 = self.hw.Food("chile relleno", 6, ["chile", "egg", "queso fresco", "tomato", "flour", "broth"], "entree", 375)
        food6 = self.hw.Food("arroz con leche", 9, ["rice", "cinnamon", "condensed milk", "raisin"], "dessert", 142)
        menu = self.hw.Menu([food1,food2,food3],[food4,food5],[food6])

        params = menu
        ans = "There are 6 items on the menu. Appetizers are [guacamole: 7: appetizer: 400, chips&queso: 5.5: appetizer: 515, ceviche: 11: appetizer: 100]. Entrees are [pork tamale: 3.5: entree: 250, chile relleno: 6: entree: 375]. Desserts are [arroz con leche: 9: dessert: 142]."
        message = "Failed {}{} expected '{}'.".format(func, params, ans)
        self.assertEqual(ans,str(menu),msg = message)

    def test_customer_init(self):
        func = "Customer __init__"
        Joe = self.hw.Server("Joe", [], "Olive Garden")
        customer1 = self.hw.Customer("Janet", 22.222, True, ["flour"], Joe)
        student_answer = [customer1.name, customer1.wallet, customer1.is_vegetarian, customer1.allergies, customer1.server]
        ans = ["Janet", 22.22, True, ["flour"], Joe]
        message = "Failed {}{} expected '{}'.".format(func, customer1, ans)
        self.assertEqual(ans, student_answer, msg=message)

    def test_customer_place_order(self):
        func = "Customer place_order"
        Joe = self.hw.Server("Joe", [], "Olive Garden")
        customer1 = self.hw.Customer("Janet", 22.222, True, ["flour", "rice"], Joe)
        food1 = self.hw.Food("guacamole", 7, ["avocado", "tomato", "onion", "cilantro", "green chili"], "appetizer", 400)
        food2 = self.hw.Food("chips&queso", 5.50, ["cheese"], "appetizer", 515)
        food3 = self.hw.Food("ceviche", 11, ["fish", "grapefruit", "lime", "cilantro"], "appetizer", 100)
        food4 = self.hw.Food("pork tamale", 3.50, ["pork", "onion", "corn husk", "cumin", "garlic", "masa harina", "chili"], "entree", 250)
        food5 = self.hw.Food("chile relleno", 6, ["chile", "egg", "queso fresco", "tomato", "flour", "broth"], "entree", 375)
        food6 = self.hw.Food("arroz con leche", 9, ["rice", "cinnamon", "condensed milk", "raisin"], "dessert", 142)
        menu = self.hw.Menu([food1,food2,food3],[food4,food5],[food6])
        ans = False
        message = "Failed {}{} expected '{}'.".format(func, ([food6], menu) , ans)
        self.assertEqual(ans, customer1.place_order([food6], menu),msg = message)

    def test_change_servers(self):
        func = "Customer change_servers"
        Joe = self.hw.Server("Joe", [], "Olive Garden")
        sally = self.hw.Server("sally", [], "Olive Garden")
        customer1 = self.hw.Customer("Janet", 22.222, True, ["flour"], Joe)
        Joe.customer_list.append(customer1)
        customer1.change_servers(sally)
        ans = "sally"
        message = "Failed {}{} expected '{}'.".format(func, customer1.server.name, ans)
        self.assertEqual(ans, customer1.server.name, msg = message)

    def test_customer_give_tip(self):
        func = "Customer give_tip"
        Joe = self.hw.Server("Joe", [], "Olive Garden")
        customer1 = self.hw.Customer("Janet", 22.222, True, ["flour"], Joe)
        Joe.customer_list.append(customer1)
        customer1.give_tip(5)
        ans = 5
        message = "Failed {}{} expected '{}'.".format(func, 5 , ans)
        self.assertEqual(ans, Joe.total_tips , msg = message)

    def test_customer_str(self):
        func = "Customer __str__"
        Joe = self.hw.Server("Joe", [], "Olive Garden")
        params = self.hw.Customer("Janet", 22.222, True, ["flour"], Joe)
        ans = "Janet has $22.22 and has allergies to ['flour']. Server is Joe"
        message = "Failed {}{} expected '{}'.".format(func, params, ans)
        self.assertEqual(ans, self.hw.Customer.__str__(params),msg=message)

    def test_server_init(self):
        func = "Customer __str__"
        server1 = self.hw.Server("Joe", [], "Olive Garden")
        student_answer = [server1.name, server1.customer_list, server1.total_tips, server1.restaurant]
        ans = ["Joe", [], 0, "Olive Garden"]
        message = "Failed {}{} expected '{}'.".format(func, server1, ans)
        self.assertEqual(ans, student_answer,
                         msg=message)

    def test_server_done_serving(self):
        func = "Server done_serving"
        Joe = self.hw.Server("Joe", [], "Olive Garden")
        customer1 = self.hw.Customer("Janet", 22.222, True, ["flour"], Joe)
        customer2 = self.hw.Customer("Jim", 40, False, [], Joe)
        customer3 = self.hw.Customer("Hannah", 80, False, [], Joe)
        customer4 = self.hw.Customer("Ellie", 0, False, ["chicken"], Joe)
        Joe.customer_list.append(customer1)
        Joe.customer_list.append(customer2)
        Joe.customer_list.append(customer3)
        Joe.customer_list.append(customer4)
        student_ans = Joe.done_serving([customer1, customer2])
        ans = "Joe still has 2 customers waiting to be served."
        message = "Failed {}{} expected '{}'.".format(func, student_ans , ans)
        self.assertEqual(ans, student_ans , msg = message)

    def test_server_str(self):
        func = "test_server_str"
        Joe = self.hw.Server("Joe", [], "Olive Garden")
        student_ans = str(Joe)
        ans = "Joe is a server."
        message = "Failed {}{} expected '{}'.".format(func, student_ans, ans)
        self.assertEqual(ans, student_ans, msg = message)


    def test_zeta_error_messages(self):
        """function to compile all errors into one place."""
        errors = [self.error_messages[key] for key in self.error_messages]
        errors_msg = "\n".join(errors)
        self.assertEqual(
            {},
            self.error_messages,
            msg=f'\n\nMissed Tests:\n{errors_msg}'
        )

# imports the student's hw and runs it through the unittests


def run(student_file):
    hw = importlib.import_module(student_file.with_suffix("").name)
    TestMyClass.set_hw(hw)

    print("starting tester")
    with Path("out.txt").open(mode="w") as f:
        runner = unittest.TextTestRunner(f)
        unittest.main(testRunner=runner, exit=False)
    print("sucessfully ran, check out.txt")


# when a python script is run directly (not through import), then it's __name__
# is main and as such should do something. for us, that's testing the hw by
# calling run


if __name__ == "__main__":
    student_file = Path("HW10.py")
    if student_file.exists is False:
        print("Cannot find student's homework file. Make sure it's in the same"
              " folder and is named {}.".format(student_file.name))
    else:
        run(student_file)



