class Graph:

    def __init__(self, nodes: int = None):
        self.current_node = 1
        self.nodes = nodes
        self.odd_nodes = []
        self.paths = {k + 1: [] for k in range(nodes)}
        self.previous_node = None
        self.travelled = {k + 1: [] for k in range(nodes)}

    # MOVE TO GRAPHICAL INTERFACE?
    def _dfs(self, start):
        for neighbour in self.paths[start]:
            if neighbour not in self.travelled[start]:
                self.previous_node = self.current_node
                self.current_node = neighbour

                self.travelled[self.current_node].append(self.previous_node)
                self.travelled[self.previous_node].append(self.current_node)

                print(f"{self.previous_node} -> {self.current_node}")
                self._dfs(self.current_node)
        for node in self.travelled.values():
            node.sort()

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

        print(f"Node quantity : {self.nodes}      ({'Even' if self.nodes % 2 == 0 else 'Odd'})")
        print(f"Odd nodes     : {', '.join(self.odd_nodes)}   (Possible starting points)")
        print(f"Graph type    : {graph_type}")

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

    def node_links(self, node=None):
        if node is None:
            node = self.current_node
        print(f"'Vertex {node}' has {len(self.paths[node])} linked nodes: {', '.join([str(v) for v in self.paths[node]])}")

        return self.paths[node]

    def search(self, start):
        self.current_node = start
        self._dfs(start)
        if self.travelled == self.paths:
            print("Solved!")
        else:
            print("Not possible from this position!")


graph = Graph(4)

graph.add_path(1, 2)
graph.add_path(1, 4)
graph.add_path(2, 4)
graph.add_path(3, 4)

graph.analysis()
graph.search(3)  # EDIT THE STARTING NODE HERE!
