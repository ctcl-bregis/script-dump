# notcounted.py
# Purpose: Formats a list of GitHub repositories to exclude from Most Used Languages
# Created: December 25, 2024
# Modified: May 26, 2025

# Example user
user = "ctcl-bregis"

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

base_url = f"https://github-readme-stats.vercel.app/api/top-langs/?username={user}&size_weight=1&count_weight=0&theme=transparent&langs_count=8&exclude_repo="

print(base_url + ",".join(repos))
