import pandas as pd

def clean_sales_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
    df.dropna(subset=["sales_amount"], inplace=True)
    return df