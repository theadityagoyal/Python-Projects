import itertools,random
deck=list(itertools.product(range(1,14),['spade','Heart','Diamond','Club']))
random.shuffle(deck)
print('you got:')
for i in range(5):
    print(deck[i][0],'of',deck[i][1])
    