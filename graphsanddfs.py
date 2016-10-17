class Node:
    def __init__(self, id, _edges = None):
        self.id = id
        self.edges = [] if _edges is None else _edges

    def connect(self, edge, recurse = True):
        self.edges.append(edge)

        if recurse:
            edge.connect(self, False)

class TreeNode:
    def __init__(self, id, children = None):
        self.id = id
        self.children = [] if children is None else children

    def __str__(self):
        res = "{}\n".format(self.id)
        for child in self.children:
            res = res + "{}".format(child)
        
        return res

class Graph:
    def __init__(self, nodes = None):
        self.nodes = [] if nodes is None else nodes

    def dfs(self, start_id):
        return self._start_dfs(start_id)

    def _start_dfs(self, start_id):
        start_node = None
        for node in self.nodes:
            if node.id == start_id:
                start_node = node
                break

        return self._dfs(node, [])
        
    def _dfs(self, node, visited):
        _queue = []
        visited.append(node)

        for out in node.edges:
            if out not in visited:
                _queue.append(out)

        _children = []
        for next in _queue:
            _children.append(self._dfs(next, visited))

        return TreeNode(node.id, _children)

def test():
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)

    n1.connect(n2)
    n1.connect(n3)
    n1.connect(n4)

    n3.connect(n4)
    n3.connect(n6)
    
    n5.connect(n4)
    n5.connect(n6)

    graph = Graph([n1, n2, n3, n4, n5, n6])
    dfs_tree = graph.dfs(1)
    print(dfs_tree)
    


test()
