# https://www.hackerrank.com/challenges/dijkstrashortreach
import sys
from heapq import *

class Edge:
    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight
        

    def __str__(self):
        return repr(self)
    

    def __repr__(self):
        return '{} --{}--> {}'.format(repr(self.src), self.weight, repr(self.dest))
        
    
    def __lt__(self, other):
        return self.weight < other.weight
    

class Node:
    def __init__(self, id, edges = None):
        self.id = id
        
        if edges is None:
            self.edges = []
            return
        
        self.edges = edges
        
    
    def __str__(self):
        return "Node ID: {}\nEdges: {}\n{}".format(self.id, len(self.edges),
                '\n'.join([str(edge) for edge in self.edges]))
        
    def __repr__(self):
        return str(self.id)
        
    def add_link(self, node, weight, recurse = True):
        self.edges.append(Edge(self, node, weight))
        
        if recurse:
            node.add_link(self, weight, False)

class Graph:
    def __init__(self, nodes = None):
        self.nodes = {}
        
        if nodes is None:
            return
            
        for node in nodes:
            self.nodes[node.id] = node
            

    def __str__(self):
        return '\n'.join([str(node) for id, node in self.nodes.items()])
    

    def add_node(self, node):
        self.nodes[node.id] = node
        

    def add_nodes(self, nodes):
        for node in nodes:
            self.add_node(node)
            
    def djikstra(self, start_node_id):
        start_node = self.nodes[start_node_id]
        
        current_values = {}
        for id, node in self.nodes.items():
            if node is not start_node:
                current_values[node] = float("inf")
                
        current_values[start_node] = 0

        visited = set()
        queue = []
        for edge in start_node.edges:
            heappush(queue, edge)
            
        while len(queue) is not 0:
            current_edge = heappop(queue)
            visited.add()
                
            
        shortest_paths = {}
        for node, value in current_values.items():
            if node is not start_node:
                shortest_paths[node] = current_values[node]

        return shortest_paths
                    
        

def parse_input(lines):
    num_tests = int(lines[0])
    graphs = []
    start_vertices = []
    offset = 1
    for i in range(num_tests):
        graph = Graph()
        [num_nodes, num_edges] = [int(i) for i in lines[offset].split(' ')]
        
        nodes = {}
        for n in range(num_nodes):
            [node_id, link_id, weight] = [int(i) for i in lines[offset + n + 1].split(' ')]
            
            if node_id not in nodes:
                nodes[node_id] = Node(node_id)
                
            if link_id not in nodes:
                nodes[link_id] = Node(link_id)
            
            node = nodes[node_id]
            link = nodes[link_id]
            
            node.add_link(link, weight)
            
        graph.add_nodes([node for id, node in nodes.items()])
        graphs.append(graph)
        start_vertices.append(int(lines[offset + num_nodes + 1]))
        
        offset = offset + num_nodes + 2
    
    return (graphs, start_vertices)


def main():
    lines = sys.stdin.readlines()
    (graphs, start_vertices) = parse_input(lines)
    for i, graph in enumerate(graphs):
        paths = graph.djikstra(start_vertices[i])
        print(paths)


main()
