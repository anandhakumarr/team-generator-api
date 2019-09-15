from itertools import combinations
from django.http import JsonResponse
import copy
from api.models import FantacyApp, Match, FantacySport, TeamRequest

def all_in(players, sequence):
    for element in players:
        if element not in sequence:
            return False
    return True


def generate_teams(data):

    teams = []
    try:
        fantacy_app_id = data['fantacy_app_id']
        match_id = data['match_id']
        team1 = data['team1_alias']
        team2 = data['team2_alias']
        players = data['players']

        must_pick_players = []
        for player, data in players.items():
            if data['must_pick']:
                must_pick_players.append(player)
        fantacy_app = FantacyApp.objects.get(pk=fantacy_app_id)
        app_name = fantacy_app.name
        match = Match.objects.get(pk=match_id)
        sport_name = match.sport.name
        fantacy_sport = FantacySport.objects.get(name=match.sport)
        skills = fantacy_sport.skills.split(', ')
        rules = fantacy_sport.fantacy_rules[app_name]

        max_credits = rules['max_credits']
        max_players = rules['max_players']
        max_team_player = rules['max_team_player']
        min_team_player = rules['min_team_player']


        for team in combinations(players.keys(), max_players):
            if all_in(must_pick_players, team):
                team_rules = copy.deepcopy(rules)
                temp_credits = max_credits
                team1_players = 0
                team2_players = 0
                team_list = []
                for row in team:
                    team_dict = {}
                    skill = players[row]['skill']
                    player_team = players[row]['team']
                    if player_team == team1:
                        team1_players += 1
                    if player_team == team2:
                        team2_players += 1
                    credit = players[row]['credit']
                    temp_credits -= credit
                    team_rules[skill]['max_count'] -=1
                    team_dict['player'] = row
                    team_dict['skill'] = skill
                    team_dict['team'] = player_team
                    team_list.append(team_dict)

                players_allowed = False
                if team1_players >= 0 and team2_players >=0 and team1_players+team2_players == max_players:
                    if team1_players <= max_team_player and team2_players >= min_team_player:
                        if team2_players <= max_team_player and team1_players >= min_team_player:
                            players_allowed = True
                    elif team2_players <= max_team_player and team1_players >= min_team_player:
                        if team1_players <= max_team_player and team2_players >= min_team_player:
                            players_allowed = True

                team_allowed = False
                if temp_credits >= 0 and players_allowed:
                    allow = False
                    for skill in skills:
                        skill_count = team_rules[skill]['max_count']
                        if skill_count >= 0 and skill_count < rules[skill]['max_count']:
                            allow = True
                        else:
                            allow = False
                            break
                    if allow:
                        teams.append(team_list)
        TeamRequest(match=match, mustpicks=must_pick_players, teamsgenerated=len(teams)).save()
        
    except:
        pass

    return JsonResponse({'teams': teams, 'team1_color': 'blue', 'team2_color': 'red'})
