'''
for str in test:
    numbers = []
    for c in str:
        try:
            a = int(c)
            numbers.append(a)
        except:
            pass
    print(numbers[0]*10+numbers[-1])
'''