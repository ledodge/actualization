"""Combine chapters/*.md into one Markdown file for the PDF build."""
import glob, re, sys

SUP = str.maketrans('⁻⁰¹²³⁴⁵⁶⁷⁸⁹', '−0123456789')

parts = []
for path in sorted(glob.glob('chapters/*.md')):
    s = open(path, encoding='utf-8').read()
    s = re.sub(r'^# (.+)$', r'# \1 {.unnumbered}', s, count=1, flags=re.M)   # titles already say "Chapter N"
    s = re.sub(r'^### (.+)$', r'*\1*\n', s, count=1, flags=re.M)               # subtitle as italic line
    s = re.sub(r'10([⁻⁰¹²³⁴⁵⁶⁷⁸⁹]+)', lambda m: '10^' + m.group(1).translate(SUP) + '^', s)
    parts.append(s)
sys.stdout.write('\n\n'.join(parts))
