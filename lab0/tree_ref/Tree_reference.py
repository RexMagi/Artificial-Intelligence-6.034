def tree_ref(tree, idx):
    pointer = tree
    for i in idx:
        pointer = pointer[i]
    return pointer


tree = (((1, 2), 3), (4, (5, 6)), 7, (8, 9, 10))
res = tree_ref(tree,  (3, 1))
print(res)
