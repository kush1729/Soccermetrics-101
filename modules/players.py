import os
import pickle as pk

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
        filename = folder + self.name.replace(" ", "_") + ".pydb"
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
    def rater(self, improvement):
        from random import random, randint
        rating_difference = self.year_2_rating - self.year_1_rating
        if rating_difference > 0 and improvement > 0:
            if improvement in range(7,11):
              self.new_rating = self.year_2_rating + 1.0
            elif improvement in range(4,8):
              self.new_rating = self.year_2_rating + 0.5
            elif improvement in range(5):
              x  = random()
              prob = randint(1,2)
              if prob == 1:
                self.new_rating = self.year_2_rating + x
              else:
                self.new_rating = self.year_2_rating - x

def load(iterate = False):
    from teams import allTeams
    folder = os.getcwd() + "\\data\\players\\"
    playerlistfile = open(folder+"players_list.txt", "rb")
    for pname in playerlistfile:
        pname = pname.rstrip("\n")
        obj = Player(pname)
        allTeams[obj.club].add(obj)
        if iterate:
            yield 0

if __name__ == '__main__':
    print "Program to add new players"
    while True:
        folder = os.getcwd().rstrip("\\modules") + "\\data\\players\\"
        name = raw_input("Enter New Player Name: ")
        with open(folder+"players_list.txt", "ab") as plf:
            plf.write(name+"\n")
        with open(folder+name.replace(" ", "_")+".pydb", "wb") as f:
            pk.dump(raw_input("Enter Club Name: "), f)
            i = raw_input("Enter New Club Name if any (if not, just press enter): ")
            if i == "":
                i = None
            pk.dump(i, f)
            pk.dump(raw_input("Enter Position: "), f)
            pk.dump(float(raw_input("Enter Year 1 Rating: ")), f)
            pk.dump(float(raw_input("Enter Year 2 Rating: ")), f)
            pk.dump(float(raw_input("Enter Market Value: ")), f)
        ch = raw_input("Continue? (Y/N): ").upper()
        if ch == "N": break
elif __name__ != "__main__":
    pass

            
