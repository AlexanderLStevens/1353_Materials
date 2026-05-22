class TreeNode:
    def __init__(self,parent,lchild,rchild,value):
        self.parent=parent
        self.left_child=lchild
        self.right_child=rchild
        self.value=value
    
    def set_value(self,v):
        self.value=v
    
    def is_external(self):
        if self.left_child is None and self.right_child is None:
            return True
        else:
            return False
    
    def is_internal(self):
        return not self.is_external()

    def __str__(self):
        return str(self.value)
    
    def __repr__(self):
        return str(self)
    def node_height(self):
        lh=-1
        rh=-1
        if self.left_child is not None:
            lh=self.left_child.node_height()
        if self.right_child is not None:
            rh=self.right_child.node_height()
        return max(lh,rh)+1
    def node_depth(self):
        if self.parent is None:
            return 0
        else:
            return self.node_depth(self.parent)+1
class BinaryTree:
    def __init__(self):
        self.root=None
        self.size=0
        
    def add_root(self,value):#keep
        if not self.root is None:
            raise ValueError("BinaryTree.add_root: root already exists")
        
        return_value=TreeNode(None,None,None,value)
        self.root=return_value
        self.size+=1
        return return_value
    
    def add(self,value):
        if self.root is None:
            self.add_root(value)
            return
        curr=self.root

        while True:
            if curr.value> value: # moving through left subtree
                if not curr.left_child:
                    self.add_left(curr,value)
                    return
                else: 
                    curr=curr.left_child
            else: #moving through right subtree
                if not curr.right_child:
                    self.add_right(curr,value)
                    return
                else: 
                    curr=curr.right_child





            

         #



    def add_left(self,parent:TreeNode,value)->TreeNode:
        if parent.left_child is not None:
            raise ValueError("left child already exists")
        return_value=TreeNode(parent, None,None,value)
        parent.left_child=return_value
        self.size+=1
        return return_value
    
    def add_right(self,parent:TreeNode,value):
        if parent.right_child is not None:
            raise ValueError("right child already exists")
        return_value=TreeNode(parent, None,None,value)
        parent.right_child=return_value
        self.size+=1
        return return_value
    
    def __str__(self):
        return self._str_helper(self.root,0)
    
    def _str_helper(self,parent:TreeNode,level):
    
        parent_str='\t'*level+str(parent)+'\n'
        
        if parent.left_child is not None:
            lchild_str=self._str_helper(parent.left_child,level+1)
            parent_str+=lchild_str
            
        if parent.right_child is not None:
            rchild_str=self._str_helper(parent.right_child,level+1)
            parent_str+=rchild_str
        
        return parent_str

        
def _main():
    tree = BinaryTree()
    n=10
    tree.add(5)
    tree.add(3)
    tree.add(2)
    tree.add(1)
    tree.add(4)
    tree.add(7)
    tree.add(6)
    tree.add(9)
    tree.add(8)
    
        # A=tree.add_root("A")
    # B=tree.add_left(A,"B")
    # C=tree.add_right(A,"C")
    # D=tree.add_left(B,"D")
    # E=tree.add_right(B,"E")
    # F=tree.add_left(C,"F")
    # H=tree.add_left(D,"H")
    # I=tree.add_right(D,"I")
    # J=tree.add_left(E,"J")
    # K=tree.add_right(E,"K")
    print(tree._str_helper(tree.root,0))
    # print(A.node_depth())


if __name__ == '__main__':
    _main()
