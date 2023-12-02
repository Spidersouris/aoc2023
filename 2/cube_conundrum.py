import re

possible_game_ids = []

with open("code_conundrum.txt", "r", encoding="utf8") as f:
    for line in f.readlines():
        ok = False
        games = re.sub(r"[\:\,]", "", line)

        game_id = int(games.split()[1])

        sets = games.split(";")

        for s in sets:
            s = s.split()
            nb_blues = sum([int(s[i-1]) for i, x in enumerate(s) if x == "blue"])
            nb_reds = sum([int(s[i-1]) for i, x in enumerate(s) if x == "red"])
            nb_greens = sum([int(s[i-1]) for i, x in enumerate(s) if x == "green"])

            if (nb_blues > 14 or nb_greens > 13 or nb_reds > 12):
                ok = False
                break

            ok = True

        if ok:
            possible_game_ids.append(game_id)

print(sum(possible_game_ids))