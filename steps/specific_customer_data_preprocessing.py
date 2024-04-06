from src.Data_Preprocessing import DataPreProcessing, MetaCreation
import pandas as pd

def specific_cust_pre_process_data(data_frame: pd.DataFrame)-> pd.DataFrame:

    pre_process = DataPreProcessing(data_frame)
    meta = MetaCreation(data_frame)
    data_frame = meta.create_meta()
    return data_frame

