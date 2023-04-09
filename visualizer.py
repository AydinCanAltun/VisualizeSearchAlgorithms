import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

class Visualizer:
    def __init__(self, graph):
        self.graph = graph
    
    def show_graph(self, title=None, current_node=None, next_node=None, visited_edges = list(), pause=3):
        plt.clf()
        if title != None:
            plt.title(title)
        pos=nx.spring_layout(self.graph,seed=5)
        nx.draw_networkx_nodes(self.graph, pos)
        nx.draw_networkx_labels(self.graph, pos)

        curved_edges = [edge for edge in self.graph.edges() if reversed(edge) in self.graph.edges()]
        curved_edge_colors = []
        for (source, target) in curved_edges:
            if source == current_node and target == next_node:
                curved_edge_colors.append('red')
            elif visited_edges.count((source, target)):
                curved_edge_colors.append('orange')
            else:
                curved_edge_colors.append('black')
        straight_edges = list(set(self.graph.edges()) - set(curved_edges))
        straight_edge_colors = []
        for (source, target) in straight_edges:
            if source == current_node and target == next_node:
                straight_edge_colors.append('red')
            elif visited_edges.count((source, target)):
                straight_edge_colors.append('orange')
            else:
                straight_edge_colors.append('black')
        nx.draw_networkx_edges(self.graph, pos, edge_color=straight_edge_colors, edgelist=straight_edges, arrowsize=50)
        arc_rad = 0.25
        nx.draw_networkx_edges(self.graph, pos, edgelist=curved_edges, edge_color=curved_edge_colors, connectionstyle=f'arc3, rad = {arc_rad}', arrowsize=50)
        edge_weights = nx.get_edge_attributes(self.graph, 'weigth')
        curved_edge_labels = {edge: edge_weights[edge] for edge in curved_edges}
        straight_edge_labels = {edge: edge_weights[edge] for edge in straight_edges}
        self.my_draw_networkx_edge_labels(self.graph, pos, edge_labels=curved_edge_labels,rotate=False,rad = arc_rad, plt=plt)
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=straight_edge_labels,rotate=False)
        plt.show(block=False)
        if pause > 0:
            plt.pause(pause)
        else:
            input("Devam etmek ister misin ?")
    
    def show_basic_graph(self, title=None, pause=3):
        plt.clf()
        if title != None:
            plt.title(title)
        pos=nx.spring_layout(self.graph,seed=5)
        nx.draw_networkx_nodes(self.graph, pos)
        nx.draw_networkx_labels(self.graph, pos)

        curved_edges = [edge for edge in self.graph.edges() if reversed(edge) in self.graph.edges()]
        curved_edge_colors = []
        for (source, target) in curved_edges:
            curved_edge_colors.append('black')
                
        straight_edges = list(set(self.graph.edges()) - set(curved_edges))
        straight_edge_colors = []
        for (source, target) in straight_edges:
            straight_edge_colors.append('black')
                
        nx.draw_networkx_edges(self.graph, pos, edge_color=straight_edge_colors, edgelist=straight_edges, arrowsize=50)
        arc_rad = 0.25
        nx.draw_networkx_edges(self.graph, pos, edgelist=curved_edges, edge_color=curved_edge_colors, connectionstyle=f'arc3, rad = {arc_rad}', arrowsize=50)
        edge_weights = nx.get_edge_attributes(self.graph, 'weigth')
        curved_edge_labels = {edge: edge_weights[edge] for edge in curved_edges}
        straight_edge_labels = {edge: edge_weights[edge] for edge in straight_edges}
        self.my_draw_networkx_edge_labels(self.graph, pos, edge_labels=curved_edge_labels,rotate=False,rad = arc_rad, plt=plt)
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=straight_edge_labels,rotate=False)
        plt.show(block=False)
        if pause > 0:
            plt.pause(pause)
        else:
            input("Devam etmek ister misin ?")

    def my_draw_networkx_edge_labels(self,
        G,
        pos,
        edge_labels=None,
        label_pos=0.5,
        font_size=10,
        font_color="k",
        font_family="sans-serif",
        font_weight="normal",
        alpha=None,
        bbox=None,
        horizontalalignment="center",
        verticalalignment="center",
        ax=None,
        rotate=True,
        clip_on=True,
        rad=0,
        plt=None
    ):

        if ax is None:
            ax = plt.gca()
        if edge_labels is None:
            labels = {(u, v): d for u, v, d in G.edges(data=True)}
        else:
            labels = edge_labels
        text_items = {}
        for (n1, n2), label in labels.items():
            (x1, y1) = pos[n1]
            (x2, y2) = pos[n2]
            (x, y) = (
                x1 * label_pos + x2 * (1.0 - label_pos),
                y1 * label_pos + y2 * (1.0 - label_pos),
            )
            pos_1 = ax.transData.transform(np.array(pos[n1]))
            pos_2 = ax.transData.transform(np.array(pos[n2]))
            linear_mid = 0.5*pos_1 + 0.5*pos_2
            d_pos = pos_2 - pos_1
            rotation_matrix = np.array([(0,1), (-1,0)])
            ctrl_1 = linear_mid + rad*rotation_matrix@d_pos
            ctrl_mid_1 = 0.5*pos_1 + 0.5*ctrl_1
            ctrl_mid_2 = 0.5*pos_2 + 0.5*ctrl_1
            bezier_mid = 0.5*ctrl_mid_1 + 0.5*ctrl_mid_2
            (x, y) = ax.transData.inverted().transform(bezier_mid)

            if rotate:
                # in degrees
                angle = np.arctan2(y2 - y1, x2 - x1) / (2.0 * np.pi) * 360
                # make label orientation "right-side-up"
                if angle > 90:
                    angle -= 180
                if angle < -90:
                    angle += 180
                # transform data coordinate angle to screen coordinate angle
                xy = np.array((x, y))
                trans_angle = ax.transData.transform_angles(
                    np.array((angle,)), xy.reshape((1, 2))
                )[0]
            else:
                trans_angle = 0.0
            # use default box of white with white border
            if bbox is None:
                bbox = dict(boxstyle="round", ec=(1.0, 1.0, 1.0), fc=(1.0, 1.0, 1.0))
            if not isinstance(label, str):
                label = str(label)  # this makes "1" and 1 labeled the same

            t = ax.text(
                x,
                y,
                label,
                size=font_size,
                color=font_color,
                family=font_family,
                weight=font_weight,
                alpha=alpha,
                horizontalalignment=horizontalalignment,
                verticalalignment=verticalalignment,
                rotation=trans_angle,
                transform=ax.transData,
                bbox=bbox,
                zorder=1,
                clip_on=clip_on,
            )
            text_items[(n1, n2)] = t

        ax.tick_params(
            axis="both",
            which="both",
            bottom=False,
            left=False,
            labelbottom=False,
            labelleft=False,
        )

        return text_items