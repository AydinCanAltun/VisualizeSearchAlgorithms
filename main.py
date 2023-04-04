from graph import AlgorithmHelper
import networkx as nx
import matplotlib.pyplot as plt
import time

g = AlgorithmHelper('matrix.txt')
print(f"bfs result: {g.bfs(3, 5)}")
input()
print(f"dfs result: {g.dfs(0, 1)}")
# print(f"ucs result: {g.ucs(0, 1)}")
# print(f"dls result: {g.dls(3, 0, 1, [], set())}")
# print(f"bidirectional reuslt: {g.bidirectional_search(0, 1)}")

# i=0
# while i in range(5):
#     plt.clf()
#     pos=nx.spring_layout(g.graph,seed=5)
#     nx.draw_networkx_nodes(g.graph, pos)
#     nx.draw_networkx_labels(g.graph, pos)


#     curved_edges = [edge for edge in g.graph.edges() if reversed(edge) in g.graph.edges()]
#     curved_edge_colors = ['red' if e[1] == i else 'black' for e in curved_edges]

#     straight_edges = list(set(g.graph.edges()) - set(curved_edges))
#     straight_edge_colors = ['red' if e[1] == i else 'black' for e in straight_edges]

#     nx.draw_networkx_edges(g.graph, pos, edge_color=straight_edge_colors, edgelist=straight_edges, arrowsize=50)
#     arc_rad = 0.25
#     nx.draw_networkx_edges(g.graph, pos, edgelist=curved_edges, edge_color=curved_edge_colors, connectionstyle=f'arc3, rad = {arc_rad}', arrowsize=50)
#     edge_weights = nx.get_edge_attributes(g.graph, 'weigth')
#     curved_edge_labels = {edge: edge_weights[edge] for edge in curved_edges}
#     straight_edge_labels = {edge: edge_weights[edge] for edge in straight_edges}
#     g.my_draw_networkx_edge_labels(g.graph, pos, edge_labels=curved_edge_labels,rotate=False,rad = arc_rad, plt=plt)
#     plt.show(block=False)
#     i = i + 1

