def points(games):
    return sum([3 if game[0] > game[2] else 1 if game[0] == game[2] else 0 for game in games])

print(points(['1:0','2:0','3:0','4:0','2:1','3:1','4:1','3:2','4:2','4:3']))