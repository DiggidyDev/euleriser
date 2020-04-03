class Graph:

    def __init__(self, nodes: int = None):
        self.current_node = 1
        self.nodes = nodes
        self.odd_nodes = []
        self.paths = {k: [] for k in range(1, nodes + 1)}
        self.previous_node = None

    def add_path(self, start, end):
        """
        Creates a path between two defined nodes, start and end.

        :param start:
        :param end:
        :return:
        """
        if not (0 < start <= self.nodes) or not (0 < start <= self.nodes):
            raise IndexError(f"Please provide valid values between the lower and upper bounds, inclusively: (1-{self.nodes})")

        try:
            self.paths[start].append(end)
        except KeyError:
            self.paths[start] = [end]

        try:
            self.paths[end].append(start)
        except KeyError:
            self.paths[end] = [start]

    def analysis(self):
        """
        Analyses the graph for the number of nodes, number of odd, even nodes,
        whether it's an Eulerian or semi-Eulerian path or invalid etc.

        :return:
        """

        self.odd_nodes = [str(node) for node in self.paths.keys() if len(self.paths[node]) % 2 == 1]

        if len(self.odd_nodes) == 2:
            graph_type = "Semi-Eulerian path"
        elif len(self.odd_nodes) == 0:
            graph_type = "Eulerian cycle"
        else:
            graph_type = "Invalid graph type"

        print(f"Node quantity : {self.nodes} ({'Even' if self.nodes % 2 == 0 else 'Odd'})")
        print(f"Odd nodes     : {', '.join(self.odd_nodes)}")
        print(f"Graph type    : {graph_type}")

    def node_links(self, node=None):
        if node is None:
            node = self.current_node
        print(f"'Vertex {node}' has {len(self.paths[node])} linked nodes: {', '.join([str(v) for v in self.paths[node]])}")

        return self.paths[node]

    def del_path(self, start, end):
        """
        Deletes a path between two defined nodes, start and end.

        :param start:
        :param end:
        :return:
        """
        if not (0 < start <= self.nodes) or not (0 < start <= self.nodes):
            raise IndexError(f"Please provide valid values between the lower and upper bounds, inclusively: (1-{self.nodes})")

        try:
            del self.paths[start][self.paths[start].index(end)]
        except KeyError:
            raise KeyError(f"Vertices {start} and {end} are not linked.")

        try:
            del self.paths[end][self.paths[end].index(start)]
        except KeyError:
            raise KeyError(f"Vertices {start} and {end} are not linked.")

    def start_journey(self, start):
        pass


graph = Graph(4)

graph.add_path(1, 2)
graph.add_path(1, 4)
graph.add_path(2, 4)
graph.add_path(3, 4)

graph.analysis()
