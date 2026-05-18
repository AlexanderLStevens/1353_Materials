import numpy as np



import numpy as np
class ArrayList:
    def __init__(self):
        self.capacity = 10  # initial capacity
        self.size = 0
        self.array = np.empty(self.capacity, dtype=object)

    def get(self, i):
        if i < 0 or i >= self.size:
            raise IndexError('Index out of range')
        return self.array[i]

    def append(self, e):
        if self.size == self.capacity:
            self.expand_array()
        self.array[self.size] = e
        self.size += 1

    def remove(self, i):
        if i < 0 or i >= self.size:
            raise IndexError('Index out of range')
        for j in range(i, self.size - 1):
            self.array[j] = self.array[j + 1]
        self.size -= 1

    def set(self, i, e):
        if i < 0 or i >= self.size:
            raise IndexError('Index out of range')
        self.array[i] = e

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size == 0



class ArrayListGeometric(ArrayList):

    def expand_array(self):
        self.capacity *= 2
        new_array = np.empty(self.capacity, dtype=object)
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
    def __iter__(self):
        return ArrayListGeometricIterator(self.array)

class ArrayListGeometricIterator:
    def __init__(self, array):
        self.array=array
        self.curr=-1
    def __next__(self):
        self.curr+=1
        try:
            return self.array[self.curr]
        except IndexError:
            raise StopIteration
    def __iter__(self):
        return self




class ArrayListArithmetic(ArrayList):

    def expand_array(self):
        self.capacity +=1000
        new_array = np.empty(self.capacity, dtype=object)
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array 

A=ArrayListGeometric()
for i in range(10):
    A.append(i)
for item in A:
    print(item)



# from time import time  
# print(f"n\t\telapsed_time\t\truntime")

# num_trial = 1
# for n in (25000, 50000, 100000, 200000):
#     start = time()

#     for j in range(num_trial):
#         A=ArrayListArithmetic()
#         for i in range(n):
#             A.append(i)
#         #Append n elements
        
#     stop = time()
#     print(f"{n}\t\t{stop - start}\t\t{(stop - start)/num_trial}")



