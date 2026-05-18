from random import shuffle, seed


#Here is how I like to make random numbers.

seed(10)
n=100
nums=[-2*i-1 for i in range(n//2)]+[2*i for i in range(n//2)]

shuffle(nums)

print(nums)