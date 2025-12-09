import duckdb

con = duckdb.connect("kantin_file_pipeline.duckdb")

try:
    con.sql("SELECT table_name, table_type FROM information_schema.tables WHERE table_schema = 'kantin'")
    
    print("\n=== BUKTI DATA ===")
    con.sql("SELECT * FROM kantin.laporan_bersih").show()
    print("Selamat! Laporan Bersih ditemukan.")
except Exception as e:
    print("Waduh, error atau tidak ketemu:", e)

con.close()