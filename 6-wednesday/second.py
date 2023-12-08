times = 48876981
distances = 255128811171623

counter = 0
for i in range(times):
    #print(i/times*100)
    vel = i
    delta = times-i
    dist = vel*delta
    #print("Hold button for ",i," travelled: ",dist)
    if dist>distances:
        counter += 1

print(counter)