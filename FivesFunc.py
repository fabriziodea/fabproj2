from Fives import Match
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from Fives import db

#filtername=input("name of the player")
def stats(filtername):
    
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

