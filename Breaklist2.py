text="John B Marc Joe Ali Feroz Gabriel Miguel  John Mc  Elmo'  Me"
lista=[]
player=""
i=0

#mettici un controllo iniziale che prende tutti gli accenti e li elimina

while i< len(text)-3:
    if text[i]==" ":
        if text[i+2]==" " or text[i+3]==" " or text[i+1]==" ":
            player+=" "
            i+=1    
        else:
            lista.append(player)
            player=""
            i+=1
    else: 
        if text[i].isalpha():
            player+=text[i]
            i+=1
        else:
            i+=1

while i<len(text):
    if text[i]==" ":
        lista.append(player)
        player=""
        i+=1
    else: 
        if text[i].isalpha():
            player+=text[i]
            i+=1
        else:
            i+=1
lista.append(player)


for x in lista:
    print(x)



            






