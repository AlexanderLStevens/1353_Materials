class Item:
    """A small object with an integer key.

    Direct hashing works best when each object has a simple integer key.
    Here the key is the item's ID number.
    """

    def __init__(self, key, name, description=""):
        if not isinstance(key, int):
            raise TypeError("Item keys must be integers for direct hashing")
        if key < 0:
            raise ValueError("Item keys must be non-negative")

        self.key = key
        self.name = name
        self.description = description

    def __repr__(self):
        return f"Item({self.key}, {self.name!r})"


class StuffMap:
    """A map that uses direct hashing.

    Big idea:
    - If an item's key is 42, store it at array index 42.
    - To find key 42 later, jump directly to array index 42.

    This is also called a direct-address table. It is fast because there is no
    searching, but it only makes sense when the key range is not too huge.
    """

    def __init__(self, max_key):
        if max_key < 0:
            raise ValueError("max_key must be non-negative")

        self.max_key = max_key
        self.table = [None] * (max_key + 1)
        self.size = 0

    def _check_key(self, key):
        if not isinstance(key, int):
            raise TypeError("Keys must be integers")
        if key < 0 or key > self.max_key:
            raise KeyError(f"Key {key} is outside the direct hash table")

    def put(self, item):
        """Store an item using item.key as the array index."""
        self._check_key(item.key)

        if self.table[item.key] is None:
            self.size += 1

        self.table[item.key] = item

    def get(self, key):
        """Return the item with this key, or None if the slot is empty."""
        self._check_key(key)
        return self.table[key]

    def remove(self, key):
        """Remove and return the item with this key, or None if not present."""
        self._check_key(key)

        item = self.table[key]
        if item is not None:
            self.table[key] = None
            self.size -= 1
        return item

    def contains(self, key):
        self._check_key(key)
        return self.table[key] is not None

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def items(self):
        """Yield only the filled slots."""
        for item in self.table:
            if item is not None:
                yield item

    def __repr__(self):
        return f"StuffMap(size={self.size}, max_key={self.max_key})"


class StuffSet:
    """A set that uses direct hashing.

    A map answers: "What object belongs to this key?"
    A set answers: "Have I seen this key?"

    Direct hashing makes the set version very small. Key 42 is present if
    table[42] is True.
    """

    def __init__(self, max_key):
        if max_key < 0:
            raise ValueError("max_key must be non-negative")

        self.max_key = max_key
        self.table = [False] * (max_key + 1)
        self.size = 0

    def _check_key(self, key):
        if not isinstance(key, int):
            raise TypeError("Keys must be integers")
        if key < 0 or key > self.max_key:
            raise KeyError(f"Key {key} is outside the direct hash table")

    def add(self, key):
        self._check_key(key)

        if not self.table[key]:
            self.table[key] = True
            self.size += 1

    def contains(self, key):
        self._check_key(key)
        return self.table[key]

    def remove(self, key):
        self._check_key(key)

        if self.table[key]:
            self.table[key] = False
            self.size -= 1
            return True
        return False

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def keys(self):
        for key in range(len(self.table)):
            if self.table[key]:
                yield key

    def __repr__(self):
        return f"StuffSet(size={self.size}, max_key={self.max_key})"


def find_item_slow(items, key):
    """A linear search version, useful for comparison."""
    for item in items:
        if item.key == key:
            return item
    return None


def direct_hashing_demo():
    print("Direct hashing idea")
    print("-------------------")
    print("If the key is 3, put the item in table[3].")
    print("If the key is 8, put the item in table[8].")
    print("Later, getting key 8 means jumping straight to table[8].")
    print()

    stuff = StuffMap(max_key=10)

    pencil = Item(3, "pencil", "writes and erases")
    notebook = Item(8, "notebook", "stores class notes")
    calculator = Item(1, "calculator", "does arithmetic")

    stuff.put(pencil)
    stuff.put(notebook)
    stuff.put(calculator)

    print("The underlying array:")
    for index in range(len(stuff.table)):
        print(f"table[{index}] = {stuff.table[index]}")

    print()
    print("Lookups:")
    print("get(8) ->", stuff.get(8))
    print("get(3) ->", stuff.get(3))
    print("get(5) ->", stuff.get(5))

    print()
    print("Why this is cool:")
    print("A list search asks: is this it? is this it? is this it?")
    print("Direct hashing asks: what key? then jumps to that exact spot.")

    print()
    print("Direct hashing as a set")
    print("-----------------------")
    print("Sometimes we only care if a key is present.")
    print("Then table[key] can just be True or False.")
    print()

    packed_lunch_numbers = StuffSet(max_key=10)
    packed_lunch_numbers.add(2)
    packed_lunch_numbers.add(4)
    packed_lunch_numbers.add(9)

    print("The set's underlying array:")
    for index in range(len(packed_lunch_numbers.table)):
        print(f"table[{index}] = {packed_lunch_numbers.table[index]}")

    print()
    print("Membership checks:")
    print("contains(4) ->", packed_lunch_numbers.contains(4))
    print("contains(7) ->", packed_lunch_numbers.contains(7))
    print("keys in the set ->", list(packed_lunch_numbers.keys()))


if __name__ == "__main__":
    direct_hashing_demo()
