# graph.py
# Created: May 29, 2024
# Modified: January 29, 2025
# Purpose: Graphs the occurences that a term appears in a user's messages

import matplotlib.pyplot as plt
import datetime
import json
import os
import string

wordlist = [
    # Example
    "the"
]

# The working directory should be under "messages" in an extracted Discord user data export
dirs = os.listdir(".")
dirs = [d for d in dirs if os.path.isdir(d)]

msgs = []
for sd in dirs:
    print(f"Loading: {sd}/messages.json")
    with open(f"{sd}/messages.json") as f:
        messagesjson = json.loads(f.read())

    msgs += messagesjson

msgcount = len(msgs)
print(f"Messages: {msgcount}")

for label, wordlist in words.items():
    bymonth = {}
    for msg in msgs:
        msgyear = msg["Timestamp"][:7]
        if msgyear not in bymonth:
            bymonth[msgyear] = 0

        # To-Do: have case sensitivity as an option
        if any(word.lower() in msg["Contents"].lower() for word in wordlist):
            bymonth[msgyear] += 1

        bymonth = dict(sorted(bymonth.items()))

    plt.plot(bymonth.keys(), bymonth.values(), label = f"{label}: {', '.join(wordlist)}" )

plt.legend()
plt.xlabel("Years")
plt.ylabel("Occurences")
plt.xticks(rotation=90)

tmpstr = ""
for word in words:
    tmpstr += f"\"{word}\","
words = tmpstr[:-1]

plt.title(f"Messages containing terms by month (not case sensitive)")
plt.show()

