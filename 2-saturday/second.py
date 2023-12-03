'''
The Elf says they've stopped producing snow because they aren't getting any water! He isn't sure why the water stopped; however, he can show you how to get to the water source to check it out for yourself. It's just up ahead!

As you continue your walk, the Elf poses a second question: in each game you played, what is the fewest number of cubes of each color that could have been in the bag to make the game possible?

Again consider the example games from earlier:

Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
In game 1, the game could have been played with as few as 4 red, 2 green, and 6 blue cubes. If any color had even one fewer cube, the game would have been impossible.
Game 2 could have been played with a minimum of 1 red, 3 green, and 4 blue cubes.
Game 3 must have been played with at least 20 red, 13 green, and 6 blue cubes.
Game 4 required at least 14 red, 3 green, and 15 blue cubes.
Game 5 needed no fewer than 6 red, 3 green, and 2 blue cubes in the bag.
The power of a set of cubes is equal to the numbers of red, green, and blue cubes multiplied together. The power of the minimum set of cubes in game 1 is 48. In games 2-5 it was 12, 1560, 630, and 36, respectively. Adding up these five powers produces the sum 2286.
'''

def getNums(string):
    nums = {"red" : 0, "green" : 0, "blue" : 0}
    n = len(string)
    i = 0
    while i<n:
        if string[i].isnumeric():
            if string[i+1].isnumeric():
                if string[i+3]=='r':
                    nums["red"] = int(string[i])*10+int(string[i+1])
                    i += 4
                elif string[i+3]=='g':
                    nums["green"] = int(string[i])*10+int(string[i+1])
                    i += 6
                else:
                    nums["blue"] = int(string[i])*10+int(string[i+1])
                    i += 5
            elif string[i+2]=='r':
                nums["red"] = int(string[i])
                #i += 3
            elif string[i+2]=='g':
                nums["green"] = int(string[i])
            else:
                nums["blue"] = int(string[i])
        
        i += 1
    return nums

def find(string,c):
    n = len(string)
    idx = []
    for i in range(n):
        if string[i]==c:
            idx.append(i)
    return idx

def powerSet(string):
    begin = find(string,':')[0]+1
    ends = find(string,';')
 
    reds = []
    greens = []
    blues = []
    for e in ends:
        mydict = getNums(string[begin:e])

        nums = list(mydict.values())
        reds.append(nums[0])
        greens.append(nums[1])
        blues.append(nums[2])
        begin = e+1
    
    mydict = getNums(string[e+1:-1])
    nums = list(mydict.values())
    reds.append(nums[0])
    greens.append(nums[1])
    blues.append(nums[2])

    min_r = max(reds)
    min_g = max(greens)
    min_b = max(blues)

    return min_r*min_g*min_b

def readGame():
    test = ["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
            "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
            "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
            "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
            "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"]

    file = open("2-saturday/input.txt",'r')
    sum = 0
    for line in file:
        sum += powerSet(line)

    print("Sum of possible games: ",sum)

if __name__=="__main__":
    readGame()