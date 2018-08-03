"""
A terminal application for logging what work someone did on a certain day.
The data is collected in a database
Author: Zachary Collins
Date: July, 2018
"""

import os

import re

import sys

from datetime import datetime

from peewee import *

# Creates a database
db = SqliteDatabase('log.db')


class Entry(Model):
    name = TextField()
    date = DateTimeField(default=datetime.now())
    task_name = TextField()
    minutes = IntegerField()
    notes = TextField()

    class Meta:
        database = db


def initialize():
    """create the database and the table if they don't exist."""

    db.connect(reuse_if_open=True)
    db.create_tables([Entry], safe=True)


def clear():
    """Clears the contents of the console"""

    os.system('cls' if os.name == 'nt' else 'clear')


def menu():
    """Provides a menu on how to operate the program"""

    clear()
    print("WORK LOG")
    print("What would you like to do?")
    print("a) Add new entry")
    print("b) Search in existing entries")
    print("c) Quit the program")


def run():
    """Runs the core function of the program"""

    initialize()
    menu()
    answer = input().lower()

    # Controls menu choice
    if answer == 'a':
        add_entry()
    elif answer == 'b':
        search()
    elif answer == 'c':
        exit()


def add_entry():
    """Adds the entry to the database"""

    clear()

    # Finds date
    date_in = datetime.now()
    date_in = datetime.strftime(date_in, '%m/%d/%Y')

    # Adds a valid name
    name_in = input("Enter Your Name: ")
    if len(name_in) == 0:
        print("Must enter a Name")
        input("Press ENTER to try again")
        add_entry()

    # Adds a valid task name
    task = input("Enter the Task Name: ")
    if len(task) == 0:
        print("Must enter a Task Name")
        input("Press ENTER to try again")
        add_entry()

    # Adds a valid amount of time
    try:
        time_spent = int(input("Enter the time spent (minutes): "))
    except ValueError:
        print("time spent must be a number")
        input("Press ENTER to try again")
        add_entry()

    # Adds optional notes
    notes_in = input("Enter any additional notes (Optional): ")
    if len(notes_in) == 0:
        notes_in = "none"

    # Adds Entry to database
    Entry.create(name=name_in,
                 date=date_in,
                 task_name=task,
                 minutes=time_spent,
                 notes=notes_in)

    input("\nEntry has been added. Press a key to return to menu. ")
    run()


def prompt():
    """Provides a menu on searching functions"""

    clear()
    print("Search Options:")
    print("a) Find by Employee")
    print("b) Find by Date")
    print("c) Find by Time Spent")
    print("d) Find by Search Term")


def search():
    """Controls the logic of how the user will seach entries"""

    prompt()
    answer = input().lower()

    if answer == 'a':
        find_employee()
    elif answer == 'b':
        find_date()
    elif answer == 'c':
        find_time()
    elif answer == 'd':
        find_term()


def find_employee():
    """Prompts the user to enter a employee name to search for,
    providing all entries containing the employee"""

    clear()

    employee = input("Please enter the name of the employee:\n").lower()
    if len(employee) == 0:
        print("Please enter a search string")
        input("Press ENTER to try again")
        find_employee()

    clear()
    entries = Entry.select().order_by(Entry.date.desc())
    counter = 1
    for entry in entries:
        if employee in entry.name.lower():
            print("*"*10)
            print("Entry {}:\nDate: {}\nName: {}".format(
                counter, entry.date, entry.name))
            print("Task: {}\nTime Spent: {} min \nNotes: {}".format(
                entry.task_name, entry.minutes, entry.notes))
            print("*"*10)
            counter = counter + 1
    if counter == 1:
        print("No entries were found")
        input("Press ENTER to try again")
        find_employee()
    input("Press a key to return to menu: ")
    run()


def find_date():
    """Prompts the user to enter a date to search for,
    providing all entries containing the string"""

    clear()
    dates = []
    entries = Entry.select().order_by(Entry.date.desc())
    for entry in entries:
        if entry.date not in dates:
            dates.append(entry.date)
    print("The following are valid dates of entries:")
    for date in dates:
        print(date)
    search = input("\nEnter the Date (Must be valid)\nUse MM/DD/YYYY: ")
    counter = 0
    if search not in dates:
        find_date()

    counter = 1
    clear()
    for entry in entries:
        if search == entry.date:
            print("*"*10)
            print("Entry {}:\nDate: {}\nName: {}".format(
                counter, entry.date, entry.name))
            print("Task: {}\nTime Spent: {} min \nNotes: {}".format(
                entry.task_name, entry.minutes, entry.notes))
            print("*"*10)
            counter = counter + 1
    input("Press a key to return to menu: ")
    run()


def find_time():
    """Prompts the user to enter an amount of time spent,
    providing all entries containing that time"""

    clear()
    try:
        time = int(input("Please enter the amount of time spent(Minutes):\n"))
    except ValueError:
        print("Please enter a valid time")
        input("Press ENTER to try again")
        find_time()

    clear()
    entries = Entry.select().order_by(Entry.date.desc())
    counter = 1
    for entry in entries:
        if time == entry.minutes:
            print("*"*10)
            print("Entry {}:\nDate: {}\nName: {}".format(
                counter, entry.date, entry.name))
            print("Task: {}\nTime Spent: {} min \nNotes: {}".format(
                entry.task_name, entry.minutes, entry.notes))
            print("*"*10)
            counter = counter + 1
    if counter == 1:
        print("No entries were found")
        input("Press ENTER to try again")
        find_time()
    input("Press a key to return to menu: ")
    run()


def find_term():
    """Prompts the user to enter term to search for,
    providing all entries containing that term"""

    clear()
    term = input("Please enter the desired search:\n").lower()
    if len(term) == 0:
        print("Please enter a search string")
        input("Press ENTER to try again")
        find_term()

    clear()
    entries = Entry.select().order_by(Entry.date.desc())
    counter = 1
    for entry in entries:
        if (term in entry.task_name.lower()) or (term in entry.notes.lower()):
            print("*"*10)
            print("Entry {}:\nDate: {}\nName: {}".format(
                counter, entry.date, entry.name))
            print("Task: {}\nTime Spent: {} min \nNotes: {}".format(
                entry.task_name, entry.minutes, entry.notes))
            print("*"*10)
            counter = counter + 1

    if counter == 1:
        print("No entries were found")
        input("Press ENTER to try again")
        find_term()
    input("Press a key to return to menu: ")
    run()

if __name__ == '__main__':
    run()
