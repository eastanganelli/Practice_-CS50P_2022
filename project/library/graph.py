import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    
    graph: dict[str, dict[str, int]]
    
    def __init__(self):
        self.graph = ditc()
        
    def addEdge(self, fromNode, toNode, cost) -> None:
        if fromNode not in self.graph:
            self.graph[fromNode] = []
            
        if toNode not in self.graph:
            self.graph[toNode] = []
            
        self.graph[fromNode].append(( inNode, int(cost) ))
        
    def printGraph(self) -> None:
        for source, destination in self.graph.items():
            print(f"{source} --> {destination}")
    
    def windowGraph(self) -> None:
        G = nx.Graph()
        G.add_node('A', color='red')
        G.add_node('B', color='green')
        G.add_node('C', color='blue')

        G.add_edges_from(
            [('A', 'B'), ('A', 'C'), ('B', 'C')])

        colors = [node[1]['color'] for node in G.nodes(data=True)]

        nx.draw(G, node_color=colors, with_labels=True, font_color='white')

        plt.show()