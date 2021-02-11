

def climbingLeaderboard(ranked, player_scores):
    ranked_unique = list(dict.fromkeys(ranked)) #https://stackoverflow.com/questions/7961363/removing-duplicates-in-the-lists
    
    player_ranks = []
    iter_start = len(ranked_unique) - 1

    for score in player_scores:

        if score >= ranked_unique[0]: #if score is greater than or equal to winning score
            player_ranks.append(1)
        else:
            for i in range(iter_start, -1, -1):
                if score < ranked_unique[i]:
                    player_ranks.append(i + 2)
                    iter_start = i
                    break
    
    return player_ranks

print(climbingLeaderboard([100, 100, 50, 40, 40, 20, 10], [5, 25, 50, 120]))
print(climbingLeaderboard([100, 90, 90, 80, 75, 60], [50, 65, 77, 90, 102]))