#!/usr/bin/env python3
import ipdb

from classes.national_park import NationalPark
from classes.visitor import Visitor
from classes.trip import Trip

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")

    v1 = Visitor("Jenny")
    v2 = Visitor("Johnny")
    np1 = NationalPark("park1")
    np2 = NationalPark("park2")
    t1 = Trip(v1, np1, "5/31", "5/31")
    t2 = Trip(v1, np2, "5/31", "5/31")
    t3 = Trip(v2, np1, "5/31", "5/31")
    t4 = Trip(v2, np2, "5/31", "5/31")

    ipdb.set_trace()