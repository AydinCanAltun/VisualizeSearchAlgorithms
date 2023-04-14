from queue import Queue, PriorityQueue
import networkx as nx
from visualizer import Visualizer

class AlgorithmHelper:

    def __init__(self, filePath, directed=True):
        with open(filePath, 'r') as f:
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
        self.visualizer.visualize_graph(title=title, draw_curved_edges=False, wait_for_action=True)
        # Add the start_node to the queue and visited list
        queue.put(start_node)
        visited.add(start_node)
        self.visualizer.color_nodes(title=title, current_node=start_node, next_node=start_node, queue=queue, draw_curved_edges=False, pause=3)
    
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
                    self.visualizer.color_nodes(title=title, current_node=current_node, next_node=next_node, draw_curved_edges=False, queue=queue, pause=3)
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
        return path 

    def dfs(self, start, target, path = [], visited = set(), visited_edges=list(), is_first_call=True, title=None):
        if is_first_call:
            if title is None:
                title = f"DFS ({start},{target})"
            self.visualizer.visualize_graph(title=title, draw_curved_edges=False, wait_for_action=True)
        path.append(start)
        visited.add(start)
      
        if start == target:
            return path
        for (neighbour, weight) in self.m_adj_list[start]:
            if neighbour not in visited:
                visited_edges.append((start, neighbour))
                self.visualizer.show_graph(current_node=start, next_node=neighbour, draw_curved_edges=False, visited_edges=visited_edges)
                result = self.dfs(neighbour, target, path, visited, visited_edges=visited_edges, is_first_call=False, title=title)
                if result is not None:
                    return result
        path.pop()
        return None    

    def ucs(self, start, goal):
        visited_edges = list()
        explored = set()
        title = f"UCS ({start},{goal})"
        self.visualizer.visualize_graph(title=title, wait_for_action=True)
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
                        self.visualizer.show_graph(title=title,current_node=node, next_node=neighbor, visited_edges=visited_edges, pause=3)
                        visited_edges.append((node, neighbor))
                        pq.put((cost + weight, neighbor, path + [neighbor]))
                        print(pq.queue)
        return None
    
    def dls(self, deep_limit, start, target, path = [], visited = set(), is_first_call=True, visited_edges=list(),title=None, show_graph=True):
        if is_first_call:
            if title is None:
                title = f"DLS ({start},{target}) Deep Limit = {deep_limit}"
            if show_graph:
                self.visualizer.show_graph(title=title,current_node=start,next_node=start,visited_edges=visited_edges,pause=0)
        path.append(start)
        visited.add(start)
        if start == target:
            return path
        elif deep_limit == 0:
            return None
        else:
            for (neighbour, weight) in self.m_adj_list[start]:
                if neighbour not in visited:
                    visited_edges.append((start, neighbour))
                    if show_graph:
                        self.visualizer.show_graph(title=title,current_node=start, next_node=neighbour, visited_edges=visited_edges, pause=3)
                    result = self.dls(deep_limit - 1, neighbour, target, path, visited, is_first_call=False, visited_edges=visited_edges, show_graph=show_graph, title=title)
                    if result is not None:
                        return result
            path.pop()
            return None
    
    def iddfs (self, start, goal, depth):
        title = f"IDDFS ({start}, {goal}) Maximum Depth Limit = {depth}"
        self.visualizer.visualize_graph(title=title, wait_for_action=True)
        for limit in range(0, depth + 1):
            title= f"IDDFS ({start}, {goal}), Current Depth = {limit}, Maximum Depth Limit = {depth}"
            path = self.dls(limit, start, goal, visited=set(), path=[], is_first_call=False, show_graph=True, title=title)
            if path is not None:
                return path
        return None

    def bidirectional_search(self, start, goal):
        visited_edges = list()
        self.visualizer.show_graph(current_node=start, next_node=start, visited_edges=visited_edges, pause=0)
        forward_queue = Queue()
        forward_queue.put(start)

        backward_queue = Queue()
        backward_queue.put(goal)
      
        forward_visited = {start: None}
        backward_visited = {goal: None}
    
        while not forward_queue.empty() and not backward_queue.empty():
            # ileri arama
            current = forward_queue.get()
            if current in backward_visited:
                return self.path(forward_visited, backward_visited, current)
              
            for (neighbor,weight) in self.m_adj_list[current]:
                if neighbor not in forward_visited:
                    self.visualizer.show_graph(current_node=current, next_node=neighbor, visited_edges=visited_edges, pause=3)
                    visited_edges.append((current, neighbor))
                    forward_visited[neighbor] = current
                    forward_queue.put(neighbor)
    
            # geri arama
            current = backward_queue.get()
            if current in forward_visited:
              path = self.path(forward_visited, backward_visited, current)
              return path
                
            for (neighbor,weight) in self.m_adj_list[current]:
                if neighbor not in backward_visited:
                    self.visualizer.show_graph(current_node=current, next_node=neighbor, visited_edges=visited_edges, pause=3)
                    visited_edges.append((current, neighbor))
                    backward_visited[neighbor] = current
                    backward_queue.put(neighbor)
                  
        return None

    def path(self, forward_visited, backward_visited, current):
        forward_path = []
        node = forward_visited[current]
        while node is not None:
            forward_path.append(node)
            node = forward_visited[node]
          
        backward_path = []
        node = current
        while node is not None:
            backward_path.append(node)
            node = backward_visited[node]
          
        return forward_path[::-1] + backward_path
    