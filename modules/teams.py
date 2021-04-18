import os
import pickle as pk
import random
import back_up as bu

"""Class Definition is incomplete.
Methods to calculate ELO, financial status etc are required."""
class Club(object):
    """Base Class of Team object.
The Team Object will store all relevant data of a particular team."""
    def __init__(self, name):
        self.name = name
        self.player_list = []
        self.get_info()
        if self.standing == 0:
            self.elo = 200
        else:
            self.elo = 1100 - 50*self.standing
        self.points = 0
        self.goaldiff = 0
    def __str__(self):
        """string representation of the team"""
        return self.name
    def __repr__(self):
        return self.name
    def __del__(self):
        pass
    def __cmp__(self, other):
        if isinstance(other, Club):
            if self.points == other.points:
                if self.goaldiff != other.goaldiff:
                    return cmp(self.goaldiff, other.goaldiff)
                else:
                    return cmp(self.standing, other.standing)
            return cmp(self.points, other.points)
        return 0
    def __hash__(self):
        """name of the team will be used for the hash"""
        return hash(self.name)
    def __len__(self):
        return len(self.player_list)
    def __iter__(self):
        """Iterates over all the players in the team"""
        for p in self.player_list:
            yield p
    def __contains__(self, player):
        """Checks whether the player is currently in the team"""
        return (player in self.player_list)
    def add(self, player):
        self.player_list.append(player)
    def get_info(self):
        folder = os.getcwd() + "\\data\\teams\\"
        try:
            filename = folder + self.name.replace(" ", "_") + ".pydb"
        except:
            filename = folder + self.name.replace(" ", "_") + "_bkup.pydb"
            bu.fixCorrupt(self.name, "t")
        with open(filename, "rb") as f:
            self.finances = pk.load(f)
            self.standing = pk.load(f)
        #self.player_list = 
    def send_info(self):
        folder = os.getcwd() + "\\data\\teams\\"
        with open(folder + self.name.replace(" ", "_") + ".pydb", "wb") as f:
            pk.dump(self.finances, f)
            pk.dump(self.standing, f)
        for player in self.player_list:
            player.send_info()
    def homematch(self, awayteam):
        if awayteam.elo > self.elo + 100:
            awayelo = awayteam.elo - random.randint(5, 10)
        elif self.elo > awayteam.elo + 100:
            awayelo = awayteam.elo - random.randint(10, 17)
        else:
            awayelo = awayteam.elo - random.randint(17, 24)
        if 150 >= abs(awayelo - self.elo)>= 0:
            self.points += 1
            awayteam.points += 1
            self.elo += 10
            awayteam.elo += 10
        elif 500 >= abs(awayelo - self.elo) > 150:
            if awayelo > self.elo: #away win
                awayteam.elo += 75
                self.elo -= 30
                awayteam.points += 3
                awayteam.goaldiff += 1
                self.goaldiff -= 1
            else:
                self.elo += 75
                awayteam.elo -= 30
                self.points += 3
                self.goaldiff += 1
                awayteam.goaldiff -= 1
        elif 850 >= abs(awayelo - self.elo) > 500:
            if awayelo > self.elo: #away win
                awayteam.elo += 50
                self.elo -= 20
                awayteam.points += 3
                awayteam.goaldiff += 2
                self.goaldiff -= 2
            else:
                self.elo += 50
                awayteam.elo -= 20
                self.points += 3
                self.goaldiff += 2
                awayteam.goaldiff -= 2
        else:
            if awayelo > self.elo: #away win
                awayteam.elo += 25
                self.elo -= 10
                awayteam.points += 3
                awayteam.goaldiff += 3
                self.goaldiff -= 3
            else:
                self.elo += 25
                awayteam.elo -= 10
                self.points += 3
                self.goaldiff += 3
                awayteam.goaldiff -= 3

def get_Fixtures(allTeams):
    l = len(allTeams)
    keys = tuple(allTeams.keys())
    hl = list(keys)
    al = list(keys)
    random.shuffle(hl)
    random.shuffle(al)
    for i in xrange(l):
        for j in xrange(l):
            if i != j:
                yield (allTeams[hl[i]], allTeams[al[j]])

def Simulate(allTeams):
    curStanding = allTeams.values()
    curStanding.sort()
    for home, away in get_Fixtures(allTeams):
        home.homematch(away)
    curStanding.sort()
    return curStanding[::-1]
            
def close(iterate = False):
    for team in allTeams:
        allTeams[team].send_info()
        if iterate:
            yield 0
    #quit()
table = []
def load(iterate = False, main = True):
    global allTeams
    if main:
        folder = os.getcwd() + "\\data\\teams\\"
    else:
        folder = os.getcwd().rstrip("\\modules") + "\\data\\teams\\"
    teamlistfile = open(folder+"teams_list.txt", "rb")
    yield len(teamlistfile.readlines())
    teamlistfile.seek(0)
    for tname in teamlistfile:
        tname = tname.rstrip("\r\n")
        allTeams[tname] = Club(tname)
        yield 0
    teamlistfile.close()
            
allTeams = dict()

if __name__ != "__main__":
    pass
elif __name__ == "__main__":
    for _ in load(main = False):
        pass
    print 'name, pts, goaldiff, elo'
    table = Simulate(allTeams)
    print table
