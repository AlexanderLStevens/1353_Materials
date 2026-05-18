class Node:
    def __init__(self,value):
        self.value=value
        self.friends=[]
    def add_friend(self,Node):
        self.friends.append(Node)
class SocialNetwork:
    def __init__(self):
        self.nodes=[]
    def add(self,name):
        self.nodes.append(Node(name))

COMP1353=SocialNetwork()
COMP1353.add('alex')
COMP1353.add('simon')
COMP1353.add('jillian')
COMP1353.nodes[0].add_friend(COMP1353.nodes[1])
print(COMP1353.nodes[0].friends)

