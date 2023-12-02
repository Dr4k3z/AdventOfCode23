'''
Your calculation isn't quite right.
It looks like some of the digits are actually spelled out with letters:
one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".
Equipped with this new information, you now need to find the real first and last digit on each line. For example:

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen

In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.
'''

# turns words into numbers
mydict = {
    1 : "one",
    2 : "two",
    3 : "three",
    4 : "four",
    5 : "five",
    6 : "six",
    7 : "seven",
    8 : "eight",
    9 : "nine"}

test = ["two1nine","eightwothree","abcone2threexyz","xtwone3four","4nineeightseven2","zoneight234","7pqrstsixteen"]

def getKey(dictionary,word):
    keys = list(dictionary.keys())
    values = list(dictionary.values())
    idx = values.index(word)
    return keys[idx]

# Given a string, find the positions of the words inside of it
def findWord(string,word):
    n = len(string)
    m = len(word)
    for i in range(n):
        if string[i]==word[0] and n-i>=m:
            counter = 1
            for j in range(1,m):
                if string[i+j]==word[j]:
                    counter += 1
            if counter==m:
                return [i,word]
    return []
            
# Replace the words with actual numbers
def words2num(string):
    nums = {}
    for k in range(1,10):
        res = findWord(string,mydict[k])
        if res!=[]:
            nums[res[0]] = res[1]

    nums = dict(sorted(nums.items()))
    numsList = list(nums)

    firstKey = numsList[0]
    lastKey = numsList[-1]

    w1 = nums[firstKey]
    w2 = nums[lastKey]
    key1 = getKey(mydict,w1)
    key2 = getKey(mydict,w2)
    string = string.replace(w1,str(key1))
    return string.replace(w2,str(key2))

for word in test:
    #newStr,nums = words2num(word)
    #print(newStr," - ",nums)
    #for k in range(1,10):
    #    word = word.replace(dict[k],str(k))
    #    print(word)
    print(words2num(word))
    #print(word)