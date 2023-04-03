from queue import Queue
import heapq
import networkx as nx

class AlgorithmHelper:

    def __init__(self, filePath, directed=True):
        with open('matris.txt', 'r') as f:
          lines = f.readlines()
        self.graph = nx.DiGraph()
        self.m_num_of_nodes = len(lines)
        self.m_nodes = range(self.m_num_of_nodes)
        self.m_directed = directed
        self.m_adj_list = {node: set() for node in self.m_nodes}
        for i in self.m_nodes:
          row = list(lines[i].strip())
          for j in range(len(row)):
            if i != j and int(row[j]) > 0:
              self.graph.add_edge(i, j, pos = (i+10, j+10), weigth = int(row[j]))
              self.m_adj_list[i].add((j, int(row[j])))
    
    # Print the graph representation
    def print_adj_list(self):
      for key in self.m_adj_list.keys():
        print("node", key, ": ", self.m_adj_list[key])

    def bfs(self, start_node, target_node):
      # Set of visited nodes to prevent loops
      visited = set()
      queue = Queue()

      # Add the start_node to the queue and visited list
      queue.put(start_node)
      visited.add(start_node)
    
      # start_node has not parents
      parent = dict()
      parent[start_node] = None

      # Perform step 3
      path_found = False
      while not queue.empty():
          current_node = queue.get()
          if current_node == target_node:
              path_found = True
              break
  
          for (next_node, weight) in self.m_adj_list[current_node]:
              if next_node not in visited:
                  queue.put(next_node)
                  parent[next_node] = current_node
                  visited.add(next_node)
                
      # Path reconstruction
      path = []
      if path_found:
          path.append(target_node)
          while parent[target_node] is not None:
              path.append(parent[target_node]) 
              target_node = parent[target_node]
          path.reverse()
      return path 

    def dfs(self, start, target, path = [], visited = set()):
      path.append(start)
      visited.add(start)
      if start == target:
          return path
      for (neighbour, weight) in self.m_adj_list[start]:
          if neighbour not in visited:
              result = self.dfs(neighbour, target, path, visited)
              if result is not None:
                  return result
      path.pop()
      return None    

    def ucs(graph, start, goal):
      visited = set()
      queue = [(0, start, [])]
      while queue:
          (cost, node, path) = heapq.heappop(queue)
          if node not in visited:
              visited.add(node)
              path = path + [node]
              if node == goal:
                  return (cost, path)
              for neighbor, neighbor_cost in graph[node].items():
                  if neighbor not in visited:
                      heapq.heappush(queue, (cost + neighbor_cost, neighbor, path))
      return None