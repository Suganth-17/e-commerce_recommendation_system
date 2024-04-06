from src.Recommendation_Process import Vectorizer
import pandas as pd


def get_product_recommendations(entire_data_frame: pd.DataFrame, customer_data_frame: pd.DataFrame, recommended_list: list):

    vector = Vectorizer(entire_data_frame= entire_data_frame, customer_data_frame= customer_data_frame)
    cosine_sim_matrix, tfidf_recommended_matrix = vector.tf_idf_vectorizer(recommended_nodes= recommended_list)
    recommendations_dict= vector.get_recommendations_1(cosine_sim_matrix, list(customer_data_frame['all_meta']), tfidf_recommended_matrix)
    return recommendations_dict