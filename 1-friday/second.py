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

from first import calibrate

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

    if nums == {}:
        return string

    print(nums)
    nums = dict(sorted(nums.items()))

    for n in nums:
        w = nums[n]
        k = getKey(mydict,w)
        string = string.replace(w,str(k)+w[-1])
        print(string)
    
    return string
    '''nums = dict(sorted(nums.items()))
    
    print(nums)
    
    numsList = list(nums)

    firstKey = numsList[0]
    lastKey = numsList[-1]

    w1 = nums[firstKey]
    w2 = nums[lastKey]
    key1 = getKey(mydict,w1)
    key2 = getKey(mydict,w2)
    string = string.replace(w1,str(key1)+w1[-1])
    return string.replace(w2,str(key2))'''

def main():
    file = open("1-friday/calibration.txt")
    
    #file = ["two1nine","eightwothree","abcone2threexyz","xtwone3four","4nineeightseven2","zoneight234","7pqrstsixteen"]
    
    #f = open("../diff1.csv",'w')

    sum = 0
    for line in file:
        n = len(line)
        line = line[0:n-1]
        new_line = words2num(line)
        sum += calibrate(new_line)
        #print(line," - ",calibrate(new_line))
        #print(sum)
        #f.write(str(sum)+'\n')
        if sum == 17081:
            print(line)
            break

    print("Sum of calibration values: ",sum)

def prova():
    s = "cpceightwo3"
    new_s = words2num(s)
    print(s," - ",calibrate(new_s))

if __name__=="__main__":
    main()
