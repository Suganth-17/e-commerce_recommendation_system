import pandas as pd
import networkx as nx


class NewUser:
    def __init__(self, interact_data_frame: pd.DataFrame, graph: nx.Graph) -> None:
        self.interact_dataframe = interact_data_frame
        self.graph = graph

    def get_nodes(self)-> list:
        nodes_list = self.graph.nodes
        return nodes_list
    
    def get_nodes_score(self, nodes_list: list)-> dict:
        scores_dict= {}
        for node in nodes_list:
            scores_dict[node] = self.graph.nodes[node]['score']  
        final_products= sorted(scores_dict, key=lambda x: scores_dict[x], reverse=True)
        return scores_dict
    
    def recommend_popular_products(self, scores_dict: dict):
        popular_products = []
        for key, value in scores_dict.items():
            popular_products.append(key)
        products_to_recommend= []
        products_ranked_dict = {}
        for sub_cat in popular_products:
            sub_cat_products = self.interact_dataframe[self.interact_dataframe['sub_category']==sub_cat]['product_name'].unique()
            for product in sub_cat_products:
                products_ranked_dict[product] = (scores_dict[sub_cat]*0.6)+ ((self.interact_dataframe['product_name']== product).sum()*0.4)
        final_products= sorted(products_ranked_dict, key=lambda x: products_ranked_dict[x], reverse=True)
        return final_products[:15]




        