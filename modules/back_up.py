import pickle as pk
from os import getcwd

datafolder = getcwd().rstrip("modules").rstrip("data") + "data"

def backupplayers():
    folder = datafolder + "\\players\\"
    playerslist = open(folder+"players_list.txt")
    for player in playerslist:
        pname = player.rstrip('\r\n')
        with open(folder+pname.replace(" ", "_")+".pydb", "rb") as f:
            l = []
            try:
                while True:
                    l.append(pk.load(f))
            except EOFError:
                f.close()
        with open(folder+pname.replace(" ", "_")+"_bkup.pydb", "w") as f:
            for i in l:
                pk.dump(i, f)
    playerslist.close()

def backupteams():
    folder = datafolder + "\\teams\\"
    teamslist = open(folder+"teams_list.txt")
    for team in teamslist:
        tname = team.rstrip('\r\n')
        with open(folder+tname.replace(" ", "_")+".pydb", "rb") as f:
            l = []
            try:
                while True:
                    l.append(pk.load(f))
            except EOFError:
                f.close()
        with open(folder+tname.replace(" ", "_")+"_bkup.pydb", "wb") as f:
            for i in l:
                pk.dump(i, f)
    teamslist.close()

def fixCorrupt(name, type = "p"):
    folder = datafolder + ("\\teams\\" if type == "t" else "\\players\\")
    fname = folder + name.replace(" ", "_")
    backf = open(fname+"_bkup.pydb", "rb")
    propf = open(fname+".pydb", "wb")
    try:
        while True:
            e = pk.load(backf)
            pk.dump(e, propf)
    except EOFError:
        backf.close()
        propf.close()
