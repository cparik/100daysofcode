#!/usr/bin/env python3

""" Perform a variety of manipulations on someone's name
"""

# Imports
from collections import namedtuple

# Constants
FIRST_NAME = 'Tim'
LAST_NAME = 'Hull'

# Create namedtuple for name attributes
Name = namedtuple('Name', 'first last')


def get_name():
    if not FIRST_NAME and LAST_NAME:
        name = Name(
            input('Enter your first name: '),
            input('Enter your last name: ')
        )
    else:
        name = Name(
            FIRST_NAME,
            LAST_NAME
        )

    return name


def name_to_title(name):
    name = name.title()

    return name


def name_to_upper(name):
    name = name.upper()

    return name


def name_to_lower(name):
    name = name.lower()

    return name


def name_to_random(name):
   
    return name
