import sys
import unittest
import os
import importlib
import datetime
from io import StringIO

"""
Student Tests Cases for HW04 - CS1301 Fall 2018
"""

__author__ = "Cory & Tiffany"
__version__ = "1"
__email__ = "txu79@gatech.edu & corybrooks@gatech.edu"


class TestMyClass(unittest.TestCase):

    def test_reverse_sentence_1(self):
        """Failed reverse_sentence with 'I love python!!'."""
        self.assertEqual('python!! love I', hw.reverse_sentence('I love python!!'),
                         msg=error_messages[1])
        del error_messages[1]

    def test_reverse_sentence_2(self):
        """Failed reverse_sentence with 'Hello'."""
        self.assertEqual('Hello', hw.reverse_sentence('Hello'),
                         msg=error_messages[2])
        del error_messages[2]

    def test_reverse_sentence_3(self):
        """Failed reverse_sentence with 'let it go'."""
        self.assertEqual('go it let', hw.reverse_sentence('let it go'),
                         msg=error_messages[3])
        del error_messages[3]

    def test_insert_string_1(self):
        """Failed insert_string with 'yummy cake', 'really ', 0."""
        self.assertEqual('really yummy cake', hw.insert_string('yummy cake', 'really ', 0),
                         msg=error_messages[4])
        del error_messages[4]

    def test_insert_string_2(self):
        """Failed insert_string with 'I am bored', ' here', 4."""
        self.assertEqual('I am not bored', hw.insert_string('I am bored', ' not', 4),
                         msg=error_messages[5])
        del error_messages[5]

    def test_insert_string_3(self):
        """Failed insert_string with 'i love python', 'so much', 5."""
        self.assertEqual('i lovso muche python', hw.insert_string('i love python', 'so much', 5),
                         msg=error_messages[6])
        del error_messages[6]

    def test_count_matches_1(self):
        """Failed count_matches with 'lll', 'll'."""
        self.assertEqual(2, hw.count_matches("lll", "ll"),
                         msg=error_messages[7])
        del error_messages[7]

    def test_count_matches_2(self):
        """Failed count_matches with 'po oop', ' op'."""
        self.assertEqual(0, hw.count_matches("po oop", " op"),
                         msg=error_messages[8])
        del error_messages[8]

    def test_count_matches_3(self):
        """Failed count_matches with 'apple', 'pl'."""
        self.assertEqual(1, hw.count_matches("apple", "pl"),
                         msg=error_messages[9])
        del error_messages[9]

    def test_list_symmetric_1(self):
        """Failed list_symmetric with []."""
        self.assertEqual(True, hw.list_symmetric([]),
                         msg=error_messages[10])
        del error_messages[10]

    def test_list_symmetric_2(self):
        """Failed list_symmetric with [3,3]."""
        self.assertEqual(True, hw.list_symmetric([3,3]),
                         msg=error_messages[11])
        del error_messages[11]

    def test_list_symmetric_3(self):
        """Failed list_symmetric with [1,1,3,3,4,4,1]."""
        self.assertEqual(False, hw.list_symmetric([1,1,3,3,4,4,1]),
                         msg=error_messages[12])
        del error_messages[12]

    def test_invite_only_1(self):
        """Failed invite_only with ["Apple", "Pear", "Peach", "Pineapple"] and ["Pineapple"]"""
        line_list = ["Apple", "Pear", "Peach", "Pineapple"]
        invite_list = ["Pineapple"]
        self.assertEqual(["Pineapple"], hw.invite_only(line_list,invite_list),
                         msg=error_messages[13])
        del error_messages[13]

    def test_invite_only_2(self):
        """Failed invite_only with [] and ["Matt Bomer"]"""
        line_list = []
        invite_list = ["Matt Bomer"]
        self.assertEqual([], hw.invite_only(line_list,invite_list),
                         msg=error_messages[14])
        del error_messages[14]

    def test_invite_only_3(self):
        """Failed invite_only with ["Jasmine"] and ["Caitlin", "Jasmine", "Erica"]"""
        line_list =  ["Jasmine"]
        invite_list = ["Caitlin", "Jasmine", "Erica"]
        self.assertEqual(["Jasmine"], hw.invite_only(line_list,invite_list),
                         msg=error_messages[15])
        del error_messages[15]

    def test_grade_counter_1(self):
        """Failed grade_counter with [10,75,30,80], 10 and "C" """
        grade_list = [10,75,30,80]
        extra_credit = 10
        letter_grade ="C"
        self.assertEqual(0, hw.grade_counter(grade_list,extra_credit,letter_grade),
                         msg=error_messages[16])
        del error_messages[16]

    def test_grade_counter_2(self):
        """Failed grade_counter with [90, 91, 80], 9 and "A" """
        grade_list = [90, 91, 80]
        extra_credit = 9
        letter_grade ="A"
        self.assertEqual(2, hw.grade_counter(grade_list,extra_credit,letter_grade),
                         msg=error_messages[17])
        del error_messages[17]

    def test_grade_counter_3(self):
        """Failed grade_counter with [0, 0, 10], 70 and "C" """
        grade_list = [0, 0, 10]
        extra_credit = 70
        letter_grade ="C"
        self.assertEqual(2, hw.grade_counter(grade_list,extra_credit,letter_grade),
                         msg=error_messages[18])
        del error_messages[18]

    def test_study_group_1(self):
        """Failed study_group with ["Cool kid, Computer Science", "Kinda cool kid, Industrial Engineering", "Kid, basket weaving"], and 'Basket Weaving'"""
        student_list = ["Cool kid, Computer Science", "Kinda cool kid, Industrial Engineering", "Kid, basket weaving"]
        major = "Basket Weaving"
        self.assertEqual(['Kid'], hw.study_group(student_list,major),
                         msg=error_messages[19])
        del error_messages[19]

    def test_study_group_2(self):
        """Failed study_group with ["erica, anime watching", "tiffany, food eating", "natalie, Anime watching"] and "Anime watching" """
        student_list = ["erica, anime watching", "tiffany, food eating", "natalie, Anime watching"]
        major = "Anime watching"
        self.assertEqual(['erica', 'natalie'], hw.study_group(student_list,major),
                         msg=error_messages[20])
        del error_messages[20]

    def test_study_group_3(self):
        """Failed study_group with [] and "Art History" """
        student_list = []
        major = "Art History"
        self.assertEqual([], hw.study_group(student_list,major),
                         msg=error_messages[21])
        del error_messages[21]
        
    def test_calculate_gpa_1(self):
        """Failed calculate_gpa with [ [100,4], [73,3], [80,2], [78,3] ]"""
        final_grades = [ [100,4], [73,3], [80,2], [78,3] ]
        self.assertEqual(2.83, hw.calculate_gpa(final_grades),
                         msg=error_messages[22])
        del error_messages[22]

    def test_calculate_gpa_2(self):
        """Failed calculate_gpa with [ [100,2], [73,4], [80,3], [78,3] ]"""
        final_grades = [ [100,2], [73,4], [80,3], [78,3] ]
        self.assertEqual(2.58, hw.calculate_gpa(final_grades),
                         msg=error_messages[23])
        del error_messages[23]

    def test_calculate_gpa_3(self):
        """Failed calculate_gpa with [ [50,2], [97,4], [79,3], [99,2] ]"""
        final_grades = [ [50,2], [97,4], [79,3], [99,2] ]
        self.assertEqual(2.73, hw.calculate_gpa(final_grades),
                         msg=error_messages[24])
        del error_messages[24]

error_messages = {
    1: """Failed reverse_sentence with 'I love python!!'.""",
    2: """Failed reverse_sentence with 'Hello'.""",
    3: """Failed reverse_sentence with 'let it go'.""",
    4: """Failed insert_string with 'yummy cake', 'really ', 0.""",
    5: """Failed insert_string with 'I am bored', ' here', 4.""",
    6: """Failed insert_string with 'i love python', 'so much', 5.""",
    7: """Failed count_matches with 'lll', 'll'.""",
    8: """Failed count_matches with 'po oop', ' op'.""",
    9: """Failed count_matches with 'apple', 'pl'.""",
    10: """Failed list_symmetric with [].""",
    11: """Failed list_symmetric with [3,3].""",
    12: """Failed list_symmetric with [1,1,3,3,4,4,1].""",
    13: """Failed invite_only with ["Apple", "Pear", "Peach", "Pineapple"] and ["Pineapple"]""",
    14: """Failed invite_only with [] and ["Matt Bomer"]""",
    15: """Failed invite_only with ["Jasmine"] and ["Caitlin", "Jasmine", "Erica"]""",
    16: """Failed grade_counter with [10,75,30,80], 10 and "C" """,
    17: """Failed grade_counter with [90, 91, 80], 9 and "A" """,
    18: """Failed grade_counter with [0, 0, 10], 70 and "C" """,
    19: """Failed study_group with ["Cool kid, Computer Science", "Kinda cool kid, Industrial Engineering", "Kid, basket weaving"], and 'Basket Weaving'""",
    20: """Failed study_group with ["erica, anime watching", "tiffany, food eating", "natalie, Anime watching"] and "Anime watching" """,
    21: """Failed study_group with [] and "Art History" """,
    22: """Failed calculate_gpa with [ [100,4], [73,3], [80,2], [78,3] ]""",
    23: """Failed calculate_gpa with [ [100,2], [73,4], [80,3], [78,3] ]""",
    24: """Failed calculate_gpa with [ [50,2], [97,4], [79,3], [99,2] ]"""    

}


if __name__ == '__main__':
    orig_stdout = sys.stdout
    f = open('out.txt', 'w')
    sys.stdout = f

    syntaxError, moduleNotFound, error = False, False, False

    try:
        hw = importlib.import_module('HW04')
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

    sys.stdout = orig_stdout
    f.close()
