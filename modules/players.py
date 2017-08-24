import os
import pickle as pk
import teams

class Player(object):
    def __init__(self, name):
        self.name = name
        self.get_info()
    def __del__(self):
        pass
    def __eq__(self, obj):
        if isinstance(obj, str):
            return self.name == obj
        if isinstance(obj, Player):
            return self.name == obj.name
        return False
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name
    def get_info(self):
        folder = os.getcwd() + "\\data\\players\\"
        try:
            filename = folder + self.name.replace(" ", "_") + ".pydb"
        except:
            filename = folder + self.name.replace(" ", "_") + "_bkup.pydb"
            bu.fixCorrupt(self.name, "p")
        with open(filename, "rb") as f:
            self.club = pk.load(f)
            self.new_club = pk.load(f)
            self.position = pk.load(f)
            self.year_1_rating = pk.load(f)
            self.year_2_rating = pk.load(f)
            self.market_value = pk.load(f)
    def send_info(self):
        folder = os.getcwd() + "\\data\\players\\"
        filename = folder + self.name.replace(" ", "_") + ".pydb"
        with open(filename, "wb") as f:
            pk.dump(self.club, f)
            pk.dump(self.new_club, f)
            pk.dump(self.position, f)
            pk.dump(self.year_1_rating, f)
            pk.dump(self.year_2_rating, f)
            pk.dump(self.market_value, f)
    def rater(self):
        from random import random, randint
##        rating_difference = self.year_2_rating - self.year_1_rating
##        if rating_difference > 0 and improvement > 0:
##            if improvement in range(7,11):
##              self.new_rating = self.year_2_rating + 1.0
##            elif improvement in range(4,8):
##              self.new_rating = self.year_2_rating + 0.5
##            elif improvement in range(5):
##              x  = random()
##              prob = randint(1,2)
##              if prob == 1:
##                self.new_rating = self.year_2_rating + x
##              else:
##                self.new_rating = self.year_2_rating - x
        
        n = 1
        self.pos = 0
        for i in teams.table:
            print "I", i, self.new_club
            if self.new_club == i:
                self.pos = n
                n += 1
            print "N", n

                
        if self.pos == 1:
            self.new_rating = self.year_2_rating + 0.1
            print "1", self.new_club
        elif self.pos == 2 or self.pos == 3:
            self.new_rating = self.year_2_rating + 0.07
            print "2, 3", self.new_club
        elif self.pos == 4 or self.pos == 5:
            print "4, 5", self.new_club
            self.new_rating = self.year_2_rating + 0.04
        elif self.pos == 6 or self.pos == 7:
            print "6, 7", self.new_club
            self.new_rating = self.year_2_rating
        elif self.pos == 8 or self.pos == 9:
            print "8, 9", self.new_club
            self.new_rating = self.year_2_rating - 0.06
        elif self.pos == 10:
            print "10", self.new_club
            self.new_rating = self.year_2_rating - 0.1
        elif self.pos == 12:
            print "12", self.new_club
            self.new_rating = self.year_2_rating - 0.15
        else:
            print self.new_club, self.pos, "HERE!"
            self.new_rating = self.year_2_rating - 0.15

        self.impr = self.year_2_rating - self.year_1_rating

        impr_dict = {'Chelsea FC': 7, 'Tottenham Hotspur FC' : 4, 'Manchester City FC' : 9, 'Liverpool FC' : 6,
                     'Arsenal FC' : 5, 'Manchester United FC' : 8, 'Everton FC' : 7, 'Southampton FC' : 4 ,
                     'Bournemouth' : 5, 'West Bromwich Albion FC' : 4, 'Leicester City FC' : 5}
        
        if self.new_club[-2:] != "FC" and self.new_club != "Bournemouth":
            self.new_club += " FC"

        print "Final!", self.new_club
        self.new_rating += (self.impr*((impr_dict[self.new_club])/10))
        
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
        for players in teams.allTeams[team_name].player_list:
            if players.position.lower() == 'g': pos_list[0].append(i)
            if players.position.lower() == 'd': pos_list[1].append(i)
            if players.position.lower() == 'm': pos_list[2].append(i)
            if players.position.lower() == 'f': pos_list[3].append(i)

            teams.allTeams[team_name].pl_pos = chel_pos

            
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

def load(iterate = False):
    folder = os.getcwd() + "\\data\\players\\"
    playerlistfile = open(folder+"players_list.txt", "rb")
    yield len(playerlistfile.readlines())
    playerlistfile.seek(0)
    for pname in playerlistfile:
        pname = pname.rstrip("\r\n")
        obj = Player(pname)
        if obj.new_club == None:
            c = obj.club
            obj.new_club = obj.club
        else:
            c = obj.new_club
        if c != 'Bournemouth' and c[-3:] != ' FC':
            c += ' FC'
        try:
            teams.allTeams[c].add(obj)
        except KeyError:
            pass
        yield 0

if __name__ == '__main__':
    pass
elif __name__ != "__main__":
    pass

            
