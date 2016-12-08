#!/usr/bin/env python
    
with open('/home/ben/Documents/computer_usage_statistics/histogram.txt', 'r') as myfile:
    data = myfile.read()

splitted_data = data.splitlines()

print "HOUR\tCOUNT"
for idx, data in enumerate(splitted_data):
    print str(idx) + "\t" + str(data)
