import regex as re

with open("trebuchet.txt", "r", encoding="utf8") as f:
    s = f.read().splitlines()

d = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6,
     "seven": 7, "eight": 8, "nine": 9}
d_rx = "|".join(k for k, v in d.items())
rx = fr"(\d|{d_rx})"
nbs = []

for line in s:
    m = re.findall(rx, line, overlapped=True)
    if m[0] in d.keys():
        n1 = str(d[m[0]])
    else:
        n1 = m[0]

    if m[-1] in d.keys():
        n2 = str(d[m[-1]])
    else:
        n2 = m[-1]
    nbs.append(int(n1+n2))

print(sum(nbs))