import sys
import unittest
import os
import importlib
import datetime
from io import StringIO

"""
Student Tests Cases for HW05 - CS1301 Fall 2018
"""

__author__ = "Jasmine & Caitlin"
__version__ = "1"
__email__ = "jyap6@gatech.edu & caitlinyang@gatech.edu"


class TestMyClass(unittest.TestCase):

    def test_yelp_rating_1(self):
        """Failed yelp_rating with 2.0, 3.0, '+'."""
        self.assertEqual(5.0, hw.yelp_rating(2.0,3.0, '+'),
                         msg=error_messages[1])
        del error_messages[1]

    def test_yelp_rating_2(self):
        """Failed yelp_rating with 9.5, 3.0, "/"."""
        self.assertEqual(3.2, hw.yelp_rating(9.5, 3.0, '/'),
                         msg=error_messages[2])
        del error_messages[2]


    def test_register_passport_1(self):
        """Failed to get register_passport of length 3 with 'Damien: 1000, JP'"""
        self.assertEqual(3, len(hw.register_passport("Damien: 1000, JP")),
                         msg=error_messages[3])
        del error_messages[3]

    def test_register_passport_2(self):
        """Failed register_passport with 'Tiffany Mehh: 20, DMK'."""
        self.assertEqual(('DMK', 'Tiffany Mehh', 20), hw.register_passport("Tiffany Mehh: 20, DMK"),
                         msg=error_messages[4])
        del error_messages[4]

    def test_register_passport_3(self):
        """Failed register_passport with 'Jakob: 5, ENG'"""
        self.assertEqual(('ENG', 'Jakob', 5), hw.register_passport("Jakob: 5, ENG"),
                         msg=error_messages[5])
        del error_messages[5]

    def test_register_passport_4(self):
        """Failed register_passport with 'Erica: 22, CHN'"""
        self.assertEqual(('CHN', 'Erica', 22), hw.register_passport("Erica: 22, CHN"),
                         msg=error_messages[6])
        del error_messages[6]

    def test_location_ideas_1(self):
        """Failed to have correct number of items in tuple for location_ideas([('New York', 530), ("Las Vegas",1553), ("Des Moines",600)])."""
        self.assertEqual(3, len(hw.location_ideas([('New York', 530), ("Las Vegas",1553), ("Des Moines",600)])),
                         msg=error_messages[7])
        del error_messages[7]

    def test_location_ideas_2(self):
        """Failed location_ideas with [('Atlanta, GA', 0), ('Seattle, WA', 1500),('LA, CA', 1300),("Austin, TX", 800)]"""
        self.assertEqual(('Atlanta, GA', 'Austin, TX', 'LA, CA', 'Seattle, WA'), hw.location_ideas([("Atlanta, GA", 0), ("Seattle, WA", 1500),("LA, CA", 1300),("Austin, TX", 800)]),
                         msg=error_messages[8])
        del error_messages[8]

    def test_find_airbnb_1(self):
        """Failed find_airbnb with ([("Alaskan Pride", 5, 5, 500),("Tundra Town Tavern", 7, 3.5, 400),("Cave off the side of a Mountain", 6, 4.5, 300)], 6, 430)."""
        list1 = [("Alaskan Pride", 5, 5, 500),("Tundra Town Tavern", 7, 3.5, 400),("Cave off the side of a Mountain", 6, 4.5, 300)]
        self.assertEqual(('Cave off the side of a Mountain', 50.0), hw.find_airbnb(list1, 6, 430),
                         msg=error_messages[9])
        del error_messages[9]

    def test_find_airbnb_2(self):
        """Failed find_airbnb with ([("Icelandic Dream", 4, 5.0, 300), ("Waterfall Mist", 10, 3.0, 200),("Califorinia Dreamin in Iceland", 4, 4.9, 400)], 4, 400)."""
        list3 = [("Icelandic Dream", 4, 5.0, 300), ("Waterfall Mist", 10, 3.0, 200),("Califorinia Dreamin in Iceland", 4, 4.9, 400)]
        self.assertEqual(('Icelandic Dream', 75.0), hw.find_airbnb(list3, 4, 400),
                         msg=error_messages[10])
        del error_messages[10]


    def test_travel_buddy_1(self):
        """Failed travel_buddy with 'Who, 500 ; is, 900 ; the, 80 ; BFF?, 0'"""
        aStr = "Who, 500 ; is, 900 ; the, 80 ; BFF?, 0"
        self.assertEqual(('is', 900), hw.travel_buddy(aStr),
                         msg=error_messages[11])
        del error_messages[11]

    def test_travel_buddy_2(self):
        """Failed travel_buddy with 'James, 220 ; Arushi, 300 ; Jamie, 300 ; James, 1800'"""
        aStr = "James, 220 ; Arushi, 300 ; Jamie, 300 ; James, 1800"
        self.assertEqual(('James', 1800), hw.travel_buddy(aStr),
                         msg=error_messages[12])
        del error_messages[12]

    def test_remove_ingredients_1(self):
        """Failed remove_ingredients with [("Tofu","Pork","Scallions","Peppers"),("Noodle","MSG","PEPPERS"),("Peanut","Jelly") and ["TOFU","rice","msg","nuts"] """
        recipeList = [("Tofu","Pork","Scallions","Peppers"),("Noodle","MSG","PEPPERS"),("Peanut","Jelly")]
        allergyList = ["TOFU","rice","msg","nuts"]
        self.assertEqual([('Pork', 'Scallions', 'Peppers'), ('Noodle', 'PEPPERS'), ('Peanut', 'Jelly')], hw.remove_ingredients(recipeList,allergyList),
                         msg=error_messages[13])
        del error_messages[13]

    def test_remove_ingredients_2(self):
        """Failed remove_ingredients with [("strawberry","cheese","cake"),("oreo","cookies","ice","cream"),("ice","frosting","Cakes"),("banana","split")] and ["ICE","cream","Cake"] """
        recipeList = [("strawberry","cheese","cake"),("oreo","cookies","ice","cream"),("ice","frosting","Cakes"),("banana","split")]
        allergyList = ["ICE","cream","Cake"]
        self.assertEqual([('strawberry', 'cheese'), ('oreo', 'cookies'), ('frosting', 'Cakes'), ('banana', 'split')], hw.remove_ingredients(recipeList,allergyList),
                         msg=error_messages[14])
        del error_messages[14]


error_messages = {
    1: """Failed yelp_rating with 2.0, 3.0, '+'.""",
    2: """Failed yelp_rating with 9.5, 3.0, "/".""",
    3: """Failed to get register_passport of length 3 with 'Damien: 1000, JP'""",
    4: """Failed register_passport with 'Tiffany Mehh: 20, DMK'.""",
    5: """Failed register_passport with 'Jakob: 5, ENG'""",
    6: """Failed register_passport with 'Erica: 22, CHN'""",
    7: """Failed to have correct number of items in tuple for location_ideas([('New York', 530), ("Las Vegas",1553), ("Des Moines",600)]).""",
    8: """Failed location_ideas with [('Atlanta, GA', 0), ('Seattle, WA', 1500),('LA, CA', 1300),("Austin, TX", 800)]""",
    9: """Failed find_airbnb with ([("Alaskan Pride", 5, 5, 500),("Tundra Town Tavern", 7, 3.5, 400),("Cave off the side of a Mountain", 6, 4.5, 300)], 6, 430).""",
    10: """Failed find_airbnb with ([("Icelandic Dream", 4, 5.0, 300), ("Waterfall Mist", 10, 3.0, 200),("Califorinia Dreamin in Iceland", 4, 4.9, 400)], 4, 400).""",
    11: """Failed travel_buddy with 'Who, 500 ; is, 900 ; the, 80 ; BFF?, 0'""",
    12: """Failed travel_buddy with 'James, 220 ; Arushi, 300 ; Jamie, 300 ; James, 1800'""",
    13: """Failed remove_ingredients with [("Tofu","Pork","Scallions","Peppers"),("Noodle","MSG","PEPPERS"),("Peanut","Jelly") and ["TOFU","rice","msg","nuts"] """,
    14: """Failed remove_ingredients with [("strawberry","cheese","cake"),("oreo","cookies","ice","cream"),("ice","frosting","Cakes"),("banana","split")] and ["ICE","cream","Cake"] """
}


if __name__ == '__main__':
    orig_stdout = sys.stdout
    f = open('out.txt', 'w')
    sys.stdout = f

    syntaxError, moduleNotFound, error = False, False, False

    try:
        hw = importlib.import_module('HW05')
    except SyntaxError as e:
        print('-' * 60)
        print('\nSubmission does not compile/run.'
              '\nError Message:\t{}\n'.format(e))
        print('-' * 60)
    except ImportError as e:
        print('-' * 60)
        print('\nFilename is not named HW04.py or file is missing.'
              '\nError Message:\t{}\n'.format(e))
        print('-' * 60)
    except Exception as e:
        print('-' * 60)
        print('\nUNEXPECTED ERROR!\nError Message:\t{}\n'.format(e))
        print('-' * 60)

    try:
        student_name = hw.__author__
    except Exception as e:
        student_name = "NO AUTHOR"

    runner = unittest.TextTestRunner(f)
    unittest.main(testRunner=runner, exit=False)
##
##    try:
##        os.chdir("../")
##        timestamp_file = open('timestamp.txt', 'r')
##        timestamp = timestamp_file.read()
##        timestamp_file.close()
##        y, mo, d, h, m, s = (int(timestamp[:4]), int(timestamp[4:6]),
##                             int(timestamp[6:8]), int(timestamp[8:10]),
##                             int(timestamp[10:12]), int(timestamp[12:14]))
##        submission_date = datetime.datetime(y, mo, d, h, m, s).replace(
##            tzinfo=datetime.timezone.utc).astimezone(tz=None)
##        deadline_date = datetime.datetime(2017, 10, 6, 3, 55, 0).replace(
##            tzinfo=datetime.timezone.utc).astimezone(tz=None)
##        if submission_date > deadline_date:
##            TestMyClass().__class__.score *= 0.75
##            print('Late Submission: {}\nScore: {}/100'.
##                  format(submission_date, TestMyClass().__class__.score))
##        else:
##            print("passed")
##    except Exception as e:
##        print('No timestamp.txt:\nScore: {}/100'.format(
##            TestMyClass().__class__.score))
##
##    sys.stdout = orig_stdout
    f.close()
