import dlt
import pandas as pd
import os

pipeline = dlt.pipeline(
    pipeline_name="kantin_file_pipeline",
    destination="duckdb",
    dataset_name="data_penjualan_file"
)

df_senin = pd.read_csv("senin.csv")
print("Loading data Senin...")

pipeline.run(df_senin, table_name="transaksi_gabungan")

df_selasa = pd.read_csv("selasa.csv")
print("Loading data Selasa (Kolom beda)...")

pipeline.run(df_selasa, table_name="transaksi_gabungan")

print("-" * 30)
print("Selesai! Cek databasenya.")

import duckdb
con = duckdb.connect("kantin_file_pipeline.duckdb")
print("\nIsi Tabel Gabungan:")
con.sql("SELECT * FROM data_penjualan_file.transaksi_gabungan ORDER BY id").show()