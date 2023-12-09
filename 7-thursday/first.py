'''
Advent of Code[About][Events][Shop][Settings][Log Out]Matteo Campagnoli 12*
      /^2023$/[Calendar][AoC++][Sponsors][Leaderboard][Stats]
Our sponsors help make Advent of Code possible:
Splunk - Come build a more resilient digital world with us.
--- Day 7: Camel Cards ---
Your all-expenses-paid trip turns out to be a one-way, five-minute ride in an airship. (At least it's a cool airship!) It drops you off at the edge of a vast desert and descends back to Island Island.

"Did you bring the parts?"

You turn around to see an Elf completely covered in white clothing, wearing goggles, and riding a large camel.

"Did you bring the parts?" she asks again, louder this time. You aren't sure what parts she's looking for; you're here to figure out why the sand stopped.

"The parts! For the sand, yes! Come with me; I will show you." She beckons you onto the camel.

After riding a bit across the sands of Desert Island, you can see what look like very large rocks covering half of the horizon. The Elf explains that the rocks are all along the part of Desert Island that is directly above Island Island, making it hard to even get there. Normally, they use big machines to move the rocks and filter the sand, but the machines have broken down because Desert Island recently stopped receiving the parts they need to fix the machines.

You've already assumed it'll be your job to figure out why the parts stopped when she asks if you can help. You agree automatically.

Because the journey will take a few days, she offers to teach you the game of Camel Cards. Camel Cards is sort of similar to poker except it's designed to be easier to play while riding a camel.

In Camel Cards, you get a list of hands, and your goal is to order them based on the strength of each hand. A hand consists of five cards labeled one of A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, or 2. The relative strength of each card follows this order, where A is the highest and 2 is the lowest.

Every hand is exactly one type. From strongest to weakest, they are:

Five of a kind, where all five cards have the same label: AAAAA
Four of a kind, where four cards have the same label and one card has a different label: AA8AA
Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
High card, where all cards' labels are distinct: 23456
Hands are primarily ordered based on type; for example, every full house is stronger than any three of a kind.

If two hands have the same type, a second ordering rule takes effect. Start by comparing the first card in each hand. If these cards are different, the hand with the stronger first card is considered stronger. If the first card in each hand have the same label, however, then move on to considering the second card in each hand. If they differ, the hand with the higher second card wins; otherwise, continue with the third card in each hand, then the fourth, then the fifth.

So, 33332 and 2AAAA are both four of a kind hands, but 33332 is stronger because its first card is stronger. Similarly, 77888 and 77788 are both a full house, but 77888 is stronger because its third card is stronger (and both hands have the same first and second card).

To play Camel Cards, you are given a list of hands and their corresponding bid (your puzzle input). For example:

32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
This example shows five hands; each hand is followed by its bid amount. Each hand wins an amount equal to its bid multiplied by its rank, where the weakest hand gets rank 1, the second-weakest hand gets rank 2, and so on up to the strongest hand. Because there are five hands in this example, the strongest hand will have rank 5 and its bid will be multiplied by 5.

So, the first step is to put the hands in order of strength:

32T3K is the only one pair and the other hands are all a stronger type, so it gets rank 1.
KK677 and KTJJT are both two pair. Their first cards both have the same label, but the second card of KK677 is stronger (K vs T), so KTJJT gets rank 2 and KK677 gets rank 3.
T55J5 and QQQJA are both three of a kind. QQQJA has a stronger first card, so it gets rank 5 and T55J5 gets rank 4.
Now, you can determine the total winnings of this set of hands by adding up the result of multiplying each hand's bid with its rank (765 * 1 + 220 * 2 + 28 * 3 + 684 * 4 + 483 * 5). So the total winnings in this example are 6440.

Find the rank of every hand in your set. What are the total winnings?
'''

def getType(h):
    counters = {}
    for c in h:
        if c not in counters.keys():
            counters[c] = h.count(c)

    m = max(counters.values())
    numPair = list(counters.values()).count(2)

    if m==5:
        #print(h," - Five of a kind")
        #return "five"
        return 7
    elif m==4:
        #print(h," - Four of a kind")
        #return "four"
        return 6
    elif m==3 and numPair==1:
        #print(h," - Full house")
        #return "full"
        return 5
    elif m==3:
        #print(h," - Three of a kind")
        #return "three"
        return 4
    elif m==2 and numPair==2:
        #print(h," - Two pair")
        #return "twopair"
        return 3
    elif m==2:
        #print(h," - One pair")
        #return "pair"
        return 2
    elif m==1:
        #print(h," - High card")
        #return "hcard"
        return 1

def readData():
    file = open("7-thursday/input.txt")
    lines = file.readlines()
    hands = []
    bids = {}
    for l in lines:
        parts = l.split(' ')
        hands.append(parts[0])
        bids[parts[0]] = int(parts[1])

    return hands,bids


#order_dict = {'A' : 1,'K' : 2,'Q' : 3,'J' : 4,'T' : 5,'9' : 6,'8' : 7,'7' : 8,'6' : 9,'5' : 10,'4' : 11,'3' : 12,'2' : 13}

#hands = ["32T3K","T55J5","KK677","KTJJT","QQQJA"]
#bids = {"32T3K" : 765, "T55J5" : 684, "KK677" : 28,"KTJJT" : 220,"QQQJA" : 483}

hands,bids = readData()

types = {}
for h in hands:
    types[h] = getType(h)

ranking = sorted(types.items(),key=lambda x:x[1],reverse=True)
#ranking = sorted(types.items(),reverse=True)
n = len(ranking)

fives = []
fours = []
fulls = []
threes = []
twopairs = []
onepairs = []
hcards = []
counter = 0
for r in ranking:
    if r[1]==7:
        fives.append(r[0])
    elif r[1]==6:
        fours.append(r[0])
    elif r[1]==5:
        fulls.append(r[0])
    elif r[1]==4:
        threes.append(r[0])
    elif r[1]==3:
        twopairs.append(r[0])
    elif r[1]==2:
        onepairs.append(r[0])
    elif r[1]==1:
        hcards.append(r[0])
    counter += 1
    
order = ['A','K','Q','J','T','9','8','7','6','5','4','3','2']

fives = sorted(fives,key=lambda word : [order.index(c) for c in word])
fours = sorted(fours,key=lambda word : [order.index(c) for c in word])
fulls = sorted(fulls,key=lambda word : [order.index(c) for c in word])
threes = sorted(threes,key=lambda word : [order.index(c) for c in word])
twopairs = sorted(twopairs,key=lambda word : [order.index(c) for c in word])
onepairs = sorted(onepairs,key=lambda word : [order.index(c) for c in word])
hcards = sorted(hcards,key=lambda word : [order.index(c) for c in word])

totalWin = 0

print("FIVE OF A KIND")
len5 = len(fives)
for i in range(len5):
    print(fives[i]," - ",n-i)
    totalWin += bids[fives[i]]*(n-i)
n = n-len5
print("-----------------")

print("FOUR OF KIND")
len4 = len(fours)
for i in range(len4):
    print(fours[i]," - ",n-i)
    totalWin += bids[fours[i]]*(n-i)
n = n-len4
print("-----------------")

print("FULL")
lenfull = len(fulls)
for i in range(lenfull):
    print(fulls[i]," - ",n-i)
    totalWin += bids[fulls[i]]*(n-i)
n = n-lenfull
print("-----------------")

print("THREE OF A KIND")
len3 = len(threes)
for i in range(len3):
    print(threes[i]," - ",n-i)
    totalWin += bids[threes[i]]*(n-i)
n = n-len3
print("-----------------")

print("TWO PAIRS")
len2p = len(twopairs)
for i in range(len2p):
    print(twopairs[i]," - ",n-i)
    totalWin += bids[twopairs[i]]*(n-i)
n = n-len2p
print("-----------------")

print("ONE PAIR")
len1p = len(onepairs)
for i in range(len1p):
    print(onepairs[i]," - ",n-i)
    totalWin += bids[onepairs[i]]*(n-i)
n = n-len1p
print("-----------------")

print("HIGH CARD")
lenh = len(hcards)
for i in range(lenh):
    print(hcards[i]," - ",n-i)
    totalWin += bids[hcards[i]]*(n-i)
n = n-lenh
print("-----------------")


print("Total win: ",totalWin)