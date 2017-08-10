class Node(object):
    def __init__(self, name):
        """Assumes name is a string"""
        self.name = name

    def get_name(self):
        return self.name

    def __str__(self):
        return self.name  # for pretty-printing


class Edge(object):
    def __init__(self, src, dest):
        """Assume src and dest are nodes"""
        self.src = src
        self.dest = dest

    def get_source(self):
        return self.src

    def get_destination(self):
        return self.dest

    def __str__(self):
        return self.src.get_name() + '->' + self.dest.get_name()


class WeightedEdge(Edge):
    def __init__(self, src, dest, weight=1.0):
        """Assumes src and dest are nodes, weight a number"""
        self.src = src
        self.dest = dest
        self.weight = weight

    def get_weight(self):
        return self.weight

    def __str__(self):
        return self.src.get_name() + '->(' + str(self.weight) + ')' \
               + self.dest.get_name()

class Digraph(object):
    """
    nodes is a list of the nodes in the graph
    edges is a dict mapping each node to a list of its children
    """
    def __init__(self):
        self.nodes = []
        self.edges = {}

    def add_node(self, node):
        if node in self.nodes:
            raise ValueError('Duplicate node.')
        else:
            self.nodes.append(node)
            self.edges[node] = [] # modify dictionary

    def add_edge(self, edge):
        src = edge.get_source()
        dest = edge.get_destination()
        if not (src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph.')
        self.edges[src].append((dest, edge.get_weight()))

    def children_of(self, node):
        return self.edges[node]

    def has_node(self, node):
        return node in self.nodes

    def __str__(self):
        result = ''
        for src in self.nodes:
            for dest in self.edges[src]:
                result = result + src.get_name() + '->' + \
                         dest.get_name() + '\m'

        return result[:-1] # omit final newline


class Graph(Digraph):
    def add_edge(self, edge):
        Digraph.add_edge(self, edge)
        rev = Edge(edge.get_destination(), edge.getSource())
        Digraph.add(self, rev)