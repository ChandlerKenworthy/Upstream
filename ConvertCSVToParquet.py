import pandas as pd
import os

FILE_NAME = "BBFails/Train_2022_Data_AtLeastOneBBFail"

csv_file = f'./data/{FILE_NAME}.txt'
df = pd.read_csv(csv_file)

# Save the DataFrame as a Parquet file
parquet_file = f'./data/{FILE_NAME}.parquet'
df.to_parquet(parquet_file, engine='pyarrow', compression='snappy')

csv_size = os.path.getsize(f"./data/{FILE_NAME}.txt")
parquet_size = os.path.getsize(f"./data/{FILE_NAME}.parquet")

print(f"CSV file size: {csv_size} bytes")
print(f"Parquet file size: {parquet_size} bytes")
print(f"Size reduction: {(1 - parquet_size / csv_size) * 100:.2f}%")