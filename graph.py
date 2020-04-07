from interface import Interface
from node import Node


class Graph:

    def __init__(self, nodes: int = None):
        self.current_node = 1
        self.nodes = []
        self.odd_nodes = []
        self.paths = {k + 1: [] for k in range(nodes)}
        self.path_count = 0
        self.previous_node = None
        self.travelled = {k + 1: [] for k in range(nodes)}

        for i in range(nodes):
            node = Node(str(i + 1))
            self.nodes.append(node)

    @property
    def node_count(self):
        return len(self.nodes)

    def __len__(self):
        """
        Returns the number of paths in a graph.

        :return:
        """
        return self.path_count

    def __str__(self):
        """
        Shows graph in image when printed.
        Used to visualise the nodes and paths.

        :return:
        """
        gui = Interface(self.node_count)

        for count in range(self.node_count + 1):
            image = gui.draw_node(count)
        else:
            image = gui.draw_node(1)
        image.show()
        return "Loading..."

    def _dfs(self, start, solution: list):
        """
        Performs a depth-first search on the graph from a given starting position.
        Returns a list containing the solution.

        :param start:
        :param solution:
        :return:
        """

        for neighbour in self.paths[start]:
            if neighbour not in self.travelled[start]:
                solution.append(str(self.current_node))

                self.previous_node = self.current_node
                self.current_node = neighbour

                self.travelled[self.current_node].append(self.previous_node)
                self.travelled[self.previous_node].append(self.current_node)

                self._dfs(self.current_node, solution)
        for node in self.travelled.values():
            node.sort()
        return solution

    def add_path(self, start, end):
        """
        Creates a path between two defined nodes, start and end.

        :param start:
        :param end:
        :return:
        """

        if not (0 < start <= self.node_count) or not (0 < start <= self.node_count):
            raise IndexError(f"Please provide valid values between the lower and upper bounds, inclusively: (1-{self.nodes})")



        try:
            self.paths[start].append(end)
        except KeyError:
            self.paths[start] = [end]
        finally:
            self.path_count += 1

        try:
            self.paths[end].append(start)
        except KeyError:
            self.paths[end] = [start]

    def analysis(self):
        """
        Analyses the graph for the number of nodes, number of odd, even nodes,
        whether it's Eulerian, semi-Eulerian or invalid.

        :return:
        """

        self.odd_nodes = [str(node) for node in self.paths.keys() if len(self.paths[node]) % 2 == 1]

        if len(self.odd_nodes) == 2:
            graph_type = "Semi-Eulerian path"
        elif len(self.odd_nodes) == 0:
            graph_type = "Eulerian cycle"
        else:
            graph_type = "Invalid graph type"

        print(f"Nodes         : {self.nodes}      ({'Even' if self.node_count % 2 == 0 else 'Odd'})")
        print(f"Odd nodes     : {', '.join(self.odd_nodes)}   (Possible starting nodes)")
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
            raise KeyError(f"Nodes {start} and {end} are not linked.")

        try:
            del self.paths[end][self.paths[end].index(start)]
        except KeyError:
            raise KeyError(f"Nodes {start} and {end} are not linked.")

    def get_node(self, label: str):
        for node in self.nodes:
            if label == node.label:
                return node

    def node_links(self, node=None):
        if node is None:
            node = self.current_node
        print(f"'Node {node}' has {len(self.paths[node])} linked nodes: {', '.join([str(v) for v in self.paths[node]])}")

        return self.paths[node]

    def search(self, start):
        self.current_node = start
        solution = []
        solve_order = ' -> '.join(self._dfs(start, solution))
        if self.travelled == self.paths:
            print(f"Solved!\n{solve_order}")
        else:
            print("Not possible from this position!")
