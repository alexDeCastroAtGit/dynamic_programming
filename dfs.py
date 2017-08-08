from digraph import *


def print_path(path):
    """Assumes path is a list of nodes"""
    result = ''
    for i in range(len(path)):
        result += str(path[i])  # PEP80 directive
        if i != (len(path) - 1):
            result += '->'
    return result


def path_length(path, graph): # recursive?
    """Assumes path is a list of nodes and that path is a valid path in graph"""
    # for n in path:
    # wt_len = graph.edges[n]
    pass


def depth_first_search(graph, start, end, path, shortest, to_print=False):
    """
    Assumes graph is a digraph; start and end are nodes;
    path and shortest are lists of nodes.
    Returns a shortest path from start to end in graph.
    """
    path += [start]
    # path = path + [start]
    if to_print:
        print('Current DFS path', print_path(path))
    if start == end:
        return path
    for node in graph.children_of(start):
        if node not in path:  # avoid circles
            if not shortest or len(path) < len(shortest):
                new_path = depth_first_search(graph, node, end, path, shortest,
                                              to_print)  # tail recursive function
                if new_path:
                    shortest = new_path
    return shortest


# helper function
def shortest_path(graph, start, end, to_print=False):
    """
    Assumes graph is digraph; start and end are nodes;
    Returns a shortest path from start to end in graph.
    """
    return depth_first_search(graph, start, end, [], None, to_print=to_print)


def test_shortest_path():
    nodes = []
    for name in range(6):  # create 6 nodes
        nodes.append(Node(str(name)))
    g = Digraph()
    for n in nodes:
        g.add_node(n)
    g.add_edge(WeightedEdge(nodes[0], nodes[1]))
    g.add_edge(WeightedEdge(nodes[1], nodes[2]))
    g.add_edge(WeightedEdge(nodes[2], nodes[3]))
    g.add_edge(WeightedEdge(nodes[2], nodes[4]))
    g.add_edge(WeightedEdge(nodes[3], nodes[4]))
    g.add_edge(WeightedEdge(nodes[3], nodes[5]))
    g.add_edge(WeightedEdge(nodes[0], nodes[2]))
    g.add_edge(WeightedEdge(nodes[1], nodes[0]))
    g.add_edge(WeightedEdge(nodes[3], nodes[1]))
    g.add_edge(WeightedEdge(nodes[4], nodes[0]))
    for n in nodes:
        print([e.get_name() for e in g.edges[n]])
    sp = shortest_path(g, nodes[0], nodes[5], to_print=True)
    try:
        print('Shortest path is', print_path(sp))
    except TypeError:
        print('\nNo path was found.')

if __name__ == '__main__':
    test_shortest_path()




