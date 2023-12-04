file = open("data/day3.txt", "r")
df = file.readlines()

lenght = len(df)
for i in range(lenght):
    df[i] = df[i][:-1] if df[i][-1] == '\n' else df[i]

width = len(df[0])

def IsInt(char):
    try:
        int(char)
    except:
        return False
    return True

numbers = []
symbols = []
row = 0
while row < lenght:
    line = df[row]
    col = 0
    while col < width:
        if IsInt(line[col]):
            number = line[col]
            coord = [(row, col)]
            col = col + 1
            while col < width:
                if IsInt(line[col]):
                    number += line[col]
                    coord.append((row, col))
                    col += 1
                else:
                    if line[col] != '.':
                        symbols.append((line[col], (row,col)))
                    break
            numbers.append((int(number), coord))
        elif line[col] != '.':
            symbols.append((line[col], (row,col)))
        col += 1
    row += 1


def Check(coord):
    x_spred, y_spred = (-1,0,1), (-1,0,1)
    for c in coord:
        for x in x_spred:
            for y in y_spred:
                for s in symbols:
                    if (c[0] + x, c[1] + y) == s[1]:
                        return True

    return False



part_numbers = []

for n in numbers:
    integer = n[0]
    coord = n[1]
    if Check(coord):
        part_numbers.append(integer)

print(sum(part_numbers))


#################### PART 2 ###################

gear_rateos = []
for s in symbols:
    if s[0] == '*':
        adjacent_parts = []
        x_spred, y_spred = (-1,0,1), (-1,0,1)
        for x in x_spred:
            for y in y_spred:
                for n in numbers:
                    integer = n[0]
                    coord = n[1]
                    for c in coord:
                        if (c[0] + x, c[1] + y) == s[1] and integer not in adjacent_parts:
                            adjacent_parts.append(integer)
        if len(adjacent_parts) == 2:
            #print(adjacent_parts)
            gear_rateos.append(adjacent_parts[0] * adjacent_parts[1])

print(sum(gear_rateos))
                        

