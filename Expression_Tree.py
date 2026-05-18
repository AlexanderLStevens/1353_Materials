from Trees import BinaryTree

class ExpressionTree(BinaryTree):
    def __str__(self)->str:
        if self.root is None:
            return ''
        return self._str_helper(self.root)
    
    def _str_helper(self,node)->str:
        if node.is_external():
            return str(node.value)
        
        if node.left_child is None or node.right_child is None:
            raise ValueError("ExpressionTree._str_helper: operators need two operands")
        
        left_string = self._str_helper(node.left_child)
        right_string = self._str_helper(node.right_child)
        return f'({left_string} {node.value} {right_string})'
        
    def evaluate(self,node)->float:
        if node is None:
            raise ValueError("ExpressionTree.evaluate: cannot evaluate an empty tree")
        
        if node.is_external():
            return float(node.value)
        
        if node.left_child is None or node.right_child is None:
            raise ValueError("ExpressionTree.evaluate: operators need two operands")
        
        left_value = self.evaluate(node.left_child)
        right_value = self.evaluate(node.right_child)
        
        if node.value == '+':
            return left_value + right_value
        elif node.value == '-':
            return left_value - right_value
        elif node.value == '*':
            return left_value * right_value
        elif node.value == '/':
            return left_value / right_value
        else:
            raise ValueError(f"ExpressionTree.evaluate: unknown operator {node.value}")
           
def _main():
    tree = ExpressionTree()

    r = tree.add_root("-")
    rl = tree.add_left(r, "/")
    rll = tree.add_left(rl, "*")
    rlll = tree.add_left(rll, "+")
    rllll = tree.add_left(rlll, "3")
    rlllr = tree.add_right(rlll, "1")
    rllr = tree.add_right(rll, "3")
    rlr = tree.add_right(rl, "+")
    rlrl = tree.add_left(rlr, "-")
    rlrll = tree.add_left(rlrl, "9")
    rlrlr = tree.add_right(rlrl, "5")
    rlrr = tree.add_right(rlr, "2")
    rr = tree.add_right(r, "+")
    rrl = tree.add_left(rr, "*")
    rrll = tree.add_left(rrl, "3")
    rrlr = tree.add_right(rrl, "-")
    rrlrl = tree.add_left(rrlr, "7")
    rrlrr = tree.add_right(rrlr, "4")
    rrr = tree.add_right(rr, "6")

    print(tree, end='')
    print('=',tree.evaluate(tree.root))


if __name__ == '__main__':
    _main()
