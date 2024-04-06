import pandas as pd
import networkx as nx

class Scores:
    def __init__(self, item_graph: nx.Graph, interacted_categories_list: list) -> None:
        self.item_graph = item_graph
        self.interacted_categories_list = list(interacted_categories_list)

    def update_initial_scores(self)-> nx.Graph:
        for node in self.item_graph.nodes:
            number_of_nodes = len(self.interacted_categories_list)
            if number_of_nodes!= 0:
                self.item_graph.nodes[node]['preference_score'] = self.interacted_categories_list.count(node) / len(self.interacted_categories_list)
            else:
                self.item_graph.nodes[node]['preference_score'] = 0
            self.item_graph.nodes[node]['overall_score'] = self.item_graph.nodes[node]['score'] + self.item_graph.nodes[node]['preference_score']
        
        return self.item_graph
    
    def update_pre_recommend_scores(self)-> nx.Graph:
        for node in self.item_graph.nodes:
            if node in self.interacted_categories_list:
                self.item_graph.nodes[node]['recommend_score'] = self.item_graph.nodes[node]['overall_score'] 
            else:
                self.item_graph.nodes[node]['recommend_score'] = 0

    def update_recommend_scores(self, edges: list, edge_weights: dict)-> nx.Graph:
        for target_node in self.item_graph.nodes:
            for edge in edges:
                if edge[0] == target_node :
                    update_score = edge_weights[edge] * self.item_graph.nodes[edge[0]]['preference_score']
                    if self.item_graph.nodes[edge[1]]['recommend_score'] < update_score:
                        self.item_graph.nodes[edge[1]]['recommend_score'] = update_score
        return self.item_graph

    def get_recommend_dict(self) -> dict:
        recommended_dict = {}
        for node in self.item_graph.nodes:
            recommended_dict[node] = self.item_graph.nodes[node]['recommend_score']
        return recommended_dict
    
    def get_recommended_nodes(self) -> list:
        recommended_dict = self.get_recommend_dict()
        recommended_nodes = sorted(recommended_dict, key=lambda x: recommended_dict[x], reverse=True)
        recommended_node_score = list(recommended_dict.values())
        recommended_node_score = sorted(recommended_node_score, reverse= True)
        sorted_recommended_dict = {}
        for key, value in zip(recommended_nodes, recommended_node_score):
            sorted_recommended_dict[key] = value
        return recommended_nodes, recommended_node_score, sorted_recommended_dict
