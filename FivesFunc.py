# from Fives import Match




#filtername=input("name of the player")

#.order_by(Match.date)
def stats(Match, filtername):
    
    data = Match.query.filter( (Match.Pl1==filtername) | (Match.Pl2==filtername) | (Match.Pl3==filtername) 
                            | (Match.Pl4==filtername) | (Match.Pl5==filtername)  | (Match.Pl6==filtername) | (Match.Pl7==filtername)  
                            | (Match.Pl8==filtername) | (Match.Pl9==filtername)  | (Match.Pl10==filtername)   ).order_by(Match.date).all()

    n= len(data)
    date1=data[0].date
    date2= data[-1].date
    results=[filtername, n, date1, date2]
    return results

#print(filtername)
#print(n)
#print(date1)
#print(date2)


#=======================================

#textraw="jp, brian mC rab, jonathan P, ólli, me, Douglas, déxy +1 , ruairidh"

def breaklist(textraw):
    #accents:
    text=""
    for c in textraw:
        if c=='è' or c=='é':
            text+='e'
        elif c=='ò' or c=='ó':
            text+='o'
        else:
            text+=c

    lista=[]
    player=""
    i=0

    while i< len(text)-3:
        if text[i]==" ":
            if text[i+2]==" " or text[i+3]==" " or text[i+1]==" ":
                player+=" "  
            else:
                player=player.capitalize()
                lista.append(player)
                player=""
        elif text[i].isalpha():
            player+=text[i]
        i+=1

    while i<len(text):
        if text[i]==" ":
            player=player.capitalize()
            lista.append(player)
            player=""
        elif text[i].isalpha():
                player+=text[i]
        i+=1
    player=player.capitalize()   
    if len(player)>0:
        lista.append(player)

    while len(lista)<10:
        lista.append('ExtraPlayer')

    return lista

#for x in lista:
#   print(x)

#=========================

def fillplayertable(db, Match, Player):
    if len(Player.query.all()) == 0:
        uniqlist=[]
    else:
        uniqlist=[ Player.name for Player in Player.query.all()]
    for mat in Match.query.all():
        k=0
        mplayer= [mat.Pl1, mat.Pl2, mat.Pl3, mat.Pl4, mat.Pl5, mat.Pl6, mat.Pl7, mat.Pl8, mat.Pl9, mat.Pl10]
        while k<10:
            if mplayer[k] not in uniqlist:
                uniqlist.append(mplayer[k])
                line= stats(Match, mplayer[k])
                newplayer = Player(name=line[0], caps=line[1], first=line[2], last=line[3])
                db.session.add(newplayer)
                db.session.commit()
            k+=1
    return Player

    



#=============================

#print(Match.query.first().Pl1)
#line= stats(Match.query.first().Pl1)
#print(line)
#print(len(Match.query.all()))

#print(Player.query.first().last)

#for player in Player.query.all():
#    db.session.delete(player)
#    db.session.commit()



#uniqlist=[]
#for mat in Match.query.all():
#    k=0
#    mplayer= [mat.Pl1, mat.Pl2, mat.Pl3, mat.Pl4, mat.Pl5, mat.Pl6, mat.Pl7, mat.Pl8, mat.Pl9, mat.Pl10]
#    while k<10:
#        if mplayer[k] not in uniqlist:
#            uniqlist.append(mplayer[k])
#            line= stats(mplayer[k])
#            newplayer = Player(name=line[0], caps=line[1], first=line[2], last=line[3])
#            db.session.add(newplayer)
#            db.session.commit()
#        k+=1
    
#for p in nlist:
#    print(p)


#print("------------All Players:-------------")
#for player in Player.query.all():
#    print(f"{player.name} Caps:{player.caps}  First Game:{player.first} Last Game:{player.last}")








#if len(Player.query.all()) == 0:
#    line= stats(Match.query.first().Pl1)
#    print(line)
#    newplayer = Player(name=line[0], caps=line[1], first=line[2], last=line[3])
#    db.session.add(newplayer)
#    db.session.commit()















#for Match in Match.query.all():
#    k=0
#    mplayer= [Match.Pl1, Match.Pl2, Match.Pl3, Match.Pl4, Match.Pl5, Match.Pl6, Match.Pl7, Match.Pl8, Match.Pl9, Match.Pl10]
#    while k<10:
#        if mplayer[k] not in player.name:
#            line= stats(mplayer[k])
#            print(line)
#           newplayer = Player(name=line[0], caps=line[1], first=line[2], last=line[3])
#            db.session.add(newplayer)
#            db.session.commit()            
#        k+=1










""" line= stats(Match.query.first().Pl2)
print(line)
newplayer = Player(name=line[0], caps=line[1], first=line[2], last=line[3])
db.session.add(newplayer)
db.session.commit()

line= stats(Match.query.first().Pl3)
print(line)
newplayer = Player(name=line[0], caps=line[1], first=line[2], last=line[3])
db.session.add(newplayer)
db.session.commit() """
    
#print(Match.Pl1)