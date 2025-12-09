MODEL (
  name kantin.laporan_bersih,
  kind FULL
);

SELECT
  id,
  menu,
  harga,
  COALESCE(diskon, 0) AS diskon_fixed,
  (harga - COALESCE(diskon, 0)) AS harga_akhir
FROM

  data_penjualan_file.transaksi_gabungan