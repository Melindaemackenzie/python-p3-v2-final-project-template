#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
from models.runner import Runner
import ipdb


jane = Runner("Jane", 33, "F", 1)
jane.save()


bob = Runner("Bob", 34, "M", 2)
bob.save()

lisa = Runner.create("Lisa", 29, "F", 2)

cameron = Runner.create("Cameron", 31, "M", 3)
cameron.name = "Cam"
cameron.age = 32
cameron.update()

ipdb.set_trace()
