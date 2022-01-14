import sys
import unittest
import os
import importlib
import datetime
from io import StringIO

"""
Student Tests Cases for HW08 - CS1301 Fall 2018
"""

__author__ = "Peter"
__version__ = "1.0"
__email__ = "phan38@gatech.edu"


class TestMyClass(unittest.TestCase):

    def test_get_roster_1(self):
        """Failed get_roster with "studentsTest.txt"."""
        self.assertEqual([('Katsuki', 'Bakugo'), ('Izuku', 'Midoriya'), ('Tenya', 'Iida'), ('Momo', 'Yaoyorozu'), ('Yuga', 'Aoyama'), ('Shoto', 'Todoroki')], hw.get_roster("students_tester.txt"),
                         msg=error_messages[1])
        del error_messages[1]

    def test_get_roster_2(self):
        """Failed get_roster with "fake.txt"."""
        self.assertEqual('File is not found.', hw.get_roster("fake.txt"),
                         msg=error_messages[2])
        del error_messages[2]


    def test_get_average_1(self):
        """Failed get_average with "studentsTest.txt" and "Tenya Iida"."""
        self.assertEqual(('Tenya Iida', 89.5), hw.get_average("students_tester.txt", "Tenya Iida"),
                         msg=error_messages[3])
        del error_messages[3]

    def test_get_average_2(self):
        """Failed get_average with "studentsTest.txt" and "Shawn Mendes"."""
        self.assertEqual('Student not found in file.', hw.get_average("students_tester.txt", "Shawn Mendes"),
                         msg=error_messages[4])
        del error_messages[4]

    def test_get_average_3(self):
        """Failed get_average with "fake.txt" and "Tenya Iida"."""
        self.assertEqual('File is not found.', hw.get_average("fake.txt", "Tenya Iida"),
                         msg=error_messages[5])
        del error_messages[5]

    def test_get_all_averages_1(self):
        """Failed get_all_averages with "studentsTest.txt"."""
        self.assertEqual({'Katsuki': 92.5, 'Izuku': 87.67, 'Tenya': 89.5, 'Momo': 100.0, 'Yuga': 67.67, 'Shoto': 86.0}, hw.get_all_averages("students_tester.txt"),
                         msg=error_messages[6])
        del error_messages[6]

    def test_get_all_averages_2(self):
        """Failed get_all_averages with "fake.txt"."""
        self.assertEqual('File is not found.', hw.get_all_averages("fake.txt"),
                         msg=error_messages[7])
        del error_messages[7]

    def test_form_groups_1(self):
        """Failed form_groups with "fake.txt", "Shawn Mendes" and 3."""
        self.assertEqual('File is not found.', hw.form_groups("fake.txt", "Shawn Mendes", 3),
                         msg=error_messages[8])
        del error_messages[8]

    def test_zero_calorie_diet_1(self):
        """Failed zero_calorie_diet with "menuTest.csv"."""
        self.assertEqual('Steamed Broccoli', hw.zero_calorie_diet("menu_tester.csv"),
                         msg=error_messages[9])
        del error_messages[9]

    def test_zero_calorie_diet_2(self):
        """Failed zero_calorie_diet with "fake.csv"."""
        self.assertEqual('File is not found.', hw.zero_calorie_diet("fake.csv"),
                         msg=error_messages[10])
        del error_messages[10]

    def test_erica_menu_1(self):
        """Failed erica_menu with "fake.csv"."""
        self.assertEqual('File is not found.', hw.erica_menu("fake.csv", 2),
                         msg=error_messages[11])
        del error_messages[11]

error_messages = {
    1: """Failed get_roster with "studentsTest.txt".""",
    2: """Failed get_roster with "fake.txt".""",
    3: """Failed get_average with "studentsTest.txt" and "Tenya Iida".""",
    4: """Failed get_average with "studentsTest.txt" and "Shawn Mendes".""",
    5: """Failed get_average with "fake.txt" and "Tenya Iida".""",
    6: """Failed get_all_averages with "studentsTest.txt".""",
    7: """Failed get_all_averages with "fake.txt".""",
    8: """Failed form_groups with "fake.txt", "Shawn Mendes" and 3.""",
    9: """Failed zero_calorie_diet with "menuTest.csv".""",
    10: """Failed zero_calorie_diet with "fake.csv".""",
    11: """Failed erica_menu with "fake.csv"."""
}


if __name__ == '__main__':
    orig_stdout = sys.stdout
    f = open('out.txt', 'w')
    sys.stdout = f

    syntaxError, moduleNotFound, error = False, False, False

    try:
        hw = importlib.import_module('HW08')
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
    f.close()
