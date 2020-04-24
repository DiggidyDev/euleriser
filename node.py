class Node:

    def __init__(self, identifier: int, interface: "Interface object"):
        self.connections = []
        self.identifier = identifier
        self.interface = interface
        self.centre = None
        self.radius = None
        self.visits = 0

    def __int__(self):
        return int(self.identifier)

    @property
    def border_positions(self):
        return (self.centre[0] - self.radius, self.centre[1] - self.radius), (self.centre[0] + self.radius, self.centre[1] + self.radius)

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
