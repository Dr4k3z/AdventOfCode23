file = open("data/day4.txt", "r")
df = file.readlines()


sum = 0
scratchcards = []
instances = {}
for line in df:
    card, numbers_ = line.split(":")
    winning_numbers_, numbers_ = numbers_.split('|')
    card = int(card.split(" ")[-1])
    winning_numbers_ = winning_numbers_.split(" ")
    numbers_ = numbers_.split(" ")
    numbers = []
    winning_numbers = []
    count = 0
    for w in winning_numbers_:
        if w != '':
            winning_numbers.append(int(w))
    for n in numbers_:
        if n != '':
            numbers.append(int(n))
            if int(n) in winning_numbers:
                count += 1
    if count:
        # print(card, 2**(count - 1))
        sum += 2**(count - 1)
    scratchcards.append((card, winning_numbers, numbers))
    instances[card] = 1
print(sum)

#################### PART 2 ###################

for card in scratchcards:
    winning_numbers = card[1]
    numbers = card[2]
    count = 0
    for n in numbers:
        if int(n) in winning_numbers:
            count += 1
    current_instance = instances[card[0]]
    for i in range(1, count + 1):
        if  i < len(scratchcards):
            instances[card[0] + i] += current_instance

sum = 0
for i in instances:
    sum += instances[i]
print(sum)
