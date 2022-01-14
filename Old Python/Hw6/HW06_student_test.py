import sys
import unittest
import os
import importlib
import datetime
from io import StringIO

"""
Student Tests Cases for HW06 - CS1301 Fall 2018
"""

__author__ = "Eddy & Peter"
__version__ = "1.0"
__email__ = "echiao6@gatech.edu & phan38@gatech.edu"


class TestMyClass(unittest.TestCase):

    def test_make_gamertag_1(self):
        """Failed make_gamertag with 'MonkaS.' and [0,1,6,10]"""
        self.assertEqual('[Mxox00]', hw.make_gamertag('MonkaS', [0,1,6,10]),
                         msg=error_messages[1])
        del error_messages[1]

    def test_make_gamertag_2(self):
        """Failed make_gamertag with 'thats a bettt' and [-0,10,20,30,40]."""
        self.assertEqual('[txtx000]', hw.make_gamertag('thats a bettt', [-0,10,20,30,40]),
                         msg=error_messages[2])
        del error_messages[2]


    def test_split_the_loot_1(self):
        """Failed split_the_loot with {"Chicken": 6.85, "Beef": 7.50, "Chorizo": 7.15}, ["Chicken", "Chorizo"], 17.38, and 4."""
        a = {"Chicken": 6.85, "Beef": 7.50, "Chorizo": 7.15}
        b = ["Chicken", "Chorizo"]
        c = 17.38
        d = 4
        answer = 7.84
        self.assertEqual(answer, hw.split_the_loot(a, b, c, d),
                         msg=error_messages[3])
        del error_messages[3]

    def test_split_the_loot_2(self):
        """Failed split_the_loot with {"TV": 599, "Computer": -100, "Exodia": 9000}, ["TV", "yuhyeet", "Computer"], 525600, and 9."""
        a = {"TV": 599, "Computer": -100, "Exodia": 9000}
        b = ["TV", "yuhyeet", "Computer"]
        c = 525600
        d = 9
        answer = "Negative"
        self.assertEqual(answer, hw.split_the_loot(a, b, c, d),
                         msg=error_messages[4])
        del error_messages[4]
        
    def test_split_the_loot_3(self):
        """Failed split_the_loot with {"Guitar": 500.123, "Piano": 800, "Flute": 321.9999}, ["guitar", "Piano"], 300, and 11."""
        a = {"Guitar": 500.123, "Piano": 800, "Flute": 321.9999}
        b = ["guitar", "Piano"]
        c = 300
        d = 11
        answer = 100.0
        self.assertEqual(answer, hw.split_the_loot(a, b, c, d),
                         msg=error_messages[5])
        del error_messages[5]

    def test_football_stars_1(self):
        """Failed football_stars with {"Texas": ["Cowboys", "Texans"], "Colorado": ["Broncos"]} and {"Falcons": "Calvin Ridley", "Patriots": "Tom Brady"}"""
        a = {"Texas": ["Cowboys", "Texans"], "Colorado": ["Broncos"]}
        b = {"Falcons": "Calvin Ridley", "Patriots": "Tom Brady"}
        self.assertEqual({}, hw.football_stars(a, b),
                         msg=error_messages[6])
        del error_messages[6]

    def test_football_stars_2(self):
        """Failed register_passport with 'Erica: 22, CHN'"""
        a = {"Maryland": ["Ravens"], "Minnesota": ["Vikings"]}
        b = {"Ravens": "Alex Collins", "Vikings": "Stefon Diggs"}
        answer = {'Alex Collins': ('Maryland', 'Ravens'), 'Stefon Diggs': ('Minnesota', 'Vikings')}
        self.assertEqual(answer, hw.football_stars(a, b),
                         msg=error_messages[7])
        del error_messages[7]

    def test_pair_rivals_1(self):
        """Failed pair_rivals with {"Guy Lee": "Kakashi", "Peter": "Caitlin", "Android": "Apple"} and {"Android": "Apple", "Kakashi": "Guy Lee"}."""
        a = {"Guy Lee": "Kakashi", "Peter": "Caitlin", "Android": "Apple"}
        b = {"Android": "Apple", "Kakashi": "Guy Lee"}
        answer = {('Guy Lee', 'Kakashi'): True}
        self.assertEqual(answer, hw.pair_rivals(a, b),
                         msg=error_messages[8])
        del error_messages[8]

    def test_pair_rivals_2(self):
        """Failed pair_rivals with {"Kanye West": "Taylor Swift", "Messi": "Ronaldo"} and {"Taylor Swift": "Ex-Boyfriends"}"""
        a = {"Kanye West": "Taylor Swift", "Messi": "Ronaldo"}
        b = {"Taylor Swift": "Ex-Boyfriends"}
        answer = {}
        self.assertEqual(answer, hw.pair_rivals(a, b),
                         msg=error_messages[9])
        del error_messages[9]

    def test_zoo_keeper_1(self):
        """Failed zoo_keeper with [('mammal', 'doge', 4), ('mammal', 'doge', 37), ('human', 'Peter', 8)]."""
        list1 = [('mammal', 'doge', 4), ('mammal', 'doge', 37), ('human', 'Peter', 8)]
        self.assertEqual({'mammal': {'doge': 41}, 'human': {'Peter': 8}}, hw.zoo_keeper(list1),
                         msg=error_messages[10])
        del error_messages[10]


    def test_zoo_keeper_2(self):
        """Failed zoo_keeper with [('bird', 'rat', 4), ('mammal', 'rat', 37), ('reptile', 'rat', 8), ('fish', 'rat', 2)]"""
        list2 = [('bird', 'rat', 4), ('mammal', 'rat', 37), ('reptile', 'rat', 8), ('fish', 'rat', 2)]
        self.assertEqual({'bird': {'rat': 4}, 'mammal': {'rat': 37}, 'reptile': {'rat': 8}, 'fish': {'rat': 2}}, hw.zoo_keeper(list2),
                         msg=error_messages[11])
        del error_messages[11]

    def test_animal_locator_1(self):
        """Failed animal_locator with {'Bronx': [('lion', 4), ('snake', 4), ('tiger', 4)], 'Atlanta': [('lion', 4), ('snake', 4), ('bee', 4)], 'Orlando': [('bee', 4), ('tiger', 4)]}"""
        dict1 = {'Bronx': [('lion', 4), ('snake', 4), ('tiger', 4)], 'Atlanta': [('lion', 4), ('snake', 4), ('bee', 4)], 'Orlando': [('bee', 4), ('tiger', 4)]}
        self.assertEqual({'lion': (['Bronx', 'Atlanta'], 8), 'snake': (['Bronx', 'Atlanta'], 8), 'tiger': (['Orlando', 'Bronx'], 8), 'bee': (['Orlando', 'Atlanta'], 8)}, hw.animal_locator(dict1),
                         msg=error_messages[12])
        del error_messages[12]

    def test_animal_locator_2(self):
        """Failed animal_locator with {'San Diego': [('lion', 4), ('lion', 2), ('lion', 8)], 'Bronx': [('tiger', 20), ('tiger', 5), ('tiger', 1)], 'Atlanta': [('snake', 3), ('snake', 2), ('snake', 4500)], 'Orlando': [('bee', 234), ('bee', 123)]}"""
        dict2 = {'San Diego': [('lion', 4), ('lion', 2), ('lion', 8)], 'Bronx': [('tiger', 20), ('tiger', 5), ('tiger', 1)], 'Atlanta': [('snake', 3), ('snake', 2), ('snake', 4500)], 'Orlando': [('bee', 234), ('bee', 123)]}
        self.assertEqual({'lion': (['San Diego'], 14), 'tiger': (['Bronx'], 26), 'snake': (['Atlanta'], 4505), 'bee': (['Orlando'], 357)}, hw.animal_locator(dict2),
                         msg=error_messages[13])
        del error_messages[13]


error_messages = {
    1: """Failed make_gamertag with 'MonkaS.' and [0,1,6,10].""",
    2: """Failed make_gamertag with 'thats a bettt' and [-0,10,20,30,40].""",
    3: """Failed split_the_loot with {"Chicken": 6.85, "Beef": 7.50, "Chorizo": 7.15}, ["Chicken", "Chorizo"], 17.38, and 4.""",
    4: """Failed split_the_loot with {"TV": 599, "Computer": -100, "Exodia": 9000}, ["TV", "yuhyeet", "Computer"], 525600, and 9.""",
    5: """Failed split_the_loot with {"Guitar": 500.123, "Piano": 800, "Flute": 321.9999}, ["guitar", "Piano"], 300, and 11.""",
    6: """Failed football_stars with {"Texas": ["Cowboys", "Texans"], "Colorado": ["Broncos"]} and {"Falcons": "Calvin Ridley", "Patriots": "Tom Brady"}""",
    7: """Failed football_stars with {"Maryland": ["Ravens"], "Minnesota": ["Vikings"]} and {"Ravens": "Alex Collins", "Vikings": "Stefon Diggs"}""",
    8: """Failed pair_rivals with {"Guy Lee": "Kakashi", "Peter": "Caitlin", "Android": "Apple"} and {"Android": "Apple", "Kakashi": "Guy Lee"}.""",
    9: """Failed pair_rivals with {"Kanye West": "Taylor Swift", "Messi": "Ronaldo"} and {"Taylor Swift": "Ex-Boyfriends"}""",
    10: """Failed zoo_keeper with ([('mammal', 'doge', 4), ('mammal', 'doge', 37), ('human', 'Peter', 8)]).""",
    11: """Failed zoo_keeper with [('bird', 'rat', 4), ('mammal', 'rat', 37), ('reptile', 'rat', 8), ('fish', 'rat', 2)].""",
    12: """Failed animal_locator with {'Bronx': [('lion', 4), ('snake', 4), ('tiger', 4)], 'Atlanta': [('lion', 4), ('snake', 4), ('bee', 4)], 'Orlando': [('bee', 4), ('tiger', 4)]}.""",
    13: """Failed animal_locator with {'San Diego': [('lion', 4), ('lion', 2), ('lion', 8)], 'Bronx': [('tiger', 20), ('tiger', 5), ('tiger', 1)], 'Atlanta': [('snake', 3), ('snake', 2), ('snake', 4500)], 'Orlando': [('bee', 234), ('bee', 123)]}."""
}


if __name__ == '__main__':
    orig_stdout = sys.stdout
    f = open('out.txt', 'w')
    sys.stdout = f

    syntaxError, moduleNotFound, error = False, False, False

    try:
        hw = importlib.import_module('HW06')
    except SyntaxError as e:
        print('-' * 60)
        print('\nSubmission does not compile/run.'
              '\nError Message:\t{}\n'.format(e))
        print('-' * 60)
    except ImportError as e:
        print('-' * 60)
        print('\nFilename is not named HW06.py or file is missing.'
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
