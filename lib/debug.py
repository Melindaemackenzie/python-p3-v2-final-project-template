#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
from models.athlete import Athlete
from models.race import Race
import ipdb;

def reset_database():
    Athlete.drop_table()
    Athlete.create_table()
    Race.drop_table()
    Race.create_table()

reset_database()



jane = Athlete("Jane", 33, "F", 1)
jane.save()


bob = Athlete("Bob", 34, "M", 2)
bob.save()

lisa = Athlete.create("Lisa", 29, "F", 2)

cameron = Athlete.create("Cameron", 31, "M", 3)
cameron.name = "Cam"
cameron.age = 32
cameron.update()

ipdb.set_trace()
