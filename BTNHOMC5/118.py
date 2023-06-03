from random import randrange
def createDeck():
    card=[]
    for i in ["s","h","d","c"]:
        for labai in ["2","3","4","5","6","7","8","9","T","J","Q","K","A"]:
            card.append(labai+i)
    return card
def tron(card):
    for i in range(len(card)):
        a=randrange(i,len(card))
        b=card[i]
        card[i]=card[a]
        card[a]=b
card=createDeck()
print('Theo thu tu: ')
print (card)
tron(card)
print ('Xao tron: ')
print (card)