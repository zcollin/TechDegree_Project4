import unittest
import work_log
from datetime import datetime
from unittest.mock import patch


class EntryError(unittest.TestCase):

    def test_menu(self):
        result = work_log.menu()
        assert result == print("WORK LOG"
                               "\nWhat would you like to do?\n"
                               "a) Add new entry\n"
                               "b) Search in existing entries\n"
                               "c) Quit the program")

    def test_prompt(self):
        result = work_log.prompt()
        assert result == print("Search Options:"
                               "\na) Find by Employee\n"
                               "b) Find by Date\n"
                               "c) Find by Time Spent\n"
                               "d) Find by Search Term")

    def test_find_name(self):
        with unittest.mock.patch('builtins.input', return_value='zach'):
                assert work_log.find_employee() == print("**********"
                                                         "\nEntry 1:\n"
                                                         "Date: 07/30/2018\n"
                                                         "Name: Zach"
                                                         "Task: Project\n"
                                                         "Time Spent: 90 min"
                                                         "\nNotes: none"
                                                         "**********")

    def test_find_date(self):
        with unittest.mock.patch('builtins.input', return_value='07/30/2018'):
                assert work_log.find_date() == print("**********"
                                                     "\nEntry 1:\n"
                                                     "Date: 07/30/2018\n"
                                                     "Name: Zach"
                                                     "Task: Project\n"
                                                     "Time Spent: 90 min"
                                                     "\nNotes: none"
                                                     "**********")

    def test_find_time(self):
        with unittest.mock.patch('builtins.input', return_value='90'):
                assert work_log.find_time() == print("**********"
                                                     "\nEntry 1:\n"
                                                     "Date: 07/30/2018\n"
                                                     "Name: Zach"
                                                     "Task: Project\n"
                                                     "Time Spent: 90 min"
                                                     "\nNotes: none"
                                                     "**********")

    def test_find_term(self):
        with unittest.mock.patch('builtins.input', return_value='project'):
                assert work_log.find_term() == print("**********"
                                                     "\nEntry 1:\n"
                                                     "Date: 07/30/2018\n"
                                                     "Name: Zach"
                                                     "Task: Project\n"
                                                     "Time Spent: 90 min"
                                                     "\nNotes: none"
                                                     "**********")

if __name__ == '__main__':
    unittest.main()
