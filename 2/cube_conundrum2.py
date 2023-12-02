import re

pws = []

with open("code_conundrum.txt", "r", encoding="utf8") as f:
    for line in f.readlines():
        games = re.sub(r"[\:\,\;]", "", line)

        game_id = int(games.split()[1])

        for game in games:
            game = games.split()
            max_blues = max([int(game[i-1]) for i, x in enumerate(game) if x == "blue"])
            max_reds = max([int(game[i-1]) for i, x in enumerate(game) if x == "red"])
            max_greens = max([int(game[i-1]) for i, x in enumerate(game) if x == "green"])

        pws.append(max_blues*max_reds*max_greens)

print(sum(pws))