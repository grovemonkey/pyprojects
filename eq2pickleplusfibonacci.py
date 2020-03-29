# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 16:42:08 2020

@author: Bill Smith
"""
import pickle

linename = []
linenum = 0
substr = "YOUR"
substr2 = "hits"
substr3 = "Jan 19 14"
with open (r'C:\Users\Public\Daybreak Game Company\Installed Games\EverQuest II\logs\Skyfire\eq2log_kafeh.txt', 'r') as myfile:
	for line in myfile:
		linenum += 1
		if line.find(substr) != -1:
			if line.find(substr2) != -1:
				if line.find(substr3) != -1:
					linename.append(line) # this takes the search parameters and appends the list with that result.
				else:
					continue
			else:
				continue
		else:
			continue
# for item in linename: #using a for loop to print the list in a better format
#     print(item)

with open("test.txt", "wb") as fp:
    pickle.dump(linename, fp)
    
