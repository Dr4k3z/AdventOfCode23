'''
The missing part wasn't the only issue - one of the gears in the engine is wrong.
A gear is any * symbol that is adjacent to exactly two part numbers.
Its gear ratio is the result of multiplying those two numbers together.
This time, you need to find the gear ratio of every gear and add them all up
so that the engineer can figure out which gear needs to be replaced.
'''

def list2int(l):
    sum = 0
    n = len(l)
    for i in range(n):
        sum += int(l[i])*pow(10,n-i-1)
    return sum

def horizontal(string):
    n = len(string)
    coeff = []
    for i in range(n):
        if string[i]=='*':
            counter_prev = 1
            counter_post = 1
            num_prev = []
            num_post = []
            while string[i+counter_post].isnumeric():
                num_post.append(string[i+counter_post])
                counter_post += 1
            while string[i-counter_prev].isnumeric():
                num_prev.insert(0,string[i-counter_prev])
                counter_prev += 1 

    return coeff

def vertical(up,curr,down):
    n = len(curr)
    coeff = []

    if down==[]:
        i = 0
        while i<n:
            num = []
            if curr[i].isnumeric():
                num.append(curr[i])
                counter = 1
                while curr[i+counter].isnumeric():
                    num.append(int(curr[i+counter]))
                    counter += 1
            
            m = len(num)
            for j in range(m):
                # vertical check
                if up[i+j]=='*':
                    coeff.append(list2int(num))
                    i += m
                    break
                # diagonal check
                if (up[i+j-1]=='*') or (up[i+j+1]=='*'):
                    coeff.append(list2int(num))
                    i += m
                    break
            i += 1
        return coeff
    elif up==[]:
        i = 0
        while i<n:
            num = []
            if curr[i].isnumeric():
                num.append(curr[i])
                counter = 1
                while curr[i+counter].isnumeric():
                    num.append(int(curr[i+counter]))
                    counter += 1
            
            m = len(num)
            for j in range(m):
                # vertical check
                if down[i+j]=='*':
                    coeff.append(list2int(num))
                    i += m
                    break
                # diagonal check
                if (down[i+j-1]=='*') or (down[i+j+1]=='*'):
                    coeff.append(list2int(num))
                    i += m
                    break
            i += 1
        return coeff
    else:
        i = 0
        while i<n:
            num = []
            if curr[i].isnumeric():
                num.append(curr[i])
                counter = 1
                while curr[i+counter].isnumeric():
                    num.append(int(curr[i+counter]))
                    counter += 1
            
            m = len(num)
            for j in range(m):
                # vertical check
                if up[i+j]=='*':
                    coeff.append(list2int(num))
                    i += m
                    break
                if down[i+j]=='*':
                    coeff.append(list2int(num))
                    i += m
                    break
                # diagonal check
                if (up[i+j-1]=='*') or (up[i+j+1]=='*'):
                    coeff.append(list2int(num))
                    i += m
                    break
                if (down[i+j-1]=='*') or (down[i+j+1]=='*'):
                    coeff.append(list2int(num))
                    i += m
                    break
            i += 1
        return coeff
            
import re
    
def main():
    file = open("3-sunday/input.txt")
    lines = file.readlines()

    n = len(lines)
    m = len(lines[0])

    for i in range(1,n-1):
        for j in range(1,m-1):
            counter = 0
            if lines[i][j]=='*':
                numsUp = re.findall(r'\d+',lines[i-1][j-3:j+3]) 
                numsCurr = re.findall(r'\d+',lines[i][j-3:j+3])
                numsDown = re.findall(r'\d+'.lines[i+1][j-3:j+3])

                
            if counter==2:
                pass 
            
# I NEED TO FINISH THIS!!!!


    '''N = len(lines)
    for i in range(1,N-1):
        h = horizontal(lines[i])
        v = vertical(lines[i-1],lines[i],lines[i+1])
        print(i," - ",h+v)'''

if __name__=="__main__":
    main()