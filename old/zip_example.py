class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


class SLL:
    """Simple singly linked list with append and iterator support."""

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node
        self.tail = new_node

    def __iter__(self):
        return SLLIterator(self.head)
class SLLIterator:
    def __init__(self,head:Node):
        self.curr=head
    def __next__(self):
        self.curr=head
        try:
            returnval=self.curr.value
            self.curr=self.curr.next
        except:
            raise StopIteration
        return returnval
    
    def __iter__(self):
        return self
    
Listy=SLL()
Listy.append(1)
Listy.append(2)
Listy.append(3)

sentinal=iter(Listy)
for num in sentinal:
    print(num)
