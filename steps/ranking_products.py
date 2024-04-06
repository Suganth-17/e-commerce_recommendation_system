from src.Final_recommendations import FinalRecommendation


def get_product_ranking(recommended_category_dict: list, recommneded_category_scores: list, sorted_recommended_dict: dict)-> list:
    
    final_recommend = FinalRecommendation(recommended_category_dict, sorted_recommended_dict)
    final_recommend = FinalRecommendation(recommended_category_dict, sorted_recommended_dict)
    final_products = final_recommend.hybrid_approach()
    return final_products

 