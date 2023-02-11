#!/usr/bin/python

Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'
belgianList = Belgium.split(",")

print("-" * len(Belgium))

print(Belgium.replace(",",":"))

print("The combined population of Belgium and Brussels is {}".format((int(belgianList[1]) + int(belgianList[3]))))
