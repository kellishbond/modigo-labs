def total_scores(rounds):
    totals = {}
    for round_scores in rounds:
        for player, points in round_scores.items():
            totals[player] = totals.get(player, 0) + points
    return totals

print(total_scores([{"Ada": 5, "Bola": 3}, {"Ada": 2, "Bola": 4}]))
print(total_scores([{"Ada": 10}]))