import pandas as pd

class DataLoader:
    def __init__(self, path):
        self.path = path
        self.df = None
    
    def load_data(self):
        self.df = pd.read_csv(self.path)
        return self.df
    
    def clean_data(self):
        if self.df is None:
            raise ValueError("Data not found")
        self.df = self.df.dropna()
        return self.df
    
    def get_data(self):
        if self.df is None:
            return self.load_data()
        return self.df
    
    def validate_record(self, record):
        required_fields = [
            "program",
            "frequency_per_week",
            "volume_sets",
            "protein_synthesis",
            "strength_gain",
            "testosterone_change",
            "cortisol_change"
        ]
        
        for field in required_fields:
            if field not in record:
                return ValueError(f"Missing field: {field}")
            
    def add_record(self, record):
        if self.df is None:
            self.load_data()

        self.validate_record(record)

        if "id" not in self.df.columns:
            self.df["id"] = range(1, len(self.df) + 1)

        new_id = self.df["id"].max() + 1 if len(self.df) > 0 else 1
        record["id"] = new_id

        new_row = pd.DataFrame([record])
        self.df = pd.concat([self.df, new_row], ignore_index = True)

        return self.df
    
    def save_data(self):
        if self.df is None:
            raise ValueError("Data not found")
        
        self.df.to_csv(self.path, index = False)