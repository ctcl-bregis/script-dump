# CalDAV to Task List Text - CTCL 2024
# Created: May 20, 2024
# Modified: May 22, 2024
# Purpose: Reads tasks from a CalDAV calendar and prints a text to-do list

# Pip Requirements:
# caldav
# icalendar

# -- Configuration --

# Server URL, not the calendar URL
dav_url = ""
# CalDAV Username
username = ""
# CalDAV Password
password = ""
# Name of the calendar
cal_name = ""

# Text to show for status
status = {
    "NEEDS-ACTION": ":grey_exclamation:",
    "IN-PROCESS": ":gear:"
}

# Show or hide task based on classification
classification = {
    "None": True,
    "PRIVATE": False
}

showfooter = True

# -- End of Configuration --

import caldav
import icalendar
import os
from datetime import datetime
from datetime import timezone
client = caldav.DAVClient(dav_url, username = username, password = password)

calendars = []
tasks = []

for todo in client.principal().calendar(cal_name).todos():
    calendars.append(icalendar.Calendar.from_ical(todo.data))

for calendar in calendars:
    for vtask in calendar.walk("VTODO"):
        task = {}
        task["class"] = str(vtask.get("CLASS"))
        task["status"] = str(vtask.get("STATUS"))
        task["priority"] = str(vtask.get("PRIORITY"))
        task["summary"] = str(vtask.get("SUMMARY"))
        tasks.append(task)

# Get list of tasks without a priority and a list of tasks that do have a priority
taskswithpriority = []
taskswithoutpriority = []
for task in tasks:
    if task["priority"] == "0":
        taskswithoutpriority.append(task)
    else:
        taskswithpriority.append(task)

taskswithpriority = sorted(taskswithpriority, key=lambda d: d["priority"], reverse = False)
tasks = taskswithpriority + taskswithoutpriority

for task in tasks:
    if classification[task["class"]]: 
        print(f"- {status[task['status']]} - {task['summary']}")



if showfooter:
    curtime = datetime.now(tz = timezone.utc).strftime("%b %-d, %Y, %H:%M %Z")
    print(f"CTCL caldav2text.py - {cal_name} {curtime}")