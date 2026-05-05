team = {
    "Virat": 180,
    "Rohit": 175,
    "Gill": 178
}

captain = max(team, key=team.get)

print("Captain (tallest):", captain)