from itertools import combinations

team1 = "MUM"
team2 = "PAT"

players = {
    "Pardeep" : {
        "credit": 17,
        "team": "PAT",
        "must_pick": True,
        "skill": "raider"
    },
    "AthulMS": {
        "credit": 13.5,
        "team": "MUM",
        "must_pick": False,
        "skill": "raider"
    },
    "Baliyan": {
        "credit": 15,
        "team": "MUM",
        "must_pick": False,
        "skill": "raider"
    },
    # "Esmaeil": {
    #     "credit": 14.5,
    #     "team": "PAT",
    #     "must_pick": False,
    #     "skill": "raider"
    # },
    "Lee": {
        "credit": 14.5,
        "team": "PAT",
        "must_pick": False,
        "skill": "raider"
    },
    "Narwal": {
        "credit": 14.5,
        "team": "MUM",
        "must_pick": False,
        "skill": "all_rounder"
    },
    "Jaglan": {
        "credit": 14,
        "team": "PAT",
        "must_pick": True,
        "skill": "all_rounder"
    },
    # "Monu": {
    #     "credit": 13,
    #     "team": "MUM",
    #     "must_pick": False,
    #     "skill": "all_rounder"
    # },
    "Deshwal": {
        "credit": 11.5,
        "team": "MUM",
        "must_pick": True,
        "skill": "raider"
    },
    "Atrachali": {
        "credit": 15,
        "team": "MUM",
        "must_pick": False,
        "skill": "defender"
    },
    "SurenderSingh": {
        "credit": 14,
        "team": "MUM",
        "must_pick": True,
        "skill": "defender"
    },
    "Jaideep": {
        "credit": 13.5,
        "team": "PAT",
        "must_pick": True,
        "skill": "defender"
    },
    "Chango": {
        "credit": 12,
        "team": "MUM",
        "must_pick": False,
        "skill": "defender"
    },
    "Neeraj": {
        "credit": 12,
        "team": "PAT",
        "must_pick": False,
        "skill": "defender"
    }
}

max_raiders = 3
max_credits = 100
max_allrounders = 2
max_players = 7
max_defenders = 4
max_team_player = 4


def all_in(players, sequence):
    for element in players:
        if element not in sequence:
            return False
    return True

must_pick_players = []
for player, data in players.iteritems():
    if data['must_pick']:
        must_pick_players.append(player)

teams = []
for team in combinations(players.keys(), 7):
    if all_in(must_pick_players, team):
        temp_credits = max_credits
        temp_raiders = max_raiders
        temp_allrounders = max_allrounders
        temp_defenders = max_defenders
        team1_players = max_team_player
        team2_players = max_team_player
        for row in team:
            skill = players[row]['skill']
            player_team = players[row]['team']
            if player_team == team1:
                team1_players -= 1
            if player_team == team2:
                team2_players -= 1
            credit = players[row]['credit']
            temp_credits -= credit
            if skill == 'raider':
                temp_raiders -= 1
            if skill == 'defender':
                temp_defenders -= 1
            if skill == 'all_rounder':
                temp_allrounders -= 1

        players_allowed = False
        if team1_players == 1 and team2_players == 0:
            players_allowed = True
        elif team2_players == 1 and team1_players == 0:
            players_allowed = True

        if temp_raiders >= 0 and temp_allrounders >= 0 and temp_defenders >= 0 and temp_credits > 0 and players_allowed:
            print team2_players, team1_players
            teams.append(team)


print "*"*25
if len(teams) == len(set(teams)):
    print "No duplicate teams"
print "*"*25
print "Total Teams - {}".format(len(teams))
for row in teams:
    print row






from itertools import combinations

team1 = "JAI"
team2 = "GUJ"

players = {
    "Salunke": {
        "credit": 13.5,
        "team": "JAI",
        "must_pick": False,
        "skill": "raider"
    },
    "Jaglan": {
        "credit": 13.5,
        "team": "GUJ",
        "must_pick": False,
        "skill": "raider"
    },
    "Tanwar": {
        "credit": 15.5,
        "team": "GUJ",
        "must_pick": False,
        "skill": "raider"
    },
    "Gulia": {
        "credit": 14.5,
        "team": "GUJ",
        "must_pick": False,
        "skill": "all_rounder"
    },
    "Niwas": {
        "credit": 15.5,
        "team": "JAI",
        "must_pick": True,
        "skill": "all_rounder"
    },
    "Sunil": {
        "credit": 15,
        "team": "GUJ",
        "must_pick": False,
        "skill": "defender"
    },
    "Bhainwal": {
        "credit": 15,
        "team": "GUJ",
        "must_pick": False,
        "skill": "defender"
    },
    "Ankit": {
        "credit": 11,
        "team": "GUJ",
        "must_pick": False,
        "skill": "defender"
    },
    "SandeepKumar": {
        "credit": 14.5,
        "team": "JAI",
        "must_pick": False,
        "skill": "defender"
    },
    "AHooda": {
        "credit": 14.5,
        "team": "JAI",
        "must_pick": False,
        "skill": "defender"
    }
}

max_raiders = 3
max_credits = 100
max_allrounders = 2
max_players = 7
max_defenders = 4
max_team_player = 5


def all_in(players, sequence):
    for element in players:
        if element not in sequence:
            return False
    return True

must_pick_players = []
for player, data in players.iteritems():
    if data['must_pick']:
        must_pick_players.append(player)

teams = []
for team in combinations(players.keys(), 7):
    if all_in(must_pick_players, team):
        temp_credits = max_credits
        temp_raiders = max_raiders
        temp_allrounders = max_allrounders
        temp_defenders = max_defenders
        team1_players = max_team_player
        team2_players = max_team_player
        total_points = 0
        for row in team:
            skill = players[row]['skill']
            player_team = players[row]['team']
            if player_team == team1:
                team1_players -= 1
            if player_team == team2:
                team2_players -= 1
            credit = players[row]['credit']
            temp_credits -= credit
            if skill == 'raider':
                temp_raiders -= 1
            if skill == 'defender':
                temp_defenders -= 1
            if skill == 'all_rounder':
                temp_allrounders -= 1
            # total_points += players[row]['points']
        allowed = False
        if team1_players >= 0 and team2_players == 3:
            allowed = True
        if team2_players >= 0 and team1_players == 3:
            allowed = True

        if temp_raiders >= 0 and temp_allrounders >= 0 and temp_defenders >= 0 and temp_credits > 0 and allowed:
            # print team, temp_credits
            teams.append(team)


print "*"*25
if len(teams) == len(set(teams)):
    print "No duplicate teams"
print "*"*25
print "Total Teams - {}".format(len(teams))
for row in teams:
    print row



Football



from itertools import combinations

team1 = "CAR"
team2 = "RDG"

players = {
    "Alex" : {
        "credit": 9,
        "team": "CAR",
        "must_pick": False,
        "skill": "goalkeeper"
    },
    "Rafael" : {
        "credit": 8.5,
        "team": "RDG",
        "must_pick": False,
        "skill": "goalkeeper"
    },
    "Sean" : {
        "credit": 10,
        "team": "CAR",
        "must_pick": False,
        "skill": "defender"
    },
    "MattMia" : {
        "credit": 9.5,
        "team": "RDG",
        "must_pick": False,
        "skill": "defender"
    },
    "Liam" : {
        "credit": 9.5,
        "team": "RDG",
        "must_pick": False,
        "skill": "defender"
    },
    "Aden" : {
        "credit": 9.5,
        "team": "CAR",
        "must_pick": False,
        "skill": "defender"
    },
    "Michael" : {
        "credit": 9,
        "team": "RDG",
        "must_pick": False,
        "skill": "defender"
    },
    "Andy" : {
        "credit": 8.5,
        "team": "RDG",
        "must_pick": False,
        "skill": "defender"
    },
    "Omar" : {
        "credit": 8.5,
        "team": "RDG",
        "must_pick": False,
        "skill": "defender"
    },
    "Joe" : {
        "credit": 8.5,
        "team": "CAR",
        "must_pick": False,
        "skill": "defender"
    },
    "David" : {
        "credit": 9.5,
        "team": "CAR",
        "must_pick": False,
        "skill": "midplayer"
    },
    "John" : {
        "credit": 9,
        "team": "RDG",
        "must_pick": False,
        "skill": "midplayer"
    },
    "JoeRalls" : {
        "credit": 9,
        "team": "CAR",
        "must_pick": False,
        "skill": "midplayer"
    },
    "Bacuna" : {
        "credit": 9,
        "team": "CAR",
        "must_pick": False,
        "skill": "midplayer"
    },
    "Nathaniel" : {
        "credit": 9,
        "team": "CAR",
        "must_pick": False,
        "skill": "midplayer"
    },
    "Ovie" : {
        "credit": 8.5,
        "team": "RDG",
        "must_pick": False,
        "skill": "midplayer"
    },
    "Pele" : {
        "credit": 8.5,
        "team": "RDG",
        "must_pick": False,
        "skill": "midplayer"
    },
    "Marlon" : {
        "credit": 8.5,
        "team": "CAR",
        "must_pick": False,
        "skill": "midplayer"
    },
    "Will" : {
        "credit": 8,
        "team": "CAR",
        "must_pick": False,
        "skill": "midplayer"
    },
    "George" : {
        "credit": 9,
        "team": "RDG",
        "must_pick": False,
        "skill": "forwarder"
    },
    "Lucas" : {
        "credit": 9,
        "team": "RDG",
        "must_pick": False,
        "skill": "forwarder"
    },
    "Robert" : {
        "credit": 8.5,
        "team": "CAR",
        "must_pick": False,
        "skill": "forwarder"
    }
}

max_forwarders = 4
max_midplayers = 2
max_defenders = 4
max_goalkeeper = 1
max_credits = 100
max_players = 11
max_team_player = 7
min_team_player = 4


def all_in(players, sequence):
    for element in players:
        if element not in sequence:
            return False
    return True

must_pick_players = []
for player, data in players.iteritems():
    if data['must_pick']:
        must_pick_players.append(player)

teams = []
for team in combinations(players.keys(), 7):
    if all_in(must_pick_players, team):
        temp_credits = max_credits
        temp_forwarders = max_forwarders
        temp_midplayers = max_midplayers
        temp_defenders = max_defenders
        temp_goalkeeper = max_goalkeeper
        team1_players = max_team_player
        team2_players = max_team_player
        for row in team:
            skill = players[row]['skill']
            player_team = players[row]['team']
            if player_team == team1:
                team1_players -= 1
            if player_team == team2:
                team2_players -= 1
            credit = players[row]['credit']
            temp_credits -= credit
            if skill == 'forwarder':
                temp_forwarders -= 1
            if skill == 'defender':
                temp_defenders -= 1
            if skill == 'midplayer':
                temp_midplayers -= 1
            if skill == 'goalkeeper':
                temp_goalkeeper -= 1

        players_allowed = False
        if team1_players <= max_team_player and team2_players >= min_team_player:
            players_allowed = True
        elif team2_players <= max_team_player and team1_players >= min_team_player:
            players_allowed = True

        if temp_forwarders >= 0 and temp_midplayers >= 0 and temp_defenders >= 0 and temp_goalkeeper >0 and temp_credits > 0 and players_allowed:
            teams.append(team)




for row in teams:
    print row
print "*"*25
if len(teams) == len(set(teams)):
    print "No duplicate teams"
print "*"*25
print "Total Teams - {}".format(len(teams))
