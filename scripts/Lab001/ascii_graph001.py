from ascii_graph import Pyasciigraph
from ascii_graph import colors

data = [('A', 5, colors.BBlu), ('B', 3, colors.BRed), ('C', 9, colors.Gre), ('D', 6, colors.BYel)]

graph = Pyasciigraph()

for line in graph.graph('Sample Graph', data):
    print(line)