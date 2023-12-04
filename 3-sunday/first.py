'''
You and the Elf eventually reach a gondola lift station; he says the gondola lift will take you up to the water source, but this is as far as he can bring you. You go inside.

It doesn't take long to find the gondolas, but there seems to be a problem: they're not moving.

"Aaah!"

You turn around to see a slightly-greasy Elf with a wrench and a look of surprise. "Sorry, I wasn't expecting anyone! The gondola lift isn't working right now; it'll still be a while before I can fix it." You offer to help.

The engineer explains that an engine part seems to be missing from the engine, but nobody can figure out which one. If you can add up all the part numbers in the engine schematic, it should be easy to work out which part is missing.

The engine schematic (your puzzle input) consists of a visual representation of the engine. There are lots of numbers and symbols you don't really understand, but apparently any number adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum. (Periods (.) do not count as a symbol.)

Here is an example engine schematic:

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: 114 (top right) and 58 (middle right). Every other number is adjacent to a symbol and so is a part number; their sum is 4361.

Of course, the actual engine schematic is much larger. What is the sum of all of the part numbers in the engine schematic?

'''
syms = [ '*', '&', '@', '/', '+', '#', '$', '%', '=', '-']

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
        if string[i] in syms:
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
        
            m1 = len(num_post)
            m2 = len(num_prev)
            n1, n2 = 0,0
            for i in range(m1):
                n1 += int(num_post[i])*pow(10,m1-i-1)
            
            for i in range(m2):
                n2 += int(num_prev[i])*pow(10,m2-i-1)

            if n1!=0:
                coeff.append(n1)
            if n2!=0:
                coeff.append(n2)
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
                if up[i+j] in syms:
                    coeff.append(list2int(num))
                    i += m
                    break
                # diagonal check
                if (up[i+j-1] in syms) or (up[i+j+1] in syms):
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
                if down[i+j] in syms:
                    coeff.append(list2int(num))
                    i += m
                    break
                # diagonal check
                if (down[i+j-1] in syms) or (down[i+j+1] in syms):
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
                if up[i+j] in syms:
                    coeff.append(list2int(num))
                    i += m
                    break
                if down[i+j] in syms:
                    coeff.append(list2int(num))
                    i += m
                    break
                # diagonal check
                if (up[i+j-1] in syms) or (up[i+j+1] in syms):
                    coeff.append(list2int(num))
                    i += m
                    break
                if (down[i+j-1] in syms) or (down[i+j+1] in syms):
                    coeff.append(list2int(num))
                    i += m
                    break
            i += 1
        return coeff

def main(file):
    lines = file.readlines()
    N = len(lines)

    sum = 0
    for i in range(N):
        if i==N-1:
            h = horizontal(lines[i])
            v = vertical(lines[i-1],lines[i],[])
            s = 0
            for el in h+v:
                s += el
            print(i,": ",s)
        elif i==0:
            h = horizontal(lines[i])
            v = vertical([],lines[i],lines[i+1])
            s = 0
            for el in h+v:
                s += el
            print(i,": ",s)
        else:
            h = horizontal(lines[i])
            v = vertical(lines[i-1],lines[i],lines[i+1])
            s = 0
            for el in h+v:
                s += el
            print(i+1,": ",s)
        sum += s

    print("Part numbers: ",sum)

if __name__=="__main__":
    file = open("3-sunday/input.txt")
    main(file)