NODE, EDGE, ATTR = range(3)


class Node:
    def __init__(self, name='', attrs=''):
        self.name = name
        self.attrs = attrs

    def __eq__(self, other):
        return self.name == other.name and self.attrs == other.attrs


class Edge:
    def __init__(self, src='', dst='', attrs=''):
        self.src = src
        self.dst = dst
        self.attrs = attrs

    def __eq__(self, other):
        return (self.src == other.src and
                self.dst == other.dst and
                self.attrs == other.attrs)


class Graph:
    def __init__(self, data=None):
        self.nodes = []
        self.edges = []
        self.attrs = {}

        if all([data != None, isinstance(data, list) == False]):
            raise TypeError('Graph data malformed')
        if data == [()]:
            raise TypeError("Graph item incomplete")

        if data is not None:  
            for d in data:
                if len(d) < 2:
                    raise TypeError('Graph item incomplete')
                if d[0] > 2:
                    raise ValueError('Unknown item')
                if d[0] == NODE:
                    if len(d) > 3:
                        raise ValueError('Node is malformed')
                    self.nodes.append(Node(*d[1:]))
                elif d[0] == EDGE:
                    if len(d) < 4:
                        raise ValueError('Edge is malformed')
                    self.edges.append(Edge(*d[1:]))
                elif d[0] == ATTR:
                    if not(any([isinstance(d[1], str), isinstance(d[1], str)])):
                        raise ValueError('Attribute is malformed')
                    self.attrs.update({d[1]: d[2]})                    