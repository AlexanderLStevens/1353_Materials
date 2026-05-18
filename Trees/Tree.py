

#DATA STRUCTURE PERSPECTIVE!!!!
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
        if self.left_child is None and self.right_child is None:
            return 0
        left_height=-1
        right_height=-1

        left_height=TreeNode.node_height(self.left_child)
        right_height=TreeNode.node_height(self.right_child)

        return max(left_height,right_height)+1
    def node_depth(self):
        if self.parent:
            return self.parent.node_depth()+1
        return 0
    def __rep__(self):
        return f'{self.parent},{self.lchild},{self.rchild},{self.value}'

class BinaryTree:
    def __init__(self):
        self.root=None
        self.size=0
        
    def add_root(self,value):#keep
        if self.root is not None:
            raise ValueError("BinaryTree.add_root: root already exists")
        
        return_value=TreeNode(None,None,None,value)
        self.root=return_value
        self.size+=1
        return return_value
    
    def add_left(self,parent:TreeNode,value)->TreeNode:
        if parent.left_child is not None:
            raise ValueError("node.add_left: left already exists")
        
        return_node = TreeNode(parent,None,None,value)
        parent.left_child=return_node
        self.size+=1
        return return_node
    
    def add_right(self,parent:TreeNode,value):
        if parent.right_child is not None:
            raise ValueError("node.add_left: left already exists")

        return_node = TreeNode(parent,None,None,value)
        parent.right_child=return_node
        self.size+=1
        return return_node
    
    def __str__(self):
        return self._str_helper(self.root,0)
    
    def _str_helper(self,parent:TreeNode,level=0):
        
        '\t'*level
        parent_string=f'{'\t'*level} {parent} \n'

        left_child = parent.left_child
        left_string=''
        if left_child:
            left_string=self._str_helper(left_child,level+1)
        
        right_child = parent.right_child
        right_string=''
        if right_child:
            right_string=self._str_helper(right_child,level+1)

        return f'{parent_string}{left_string}{right_string}'
        #process the parent, then left and then print right



    def __rep__(self):
        return f'{self.root},{self.size}'