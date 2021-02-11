

def climbingLeaderboard(ranked, player_scores):
    ranked_unique = list(dict.fromkeys(ranked)) #https://stackoverflow.com/questions/7961363/removing-duplicates-in-the-lists
    
    player_ranks = []

    for score in player_scores:

        if score < ranked[-1]: #if score is less than lowest score on the leaderboard
            player_ranks.append(len(ranked_unique) + 1)
        else:
            for i in range(len(ranked_unique)):
                if score >= ranked_unique[i]:
                    player_ranks.append(i + 1)
                    break

    
    
    return player_ranks

print(climbingLeaderboard([100, 100, 50, 40, 40, 20, 10], [5, 25, 50, 120]))
print(climbingLeaderboard([100, 90, 90, 80, 75, 60], [50, 65, 77, 90, 102]))