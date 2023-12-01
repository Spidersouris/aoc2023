import re

with open("trebuchet.txt", "r", encoding="utf8") as f:
    s = f.read().splitlines()

rx = r"\d"
nbs = []

for line in s:
    m = re.findall(rx, line)
    number = m[0] + m[-1]
    nbs.append(int(number))

print(sum(nbs))