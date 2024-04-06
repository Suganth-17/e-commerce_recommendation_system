from src.Scores import Scores
import networkx as nx
from src.Create_Graph import CreateEdges
import pandas as pd


def recommneded_categories(item_graph: nx.Graph,data_frame: pd.DataFrame,  interacted_categories_list)-> list:
    score = Scores(item_graph, interacted_categories_list)
    item_graph = score.update_initial_scores()
    item_graph = score.update_pre_recommend_scores()
    graph = CreateEdges(item_graph, data_frame= data_frame)
    edges = graph.get_edges_list(data_frame)
    edge_weights = graph.get_edge_weights_dict(data_frame)
    item_graph = score.update_recommend_scores(edges=edges, edge_weights=edge_weights)
    recommended_nodes, recommended_node_scores,sorted_recommended_dict = score.get_recommended_nodes()
    return recommended_nodes, recommended_node_scores, sorted_recommended_dict
