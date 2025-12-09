# 🍱 Adaptive Schema Pipeline: Canteen Analytics

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![dlt](https://img.shields.io/badge/ELT-dlt-orange)
![SQLMesh](https://img.shields.io/badge/Transform-SQLMesh-black)
![DuckDB](https://img.shields.io/badge/Database-DuckDB-yellow)

> **A resilient ELT pipeline built to handle schema evolution in high-school canteen transaction data.**

## 📖 Project Overview

Proyek ini adalah implementasi **Modern Data Pipeline** yang dirancang untuk menangani masalah umum dalam data engineering: **Schema Evolution** (Perubahan struktur data).

Studi kasus yang digunakan adalah **Data Transaksi Kantin Sekolah**, di mana format laporan harian sering berubah (contoh: penambahan kolom baru `diskon` secara tiba-tiba). Pipeline ini menggunakan pendekatan **ELT (Extract, Load, Transform)** agar data tetap bisa diproses otomatis tanpa error.

## 🚀 Tech Stack

* **[dlt (Data Load Tool)](https://dlthub.com/)**: Untuk proses *Ingestion* (Extract & Load). Secara otomatis menangani perubahan skema dan menggabungkan data CSV yang berbeda struktur.
* **[DuckDB](https://duckdb.org/)**: Berperan sebagai *Local Data Lakehouse*. Menyimpan raw data dan melakukan komputasi analitik yang cepat (Single-file database).
* **[SQLMesh](https://sqlmesh.com/)**: Untuk proses *Transformation*. Membersihkan data (handling NULLs), menerapkan logika bisnis, dan memastikan kualitas data (Data Quality).

## 📂 Project Structure

Proyek ini menggunakan konsep **Monorepo** yang memisahkan layer Ingestion dan Transformation:

```Text
ADAPTIVE-SCHEMA-PIPELINE/
├── ingestion/                  # Layer 1: Data Ingestion
│   ├── pipeline_kantin.py      # Script utama dlt untuk load CSV ke DuckDB
│   ├── senin.csv               # Data Raw Hari 1 (Tanpa diskon)
│   ├── selasa.csv              # Data Raw Hari 2 (Ada kolom diskon)
│   └── kantin_file_pipeline.duckdb  # (Generated Database)
│
├── transformation/             # Layer 2: Data Transformation
│   ├── config.yaml             # Konfigurasi koneksi SQLMesh ke DuckDB
│   ├── laporan_bersih.sql      # Model SQL untuk membersihkan data NULL
│   ├── cek_data.py             # Script Python untuk validasi hasil akhir
│   └── kantin_file_pipeline.duckdb  # (Database Reference)
│
├── .gitignore                  # Daftar file yang diabaikan git (DB, cache)
└── README.md                   # Dokumentasi Proyek
```

## ⚡ How It Works (Workflow)
Ingestion Layer (dlt):

Script pipeline_kantin.py membaca senin.csv dan selasa.csv.

dlt mendeteksi kolom baru (diskon) pada file Selasa.

Tabel di DuckDB diperbarui otomatis (Schema Evolution). Data Senin yang tidak memiliki diskon diisi dengan NULL.

Transformation Layer (SQLMesh):

SQLMesh membaca raw data dari DuckDB.

Menjalankan logika transformasi di laporan_bersih.sql.

Menggunakan fungsi COALESCE(diskon, 0) untuk mengubah NULL menjadi 0.

Menghitung harga_akhir (Revenue bersih) secara otomatis.

## 🛠️ Getting Started
Ikuti langkah ini untuk menjalankan pipeline di komputer lokal:

1. Prerequisites
Install library yang dibutuhkan:
```

```Bash

pip install dlt[duckdb] sqlmesh pandas
```
2. Run Ingestion (Layer 1)
Masuk ke folder ingestion dan jalankan pipeline:

```Bash

cd ingestion
python pipeline_kantin.py
```
Output: Data CSV akan dimuat ke dalam file database DuckDB.

3. Run Transformation (Layer 2)
Pindah ke folder transformation dan jalankan SQLMesh:

```Bash

cd ../transformation
sqlmesh plan
sqlmesh apply
Output: SQLMesh akan membuat tabel bersih (laporan_bersih) yang siap dianalisis.
```

4. Verify Results
Jalankan script pengecekan untuk melihat data sebelum vs sesudah:

```Bash

python cek_data.py
```

## 👤 Author
Data Engineering Intern

Vocational High School (SMK) Student.

Passionate about Modern Data Stack, Data Warehousing, and Python.

Created as part of an Internship Project exploring dlt & SQLMesh.