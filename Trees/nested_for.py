# import random

# n=10
# the_table=[[] for _ in range(2)]
# for i in range(n):
#     index=random.randint(0,1)
#     the_table[index].append(i)


# for i in range(2):
#     print(the_table[i])

# for item in the_table[0]: # this has length k
#     print(item)
# for item in the_table[1]: # has length n-k
#     print(item)

#total will be n-k+k=n

# def get(self, k):
#     for bucket in self.the_table: #O(n) The length of the table
#         for item in bucket: #O(1) Load factor guarantees that this is O(1)_Expected
#             if item.key == k:
#                 return item.value
#     return None


prefixSums = { 0 : 1 }


try:
    thing=prefixSums[2]
except:
    thing=0

print(thing)
