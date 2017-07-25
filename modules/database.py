from os import getcwd
from pickle import load, dump

allTeams = []


"""Class Definition is incomplete.
Methods to calculate ELO, financial status etc are required."""
class Team(object):
    """Base Class of Team object.
The Team Object will store all relevant data of a particular team."""
    def __init__(self, name, players = []):
        self.name = name
        self.player_list = players
        self.ELO = 0  #to be calculated later
        allTeams.append(self)
    def __str__(self):
        """string representation of the team"""
        return self.name
    def __repr__(self):
        """formal string representaion for debugging"""
        return "< %s: dict:= %s > \n"%(self.name, str(self.__dict__))
    def __del__(self):
        """On deletion of the object, the team shall be removed from the list of teams, as well as the binary file.
Hence, proper care must be taken when deleting a Team object."""
        allTeams.remove(self)
    def __lt__(self, obj):
        """Compares current ELO rating with obj.
If obj is an int object, then it will be assumed to be an ELO rating."""
        if isinstance(obj, int):
            return self.ELO < obj
        elif isinstance(obj, Team):
            return self.ELO < obj.ELO
        raise NotImplemented
    def __le__(self, obj):
        """Compares current ELO rating with obj.
If obj is an int object, then it will be assumed to be an ELO rating."""
        if isinstance(obj, int):
            return self.ELO <= obj
        elif isinstance(obj, Team):
            return self.ELO <= obj.ELO
        raise NotImplemented
    def __gt__(self, obj):
        return not(self <= obj)
    def __ge__(self, obj):
        return not(self < obj)
    def __eq__(self, obj):
        """If obj is of team type, then checks if they have the same name.
Otherwise, the object should be an integer, which will be compared with the ELO rating"""
        if isinstance(obj, int):
            return self.ELO == int
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

def _load():
    global allTeams
    folder = getcwd()
    filename = folder + r"\data\TeamDatabase.pydb"
    allTeams = []
    with open(filename, "rb") as f:
        while True:
            try:
                t = load(f)
            except EOFError:
                break
            else:
                allTeams.append(t)

def _dump():
    global allTeams
    folder = getcwd()
    filename = folder + r"\data\TeamDatabase.pydb"
    with open(filename, "wb") as f:
        for t in allTeams:
            dump(t, f)
    allTeams = []

def save_backup():
    """Function that will save all the data in a text file as a backup.
This text file will only be accessed by this function and the function 'load_backup()'"""
    folder = getcwd()
    filename = folder + r"\data\BackupDatabase.txt"
    with open(filename, "wb") as f:
        for t in allTeams:
            dump(t, f)

def load_backup():
    """Will load the backup database that is stored in the text file.
Will return a list of all the team objects stored in the text file."""
    folder = getcwd()
    filename = folder + r"\data\BackupDatabase.txt"
    l = []
    with open(filename, "rb") as f:
        while True:
            try:
                t = load(f)
            except EOFError:
                break
            else:
                l.append(t)
    return l

def close():
    """This method should be called everytime the program stops using this module, especially if any data has been changed"""
    _dump()
    save_backup()
    quit()

if __name__ != "__main__":
    allTeams = _load()
elif __name__ == "__main__":
    testobj = Team("Test Team", ["Player Name 1", "Player Name 2"])
    save_backup()
    
        
        
