#!/usr/bin/python3

from math import floor

text = input("Paste text...\n").strip().split(" ")
if len(text)/200 < 1:
    print("~%d seconds reading" % (float(len(text))*0.3))
else:
    print("~%d minutes %d seconds reading" % (floor(len(text)/float(200)), ((len(text)/float(200))-floor(len(text)/float(200)))*60))
