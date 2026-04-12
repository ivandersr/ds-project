import pandas as pd

def clean_sales_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
    df["sales_amount"].fillna(df["sales_amount"].median(), inplace=True)
    return df