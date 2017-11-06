import teams
import players
import random
import itertools
from operator import itemgetter

def suggester():

    for team_name in teams.allTeams:
        pos_list = [[], [], [], []]
        for player in teams.allTeams[team_name].player_list:
            if player.position.lower() == 'g': pos_list[0].append(player)
            if player.position.lower() == 'd': pos_list[1].append(player)
            if player.position.lower() == 'm': pos_list[2].append(player)
            if player.position.lower() == 'f': pos_list[3].append(player)

            teams.allTeams[team_name].pl_pos = pos_list


    group_1 = [teams.allTeams['Chelsea FC'], teams.allTeams['Manchester City FC'],
               teams.allTeams['Liverpool FC'], teams.allTeams['Arsenal FC'],
               teams.allTeams['Manchester United FC']]
    
    group_2 = [teams.allTeams['Tottenham Hotspur FC'], teams.allTeams['Everton FC']]
    group_3 = [teams.allTeams['Southampton FC'], teams.allTeams['Bournemouth']]
    group_4 = [teams.allTeams['West Bromwich Albion FC'], teams.allTeams['Leicester City FC']]


    grouplist = [group_1, group_2, group_3, group_4]

    
    for team_name in teams.allTeams:
        teams.allTeams[team_name].sug_list = [[],[],[],[]]

    

    n = 0
    while n < 4: #accessing positions
        for group in range(len(grouplist)):#financial groups
            for team in grouplist[group]: #teams in the group
                for person in team.pl_pos[n]: #player
                    for market_group in range(group, len(grouplist)): #financially LESSER GRPS
                        
                        for market_team in grouplist[market_group]: #team you wanna buy from
                            if team != market_team: #team not yours
                                for market_person in market_team.pl_pos[n]: #player i wanna buy
                                    if market_person.new_rating > person.new_rating:
                                        s = str(market_person.name) + ' for ' + str(person.name)
                                        team.sug_list[n].append(s)

        
        n += 1



def get_Fixtures(allTeams):
    l = len(allTeams)
    keys = tuple(allTeams.keys())
    hl = list(keys)
    al = list(keys)
    random.shuffle(hl)
    random.shuffle(al)
    indprod = list(itertools.product(xrange(l), xrange(l))) #cartesian product of indices
    random.shuffle(indprod)
    for i, j in indprod:
        if hl[i] != al[j]:      # So you dont play against yourself
            yield (allTeams[hl[i]], allTeams[al[j]])
    del indprod

def Simulate(allTeams):
    results = []
    curStanding = allTeams.values()
    #curStanding.sort()
    for home, away in get_Fixtures(allTeams):
        gd = home.homematch(away)
        loss_score = int(random.normalvariate(1.5, 0.75))
        s = "{:^s} %d - {:^s} %d".format(home.name, away.name)
        if gd < 0:
            results.append(s%(loss_score, loss_score + abs(gd)))
            home.match_det[(home.name, away.name)] = match_details(home, away, loss_score, loss_score + abs(gd))
            away.match_det[(home.name, away.name)] = match_details(home, away, loss_score, loss_score + abs(gd))
        else:
            results.append(s%(loss_score + gd, loss_score))
            home.match_det[(home.name, away.name)] = match_details(home, away, loss_score + gd, loss_score)
            away.match_det[(home.name, away.name)] = match_details(home, away, loss_score + gd, loss_score)
        home.fixtures_results.append(s)
        away.fixtures_results.append(s)
    curStanding.sort()
    return curStanding[::-1], results

def match_details(home, away, h_score, a_score):
    time = range(1, 91)
    det = []
    if h_score > 0:
        hometeam = home.player_list
        for goal in xrange(h_score):
            chosen = False
            while not chosen:
                player = random.choice(hometeam)
                if player.position.lower() == 'g':
                    chosen = False
                elif player.position.lower() == 'd':
                    chosen = random.choice([False, False, False, True, True])
                elif player.position.lower() == 'm':
                    chosen = random.choice([False, True, True, True, True])
                elif player.position.lower() == 'f':
                    chosen = True

            minute = random.choice(time)
            for m in xrange(minute - 2, minute + 2):
                try:
                    time.remove(m)
                except ValueError:
                    pass

            det.append([home.name, player, minute])
            

                
            
            
                    
                    
                    
    if a_score > 0:
        awayteam = away.player_list
        for goal in xrange(a_score):
            chosen = False
            while not chosen:
                player = random.choice(awayteam)
                if player.position.lower() == 'g':
                    chosen = False
                elif player.position.lower() == 'd':
                    chosen = random.choice([False, False, False, True, True])
                elif player.position.lower() == 'm':
                    chosen = random.choice([False, True, True, True, True])
                elif player.position.lower() == 'f':
                    chosen = True

            minute = random.choice(time)
            for m in xrange(minute - 2, minute + 2):
                try:
                    time.remove(m)
                except ValueError:
                    pass
            det.append([away.name, player, minute])

    det.sort(key = itemgetter(2))   # Sorts the nested list by third item, i.e., time
    return det
                    
    
