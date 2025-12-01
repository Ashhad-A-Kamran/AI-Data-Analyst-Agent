import pandas as pd
import os

class ProcessDataset:
    def __init__(self, dataset, filename: str):
        self.dataset = dataset
        ext = os.path.splitext(filename)[1].lower()
        
        if ext == ".csv":
            self.df = pd.read_csv(dataset)
        elif ext in [".xls", ".xlsx"]:
            self.df = pd.read_excel(dataset)
        else:
            raise ValueError(f"Unsupported file type: {ext}")

    def columns(self):
        return {"columns": list(self.df.columns)}        


        