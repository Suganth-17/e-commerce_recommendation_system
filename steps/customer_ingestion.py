from src.Ingest_Data import IngestData
import pandas as pd

def customer_data_ingest()-> pd.DataFrame:
    data_path = "data\\customer_buy.xlsx"
    ingest_data = IngestData(data_path)
    data_frame = ingest_data.get_data_frame()
    return data_frame