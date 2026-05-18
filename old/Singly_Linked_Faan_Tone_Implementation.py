import random
import logging
# An individual node in a singly-linked list.
# The value instance variable stores the contents of the element
# The type of the value instance variable should be consistent
# within a singly linked list. Other languages offer ways to
# ensure this. You will learn about that in OOP.
# The next instance variable refers to the next Node in the list,
# when next is None, then this node is the end of the list
class Node:
    def __init__(self, v, n = None):
        self.value = v
        self.next = n

    def __str__(self):
        return str(self.value)  
        # or return f"{self.value}"  
    
    # python has a flaw, that __str__ won't be called when you ask to output
    # a python list, instead __repr__ is called. We'll put this in here in
    # case we ever have a list of Node objects
    def __repr__(self):
        return self.__str__()

    # Two nodes are equal if their values are equal
    def __eq__(self, other):
        return self.value == other.value

# Note that we use CamelCase for class names in python
class SinglyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def __str__(self):
        if self.head is None:
            return "[]"
        else:
            current = self.head
            result = "["
            while not current.next is None:
                result += str(current) + " "
                current = current.next
            result = result + str(current) + ']'
            return result

    def __repr__(self):
        return self.__str__()

    def get_size(self)->int:
        return self.size

    def add_first(self, value)->None:
        """
            parameters:
                value: type is the same type as all other Nodes
            return value:
                None
           add a new node at the head of the list, with value as contents
        """
        # Create the new node, having it point to head:
        newNode = Node(value, self.head)
        self.head = newNode
        self.size += 1

    def add_last(self, value)->None:
        """
            parameters:
                value: type is the same type as all other Nodes
            return value:
                None
           add a new node at the end of the list, with value as contents
        """
        # Create the new node
        newNode = Node(value)
        # special case for empty list:
        if self.head is None:
            self.head = newNode
        else:
            # Find the last element
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            # attach the new node to the end of the list
            temp.next = newNode
        self.size += 1

    def remove_first(self):
        if self.head is None:
            return None
        else:
            value = self.head.value
            self.head = self.head.next
            self.size -= 1
            return value

    def remove_last(self):
        # if the list is empty, can't remove:
        if self.head is None:
            return None
        # if the list has exactly one element, the list becomes empty
        elif self.head.next is None:
            value = self.head.value
            self.head = None
            self.size = 0
            return value
        # general case, there are at least two elements:
        else:
            # Find the second-to-last element
            temp = self.head
            while not temp.next.next is None:
                temp = temp.next
            # now temp points to second-to-last, which will be the new last element
            value = temp.next.value
            temp.next = None
            self.size -= 1
            return value

    def remove_at_index(self, index:int):
        # confirm the index is valid
        if index > self.size-1 or index<0:
            raise IndexError(f"Index {index} invalid for size {self.size} in SinglyLinkedList.remove_at_index")
        # Special case for removing the first element:
        if index == 0:
            value = self.head.value
            self.head = self.head.next
            self.size-=1
            return value
        else:
            # There are at least two elements.
            # make temp point to the node BEFORE the one to remove
            temp = self.head
            for i in range(index-1):
                temp = temp.next
            value = temp.next.value
            temp.next = temp.next.next
            self.size -= 1
            return value

    def min(self):
        if self.head is None:
            return None
        result = self.head.value
        current = self.head.next
        result = self.head.value
        while not current is None:
            if current.value < result:
                result = current.value
            current = current.next
        return result
    
    def verify(self):
        # Empty List Check
        if self.head is None:
            if self.size != 0:
                print("SLL verify: head is None but list size is not 0")
                return False
        else:
            # Traverse the list. Make sure none of the values are None.
            # Also count the nodes and make sure the count matches the size
            temp = self.head
            count = 0
            while temp is not None:
                if temp.value is None:
                    print(f"SLL verify: node index {count} has a None pointer for its value.")
                    return False
                temp = temp.next
                count += 1
            if count != self.size:
                print(f"SLL verify: size ({self.size}) does not match the number of nodes ({count}).")
                return False
        return True
    

test_list = SinglyLinkedList()

# Say we forgot to increment the size in the add_first() method
test_list.add_first(5)

if test_list.verify():
    print("addFirst() method ok.")
else:
    print("Error in add_first() method")


def HomeworkDriver():
    random.seed(1)
    TestingList= SinglyLinkedList()
    for i in range(1,4):
        TestingList.add_first(i * random.randint(0,10))
        TestingList.add_last(i * random.randint(0,10))
        TestingList.add_first(i * random.randint(0,10))
        TestingList.add_last(i * random.randint(0,10))
    print(TestingList.verify())
    # print(TestingList)
    for _ in range(5):
        rand_index=random.randint(0,20)
        # print(f'rand_index is {rand_index}')
        try: TestingList.remove_at_index(rand_index)
        except IndexError as e:
            pass
            # print(e)
    print(TestingList)
HomeworkDriver()