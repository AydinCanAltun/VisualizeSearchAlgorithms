from queue import Queue, PriorityQueue
import networkx as nx
from visualizer import Visualizer

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
        self.visualizer = Visualizer(self.graph)
    
    # Print the graph representation
    def print_adj_list(self):
      for key in self.m_adj_list.keys():
        print("node", key, ": ", self.m_adj_list[key])

    def bfs(self, start_node, target_node):
        # Set of visited nodes to prevent loops
        visited = set()
        queue = Queue()
        visited_edges = list()
        title = f"BFS ({start_node},{target_node})"
        self.visualizer.show_graph(title=title, current_node=0, next_node=0, visited_edges=visited_edges, pause=0)
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
                    self.visualizer.show_graph(title=title, current_node=current_node, next_node=next_node, visited_edges=visited_edges, pause=3)
                    queue.put(next_node)
                    parent[next_node] = current_node
                    visited.add(next_node)
                    visited_edges.append((current_node, next_node))
                    
                
        # Path reconstruction
        path = []
        if path_found:
            path.append(target_node)
            while parent[target_node] is not None:
                path.append(parent[target_node]) 
                target_node = parent[target_node]
            path.reverse()
        input()
        return path 

    def dfs(self, start, target, path = [], visited = set(), visited_edges=list(), is_first_call=True, title=None):
      if is_first_call:
          title = f"DFS ({start},{target})"
          self.visualizer.show_graph(title=title, current_node=start, next_node=target, visited_edges=visited_edges, pause=0)
      path.append(start)
      visited.add(start)
      
      if start == target:
          return path
      for (neighbour, weight) in self.m_adj_list[start]:
          if neighbour not in visited:
              visited_edges.append((start, neighbour))
              self.visualizer.show_graph(current_node=start, next_node=neighbour, visited_edges=visited_edges)
              result = self.dfs(neighbour, target, path, visited, visited_edges=visited_edges, is_first_call=False, title=title)
              if result is not None:
                  return result
      path.pop()
      return None    

    def ucs(self, start, goal):
        explored = set()
        pq = PriorityQueue()
        pq.put((0, start, [start]))

        while not pq.empty():
            cost, node, path = pq.get()
            if node == goal:
                return path
            if node not in explored:
                explored.add(node)
                for neighbor, weight in self.m_adj_list[node]:
                    if neighbor not in explored:
                        pq.put((cost + weight, neighbor, path + [neighbor]))

        return None
    

    def dls(self, deep_limit, start, target, path = [], visited = set()):
        path.append(start)
        visited.add(start)
        if start == target:
            return path
        elif deep_limit == 0:
            path.pop()
            return None
        else:
            for (neighbour, weight) in self.m_adj_list[start]:
                if neighbour not in visited:
                    result = self.dls(deep_limit - 1, neighbour, target, path, visited)
                    if result is not None:
                        return result
            path.pop()
        return None
    
    def bidirectional_search(self, start, goal):
        # create two sets to track visited nodes
        visited_forward = set()
        visited_backward = set()
        # create two queues for BFS
        queue_forward = [start]
        queue_backward = [goal]

        forwardPath = self.bfs(start, goal)
        if goal in forwardPath:
            return forwardPath
        
        backwardPath = self.bfs(goal, start)
        if start in backwardPath:
            return backwardPath
       
        # while queue_forward and queue_backward:
        #     # perform BFS from the forward direction
        #     current_forward = queue_forward.pop(0)
        #     visited_forward.add(current_forward)
        #     for (neighbor, weight) in self.m_adj_list[current_forward]:
        #         if neighbor not in visited_forward:
        #             queue_forward.append(neighbor)
        #     # check if the current node has been visited in the backward search
        #     if current_forward in visited_backward:
        #         return True
        #     # perform BFS from the backward direction
        #     current_backward = queue_backward.pop(0)
        #     visited_backward.add(current_backward)
        #     for neighbor in graph[current_backward]:
        #         if neighbor not in visited_backward:
        #             queue_backward.append(neighbor)
        #     # check if the current node has been visited in the forward search
        #     if current_backward in visited_forward:
        #         return True
        return None
    