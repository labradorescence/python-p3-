#!/usr/bin/env python3
import ipdb

from classes.many_to_many import NationalPark
from classes.many_to_many import Visitor
from classes.many_to_many import Trip

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")

    v1 = Visitor("Jeffrey")
    v2 = Visitor("Zaquari")
    v3 = Visitor("Igor")
    v4 = Visitor("Tyler")

    np1 = NationalPark("Kingston Point Beach")
    np2 = NationalPark("Central Park")

    t1 = Trip(v1, np1, "January 17th", "January 17th")
    t2 = Trip(v1, np2, "January 17th", "January 17th")
    t3 = Trip(v1, np1, "January 17th", "January 17th")
    t4 = Trip(v2, np1, "January 17th", "January 17th")
    t5 = Trip(v4, np1, "January 17th", "January 17th")
    t6 = Trip(v3, np2, "January 17th", "January 17th")

    ipdb.set_trace()
