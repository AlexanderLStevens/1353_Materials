# # get on slack
# # get on zoom
# # fill out OH 
# # get zybooks working



# # Indexed ~   contiguous    ~ relative address is computed via index 
# # Linked ~    disjoint units    ~ linked to one another using addresses

# # Most data structures use some combination of both

# #We start by looking at the linked list-- to do this we must understand a node

# #A node is some container for information (you can think of this as contiguous)

# #The node stores addresses (in some language it has a pointer, but in python we just think of address)

# #Lets look at a Node and see what attributes it should have!!


# #LinkedList class
# # __init__(self)  (with no additional arguments)
# # get_size(self) - returns the number of nodes in the list
# # is_empty(self) - returns True/False depending on whether the list has no nodes, or contains nodes
# # __str__(self) -  returns a str, representing the values of all items in the list
# # add_first(self, value) - inserts a new node with the parameter as the new first element
# # add_last(self, value) - appends a new node with the parameters as the new last element
# # remove_first(self) - removes the first node, returning its associated value
# # remove_last(self) - removes the last node, returning its associated value
# # get(self, index) - return the value stored at the given index position
# # remove_at_index(self, index) - removes the node at index i from the list, returning its associated value

class SLLIterator:
    def __init__(self,curr):
        self.curr=curr #the last node I was creeping and crawling on
    def __next__(self):
        
        try:
            return_val=self.curr.value
            self.curr=self.curr.next
        except AttributeError:
            raise StopIteration
        return return_val

    def __iter__(self):
        return self

class Node:
    def __init__(self,value=None,next=None):
        self.value=value
        self.next=next

class SinglyLinkedList:
    def __init__(self):
        self.head=None
        self.size=0
    
    def add_first(self,value):
        temp_node=Node(value)
        temp_node.next=self.head
        self.head=temp_node
    
    def __iter__(self):
        return SLLIterator(self.head)            

    
A=SinglyLinkedList()
for i in range(10):
    A.add_first(i)

for thing in A:
    print(thing)
