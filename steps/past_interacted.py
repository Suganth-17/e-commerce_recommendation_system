from src.Ingest_Data import IngestData
import pandas as pd

def past_data_ingest()-> pd.DataFrame:
    ingest_data = IngestData('data\customer_interactions.xlsx')
    data_frame = ingest_data.get_data_frame()
    return data_frame