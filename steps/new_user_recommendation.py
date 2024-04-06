from src.New_User import NewUser
import pandas as pd
import networkx as nx
import streamlit as st

def recommendation_new_users(interact_data_frame: pd.DataFrame, graph: nx.Graph):

    new_user = NewUser(interact_data_frame= interact_data_frame, graph= graph)
    nodes_list = new_user.get_nodes()
    nodes_score_dict = new_user.get_nodes_score(nodes_list= nodes_list)
    products_to_recommend = new_user.recommend_popular_products(scores_dict= nodes_score_dict)
    for product in products_to_recommend:
        st.subheader(product)