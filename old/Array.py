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
    
