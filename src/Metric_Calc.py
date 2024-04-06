import pandas as pd
import numpy as np


class Metrics:
    def __init__(self, entire_dataframe: pd.DataFrame,customer_dataframe: pd.DataFrame, products_list: list, node_list: list) -> None:
        self.data_frame = entire_dataframe
        self.product_list = products_list
        self.node_list = node_list
        self.cust_data_frame = customer_dataframe

    def find_top_categories(self):
        top_categories = self.node_list[:3]
        return top_categories
    
    def top_categories_recommended(self):
         
        categories_recommended = []
        for product in self.product_list:  
            index = self.data_frame.loc[self.data_frame['product_name'] == product].index[0]
            categories_recommended.append(self.data_frame['sub_category'][index])
        return categories_recommended
    

    def percentage_of_coverage_metric(self, recommended_categories):
        percentage_of_coverage = (len(set(recommended_categories))/self.data_frame['sub_category'].nunique())*100
        return percentage_of_coverage
    
    def non_interacted_sub_category_metric(self, recommended_categories):
        no_of_new_sub_category_exposure =  (len(set(recommended_categories))) - len(set(self.cust_data_frame['sub_category'].unique()))
        return no_of_new_sub_category_exposure
    
    def percentage_of_top_three_sub_cat_items(self, top_categories, recommended_categories):
        no_of_items_present_in_top_sub_cat = 0
        for sub_cat in recommended_categories:
            if sub_cat in top_categories:
                no_of_items_present_in_top_sub_cat += 1
        percentage_of_dominance = (no_of_items_present_in_top_sub_cat/ len(recommended_categories)) *100
        return percentage_of_dominance

    def percentage_of_items_in_user_interacted_sub_cat(self, recommended_categories):
        no_of_items = 0
        sub_categories = self.cust_data_frame['sub_category'].unique()
        for sub_cat in recommended_categories:
            if sub_cat in sub_categories:
                no_of_items += 1
        percentage_of_items_in_user_interacted_sub_cat = (no_of_items/len(recommended_categories)) *100
        return percentage_of_items_in_user_interacted_sub_cat

        

        