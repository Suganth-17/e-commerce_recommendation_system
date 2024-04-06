import pandas as pd


class FinalRecommendation:
    def __init__(self, recommended_category_dict: list, sorted_recommended_dict: dict) -> None:
        self.recommended_category_dict = recommended_category_dict
        self.sorted_recommended_dict = sorted_recommended_dict

    
    def hybrid_approach(self):
        dict_list = []
        for dict in self.recommended_category_dict:
                for key, value in dict.items():
                    dict[key] = (value[0]* 0.40 ) + (self.sorted_recommended_dict[value[1]]*0.60)
                dict_list.append(dict)
        
        final_product_dict = {}
        for dict in dict_list:
            for key, value in dict.items():
                final_product_dict[key] = value

        final_products= sorted(final_product_dict, key=lambda x: final_product_dict[x], reverse=True)
        return final_products[:15]

