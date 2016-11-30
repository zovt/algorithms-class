import sys
import time


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
    def bfs(source, sink, capacities, residual_graph, residual, flows):
        parents = {}
        visited = set()
        queue = []
        path_caps = {}

        parents[source] = None
        path_caps[source] = float('inf')
        queue.append(source)
        visited.add(source)

        while len(queue) is not 0:
            current = queue.pop(0)

            for out in residual_graph[current]:
                if out not in visited and residual[(current, out)] > 0:
                    parents[out] = current
                    path_caps[out] = min(path_caps[current],
                            capacities[(current, out)] - flows[(current, out)])
                    
                    if out is not sink:
                        queue.append(out)
                    else:
                        return path_caps[sink], parents
                    
        return 0, None

    # Edmonds-Karp
    # init network flow graph
    flow_graph = {}
    flow_graph['source'] = []
    flow_graph['dest'] = []
    for n, e in graph.items():
        if n <= 99:
            flow_graph[n] = e
            flow_graph['source'].append(n)
        else:
            flow_graph[n] = ['dest']
            flow_graph['dest'].append(n)
            
    flows = {}
    for n, e in flow_graph.items():
        for ep in e:
            flows[(n, ep)] = 0
            flows[(ep, n)] = 0
            
    # flows and capacities
    capacities = {}
    for n, e in flow_graph.items():
        for ep in e:
            capacities[(n, ep)] = 1
            capacities[(ep, n)] = 1
    
    residual = dict(capacities)
    residual_graph = dict(flow_graph)
            
    flow = 0
    while True:
        (min_cap, parents) = bfs('source', 'dest', capacities, residual_graph, residual, flows)
        if min_cap is 0: break
        
        flow += min_cap
            
        current = 'dest'
        while True:
            if current is 'source': break
            parent = parents[current]
            
            # add residual graph edges
            if parent not in residual_graph:
                residual_graph[parent] = []
                
            if current not in residual_graph:
                residual_graph[current] = []
                
            if current not in residual_graph[parent]:
                residual_graph[parent].append(current)
                
            if parent not in residual_graph[current]:
                residual_graph[current].append(parent)
            
            # update flows and capacities
            flows[(parent, current)] += min_cap
            flows[(current, parent)] -= min_cap
            residual[(parent, current)] -= min_cap
            residual[(current, parent)] += min_cap
            current = parents[current]
    
    out = {source: dest for (source, dest), weight in flows.items() if weight is 1 and source in graph and dest in graph}
    
    return (flow, out)

def main():
    lines = sys.stdin.readlines()
    graph = parse_input(lines)
    (flow, result) = match(graph)
    for i, j in result.items():
        print('{},{}'.format(i, j))


main()
