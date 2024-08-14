"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

phone_numbers = {}

for i in calls:
  if i[0] in phone_numbers:
    phone_numbers[i[0]] = int(phone_numbers[i[0]]) + int(i[3])
  else:
    phone_numbers[i[0]] = int(i[3])
for i in calls:
  if i[1] in phone_numbers:
    phone_numbers[i[1]] = int(phone_numbers[i[1]]) + int(i[3])
  else:
    phone_numbers[i[1]] = int(i[3])

max_phone_number = max(phone_numbers, key = phone_numbers.get)
max_time = max(phone_numbers.values())

print(f"<{max_phone_number}> spent the longest time, <{max_time}> seconds, on the phone during September 2016.")

"""
Running time: O(n)
"""
