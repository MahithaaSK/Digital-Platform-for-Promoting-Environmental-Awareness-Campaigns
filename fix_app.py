#!/usr/bin/env python
"""Fix duplicate Flask configuration in app.py"""

import re

# Read app.py
with open('app.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find and remove duplicate lines (old hardcoded config at lines 16-19)
# Keep track of what we find
new_lines = []
skip_until = None

for i, line in enumerate(lines):
    # Skip if this is the old hardcoded config (lines 15-18, 0-indexed)
    if i == 15 and "app = Flask(__name__)" in line:
        # Check if next 3 lines are the old config
        if (i + 3 < len(lines) and 
            "app.config['SECRET_KEY'] = 'a_very_secret_key" in lines[i+1] and
            "app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:" in lines[i+2] and
            "app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False" in lines[i+3]):
            # Skip these 4 lines
            skip_until = i + 4
            continue
    
    if skip_until is not None and i < skip_until:
        continue
    else:
        skip_until = None
    
    new_lines.append(line)

# Write back
with open('app.py', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("✓ Fixed duplicate Flask configuration")
