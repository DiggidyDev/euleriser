import math

class Node:

    def __init__(self, identifier: int, interface: "Interface object"):
        self.connections = []
        self.identifier = identifier
        self.interface = interface
        self.centre = (0, 0)
        self.radius = None
        self.visits = 0

    def __int__(self):
        return int(self.identifier)

    @property
    def border_positions(self):
        return (self.centre[0] - self.radius, self.centre[1] - self.radius), (self.centre[0] + self.radius, self.centre[1] + self.radius)

    @property
    def x(self):
        return self.centre[0]

    @property
    def y(self):
        return self.centre[1]

    def connect_to(self, node: "Node object"):
        if node.identifier not in self.connections and self.identifier not in node.connections:
            self.connections.append(node.identifier)
            node.connections.append(self.identifier)
        else:
            raise PermissionError(f"Path connection already exists between nodes {self.identifier} and {node.identifier}")

    def disconnect_from(self, node: "Node object"):
        if node.identifier in self.connections and self.identifier in node.connections:
            self.connections.pop(self.connections.index(node.identifier))
            node.connections.pop(node.connections.index(self.identifier))
        else:
            raise PermissionError(f"No initial path connection found between nodes {self.identifier} and {node.identifier}")

    def distance_from(self, identifier: "Node identifier"=None):
        """
        Gets the distance (in pixels) between the node this method is being called from
        and a target node.
        :param node:
        :return:
        """
        try:
            node = self.interface.graph.get_node(identifier)
            return math.sqrt((self.x-node.x)**2 + (self.y-node.y)**2)
        except:
            return min([v for k, v in self.get_all_distances().items() if k != self.identifier])

    def get_all_distances(self):
        return {k.identifier: self.distance_from(k.identifier) for k in self.interface.graph.nodes}

    def set_position(self, x, y):
        """
        Sets the centre position of the node.

        :param x:
        :param y:
        :return:
        """
        self.centre = (x, y)

    def set_radius(self, r):
        """
        Sets radius of the node.

        :param r:
        :return:
        """
        self.radius = r
