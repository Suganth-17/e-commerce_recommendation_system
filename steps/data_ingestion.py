from src.Ingest_Data import IngestData
import pandas as pd

def data_ingest()-> pd.DataFrame:
    ingest_data = IngestData('data\product_dataset.xlsx')
    data_frame = ingest_data.get_data_frame()
    return data_frame