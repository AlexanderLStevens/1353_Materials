from Trees.Tree import BinaryTree

#ABSTRACT DATA TYPE

tree = BinaryTree()
A=tree.add_root("A")
B=tree.add_left(A,"B")
C=tree.add_right(A,"C")
D=tree.add_left(B,"D")
E=tree.add_right(B,"E")
F=tree.add_left(C,"F")
G=tree.add_right(C,"G")

# H=tree.add_left(D,"H")

print(tree._str_helper(tree.root,0))

print((tree.root.left_child.left_child).node_depth())

# print(tree._str_helper(tree.root,0))
# print(A.node_depth())
