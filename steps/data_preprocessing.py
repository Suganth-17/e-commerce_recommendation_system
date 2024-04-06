from src.Data_Preprocessing import DataPreProcessing, MetaCreation
import pandas as pd

def pre_process_data(data_frame: pd.DataFrame)-> pd.DataFrame:

    pre_process = DataPreProcessing(data_frame)
    data_frame = pre_process.drop_duplicates()
    meta = MetaCreation(data_frame)
    data_frame = meta.create_meta()
    return data_frame