from graph import Graph
from interface import Interface

graph = Graph(4)  # INITIALISE THE GRAPH SIZE HERE
gui = graph.init_gui()

graph.add_path(1, 2)
graph.add_path(1, 4)
graph.add_path(2, 4)
graph.add_path(3, 4)

graph.analysis()

# graph.search(graph.get_node(4))  # EDIT THE STARTING NODE HERE!
print(graph)
