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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
telephone_marketing = set()
for call in calls:
  if call[0] not in texts:
    telephone_marketing.add(call[0])

for call in calls:
  if call[1] in telephone_marketing:
    telephone_marketing.remove(call[1])

telephone_marketing = list(telephone_marketing)
telephone_marketing.sort()

print("These numbers could be telemarketers: ")
for telephone in telephone_marketing:
      print(f"<{telephone}>")

"""
Running time: O(n)
"""
