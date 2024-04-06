import pandas as pd
import numpy as np
from  src.Metric_Calc import Metrics
import streamlit as st

def metric_calc(entire_dataframe: pd.DataFrame,customer_dataframe: pd.DataFrame, products_list: list, node_list: dict):

    st.title(":blue[Metrics]")

    no_of_sub_categories = entire_dataframe['sub_category'].unique()

    metric= Metrics(entire_dataframe= entire_dataframe, products_list= products_list, node_list= node_list, customer_dataframe= customer_dataframe)
    top_categories = metric.find_top_categories()
    top_categories_recommended = metric.top_categories_recommended()

    percentage_of_coverage_metric = metric.percentage_of_coverage_metric(recommended_categories= top_categories_recommended)
    st.subheader(f"{percentage_of_coverage_metric} percentage of sub-categories are recommended out of total sub-categories")

    non_interacted_sub_category_metric = metric.non_interacted_sub_category_metric(recommended_categories= top_categories_recommended)
    st.subheader(f"{non_interacted_sub_category_metric} unexposed sub-categories(sub-category) are recommended")

    percentage_of_top_three_sub_cat_items = metric.percentage_of_top_three_sub_cat_items(top_categories= top_categories, recommended_categories= top_categories_recommended)
    st.subheader(f"{percentage_of_top_three_sub_cat_items} percentage of items are recommended from the top three sub-categories")

    percentage_of_items_in_user_interacted_sub_cat = metric.percentage_of_items_in_user_interacted_sub_cat(recommended_categories= top_categories_recommended)
    st.subheader(f"{percentage_of_items_in_user_interacted_sub_cat} percentage of items are in user interacted sub-categories")