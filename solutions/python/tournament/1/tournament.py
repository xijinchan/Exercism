def tally(rows):
    rows_formatted = [k.split(';') for k in rows]
    teams = list(set([rows_formatted[i][j] for i, k in enumerate(rows_formatted) for j in range(len(rows_formatted[0])) if rows_formatted[i][j] not in ['win', 'loss', 'draw']]))
    scores = []

    for team in teams:
        matches = [k for k in rows_formatted if team in k]
        matches_played = len([k for k in rows_formatted if team in k])
        wins = len([k for k in matches if any([k[0] == team and k[2] == 'win', k[1] == team and k[2] == 'loss'])])
        draws = len([k for k in matches if k[2] == 'draw'])
        losses = len([k for k in matches if any([k[1] == team and k[2] == 'win', k[0] == team and k[2] == 'loss'])])
        points = 3 * wins + draws
        scorecard = {'Team': team, 'MP': matches_played, 'W': wins, 'D':draws, 'L': losses, 'P': points}
        scores.append(scorecard)
        
    scores.sort(key=lambda k: (k['Team']))
    scores.sort(reverse=True, key=lambda k: (k['P']))
    
    output = ['Team                           | MP |  W |  D |  L |  P']

    for x in scores:
        scorecard_formatted = ''.join([x['Team'] + ' '*(30-len(x['Team'])) + ' |',
                                       ' '*(3-len(str(x['MP']))) + str(x['MP']) + ' |',
                                       ' '*(3-len(str(x['W']))) + str(x['W']) + ' |',
                                       ' '*(3-len(str(x['D']))) + str(x['D']) + ' |',
                                       ' '*(3-len(str(x['L']))) + str(x['L']) + ' |',
                                       ' '*(3-len(str(x['P']))) + str(x['P'])])
        output.append(str(scorecard_formatted))
    
    return output