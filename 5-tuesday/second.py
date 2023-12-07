# THIS CODE DOESN'T WORK

import re

fileNamesExample = ["5-tuesday/input/seed2soil.txt","5-tuesday/input/soil2fertilizer.txt","5-tuesday/input/fertilizer2water.txt","5-tuesday/input/water2light.txt","5-tuesday/input/light2temperature.txt","5-tuesday/input/temperature2humidity.txt","5-tuesday/input/humidity2location.txt"]
fileNames = ["5-tuesday/seed2soil.txt","5-tuesday/soil2fertilizer.txt","5-tuesday/fertilizer2water.txt","5-tuesday/water2light.txt","5-tuesday/light2temperature.txt","5-tuesday/temperature2humidity.txt","5-tuesday/humidity2location.txt"]

def createMaps(fileName):
    #print(fileName)
    file = open(fileName)
    src_range = []
    for line in file:
        numsStr = re.findall(r'\d+',line)
        nums = len(numsStr)*[None]
        for i in range(len(numsStr)):
            nums[i] = int(numsStr[i])
        src_range.append([nums[0],nums[1],nums[1]+nums[2]-1])
    return src_range

def location(s):
    chain = [s]
    for file in fileNames:
        src_range = createMaps(file)
        n = len(src_range)
        flag = False
        for i in range(n):
            if chain[-1]>=src_range[i][1] and chain[-1]<=src_range[i][2]:
                #print(chain[-1]," found in range ",src_range)
                diff = chain[-1]-src_range[i][1]
                chain.append(src_range[i][0]+diff)
                flag = True
                break
        if not flag:
            chain.append(chain[-1])
        #print(chain[-1])
    return chain[-1]

def main():
    file_seeds = open("5-tuesday/seeds.txt")
    seeds = []
    for line in file_seeds:
        nums = re.findall(r'\d+',line)
        i = 0
        while i<len(nums)-1:
            print(i/len(nums)*100)
            rng = range(int(nums[i]),int(nums[i])+int(nums[i+1]))
            counter = 0
            for r in rng:
                print(counter/len(rng)*100)
                seeds.append(r)
                counter += 1
            i += 2
    #print(seeds)

    map = {}
    for s in seeds:
        #print("Seed ",s)
        map[s] = location(s)
    #print(map)

    idx = min(map.values())
    print("lowest location number: ",idx)

if __name__=="__main__":
    main()