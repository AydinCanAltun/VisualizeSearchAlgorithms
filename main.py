from graph import AlgorithmHelper
import networkx as nx
import matplotlib.pyplot as plt
import time

g = AlgorithmHelper('matris.txt')
#print(f"bfs result: {g.bfs(3, 5)}")
#print(f"dfs result: {g.dfs(0, 1)}")
#print(f"ucs result : {g.ucs(3, 5)}")
print(f"dls result: {g.dls(deep_limit=4, start=3,target=5)}")
