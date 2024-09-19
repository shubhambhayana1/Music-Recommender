#Logan Scheffler, Shubham Bhayana, Fredric Kabeiseman
#I pledge my honor that I have abided by the Stevens Honor System

nameOfFile = "musicrecplus.txt"
Dictionary = {}

def load(f):
    """Imports the file containing the list of users and their preferences as a dictionary - Shubham Bhayana""" 
    try:
        file = open(f, 'r')
    except:
        file = open(f, 'x')
    else:
        file = open(f, 'r')
        for line in file:
            values = line.strip().split(":")
            username = values[0]
            artists = values[1].split(",")
            Dictionary[username] = artists
        return Dictionary

def menu():
    """If the user is new, then they will be asked for their preferences. Then the user is presented with the main menu - Logan Scheffler"""
    name = input("Enter your name (put a $ symbol after your name if you wish your preferences to remain private):\n")
    if (name in Dictionary) or ((name + "$") in Dictionary):
        pass
    else:
        artistList = []
        while True:
            artist = input("Enter an artist that you like ( Enter to finish ):\n")
            if artist == "":
                Dictionary[name] = artistList
                break
            else:
                artistList.append(artist.title())
    while True:
        choice = input("Enter a letter to choose an option :\ne - Enter preferences\nd - Delete preferences\ns - Show preferences\nr - Get recommendations\np - Show most popular artists\nh - How popular is the most popular\nm - Which user has the most likes\nq - Save and quit\n")
        if choice == "e":
            enter_preferences(Dictionary[name])
        elif choice == "d":
            deletePref(name)
        elif choice == "s":
            showPref(name)
        elif choice == "r":
            getRec(name)
        elif choice == "p":
            popArtist()
        elif choice == "h":
            howPop()
        elif choice == "m":
            whichUserLikesMostArtists()
        elif choice == "q":
            save(name)
        else:
            print("Please select a valid option\n")

def enter_preferences(artists):
    '''User enters their artist preferences - Fredric Kabeiseman'''
    newPref = input("Enter an artist that you like (Enter to finish):\n").title()
    while newPref != '':
        artists.append(newPref)
        newPref = input("Enter an artist that you like (Enter to finish):\n").title()
    return


def deletePref(name):
    """Deletes the typed artist from the users list of preferences - Logan Scheffler"""
    while True:
        if Dictionary[name] == []:
            print("No artists found\n")
            break
        else:
            print("Current preferences:")
            for artist in Dictionary[name]:
                print(artist)
            artist = input("Enter an artist that you would like to remove ( Enter to finish ):\n")
            if artist in Dictionary[name]:
                Dictionary[name].remove(artist)
            elif artist == "":
                break
            else:
                print("Artist not found: Please try again\n")

def showPref(name):
    """Shows a list of the users current preferences - Logan Scheffler"""
    print("Current preferences:")
    for artist in Dictionary[name]:
        print(artist)
    

def getRec(user):
    """Gives the user artist recommendations based on their preferences and others preferences (except private users) - Logan Scheffler"""
    userList = Dictionary[user]
    listLength = len(userList)
    idk = []
    for U in Dictionary:
        if U[-1] == "$":
            pass
        elif U == user:
            pass
        else:
            i = 0
            for x in userList:
                if x in Dictionary[U]:
                    i += 1
                else:
                    pass
            idk.append([i,U])
    p = 0
    current = 0
    while p < len(idk):
        if (idk[p][0] > current) and (idk[p][0] != len(Dictionary[idk[p][1]])):
            current = idk[p][0]
        else:
            pass
        p += 1
    if current == 0:
        print("No recommendations available at this time.")
    else:
        for b in idk:
            if b[0] == current:
                gottem = Dictionary[b[1]]
                for artist in userList:
                    gottem = list(filter(lambda x:artist != x,gottem))
                for i in gottem:
                    print(i)
                break
            else:
                pass
            

def popArtist():
    """Prints the top three most popular artists contained in the preferences of all users (except private users) - Logan Scheffler"""
    POPULARDICTIONARY = {}
    for U in Dictionary:
        if U[-1] == "$":
            pass
        else:
            for x in Dictionary[U]:
                if x in POPULARDICTIONARY:
                    POPULARDICTIONARY[x] += 1
                else:
                    POPULARDICTIONARY[x] = 1
    SORTEDDICTIONARY = sorted(POPULARDICTIONARY.items(),key = lambda x:-x[1])
    i = 0
    for U in SORTEDDICTIONARY:
        if i == 0 and U[1] == 0:
            print("Sorry, no artists found.")
        elif U[1] == 0:
            break
        elif i == 3:
            break
        else:
            print(U[0])
            i += 1

def howPop():
    """Prints the total amount of times the most popular artist appears in all of the users preferences (except private users) - Logan Scheffler"""
    POPULARDICTIONARY = {}
    for U in Dictionary:
        if U[-1] == "$":
            pass
        else: 
            for x in Dictionary[U]:
                if x in POPULARDICTIONARY:
                    POPULARDICTIONARY[x] += 1
                else:
                    POPULARDICTIONARY[x] = 1
    SORTEDDICTIONARY = sorted(POPULARDICTIONARY.items(),key = lambda x:-x[1])
    i = 0
    for U in SORTEDDICTIONARY:
        if U[1] == 0:
            print("Sorry, no artists found.")
        print(U[1])
        break

def whichUserLikesMostArtists():
    """Returns the name of the user who likes the most artists - Shubham Bhayana"""
    s = 0
    for user in Dictionary:
        if user[-1] != '$':
            if len(Dictionary[user]) > s:
                s = len(Dictionary[user])
                t = user
    print(t)

def save(userName):
    '''Saves the preferences, and closes the application - Fredric Kabeiseman'''
    file = open(nameOfFile, 'w')
    for user in Dictionary:
        toSave = str(user) + ':' + ','.join(Dictionary[user]) + "\n"
        file.write(toSave)
    file.close()
    exit()

load(nameOfFile)
menu()
