"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates."""

def isBangalore(calllist):
    for item in calllist:
        if item[0].startswith("(080)"):
            return True

def isFixed(calllist):
    for item in calllist:
        if item[1].startswith("("):
            return True

def isMobile(calllist):
    for item in calllist:
        if item[1].startswith("7") or item[1].startswith("8") or item[1].startswith("9"):
            return True

def isTelemark(calllist):
    for item in calllist:
        if item[1].startswith("140"):
            return True

prefixlist=[]
for item in calls:
    if isBangalore(calls) and isFixed(calls) and not isMobile(calls) and not isTelemark(calls):
        pos1=item[1].find("(")
        pos2=item[1].find(")")
        prefix=item[1][pos1:pos2+1]
        prefixlist.append(prefix)

print(prefixlist)
