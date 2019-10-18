import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()


# runtime 6.8 seconds
# duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)


# first pass solution
# runtime 1.5 seconds
# duplicates = []
# for name in names_1:
#     if name in names_2:
#         duplicates.append(name)


# soultion using Binary Search Tree
# runtime 1.3 seconds
duplicates = []
# print(names_1[0])
container = BinarySearchTree(names_1[0])

for name in names_2:
    container.insert(name)

for name in names_1:
    if container.contains(name):
        duplicates.append(name)


end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
