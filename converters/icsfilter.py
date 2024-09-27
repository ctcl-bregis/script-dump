# iCalendar file filter - CTCL 2024
# Created: September 27, 2024
# Modified: September 27, 2024
# Purpose: Filters out calendar events from ics data passed from stdin then prints the result to stdout

import sys
import os
from icalendar import Calendar

titlebl = ""

inp = sys.stdin

cal = Calendar.from_ical(inp)
newcal = Calendar()
for prop in cal.property_items(recursive=False):
    newcal.add(prop[0], prop[1])

for component in cal.walk():
    if component.get("SUMMARY"):
        if not titlebl in str(component.get("SUMMARY")):
            newcal.add_component(component)

print(newcal.to_ical())
