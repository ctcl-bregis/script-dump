# notcounted.py - CTCL 2024
# Purpose: Formats a list of GitHub repositories to exclude from Most Used Languages
# Created: December 25, 2024
# Modified: December 25, 2024
# License: The Unlicense

# Example list
repos = [
    "lysine", # Non-original code
    "contactlist-rust", # Superseded
    "ctclsite-python", # Superseded
    "ctclsite-rust", # Superseded
    "slag-rust", # Superseded
    "slag-python", # Superseded
    "todokiosk-python", # Superseded
    "mct2-smec-kernel", # Non-original code
    "pixel-fonts", # C files only store glyphs
]

print(f"https://github-readme-stats.vercel.app/api/top-langs/?username=ctcl-bregis&size_weight=1&count_weight=0&theme=transparent&langs_count=8&exclude_repo={",".join(repos)}")

print(f"Not Counted: {", ".join(repos)}")