textraw5="234 jp, brian mC rab, jonathan P , ólli, me, Douglas3, d5éxy John Mc me  "
textraw4="  jp,  brian mC  carmelino , jonathan 6P , ólli ko  , me, Douglas, déxy John Mc me  "

textraw3="jp, brian mC rab, jonathan P, ólli, me, Douglas, déxy +1 ,me "

textraw2="jp, brian mC rab, jonathan P, ólli, me, Douglas, déxy pino , me"

textraw1="jp, brian mC rab, jonathan P, ólli, me, Douglas, déxy camila , ruairidh"
lista = []

def breaklist(textraw):
    #accents:
    textraw = textraw.strip()      # no trailing or leading spaces
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
        if text[i]==" " and text[i+1]==" ":         #modified to remove double spaces
            i+=1                                    #
            continue                                # 
        if text[i]==" ":
            if text[i+2]==" " or text[i+3]==" ":
                player+=" "  
            else:
                player=player.capitalize()
                lista.append(player.rstrip())      #modified no trailing spaces due to special chars   
                player=""
        elif text[i].isalpha():
            player+=text[i]
        i+=1

    while i<len(text):
        if text[i]==" ":
            player=player.capitalize()
            lista.append(player.rstrip())      #modified no trailing spaces due to special chars     
            player=""
        elif text[i].isalpha():
                player+=text[i]
        i+=1
    player=player.capitalize()   
    if len(player)>0:
        lista.append(player.rstrip())      #modified no trailing spaces due to special chars           

    while len(lista)<10:
        n=10-len(lista)
        lista.append(f'ExtraPlayer{n}')

    return lista


lista = breaklist(textraw5)

#textraw = textraw3
#i=0
#while i< len(textraw)-3:
#    print(textraw[i], textraw[i+1])   
#    i+=1


for x in lista:
   print(x+'N')

#=========================