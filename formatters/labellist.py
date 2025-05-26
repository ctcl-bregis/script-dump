# labelist.py
# Purpose: Find all labels defined in a hierarchical KiCAD schematic
# Created: May 26, 2025
# Modified: May 26, 2025

import os
import re

root_sch_file = "mct2_lite.kicad_sch"
all_labels = set()
visited_sch_files = set()
label_pattern = re.compile(r'\(\s*(?:label|global_label|hierarchical_label)\s+"([^"]+)"')

# Regex to match hierarchical sheet includes
sheet_file_pattern = re.compile(r'\(sheet\s+[^\(]*\(sheetfile\s+"([^"]+\.kicad_sch)"')

def process_schematic(filepath, base_dir):
    filepath = os.path.abspath(filepath)
    if filepath in visited_sch_files or not os.path.exists(filepath):
        return
    visited_sch_files.add(filepath)

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    labels = label_pattern.findall(content)
    all_labels.update(labels)

    sub_sheets = sheet_file_pattern.findall(content)
    for rel_path in sub_sheets:
        sub_path = os.path.join(base_dir, rel_path)
        process_schematic(sub_path, os.path.dirname(sub_path))

process_schematic(root_sch_file, os.path.dirname(root_sch_file))

print(len(all_labels), "labels found")
for label in sorted(all_labels):
    print(label)
