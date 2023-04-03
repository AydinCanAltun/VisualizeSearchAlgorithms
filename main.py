from graph import AlgorithmHelper
import networkx as nx
import matplotlib.pyplot as plt
g = AlgorithmHelper('matrix.txt')

print(f"bfs result: {g.bfs(0, 1)}")
print(f"dfs result: {g.dfs(0, 1)}")

pos = nx.spring_layout(g.graph)
nx.draw_networkx(g.graph, pos)
labels = nx.get_edge_attributes(g.graph, 'weigth')
nx.draw_networkx_edge_labels(g.graph, pos, edge_labels=labels)
plt.show()

