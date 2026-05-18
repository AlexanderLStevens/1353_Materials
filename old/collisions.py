







# # SET DATA TYPE

# A=frozenset(['a','b','b','c','f'])

# B=frozenset(['a','b','b','c','d','e'])

# C=frozenset(['a','b', 'r'])


# print(A.union(B.intersection(C)))

# print((A.union(B)).intersection(A.union(C)))

import random
n=77
numbers=[random.randint(-100,100) for _ in range(n)]
def alg2(target:int,numbers:list):
    seen={} # with dict
    for num in numbers:
        if target-num in seen:
            return True
        seen[num]='whatever'

    return num, target-num

print(alg2(8,numbers))





















# import random
# capacity=150
# the_table=[[] for _ in range(capacity)]

# size=100
# for i in range(size):
#     index=random.randint(0,capacity-1)
#     bucket=the_table[index]
#     bucket.insert(0,i)

# for bucket in the_table:
#     print(bucket)

