from graph import Graph

graph = Graph(4)  # INITIALISE THE GRAPH SIZE HERE
gui = graph.init_gui()

graph.add_path(1, 2)
graph.add_path(1, 4)
graph.add_path(2, 4)
graph.add_path(3, 4)

graph.analysis()

print(graph.search(graph.get_node(3)))  # EDIT THE STARTING NODE HERE!
print(type(graph.node_links(2)))
