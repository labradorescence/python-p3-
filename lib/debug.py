#!/usr/bin/env python3
import ipdb

from classes.many_to_many import NationalPark
from classes.many_to_many import Visitor
from classes.many_to_many import Trip

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")

    v1 = Visitor("Hammurabi")
    v2 = Visitor("Hadil")
    v3 = Visitor("Steven")
    v4 = Visitor("Zaquari")

    np1 = NationalPark("Kingston Point Park")
    np2 = NationalPark("Kaaterskill Falls")
    np3 = NationalPark("Central Park")

    t1 = Trip(v1, np1, "September 4th", "September 4th")
    t2 = Trip(v1, np2, "September 4th", "September 4th")
    t3 = Trip(v2, np1, "September 4th", "September 4th")
    t4 = Trip(v2, np2, "September 4th", "September 4th")

    ipdb.set_trace()
