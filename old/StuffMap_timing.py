from random import randint, seed, shuffle
from time import time

from old.StuffMap import Item, StuffMap, StuffSet, find_item_slow


def print_line():
    print("-" * 72)


def print_workbook_header():
    print("Direct Hashing Timing Workbook")
    print("==============================")
    print()
    print("Goal:")
    print("Compare three ways to answer lookup questions.")
    print()
    print("1. Linear search: walk through a list until the key is found.")
    print("2. StuffMap: jump straight to table[key] and return an item.")
    print("3. StuffSet: jump straight to table[key] and return True or False.")
    print()
    print_line()
    print()


def print_prediction_prompts():
    print("Before running the experiment, think:")
    print()
    print("A. If n doubles, what should happen to linear search time?")
    print("   Prediction: __________________________________________")
    print()
    print("B. If n doubles, what should happen to StuffMap lookup time?")
    print("   Prediction: __________________________________________")
    print()
    print("C. Why might StuffSet be a little simpler than StuffMap?")
    print("   Reason: ______________________________________________")
    print()
    print_line()
    print()


def build_items(n):
    """Create n items with keys 0 through n - 1, then shuffle them."""
    items = [Item(i, f"item-{i}") for i in range(n)]
    shuffle(items)
    return items


def time_linear_search(items, keys_to_find):
    start = time()
    for key in keys_to_find:
        find_item_slow(items, key)
    stop = time()
    return stop - start


def time_stuff_map(stuff, keys_to_find):
    start = time()
    for key in keys_to_find:
        stuff.get(key)
    stop = time()
    return stop - start


def time_stuff_set(stuff_set, keys_to_find):
    start = time()
    for key in keys_to_find:
        stuff_set.contains(key)
    stop = time()
    return stop - start


def run_timing():
    seed(1353)

    num_lookups = 5000
    print_workbook_header()
    print_prediction_prompts()

    print("Experiment setup:")
    print(f"Each row builds n items, then performs {num_lookups} random lookups.")
    print("The keys are direct hash keys: 0, 1, 2, ..., n - 1.")
    print()
    print("Timing results:")
    print("n\t\tlinear_search\t\tStuffMap\t\tStuffSet")

    for n in (1000, 2500, 5000, 10000, 20000):
        items = build_items(n)

        stuff = StuffMap(max_key=n - 1)
        stuff_set = StuffSet(max_key=n - 1)
        for item in items:
            stuff.put(item)
            stuff_set.add(item.key)

        keys_to_find = [randint(0, n - 1) for _ in range(num_lookups)]

        linear_time = time_linear_search(items, keys_to_find)
        stuff_map_time = time_stuff_map(stuff, keys_to_find)
        stuff_set_time = time_stuff_set(stuff_set, keys_to_find)

        print(f"{n}\t\t{linear_time:.6f}\t\t{stuff_map_time:.6f}\t\t{stuff_set_time:.6f}")

    print()
    print_line()
    print()
    print("After running the experiment:")
    print()
    print("1. Which column grows the most as n gets bigger?")
    print("   Answer: ______________________________________________")
    print()
    print("2. Which columns stay almost flat?")
    print("   Answer: ______________________________________________")
    print()
    print("3. What is the tradeoff for direct hashing?")
    print("   Hint: Think about a table with max_key = 1,000,000 but only 5 items.")
    print("   Answer: ______________________________________________")
    print()
    print("Big idea:")
    print("Direct hashing buys fast lookup by spending space on a table indexed by key.")


if __name__ == "__main__":
    run_timing()
