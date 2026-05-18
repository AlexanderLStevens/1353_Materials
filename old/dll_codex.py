class Node:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return self.__str__()


class DoublyLinkedList:
    """A doubly linked list that stores values in Node objects."""

    def __init__(self):
        """
        Create an empty doubly linked list.

        TODO:
        - Set head to None.
        - Set tail to None.
        - Set size to 0.
        """
        self.head = None
        self.tail = None
        self.size = 0

    def get_size(self):
        """
        Return the number of nodes currently in the list.

        Returns:
            int: The current size of the list.
        """
        return self.size

    def is_empty(self):
        """
        Return True if the list has no nodes, otherwise return False.

        Returns:
            bool: True when the list is empty, False otherwise.

        TODO:
        - Use self.size, self.head, or both to determine whether the list
          is empty.
        """
        return self.size == 0

    def __str__(self):
        """
        LAB TASK:
        Implement __str__ for the DoublyLinkedList class.

        Return a string showing all values in the list from first to last.

        Example format:
            [2 4 6]

        Returns:
            str: A string representation of the list contents.

        TODO:
        - This method is intended to be completed during lab.
        - Traverse from self.head to the end of the list.
        - Collect each node's value as a string.
        - Return the values inside square brackets.
        - Separate the values with spaces or commas.
        """
        values = []
        current = self.head
        while current is not None:
            values.append(str(current.value))
            current = current.next
        return "[" + " ".join(values) + "]"

    def __repr__(self):
        return self.__str__()

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.value
            current = current.next

    def _validate_index(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")

    def _node_at(self, index):
        self._validate_index(index)
        if index < self.size // 2:
            current = self.head
            for _ in range(index):
                current = current.next
        else:
            current = self.tail
            for _ in range(self.size - 1, index, -1):
                current = current.prev
        return current

    def add_first(self, value):
        """
        Insert a new node containing value at the front of the list.

        Args:
            value: The value to store in the new first node.

        Returns:
            None

        TODO:
        - Create a new Node.
        - If the list is empty, update both head and tail.
        - Otherwise, link the new node before the current head.
        - Increase self.size by 1.
        """
        new_node = Node(value, None, self.head)
        if self.is_empty():
            self.tail = new_node
        else:
            self.head.prev = new_node
        self.head = new_node
        self.size += 1

    def add_last(self, value):
        """
        Append a new node containing value to the end of the list.

        Args:
            value: The value to store in the new last node.

        Returns:
            None

        #TODO
        - Create a new Node.
        - If the list is empty, update both head and tail.
        - Otherwise, link the new node after the current tail.
        - Increase self.size by 1.
        """
        new_node = Node(value, self.tail, None)
        if self.is_empty():
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.size += 1

    def remove_first(self):
        """
        LAB TASK:
        Implement remove_first for the DoublyLinkedList class.

        Remove the first node from the list and return its value.

        Returns:
            The value stored in the removed first node.

        Raises:
            IndexError: If the list is empty.

        TODO:
        - This method is intended to be completed during lab.
        - If your class later includes a helper like remove_between,
          this method may be only one line of code.
        - Check for the empty-list case.
        - Save the value at the head.
        - Update head to the next node.
        - Fix prev/next references as needed.
        - Update tail too if the list becomes empty.
        - Decrease self.size by 1 and return the saved value.
        """
        if self.is_empty():
            raise IndexError("Cannot remove from an empty list")

        value = self.head.value
        self.head = self.head.next

        if self.head is None:
            self.tail = None
        else:
            self.head.prev = None

        self.size -= 1
        return value

    def remove_last(self):
        """
        LAB TASK:
        Implement remove_last for the DoublyLinkedList class.

        Remove the last node from the list and return its value.

        Returns:
            The value stored in the removed last node.

        Raises:
            IndexError: If the list is empty.

        TODO:
        - This method is intended to be completed during lab.
        - If your class later includes a helper like remove_between,
          this method may be only one line of code.
        - Check for the empty-list case.
        - Save the value at the tail.
        - Update tail to the previous node.
        - Fix prev/next references as needed.
        - Update head too if the list becomes empty.
        - Decrease self.size by 1 and return the saved value.
        """
        if self.is_empty():
            raise IndexError("Cannot remove from an empty list")

        value = self.tail.value
        self.tail = self.tail.prev

        if self.tail is None:
            self.head = None
        else:
            self.tail.next = None

        self.size -= 1
        return value

    def get(self, index: int):
        """
        Return the value stored at the given index.

        Args:
            index (int): The position to retrieve.

        Returns:
            The value stored at the given index.

        Raises:
            IndexError: If index is out of bounds.

        TODO:
        - Validate that index is between 0 and self.size - 1.
        - Traverse to the node at that position.
        - Return that node's value.
        """
        return self._node_at(index).value

    def remove_at_index(self, index: int):
        """
        Remove the node at the given index and return its value.

        Args:
            index (int): The position of the node to remove.

        Returns:
            The value stored in the removed node.

        Raises:
            IndexError: If index is out of bounds.

        TODO:
        - Validate that index is between 0 and self.size - 1.
        - If index is 0, remove the first node.
        - If index is self.size - 1, remove the last node.
        - Otherwise, traverse to the target node.
        - Re-link the previous and next nodes around it.
        - Decrease self.size and return the removed value.
        """
        self._validate_index(index)
        if index == 0:
            return self.remove_first()
        if index == self.size - 1:
            return self.remove_last()

        target = self._node_at(index)
        value = target.value
        target.prev.next = target.next
        target.next.prev = target.prev
        target.prev = None
        target.next = None
        self.size -= 1
        return value

    def remove(self, value):
        """
        Remove the first node containing value and return that value.

        Raises:
            ValueError: If value does not appear in the list.
        """
        current = self.head
        index = 0
        while current is not None:
            if current.value == value:
                return self.remove_at_index(index)
            current = current.next
            index += 1
        raise ValueError(f"{value} is not in list")

    def search(self, value):
        """
        Return the index of the first occurrence of value in the list.

        Args:
            value: The value to search for.

        Returns:
            int: The index of the first matching node, or -1 if the value
            does not appear in the list.

        TODO:
        - Start at self.head.
        - Walk through the list one node at a time while tracking the
          current index.
        - If a node's value matches value, return that index immediately.
        - If the loop finishes without a match, return -1.
        """
        current = self.head
        index = 0
        while current is not None:
            if current.value == value:
                return index
            current = current.next
            index += 1
        return -1
    

if __name__ == "__main__":
    D = DoublyLinkedList()

    for i in range(10):
        D.add_first(i)

    print(D)
