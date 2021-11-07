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



            







