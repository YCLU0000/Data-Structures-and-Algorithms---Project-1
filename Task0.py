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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

first_text = texts[0]
first_text
incoming_number = first_text[0]
answering_number = first_text[1]
time = first_text[2]
print(f"First record of texts, <{incoming_number}> texts <{answering_number}> at time <{time}>")

last_call = calls[len(calls)-1]
last_call
incoming_number = last_call[0]
answering_number = last_call[1]
time = last_call[2]
during = last_call[3]

print(f"Last record of calls, <{incoming_number}> calls <{answering_number}> at time <{time}>, lasting <{during}> seconds")

"""
Running time: O(1)
"""
