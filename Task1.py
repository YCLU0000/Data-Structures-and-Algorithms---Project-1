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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
phone_number = []
for i in calls:
  if i[0] not in phone_number:
    phone_number.append(i[0])
  elif i[1] not in phone_number:
    phone_number.append(i[1])

for i in texts:
  if i[0] not in phone_number:
    phone_number.append(i[0])
  elif i[1] not in phone_number:
    phone_number.append(i[1])

count = len(phone_number)
print(f"There are <{count}> different telephone numbers in the records.")
