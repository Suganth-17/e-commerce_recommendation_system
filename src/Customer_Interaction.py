import pandas as pd

class CustomerInteraction:
    def __init__(self, data_frame: pd.DataFrame) -> None:
        self.data_frame = data_frame

    def get_specific_customer_dataframe(self, customer_id) -> pd.DataFrame:
        specific_customer_dataframe = self.data_frame[self.data_frame['customer_id'] == customer_id]
        return specific_customer_dataframe

    def interacted_categories(self) -> list:
        interacted_categories_list = self.data_frame['sub_category'].unique()
        return interacted_categories_list
    def get_product_names(self) ->list:
        product_names_list = self.data_frame['product_name'].unique()
        return product_names_list
