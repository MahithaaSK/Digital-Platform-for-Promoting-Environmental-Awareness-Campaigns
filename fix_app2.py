#!/usr/bin/env python
"""Remove indented Flask configuration that got pasted in the middle of a function"""

with open('app.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
skip_block = False
skip_count = 0

for i, line in enumerate(lines):
    # Check if we're entering the indented Flask config block
    if i > 600 and i < 650 and line.strip().startswith('# Flask Configuration'):
        skip_block = True
        skip_count = 0
        # Count how many lines to skip (the entire indented block)
        for j in range(i, min(i + 30, len(lines))):
            if lines[j].strip() and not lines[j].strip().startswith('#') and not lines[j].startswith('    '):
                # Found the next non-indented line, we should stop
                if j > i + 5:  # But only if we skipped at least a few lines
                    skip_count = j - i
                    break
    
    if skip_block:
        if skip_count > 0:
            skip_count -= 1
            if skip_count == 0:
                skip_block = False
        else:
            skip_block = False
        continue
    
    new_lines.append(line)

# Filter out the misplaced lines (those heavily indented around lines 606-630)
final_lines = []
i = 0
while i < len(new_lines):
    line = new_lines[i]
    # Skip the misplaced indented Flask config
    if (i > 595 and i < 650 and 
        line.startswith('        # Flask Configuration')):
        # Skip until we find the proper "return render_template" line
        while i < len(new_lines) and not ('return render_template' in new_lines[i] and 'messages.html' in new_lines[i]):
            i += 1
        if i < len(new_lines):
            final_lines.append(new_lines[i])
            i += 1
    else:
        final_lines.append(line)
        i += 1

with open('app.py', 'w', encoding='utf-8') as f:
    f.writelines(final_lines)

print("✓ Removed misplaced indented Flask configuration")
