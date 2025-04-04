import polars as pl

def csv_to_parquet(csv_path, parquet_path):
    df = pl.read_csv(csv_path)
    df.write_parquet(parquet_path)

csv_to_parquet("./training.csv", "./data/training.parquet")