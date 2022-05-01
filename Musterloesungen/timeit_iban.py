#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 16:22:34 2022

@author: rene
"""

import timeit
import ibantools, ibantools2


def validiere1(iban):
    return ibantools.validiere(iban)

def validiere2(iban):
    return ibantools2.validiere(iban)


if __name__ == "__main__":
    t1 = timeit.Timer("validiere1('IBAN CH82 0900 0000 1001 5000 6')", globals=globals())
    t2 = timeit.Timer("validiere2('IBAN CH82 0900 0000 1001 5000 6')", globals=globals())

    print("ibantools:  ", t1.timeit())
    print("ibantools2: ", t2.timeit())

    print("ibantools:  ", min(t1.repeat(100, 10000)))
    print("ibantools2: ", min(t2.repeat(100, 10000)))
