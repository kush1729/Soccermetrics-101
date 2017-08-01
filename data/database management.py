#comment
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
        print
        ReadFile(name, type)
        print
        f = open(filename, "wb")
        print "The attributes of the file shall be cycled through once."
        print "If you want to change an attribute then type the new attribute."
        print "If there is no change, then do not type anything; just press enter."
        print "If a field is to be left empty ('None' python type), type '/'"
        for i in xrange(6):
            field = fields[i]
            try:
                entry = attrtype[field](raw_input("Enter %s: "%field))
                if entry == "":
                    entry = l[i]
                elif entry == '/':
                    entry = None
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
    name = raw_input("Enter New %s Name (FULL): "%("Player" if type == "p" else "Team"))
    filename = getFileName(name, folder)
    attrtype = pattrtype if type == "p" else tattrtype
    fields = playerattr if type == "p" else teamattr
    l = "teams_list.txt" if type == "t" else "players_list.txt"
    n = len(fields)
    print "If a field has to be left empty ('None' python type), type '/'"
    with open(filename, "wb") as f:
        for field in fields:
            try:
                i = attrtype[field](raw_input("Enter %s: "%field))
                if i == "":
                    raise ValueError
                elif i == "/":
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

print "\nList of Teams:"
with open(teamfolder+"teams_list.txt") as f:
    print f.read()
print "List of Players:"
with open(playerfolder+"players_list.txt") as f:
    print f.read()
print '''Choices:
Key  Action
1.   Add A Team File
2.   Add A Player File
3.   Read A Team's File
4.   Read A Player's File
5.   Edit A Team's File
6.   Edit A Player's File
Anything else to quit.
'''
while True:
    ch = raw_input("Enter your choice: ")
    if ch == "1":
        AddFile("t")
        with open(teamfolder+"teams_list.txt") as f:
            print f.read()
    elif ch == "2":
        AddFile("p")
        with open(playerfolder+"players_list.txt") as f:
            print f.read()
    elif ch == "3":
        name = raw_input("Enter FULL NAME of the team: ")
        ReadFile(name, "t")
    elif ch == "4":
        name = raw_input("Enter FULL NAME of player: ")
        ReadFile(name, "p")
    elif ch == "5":
        name = raw_input("Enter FULL NAME of the team: ")
        EditFile(name, "t")
    elif ch == "6":
        name = raw_input("Enter FULL NAME of the player: ")
        EditFile(name, "p")
    else:
        print "Exiting..."
        break
    print

        
                    
        
            
