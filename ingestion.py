import pandas as pd
import os



class IngestData():
    def __init__(self, dataset):
        self.dataset = dataset

    def _load_dataset(self):
        ext = os.path.splitext(self.dataset)[1].lower()
        if ext == ".csv":
            return pd.read_csv(self.dataset)
        elif ext in [".xlsx", ".xls"]:
            return pd.read_excel(self.dataset)
        else:
            return "Unsupported file format. Please ensure it is a CSV or Excel file."
        


        