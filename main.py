from graph import Graph

graph = Graph(5)  # INITIALISE THE GRAPH SIZE HERE

graph.add_path(1, 2)
graph.add_path(1, 4)
graph.add_path(2, 4)
graph.add_path(3, 4)
graph.add_path(3, 5)

graph.analysis()

graph.search(3)  # EDIT THE STARTING NODE HERE!

print(graph)
