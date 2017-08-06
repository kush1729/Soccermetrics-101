import pickle as pk

def oldclubfile(s, nf):
    pk.dump(s[0].strip(".S").strip("'"), nf)
    pk.dump(None, nf)
    if 'D' in s[2].upper(): p = 'D'
    elif 'G' in s[2].upper(): p = 'G'
    elif 'M' in s[2].upper(): p = 'M'
    elif 'F' in s[2].upper(): p = 'F'
    pk.dump(p, nf)
    pk.dump(float(s[4].strip(".F")), nf)
    pk.dump(float(s[5].strip(".F")), nf)
    pk.dump(float(s[6].strip(".F")), nf)

def newclubfile(s, nf):
    pk.dump(s[0].strip(".S").strip("'"), nf)
    pk.dump(s[2].strip(".S").strip("'"), nf)
    if 'D' in s[4].upper(): p = 'D'
    elif 'G' in s[4].upper(): p = 'G'
    elif 'M' in s[4].upper(): p = 'M'
    elif 'F' in s[4].upper(): p = 'F'
    pk.dump(p, nf)
    pk.dump(float(s[6].strip(".F")), nf)
    pk.dump(float(s[7].strip(".F")), nf)
    pk.dump(float(s[8].strip(".F")), nf)

with open("players_list.txt", "r") as listfile:
    for name in listfile:
        name = name.rstrip("\r\n").replace(" ", "_")
        with open(name+".pydb", "rb") as f:
            s = f.readlines()
        s = [line.strip("\r\n") for line in s]
        if len(s) not in (8, 10):
            with open(name+"_bkup.pydb", "rb") as f:
                s = f.readlines()
        with open(name+".pydb", "wb") as f:
            print name, s
            if len(s) == 10:
                newclubfile(s, f)
            else:
                oldclubfile(s, f)
        
