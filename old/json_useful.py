nums=[0 for _ in range(7)]

collisions=0

for i in range(7):
    for j in range(7):
        for k in range(7):
            collisions+=3-len(set([i,j,k]))

print(collisions/(7**3)) # expected number of collisions (smaller)

print(3/7) #this is a more honest expected number of edges in buckets across all buckets

