class Node:

    def __init__(self, label: 'Node ID' = None):
        self.label = label
        self.position = None
        self.connections = []

    def __str__(self):
        return

    def connect_to(self, label: "Node"):
        self.connections.append(label)
