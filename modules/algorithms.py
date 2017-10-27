import teams
import players

def suggester():
##    chel_pos = [[],[],[],[]]
##    tot_pos = [[],[],[],[]]
##    manc_pos = [[],[],[],[]]
##    liv_pos = [[],[],[],[]]
##    ars_pos = [[],[],[],[]]
##    manu_pos = [[],[],[],[]]
##    ever_pos = [[],[],[],[]]
##    sout_pos = [[],[],[],[]]
##    bou_pos = [[],[],[],[]]
##    west_pos = [[],[],[],[]]

    pos_list = [[], [], [], []]
    for team_name in teams.allTeams:
        for player in teams.allTeams[team_name].player_list:
            if player.position.lower() == 'g': pos_list[0].append(player)
            if player.position.lower() == 'd': pos_list[1].append(player)
            if player.position.lower() == 'm': pos_list[2].append(player)
            if player.position.lower() == 'f': pos_list[3].append(player)

            teams.allTeams[team_name].pl_pos = pos_list

            
##    for i in teams.allTeams['Chelsea FC'].player_list:
##        if i.position.lower() == 'g': chel_pos[0].append(i)
##        if i.position.lower() == 'd': chel_pos[1].append(i)
##        if i.position.lower() == 'm': chel_pos[2].append(i)
##        if i.position.lower() == 'f': chel_pos[3].append(i)
##
##        teams.allTeams['Chelsea FC'].pl_pos = chel_pos
##        
##    for i in teams.allTeams['Tottenham Hotspur FC'].player_list:
##        if i.position.lower() == 'g': tot_pos[0].append(i)
##        if i.position.lower() == 'd': tot_pos[1].append(i)
##        if i.position.lower() == 'm': tot_pos[2].append(i)
##        if i.position.lower() == 'f': tot_pos[3].append(i)
##
##        teams.allTeams['Tottenham Hotspur FC'].pl_pos = tot_pos
##        
##    for i in teams.allTeams['Manchester City FC'].player_list:
##        if i.position.lower() == 'g': manc_pos[0].append(i)
##        if i.position.lower() == 'd': manc_pos[1].append(i)
##        if i.position.lower() == 'm': manc_pos[2].append(i)
##        if i.position.lower() == 'f': manc_pos[3].append(i)
##
##        teams.allTeams['Manchester City FC'].pl_pos = manc_pos
##        
##    for i in teams.allTeams['Liverpool FC'].player_list:
##        if i.position.lower() == 'g': liv_pos[0].append(i)
##        if i.position.lower() == 'd': liv_pos[1].append(i)
##        if i.position.lower() == 'm': liv_pos[2].append(i)
##        if i.position.lower() == 'f': liv_pos[3].append(i)
##
##        teams.allTeams['Liverpool FC'].pl_pos = liv_pos
##        
##    for i in teams.allTeams['Arsenal FC'].player_list:
##        if i.position.lower() == 'g': ars_pos[0].append(i)
##        if i.position.lower() == 'd': ars_pos[1].append(i)
##        if i.position.lower() == 'm': ars_pos[2].append(i)
##        if i.position.lower() == 'f': ars_pos[3].append(i)
##
##        teams.allTeams['Arsenal FC'].pl_pos = ars_pos
##        
##    for i in teams.allTeams['Manchester United FC'].player_list:
##        if i.position.lower() == 'g': manu_pos[0].append(i)
##        if i.position.lower() == 'd': manu_pos[1].append(i)
##        if i.position.lower() == 'm': manu_pos[2].append(i)
##        if i.position.lower() == 'f': manu_pos[3].append(i)
##
##        teams.allTeams['Manchester United FC'].pl_pos = manu_pos
##        
##    for i in teams.allTeams['Everton FC'].player_list:
##        if i.position.lower() == 'g': ever_pos[0].append(i)
##        if i.position.lower() == 'd': ever_pos[1].append(i)
##        if i.position.lower() == 'm': ever_pos[2].append(i)
##        if i.position.lower() == 'f': ever_pos[3].append(i)
##
##        teams.allTeams['Everton FC'].pl_pos = ever_pos
##        
##    for i in teams.allTeams['Southampton FC'].player_list:
##        if i.position.lower() == 'g': sout_pos[0].append(i)
##        if i.position.lower() == 'd': sout_pos[1].append(i)
##        if i.position.lower() == 'm': sout_pos[2].append(i)
##        if i.position.lower() == 'f': sout_pos[3].append(i)
##
##        teams.allTeams['Southampton FC'].pl_pos = sout_pos
##        
##    for i in teams.allTeams['Bournemouth'].player_list:
##        if i.position.lower() == 'g': bou_pos[0].append(i)
##        if i.position.lower() == 'd': bou_pos[1].append(i)
##        if i.position.lower() == 'm': bou_pos[2].append(i)
##        if i.position.lower() == 'f': bou_pos[3].append(i)
##
##        teams.allTeams['Bournemouth'].pl_pos = bou_pos
##        
##    for i in teams.allTeams['West Bromwich Albion FC'].player_list:
##        if i.position.lower() == 'g': west_pos[0].append(i)
##        if i.position.lower() == 'd': west_pos[1].append(i)
##        if i.position.lower() == 'm': west_pos[2].append(i)
##        if i.position.lower() == 'f': west_pos[3].append(i)
##
##        teams.allTeams['West Bromwich Albion FC'].pl_pos = west_pos
##        

    group_1 = [teams.allTeams['Chelsea FC'], teams.allTeams['Manchester City FC'],
               teams.allTeams['Liverpool FC'], teams.allTeams['Arsenal FC'],
               teams.allTeams['Manchester United FC']]
    
    group_2 = [teams.allTeams['Tottenham Hotspur FC'], teams.allTeams['Everton FC']]
    group_3 = [teams.allTeams['Southampton FC'], teams.allTeams['Bournemouth']]
    group_4 = [teams.allTeams['West Bromwich Albion FC']]


    grouplist = [group_1, group_2, group_3, group_4]

##    chel_sug = [[],[],[],[]]
##    tot_sug = [[],[],[],[]]
##    manc_sug = [[],[],[],[]]
##    manu_sug = [[],[],[],[]]
##    ars_sug = [[],[],[],[]]
##    liv_sug = [[],[],[],[]]
##    ever_sug = [[],[],[],[]]
##    sout_sug = [[],[],[],[]]
##    west_sug = [[],[],[],[]]
##    bou_sug = [[],[],[],[]]

    suggestions = [[],[],[],[]]
    for team_name in teams.allTeams:
        teams.allTeams[team_name].sug_list = suggestions
   
##    teams.allTeams['Tottenham Hotspur FC'].sug_list = tot_sug
##    teams.allTeams['Manchester City FC'].sug_list = manc_sug
##    teams.allTeams['Liverpool FC'].sug_list = liv_sug
##    teams.allTeams['Arsenal FC'].sug_list = ars_sug
##    teams.allTeams['Manchester United FC'].sug_list = manu_sug
##    teams.allTeams['Everton FC'].sug_list = ever_sug
##    teams.allTeams['Southampton FC'].sug_list = sout_sug
##    teams.allTeams['Bournemouth'].sug_list = bou_sug
##    teams.allTeams['West Bromwich Albion FC'].sug_list = west_sug
    

    n = 0
    while n < 4: #accessing positions
        for group in range(len(grouplist)):
            for team in grouplist[group]: #teamlists of 1
                for person in team.pl_pos[n]:
                    for market_group in range(group, len(grouplist)):
                        
                        for market_team in grouplist[market_group]:
                            if team != market_team:
                                for market_person in market_team.pl_pos[n]:
                                    
                                    if market_person.new_rating > person.new_rating:
                                        team.sug_list[n].append(str(market_person.name) + ' for ' + str(person.name))
        n += 1
    for tname in teams.allTeams:
        for i in xrange(4):
            print "Length of sug_list[%d] for team %s is %d"%(i, tname, len(teams.allTeams[tname].sug_list[i]))
        print
