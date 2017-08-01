import os
import pickle as pk


"""Class Definition is incomplete.
Methods to calculate ELO, financial status etc are required."""
class Club(object):
    """Base Class of Team object.
The Team Object will store all relevant data of a particular team."""
    def __init__(self, name):
        self.name = name
        self.player_list = []
        self.get_info()
    def __str__(self):
        """string representation of the team"""
        return self.name
    def __repr__(self):
        """formal string representaion for debugging"""
        return "< %s: dict:= %s > \n"%(self.name, str(self.__dict__))
    def __del__(self):
        pass
    def __lt__(self, obj):
        """Compares current ELO rating with obj.
If obj is an int object, then it will be assumed to be an ELO rating."""
        if isinstance(obj, int):
            return self.standing < obj
        elif isinstance(obj, Team):
            return self.standing < obj.standing
        raise NotImplemented
    def __le__(self, obj):
        """Compares current ELO rating with obj.
If obj is an int object, then it will be assumed to be an ELO rating."""
        if isinstance(obj, int):
            return self.standing <= obj
        elif isinstance(obj, Team):
            return self.standing <= obj.standing
        raise NotImplemented
    def __gt__(self, obj):
        return not(self <= obj)
    def __ge__(self, obj):
        return not(self < obj)
    def __eq__(self, obj):
        """If obj is of team type, then checks if they have the same name.
Otherwise, the object should be an integer, which will be compared with the ELO rating"""
        if isinstance(obj, int):
            return self.standing == obj
        elif isinstance(obj, Team):
            return self.name == obj.name
        raise NotImplemented
    def __ne__(self, obj):
        return not (self == obj)
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
        with open(folder + self.name.replace(" ", "_") + ".pydb", "rb") as f:
            self.finances = pk.load(f)
            self.standing = pk.load(f)
        self.player_list
    def send_info(self):
        folder = os.getcwd() + "\\data\\teams\\"
        with open(folder + self.name.replace(" ", "_") + ".pydb", "wb") as f:
            pk.dump(self.finances, f)
            pk.dump(self.standing, f)
        for player in self.player_list:
            player.send_info()
            
def close(iterate = False):
    for team in allTeams:
        allTeams[team].send_info()
        if iterate:
            yield 0
    #quit()

def load(iterate = False):
    folder = os.getcwd() + "\\data\\teams\\"
    teamlistfile = open(folder+"teams_list.txt", "rb")
    for tname in teamlistfile:
        tname = tname.rstrip("\n")
        allTeams[tname] = Club(tname)
        if iterate:
            yield 0
allTeams = dict()

if __name__ != "__main__":
    pass
elif __name__ == "__main__":
    while True:
        folder = os.getcwd().rstrip("\\modules") + "\\data\\teams\\"
        name = raw_input("Enter New Club Name: ")
        with open(folder+"teams_list.txt", "ab") as tlf:
            tlf.write(name+"\n")
        with open(folder+name.replace(" ", "_")+".pydb", "wb") as f:
            pk.dump(float(raw_input("Enter Finances: ")), f)
            pk.dump(int(raw_input("Enter Standing: ")), f)
        ch = raw_input("Continue? (Y/N): ").upper()
        if ch == "N": break
