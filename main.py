from graph import AlgorithmHelper
import networkx as nx
import matplotlib.pyplot as plt
import time

g = AlgorithmHelper('matrix.txt')
#print(f"bfs result: {g.bfs(3, 5)}")
print(f"dfs result: {g.dfs(0, 1)}")

