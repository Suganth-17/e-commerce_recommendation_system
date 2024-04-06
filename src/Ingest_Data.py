import pandas as pd


class IngestData:
    def __init__(self, data_path: str) -> None:
        self.data_path = data_path

    def get_data_frame(self) -> pd.DataFrame:
        data_frame = pd.read_excel(self.data_path)
        return data_frame