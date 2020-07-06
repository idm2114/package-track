#!/usr/bin/env python

#combining both scripts
#to run from one place easily
#author: ian macleod

from pyfiglet import Figlet
f = Figlet(font="slant")

print(f.renderText("packagetracker"))

import getemails
import inputPackage
import tracker

# print("Thanks for using our basic package tracker!")
