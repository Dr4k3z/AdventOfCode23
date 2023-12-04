file = open("data/day2.txt", "r")
df = file.readlines()

max_amount = {"red": 12, "green": 13, "blue": 14}
def IsPossible(bag):
    for color in bag:
        if bag[color] > max_amount[color]:
            return False
    return True

playable_games = {}
for line in df:
    id, cubes = line.split(":")
    id = int(id.split(" ")[-1])
    hands = cubes.split(";")
    playable_games[id] = True
    for h in hands:
        hand = h.split(",")
        hand_ = {"red": 0, "green": 0, "blue": 0}
        for cube_color in hand:
            amount, color = cube_color[1:].split(" ")
            if color[-1] == "\n":
                color = color[:-1]
            hand_[color] += int(amount)
        if not IsPossible(hand_) and playable_games[id]:
            playable_games[id] = False

sum = 0
for id in playable_games:
    sum += id if playable_games[id] else 0
print(sum)

################### Part 2 ###################

def Add(hand, new_hand):
    for color in hand:
        if hand[color] < new_hand[color]:
            hand[color] = new_hand[color]
    return(hand)

def PowerSet(hand):
    prod = 1
    for color in hand:
        prod *= hand[color]
    return(prod)

sum_power_set = 0
for line in df:
    id, cubes = line.split(":")
    id = int(id.split(" ")[-1])
    hands = cubes.split(";")
    playable_games[id] = True
    hand_minimum = {"red": 0, "green": 0, "blue": 0}
    for h in hands:
        hand = h.split(",")
        hand_ = {"red": 0, "green": 0, "blue": 0}
        for cube_color in hand:
            amount, color = cube_color[1:].split(" ")
            if color[-1] == "\n":
                color = color[:-1]
            hand_[color] += int(amount)
        hand_minimum = Add(hand_minimum, hand_)
    sum_power_set += PowerSet(hand_minimum)

print(sum_power_set)
