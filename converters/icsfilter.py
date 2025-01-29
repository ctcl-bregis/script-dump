# icsfilter.py
# Purpose: Filters out calendar events from ics data passed from stdin then prints the result to stdout
# Created: September 27, 2024
# Modified: January 29, 2025

import sys
import os
from icalendar import Calendar

# TODO: have this defined by a command line argument
titlebl = "ART.116"

inp = sys.stdin

cal = Calendar.from_ical(inp.read())
newcal = Calendar()
for prop in cal.property_items(recursive=False):
    newcal.add(prop[0], prop[1])

for component in cal.walk():
    if component.get("SUMMARY"):
        if not titlebl in str(component.get("SUMMARY")):
            newcal.add_component(component)

print(newcal.to_ical().decode("utf-8"))
