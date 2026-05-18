import random
class Cell:
    def __init__(self,row,col):
        self.row=row
        self.col=col
    def __repr__(self):
        return f'{self.row,self.col}'
    

# MINIMAL WORKING COUNTEXAMPLE MINIMAL WORKING ISSUE

#in a constructor evenutally

width=10 #self.
height=10 #self.
d=.7 #self.
grid=[] #self.
stack=[] #python list

for _ in range(height):
    new_row=[]
    for _ in range(width):
        randnumn=random.random()
        if randnumn<d:
            new_row.append(1)
        else:
            new_row.append(0)
    grid.append(new_row)

# end of constructor


grid #self.grid
for i in range(width):
    stack.append(Cell(0,i))

while stack: #while there are things left to explore!
    ted=stack.pop(-1) #this is the top of the stack in python!!!!!!
    ted_row=ted.row
    ted_col=ted.col
    
    neighbors=[]
    for horizontal in [-1,1]:
        neighbors.append(Cell(ted_row+horizontal,ted_col))    
    for vertical in [-1,1]:
        neighbors.append(Cell(ted_row,ted_col+vertical))
    for neighbor in neighbors:
        if not neighbor.row<height:
            continue # not a valid location!
        if not neighbor.col<width:
            continue # not a valid location!
        if grid[neighbor.row][neighbor.col]==5 or grid[neighbor.row][neighbor.col]==0:
            continue #already on fire or this is dirt!
        grid[neighbor.col][neighbor.row]=5
        stack.append(neighbor)


#beginning of __str__
return_str=''
for row in grid:
    return_str+=str(row)
    return_str+='\n'
return_str #return this
print(return_str)
#end of __str__


