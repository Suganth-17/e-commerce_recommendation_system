import networkx as nx 
import pandas as pd

class CreateGraph:
    def __init__(self) -> None:
        self.item_graph = nx.Graph()
    def create(self):
        return self.item_graph
    

class CreateNodes:
    def __init__(self, item_graph: nx.Graph, data_frame: pd.DataFrame) -> None:
        self.item_graph = item_graph
        self.data_frame = data_frame

    def get_nodes(self) -> list:
        nodes_list = self.data_frame['sub_category'].unique()
        return nodes_list
    
    def score_calc(self, node) -> float:
        score = len(self.data_frame[self.data_frame['sub_category']== node]) / self.data_frame.shape[0]
        return score
    
    def get_initial_scores(self,nodes_list: list) -> dict:
        initial_score_dict = {}
        for node in nodes_list:
            initial_score_dict[node] = self.score_calc(node= node)
        return initial_score_dict

    def create_nodes(self) -> nx.Graph():
        nodes_list = self.get_nodes()
        initial_scores = self.get_initial_scores(nodes_list= nodes_list)
        for node in nodes_list:
            self.item_graph.add_node(node, score= initial_scores[node])
        return self.item_graph
    

class CreateEdges(CreateNodes):
    def __init__(self, item_graph: nx.Graph(), data_frame: pd.DataFrame) -> None:
        self.item_graph = item_graph
        self.data_frame = data_frame

    def edge_weights(self, interacted_series : pd.Series , edge ) -> float:
        node1_occurence = node2_occurence = 0
        for interacted_list in interacted_series:
            if edge[0] in interacted_list:
                node1_occurence+= 1
            if edge[0] in interacted_list and edge[1] in interacted_list:
                node2_occurence+=1 
        if node1_occurence!= 0:
                return (node2_occurence/node1_occurence)
        else:
            return 0


    def create_edges(self, data_frame: pd.DataFrame)-> nx.Graph():
        nodes_list = self.get_nodes()
        edges = []
        for x_node in nodes_list:
            for y_node in nodes_list:
                if x_node != y_node:
                    edges.append((x_node, y_node))
        
        interacted_series = data_frame.groupby('customer_id')['sub_category'].unique()
        edge_weights_dict = {}
        for edge in edges:
            edge_weights_dict[edge] = self.edge_weights(interacted_series, edge)

        for edge, weight in edge_weights_dict.items():
            self.item_graph.add_edge(*edge, weight=weight)
        return self.item_graph
    
    def get_edge_weights_dict(self, data_frame: pd.DataFrame)-> dict:
        nodes_list = self.get_nodes()
        edges = []
        for x_node in nodes_list:
            for y_node in nodes_list:
                if x_node != y_node:
                    edges.append((x_node, y_node))
        
        interacted_series = self.data_frame.groupby('customer_id')['sub_category'].unique()
        edge_weights_dict = {}
        for edge in edges:
            edge_weights_dict[edge] = self.edge_weights(interacted_series, edge)

        return edge_weights_dict
    
    def get_edges_list(self, data_frame: pd.DataFrame)-> list:
        nodes_list = self.get_nodes()
        edges = []
        for x_node in nodes_list:
            for y_node in nodes_list:
                if x_node != y_node:
                    edges.append((x_node, y_node))
        
        return edges