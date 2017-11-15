import os
import pickle as pk
import teams

class Player(object):
    def __init__(self, name):
        self.name = name
        self.season_impr = 0
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

        
        n = 1
        self.pos = 0
        for i in teams.table:
            if self.new_club == i.name:
                self.pos = n
                n += 1

                
        if self.pos == 1:
            self.new_rating = self.year_2_rating + 0.1
        elif self.pos == 2 or self.pos == 3:
            self.new_rating = self.year_2_rating + 0.07
        elif self.pos == 4 or self.pos == 5:
            self.new_rating = self.year_2_rating + 0.04
        elif self.pos == 6 or self.pos == 7:
            self.new_rating = self.year_2_rating
        elif self.pos == 8 or self.pos == 9:
            self.new_rating = self.year_2_rating - 0.06
        elif self.pos == 10:
            self.new_rating = self.year_2_rating - 0.1
        elif self.pos == 12:
            self.new_rating = self.year_2_rating - 0.15
        else:
            self.new_rating = self.year_2_rating - 0.15

        self.impr = self.year_2_rating - self.year_1_rating + self.season_impr

        impr_dict = {'Chelsea FC': 7, 'Tottenham Hotspur FC' : 4, 'Manchester City FC' : 9, 'Liverpool FC' : 6,
                     'Arsenal FC' : 5, 'Manchester United FC' : 8, 'Everton FC' : 7, 'Southampton FC' : 4 ,
                     'Bournemouth' : 5, 'West Bromwich Albion FC' : 4, 'Leicester City FC' : 5}
        
        if self.new_club[-2:] != "FC" and self.new_club != "Bournemouth":
            self.new_club += " FC"

        #print "Final!", self.new_club
        self.new_rating += (self.impr*((impr_dict[self.new_club])/10))
        

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

            
