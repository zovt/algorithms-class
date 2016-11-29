import sys


def parse_input(lines):
    # graph as an adjacency list
    graph = {}

    for line in lines:
        split = line.split(',')
        origin_id = int(split[0])
        edge_ids = [int(id) for id in split[1:]]
        
        graph[origin_id] = []
        for edge_id in edge_ids:
            if edge_id not in graph:
                graph[edge_id] = []

            graph[origin_id].append(edge_id)
            graph[edge_id].append(origin_id)

    return graph


def match(graph):
    # initialize network flow graph
    network_flow_graph = {}
    for id, edges in graph.items():
        if id <= 99:
            network_flow_graph[id] = edges

    # set up source and dest nodes
    copy = dict(network_flow_graph)
    network_flow_graph['source'] = []
    network_flow_graph['dest'] = []
    for id, edges in copy.items():
        network_flow_graph['source'].append(id)

        for edge in edges:
            network_flow_graph[edge] = ['dest']

    # check if there is a path between nodes
    def check_path(source, sink):
        path = []
        parents = {}
        visited = set()
        queue = []

        parents[source] = None
        queue.append(source)
        visited.add(source)

        while len(queue) is not 0:
            current = queue.pop()

            for edge in network_flow_graph[current]:
                if edge not in visited:
                    queue.append(edge)
                    parents[edge] = current
                    visited.add(edge)

        if sink in visited:
            current = sink
            while current in parents:
                path.append(current)
                current = parents[current]
            
            path.reverse()
            return (True, path)

        return (False, None)


    # Ford-Fulkerson
    max_flow = 0
    flows = {}
    for id, edges in network_flow_graph.items():
        for edge in edges:
            flows[(id, edge)] = 0

    (is_path, path) = check_path('source', 'dest')
    while is_path:
        current_path_flow = float('inf')


        (is_path, path) = check_path('source', 'dest')



def main():
    lines = sys.stdin.readlines()
    graph = parse_input(lines)
    result = match(graph)
    print(result)


main()
