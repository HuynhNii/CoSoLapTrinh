from random import randrange
def createDeck():
    card=[]
    for i in ['s','h','d','c']:
        for labai in ['2','3','4','5','6','7','8','9','T','J','Q','K','A']:
            card.append(labai+i)
    return card
def tron(card):
    for i in range(len(card)):
        a=randrange(i,len(card))
        b=card[i]
        card[i]=card[a]
        card[a]=b
card=createDeck()
def chiabai(sotay,baimoitay,card):
    hands=[]
    for i in range(sotay):
        hand=[]
        for j in range(baimoitay):
            hand.append(card.pop(0))
        hands.append(hand)
    return hands
hands = chiabai(4, 5, card)
for i, hand in enumerate(hands):
    print('Tay bai',i+1,':',hand)
print('Quan bai con lai:', card)