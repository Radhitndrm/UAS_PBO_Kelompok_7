# Sistem Manajemen Limbah Pasca Bencana

## Deskripsi

Sistem Manajemen Limbbah Pasca Bencana adalah aplikasi berbasis **Python (CLI)** yang dirancang untuk mengelola data limbah yang dihasilkan akibat bencana. Sistem ini menerapkan konsep **Object-Oriented Programming (OOP)**, **Repository Pattern**, dan **Service Layer** untuk memastikan struktur kode rapi, terstruktur, dan mudah dikembangkan.

Aplikasi ini mendukung pendaftaran berbagai jenis limbah, pengelolaan status limbah, serta proses pengangkutan dengan pencatatan log aktivitas.

---

## Fitur Utama

* Pendaftaran limbah berdasarkan jenis:

  * Limbah Organik
  * Limbah Medis
  * Limbah B3
* Validasi data limbah
* Penyimpanan data limbah sementara (in-memory)
* Proses pengangkutan limbah
* Perubahan status limbah otomatis
* Logging aktivitas sistem

---

## Struktur Proyek

```
main.py
│
├── models
│   ├── limbah.py
│   ├── limbah_organik.py
│   ├── limbah_medis.py
│   ├── limbah_b3.py
│   ├── lokasi.py
│   └── petugas.py
│
├── repositories
│   ├── in_memory_limbah_repository.py
│   ├── limbah_repository.py
│   └── lokasi_repository.py
│
├── services
│   ├── limbah_service.py
│   └── pengangkutan_service.py
│
└── utils
    ├── logging_config.py
    ├── date_helper.py
    └── validator.py
```

---

## Penjelasan Struktur Folder

### 1. Models

Berisi representasi entitas inti dalam sistem:

* **Limbah**: kelas abstrak induk untuk seluruh jenis limbah
* **LimbahOrganik / LimbahMedis / LimbahB3**: turunan dari kelas Limbah sesuai jenisnya
* **Lokasi**: menyimpan informasi lokasi dan jenis bencana
* **Petugas**: merepresentasikan petugas yang menangani limbah beserta keahliannya

### 2. Repositories

Lapisan akses data yang bertugas menyimpan dan mengambil data:

* **LimbahRepository**: kontrak/interface repository limbah
* **InMemoryLimbahRepository**: penyimpanan data limbah di memori selama aplikasi berjalan
* **LokasiRepository**: pengelolaan data lokasi (opsional/pengembangan lanjutan)

### 3. Services

Berisi logika bisnis aplikasi:

* **LimbahService**: menangani pendaftaran, validasi, dan pengelolaan data limbah
* **PengangkutanService**: menangani proses pengangkutan limbah dan perubahan status

### 4. Utils

Modul pendukung yang digunakan secara umum:

* **logging_config**: konfigurasi logging sistem
* **date_helper**: utilitas pengelolaan tanggal dan waktu
* **validator**: validasi input umum

### 5. main.py

Merupakan entry point aplikasi. File ini menangani interaksi pengguna melalui menu CLI dan memanggil service sesuai kebutuhan.

---

## Cara Menjalankan Aplikasi

1. Pastikan Python versi 3.10 atau lebih baru terinstal
2. Masuk ke direktori proyek
3. Jalankan perintah:

```
python main.py
```

---

## Konsep OOP yang Digunakan

* **Abstraction**: melalui kelas abstrak `Limbah`
* **Inheritance**: turunan `LimbahOrganik`, `LimbahMedis`, dan `LimbahB3`
* **Encapsulation**: penggunaan atribut private dan method getter/setter
* **Polymorphism**: implementasi berbeda dari `hitung_risiko()` dan `proses_pengolahan()`

---

## Tujuan Pembelajaran

* Menerapkan konsep OOP dalam studi kasus nyata
* Memahami pemisahan tanggung jawab (Separation of Concerns)
* Mengimplementasikan Service dan Repository Pattern
* Melatih pembuatan aplikasi terstruktur dan mudah dikembangkan

---
