from src.Customer_Interaction import CustomerInteraction
import pandas as pd

def cust_interact(data_frame: pd.DataFrame, customer_id)-> pd.DataFrame:

    interact = CustomerInteraction(data_frame)
    specific_dataframe = interact.get_specific_customer_dataframe(customer_id)
    return specific_dataframe

def get_interacted_categories(specific_customer_dataframe: pd.DataFrame) -> list:
    interact = CustomerInteraction(specific_customer_dataframe)
    interacted_categories_list = interact.interacted_categories()
    return interacted_categories_list

def get_products(specific_customer_dataframe: pd.DataFrame):
        interact = CustomerInteraction(specific_customer_dataframe)
        interacted_product_names = interact.get_product_names()
        return interacted_product_names

