all_nodes = {}
class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
    def add_right(self,node):
        if self.right == None:
            self.right = node
    def add_left(self,node):
        if self.left == None:
            self.left = node
    def __repr__(self):
        return f"{self.value} has left node({self.left.value}) and right node({self.right.value})"

def add_node(node):
    if node not in all_nodes.keys():
        n = Node(node)
        all_nodes[node] = n
    else:
        n = all_nodes[node]
    return n

def add_node_line(node,left,right):
    n = add_node(node)
    l = add_node(left)
    r = add_node(right)
    n.add_left(l)
    n.add_right(r)    

with open("input.txt") as map:
    for i,line in enumerate(map):
        if line.strip() == "":
            continue
        if i == 0:
            direction = line[:-1]
        else:
            node,path = line.split("=")
            left,right = path.strip()[1:-1].split(",")
            add_node_line(node.strip(),left.strip(),right.strip())

steps = 0
current_node = all_nodes["AAA"]
while current_node.value != "ZZZ":
    for d in direction:
        if d == 'R':
            current_node = current_node.right
        else:
            current_node = current_node.left
        steps += 1

print(steps)

            

