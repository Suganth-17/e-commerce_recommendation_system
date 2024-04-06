from steps.data_ingestion import data_ingest
from steps.data_preprocessing import pre_process_data
from steps.graph_creation import graph_creation
from steps.customer_ingestion import customer_data_ingest
from steps.interaction import cust_interact, get_interacted_categories, get_products
from steps.get_scores import recommneded_categories
from steps.recommendation import get_product_recommendations
from steps.past_interacted import past_data_ingest
from steps.specific_customer_data_preprocessing import specific_cust_pre_process_data
from steps.ranking_products import get_product_ranking
from steps.new_user_recommendation import recommendation_new_users
from steps.metrics import metric_calc
import pandas as pd
import warnings
import streamlit as st

with warnings.catch_warnings():
    warnings.filterwarnings("ignore")

def execution():
    entire_data = data_ingest()
    entire_data = pre_process_data(entire_data)
    interact_data = past_data_ingest()
    item_graph = graph_creation(interact_data)
    customer_data = customer_data_ingest()
    if customer_data.shape[0]== 0:
        st.title("Recommendation for new Users")
        recommendation_new_users(interact_data_frame= interact_data,  graph= item_graph)
    else:
        st.title(":blue[Personalized Recommendation]")
        customer_data = specific_cust_pre_process_data(data_frame= customer_data) 
        specific_customer_data = cust_interact(customer_data, customer_id= 1)
        interacted_categories = get_interacted_categories(specific_customer_data)
        recommneded_category_list, recommneded_category_scores,sorted_recommended_dict = recommneded_categories(item_graph= item_graph, data_frame= interact_data, interacted_categories_list= interacted_categories)
        recommended_category_dict = get_product_recommendations(entire_data_frame= entire_data, customer_data_frame= specific_customer_data, recommended_list= recommneded_category_list)
        product_ranking_list= get_product_ranking(recommended_category_dict, recommneded_category_scores, sorted_recommended_dict)
        for products in product_ranking_list:
            st.subheader(products)

        metric_calc(entire_dataframe= entire_data,customer_dataframe=specific_customer_data ,products_list= product_ranking_list, node_list= recommneded_category_list)


if __name__ == '__main__':
    execution()
    