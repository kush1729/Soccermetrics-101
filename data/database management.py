import os
import pickle as pk

if __name__ != "__main__":
    raise ImportError("This file is unimportable.")

teamfolder = os.getcwd() + "\\teams\\"
playerfolder = os.getcwd() + "\\players\\"
playerattr = ("Club", "New Club", "Position", "Year 1 Rating", "Year 2 Rating", "Market Value")
pattrtype = {"Club":str, "New Club":str, "Position":str, "Year 1 Rating":float, "Year 2 Rating":float, "Market Value":float}
tattrtype = {"Finances":float, "Standing":int}
teamattr = ("Finances", "Standing")

def getFileName(name, folder = playerfolder):
    return folder + name.replace(" ", "_") + ".pydb"

def ReadFile(name, type = "p"): #p == player, t == team
    filename = getFileName(name, (teamfolder if type == "t" else playerfolder))
    try:
        f = open(filename, "rb")
    except IOError:
        print "Non Existant File:", filename
    else:
        if type == "p":
            attributes = playerattr
        else:
            attributes = teamattr
        print "Name:", name
        for a in attributes:
            print a+":", pk.load(f)

def EditFile(name, type = "p"):
    filename = getFileName(name, (playerfolder if type == "p" else teamfolder))
    attrtype = pattrtype if type == "p" else tattrtype
    fields = playerattr if type == "p" else teamattr
    n = len(fields)
    try:
        f = open(filename, "rb")
    except IOError:
        print "Non Existant File:", filename
    else:
        l = [None]*n
        for i in xrange(n):
            l[i] = pk.load(f)
        f.close()
        f = open(filename, "wb")
        print "The attributes of the file shall be cycled through once."
        print "If you want to change an attribute then type the new attribute."
        print "If there is no change, then do not type anything; just press enter."
        for i in xrange(6):
            field = fields[i]
            try:
                entry = attrtype[field](raw_input("Enter %s: "%field))
                if entry == "":
                    entry = l[i]
            except ValueError:
                entry = l[i]
            l[i] = entry
        for i in xrange(6):
            pk.dump(l[i], f)
        f.close()
    print
    ReadFile(name, type)

def AddFile(type = "p"):
    folder = (playerfolder if type == "p" else teamfolder)
    name = raw_input("Enter New %s Name: "%("Player" if type == "p" else "Team"))
    filename = getFileName(name, (playerfolder if type == "p" else teamfolder))
    attrtype = pattrtype if type == "p" else tattrtype
    fields = playerattr if type == "p" else teamattr
    l = "teams_list.txt" if type == "t" else "players_list.txt"
    n = len(fields)
    with open(filename, "wb") as f:
        for field in fields:
            try:
                i = attrtype[field](raw_input("Enter %s: "%field))
                if i == "":
                    i = None
                pk.dump(i, f)
            except ValueError:
                f.close()
                print "Wrong Input. If you are gonna type like BD then I shall stop taking your input." #xP
                print "Whatever has already been input shall be discarded."
                os.remove(filename)
                return
    with open(folder+l, "a") as f:
        f.write(name + "\n")

#EditFile("Test Player3", "p")

        
                    
        
            
