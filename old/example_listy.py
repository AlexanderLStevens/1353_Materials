example_list=[1,2,3,4,5,6,7,8,9]

# example_list.remove(4)

for i in range(len(example_list)):
    if example_list[i]==4:
        bad_index=i
example_list.pop(bad_index)

print(example_list)