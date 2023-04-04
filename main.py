from graph import AlgorithmHelper
import networkx as nx
import matplotlib.pyplot as plt

g = AlgorithmHelper('matrix.txt')
print(f"bfs result: {g.bfs(0, 1)}")
print(f"dfs result: {g.dfs(0, 1)}")
print(f"ucs result: {g.ucs(0, 1)}")
print(f"dls result: {g.dls(3, 0, 1, [], set())}")
print(f"bidirectional reuslt: {g.bidirectional_search(0, 1)}")
pos=nx.spring_layout(g.graph,seed=5)
nx.draw_networkx_nodes(g.graph, pos)
nx.draw_networkx_labels(g.graph, pos)


curved_edges = [edge for edge in g.graph.edges() if reversed(edge) in g.graph.edges()]
curved_edge_colors = ['red' if e[1] == 3 else 'black' for e in curved_edges]

straight_edges = list(set(g.graph.edges()) - set(curved_edges))
straight_edge_colors = ['red' if e[1] == 3 else 'black' for e in straight_edges]

nx.draw_networkx_edges(g.graph, pos, edge_color=straight_edge_colors, edgelist=straight_edges)
arc_rad = 0.25
nx.draw_networkx_edges(g.graph, pos, edgelist=curved_edges, edge_color=curved_edge_colors, connectionstyle=f'arc3, rad = {arc_rad}')
edge_weights = nx.get_edge_attributes(g.graph, 'weigth')
curved_edge_labels = {edge: edge_weights[edge] for edge in curved_edges}
straight_edge_labels = {edge: edge_weights[edge] for edge in straight_edges}
g.my_draw_networkx_edge_labels(g.graph, pos, edge_labels=curved_edge_labels,rotate=False,rad = arc_rad, plt=plt)
nx.draw_networkx_edge_labels(g.graph, pos, edge_labels=straight_edge_labels,rotate=False)

plt.show(block=False)
input("a")