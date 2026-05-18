


#Using the MAD method (multiply by a, add b)
# a=2 b=3 N=10 p=11

#draw the hashtable with the following values inserted
# [0,1,2,3,4,5]

hashtable=[[] for _ in range(10)]


hashtable[3].insert(0,0) # (((2*0)+3)%11)%10
hashtable[5].insert(0,1)
hashtable[7].insert(0,2)
hashtable[9].insert(0,3)
hashtable[0].insert(0,4)
hashtable[0].insert(0,'p')

print(hashtable)
