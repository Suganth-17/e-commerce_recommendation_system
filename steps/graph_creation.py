from src.Create_Graph import CreateGraph, CreateNodes, CreateEdges
import pandas as pd
import networkx as nx

def graph_creation(data_frame: pd.DataFrame) -> nx.Graph:
    graph = CreateGraph()
    item_graph = graph.create()
    graph_nodes = CreateNodes(item_graph, data_frame= data_frame)
    nodes_list = graph_nodes.get_nodes()
    item_graph = graph_nodes.create_nodes()
    graph_edges = CreateEdges(item_graph, data_frame= data_frame)
    item_graph = graph_edges.create_edges(data_frame)
    return item_graph