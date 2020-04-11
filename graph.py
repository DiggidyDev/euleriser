from interface import Interface
from node import Node

import numpy as np


class Graph:

    def __init__(self, nodes: int = None):
        self.current_node = None
        self.image = None
        self.interface = None
        self.nodes = []
        self.odd_nodes = []
        self.path_count = 0
        self.previous_node = None
        self.travelled = {k + 1: [] for k in range(nodes)}

    @property
    def node_count(self):
        return len(self.travelled.keys())

    @property
    def paths(self):
        return {k: c.connections for k, c in enumerate(self.nodes, 1)}

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

        w = self.interface.dimensions[0]
        h = self.interface.dimensions[1]

        for count in range(1, self.node_count + 1):
            x = ((count % 2) + 1) * w / (self.node_count / 1.5)
            y = ((count % 2) + (count % 3)) * h / (self.node_count / 1.5)
            self.image = self.interface.draw_node(self.get_node(count), (x, y), 20)

        self.image.show()
        return "Graph successfully loaded!"

    def _dfs(self, solution):
        """
        Performs a depth-first search on the graph from a given starting position.
        Returns a list containing the solution.

        :param solution:
        :return:
        """

        return

    def add_path(self, start_node, end_node):
        """
        Creates a path between two defined nodes, start and end.

        :param start_node:
        :param end_node:
        :return:
        """

        if not (0 < start_node <= self.node_count) or not (0 < start_node <= self.node_count):
            raise IndexError(f"Please provide valid values between the lower and upper bounds, inclusively: (1-{self.node_count})")

        try:
            start_node = self.get_node(start_node)
            end_node = self.get_node(end_node)

            start_node.connect_to(end_node)
            end_node.connect_to(start_node)

            self.image = self.interface.draw_path(start_node.centre, end_node.centre)

            self.path_count += 1
        except Exception as e:
            print(f"{type(e).__name__}: {e}")

    def analysis(self):
        """
        Analyses the graph for the number of nodes, number of odd, even nodes,
        whether it's Eulerian, semi-Eulerian or invalid.

        :return:
        """

        self.odd_nodes = [str(node) for node in self.paths.keys() if len([c for c in self.paths[node]]) % 2 == 1]

        if len(self.odd_nodes) == 2:
            graph_type = "Semi-Eulerian path"
        elif len(self.odd_nodes) == 0:
            graph_type = "Eulerian cycle"
        else:
            graph_type = "Invalid graph type"

        print(f"Nodes         : {self.node_count}      ({'Even' if self.node_count % 2 == 0 else 'Odd'})")
        print(f"Odd nodes     : {', '.join(self.odd_nodes)}   (Possible starting nodes)")
        print(f"Graph type    : {graph_type}")

    def del_path(self, start, end):
        """
        Deletes a path between two defined nodes, start and end.

        :param start:
        :param end:
        :return:
        """
        if not (0 < start <= self.node_count) or not (0 < start <= self.node_count):
            raise IndexError(f"Please provide valid values between the lower and upper bounds, inclusively: (1-{self.nodes})")

        try:
            del self.paths[start][self.paths[start].index(end)]
        except KeyError:
            raise KeyError(f"Nodes {start} and {end} are not linked.")

        try:
            del self.paths[end][self.paths[end].index(start)]
        except KeyError:
            raise KeyError(f"Nodes {start} and {end} are not linked.")

    def get_node(self, identifier):
        for node in self.nodes:
            if identifier == node.identifier:
                return node

    def init_gui(self):
        gui = Interface(self.node_count)
        self.interface = gui

        for i in range(len(self.travelled.keys())):
            node = Node(i + 1, self.interface)
            self.nodes.append(node)

        self.interface.graph = self
        w = self.interface.dimensions[0]
        h = self.interface.dimensions[1]

        for count in range(1, self.node_count + 1):
            x = ((count % 2) + 1) * w / (self.node_count / 1.5)
            y = ((count % 2) + (count % 3)) * h / (self.node_count / 1.5)
            self.get_node(count).set_position(x, y, 20)

        return self.interface

    def node_links(self, node=None):
        if node is None:
            node = self.current_node
        print(f"'Node {node}' has {len(self.paths[node])} linked nodes: {', '.join([str(v) for v in self.paths[node]])}")

        return self.paths[node]

    def search(self, start):
        if not isinstance(start, Node):
            self.current_node = self.get_node(start)
        else:
            self.current_node = start
        solve_order = ' -> '.join([str(node) for node in self._dfs([])])

        for node in self.travelled.values():
            node.sort()

        print(self.travelled)
        print(self.paths)
        print(solve_order)
        if self.travelled == self.paths:
            print(f"Solved!\n{solve_order}")
        else:
            print("Not possible from this position!")
