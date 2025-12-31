# Sistem Manajemen Limbah Pasca Bencana

## Deskripsi

Sistem Manajemen Limbah Pasca Bencana adalah aplikasi berbasis **Python (CLI)** yang dirancang untuk mengelola data limbah yang dihasilkan akibat bencana. Sistem ini menerapkan konsep **Object-Oriented Programming (OOP)**, **SOLID Principles**, **Repository Pattern**, dan **Service Layer** untuk memastikan struktur kode rapi, terstruktur, dan mudah dikembangkan.

Aplikasi ini mendukung pendaftaran berbagai jenis limbah, pengelolaan status limbah, proses pengangkutan dengan pencatatan log aktivitas, serta dilengkapi dengan **unit testing** untuk menjamin reliabilitas sistem.

---

## Fitur Utama

- **Pendaftaran limbah** berdasarkan jenis:
  - Limbah Organik (dengan tingkat pembusukan)
  - Limbah Medis (dengan tingkat infeksi)
  - Limbah B3 (dengan kandungan kimia)
- **Validasi data** yang ketat untuk input pengguna
- **Penyimpanan data** limbah sementara (in-memory repository)
- **Proses pengangkutan** limbah dengan tracking petugas dan kendaraan
- **Perubahan status** limbah otomatis berdasarkan proses
- **Logging aktivitas** sistem (INFO, WARNING, ERROR) untuk audit trail
- **Perhitungan risiko** otomatis berdasarkan jenis limbah
- **Unit testing** lengkap untuk models, services, repositories, dan utils
- **Error handling** yang komprehensif dengan exception yang spesifik

---

## Struktur Proyek

```
UAS_PBO_Kelompok_7/
│
├── main.py                  # Entry point aplikasi
├── readme.md               # Dokumentasi proyek
│
├── models/                 # Model/Entity classes
│   ├── limbah.py          # Abstract base class Limbah
│   ├── limbah_organik.py  # Limbah organik (inheritance)
│   ├── limbah_medis.py    # Limbah medis (inheritance)
│   ├── limbah_b3.py       # Limbah B3 (inheritance)
│   ├── lokasi.py          # Model lokasi bencana
│   └── petugas.py         # Model petugas penanganan
│
├── repositories/          # Data access layer
│   ├── limbah_repository.py           # Interface (ABC)
│   ├── in_memory_limbah_repository.py # Implementasi in-memory
│   └── lokasi_repository.py           # Interface lokasi
│
├── services/              # Business logic layer
│   ├── limbah_service.py        # Service pengelolaan limbah
│   └── pengangkutan_service.py  # Service pengangkutan
│
├── utils/                 # Utility modules
│   ├── logging_config.py  # Konfigurasi logging
│   ├── date_helper.py     # Helper tanggal/waktu
│   └── validator.py       # Validasi input
│
└── tests/                 # Unit testing
    ├── __init__.py
    ├── test_models.py      # Test untuk models
    ├── test_repositories.py # Test untuk repositories
    ├── test_services.py    # Test untuk services
    └── test_utils.py       # Test untuk utils
```

---

## Penjelasan Struktur Folder

### 1. Models (Entitas Domain)

Berisi representasi entitas inti dalam sistem dengan enkapsulasi penuh:

- **Limbah** (abstract class):

  - Kelas abstrak induk dengan atribut private (`__id`, `__volume`, `__status`)
  - Method abstrak `hitung_risiko()` dan `proses_pengolahan()`
  - Getter/setter dengan validasi untuk semua atribut
  - Property `volume` menggunakan Python property decorator

- **LimbahOrganik / LimbahMedis / LimbahB3**:

  - Turunan dari kelas Limbah (inheritance)
  - Override method `hitung_risiko()` dan `proses_pengolahan()` (polymorphism)
  - Atribut spesifik private: `__tingkat_pembusukan`, `__tingkat_infeksi`, `__kandungan_kimia`
  - Custom `__str__()` untuk representasi yang readable

- **Lokasi**:

  - Enkapsulasi data lokasi bencana
  - Atribut private dengan getter/setter dan validasi
  - Validasi input tidak boleh kosong

- **Petugas**:
  - Merepresentasikan petugas penanganan limbah
  - Enkapsulasi lengkap dengan validasi
  - Method `get_info()` untuk mendapatkan data sebagai dictionary

### 2. Repositories (Data Access Layer)

Menerapkan **Repository Pattern** dan **Dependency Inversion Principle**:

- **LimbahRepository (ABC)**:

  - Interface/kontrak untuk operasi data limbah
  - Method: `save()`, `get_all()`, `get_by_id()`
  - Memungkinkan implementasi berbeda (in-memory, database, file)

- **InMemoryLimbahRepository**:

  - Implementasi konkret menggunakan list Python
  - Penyimpanan data di memori selama runtime
  - Mendukung CRUD operations dasar

- **LokasiRepository**:
  - Interface untuk pengelolaan data lokasi (untuk pengembangan lanjutan)

### 3. Services (Business Logic Layer)

Menerapkan **Single Responsibility Principle**:

- **LimbahService**:

  - Menangani registrasi limbah (organik, medis, B3)
  - Validasi input menggunakan private methods
  - Integrasi dengan `utils.validator` untuk validasi volume
  - Perhitungan total risiko dari semua limbah
  - Proses pengolahan limbah dengan perubahan status
  - Pencarian limbah by ID
  - Logging semua aktivitas untuk audit trail

- **PengangkutanService**:
  - Menangani proses pengangkutan limbah
  - Validasi status limbah sebelum pengangkutan
  - Update status limbah menjadi "Diangkut"
  - Pembuatan catatan pengangkutan dengan timestamp
  - Error handling untuk kasus edge cases

### 4. Utils (Utility Modules)

Modul helper yang mendukung **Single Responsibility Principle**:

- **logging_config.py**:

  - Setup konfigurasi logging aplikasi
  - Format: timestamp, level, dan message

- **date_helper.py**:

  - Utilitas pengelolaan tanggal dan waktu
  - Function `get_current_timestamp()` untuk format konsisten

- **validator.py**:
  - Validasi input umum yang reusable
  - `validate_volume()`: validasi volume > 0
  - `validate_status()`: validasi status sesuai allowed values

### 5. Tests (Unit Testing)

Comprehensive unit testing menggunakan **unittest framework**:

- **test_models.py**:

  - Test untuk semua model classes
  - Test enkapsulasi, validasi, dan polymorphism
  - Coverage: LimbahOrganik, LimbahMedis, LimbahB3, Petugas, Lokasi

- **test_repositories.py**:

  - Test operasi CRUD repository
  - Test isolation antar instance
  - Test `get_by_id()` dengan berbagai scenario

- **test_services.py**:

  - Test business logic di LimbahService dan PengangkutanService
  - Test validasi input dan error handling
  - Test integrasi dengan repository

- **test_utils.py**:
  - Test validator functions
  - Test date helper format dan konsistensi

### 6. main.py (Entry Point)

- Orchestrator aplikasi dengan menu CLI interaktif
- Dependency injection untuk repository dan services
- Error handling dengan specific exceptions (ValueError, LookupError)
- Logging untuk sistem events (bukan UI output)
- `print()` hanya untuk user interaction

---

## Cara Menjalankan Aplikasi

### Persyaratan Sistem

- Python versi **3.9** atau lebih baru
- Tidak memerlukan instalasi dependencies eksternal (hanya standard library)

### Menjalankan Aplikasi Utama

1. Buka terminal dan masuk ke direktori proyek:

   ```bash
   cd /path/to/UAS_PBO_Kelompok_7
   ```

2. Jalankan aplikasi:

   ```bash
   python main.py
   ```

   atau

   ```bash
   python3 main.py
   ```

3. Ikuti menu interaktif yang tersedia:
   - **Menu 1**: Tambah Limbah Organik
   - **Menu 2**: Tambah Limbah Medis
   - **Menu 3**: Tambah Limbah B3
   - **Menu 4**: Lihat Semua Limbah
   - **Menu 5**: Angkut Limbah
   - **Menu 0**: Keluar

### Menjalankan Unit Tests

Untuk menjalankan semua unit tests:

```bash
python -m unittest discover -s tests -v
```

Atau menjalankan test file spesifik:

```bash
python -m unittest tests.test_models -v
python -m unittest tests.test_services -v
python -m unittest tests.test_repositories -v
python -m unittest tests.test_utils -v
```

### Contoh Penggunaan

**Menambah Limbah Organik:**

```
Pilih menu: 1
ID limbah: L001
Volume (kg): 100
Tingkat pembusukan: 5
Nama lokasi: Jakarta Barat
Alamat lokasi: Jl. Raya
Jenis bencana: Banjir
```

**Melihat Daftar Limbah:**

```
Pilih menu: 4
--- DAFTAR LIMBAH ---
LimbahOrganik(ID: L001, Volume: 100.0 kg, Status: Terdaftar, Tingkat Pembusukan: 5, Risiko: 400.00)
```

**Mengangkut Limbah:**

```
Pilih menu: 5
ID limbah yang akan diangkut: L001
ID petugas: P001
Nama petugas: Ahmad
Keahlian petugas: Pengangkutan
Nama/jenis kendaraan: Truk Besar
Tujuan pengangkutan: TPS Kalibata
```

---

## Konsep OOP yang Diimplementasikan

### 1. Abstraction

- Menggunakan kelas abstrak `Limbah(ABC)` dengan abstract methods
- Abstract methods: `hitung_risiko()` dan `proses_pengolahan()`
- Memaksa child classes untuk mengimplementasikan method spesifik

### 2. Inheritance

- **LimbahOrganik**, **LimbahMedis**, dan **LimbahB3** mewarisi dari **Limbah**
- Menggunakan `super().__init__()` untuk memanggil constructor parent
- Hubungan "is-a" yang jelas (LimbahOrganik _is a_ Limbah)

### 3. Encapsulation

- **Semua atribut bersifat private** dengan prefix `__`:
  - Contoh: `__id`, `__volume`, `__status`, `__tingkat_pembusukan`
- **Akses melalui getter/setter**:
  - `get_id()`, `get_volume()`, `set_volume()`, dll.
- **Validasi di setter**:
  - Volume harus > 0
  - String tidak boleh kosong
  - Tipe data harus sesuai
- **Python property** untuk akses natural:
  ```python
  limbah.volume = 100.0  # Memanggil set_volume() dengan validasi
  ```

### 4. Polymorphism

- **Method Overriding**:
  - `hitung_risiko()` berbeda di setiap child class:
    - LimbahOrganik: `volume * tingkat_pembusukan * 0.8`
    - LimbahMedis: `volume * tingkat_infeksi * 1.5`
    - LimbahB3: `volume * 2.0`
  - `proses_pengolahan()` menghasilkan output berbeda:
    - LimbahOrganik → "Didaur Ulang"
    - LimbahMedis → "Dimusnahkan"
    - LimbahB3 → "Diproses Khusus"
- **Dynamic Dispatch**: Method yang dipanggil ditentukan saat runtime berdasarkan tipe object

---

## Prinsip SOLID yang Diterapkan

### 1. Single Responsibility Principle (SRP)

- **Models**: Hanya menangani data dan behavior entitas
- **Repositories**: Hanya bertanggung jawab untuk data access
- **Services**: Hanya menangani business logic
- **Utils**: Hanya menyediakan utility functions
- Tidak ada "God Class" yang melakukan terlalu banyak hal

### 2. Open/Closed Principle (OCP)

- Class terbuka untuk extension (inheritance) tapi tertutup untuk modification
- Contoh: Menambah jenis limbah baru (misal: LimbahElektronik) tanpa mengubah class Limbah

### 3. Liskov Substitution Principle (LSP)

- Semua child class (LimbahOrganik, LimbahMedis, LimbahB3) dapat menggantikan parent (Limbah)
- Method yang menerima parameter `Limbah` dapat menerima instance dari child class

### 4. Interface Segregation Principle (ISP)

- Interface (ABC) hanya mendefinisikan method yang benar-benar diperlukan
- Tidak ada method yang tidak digunakan oleh implementor

### 5. Dependency Inversion Principle (DIP)

- **High-level modules** (Services) tidak bergantung pada **low-level modules** (Repositories)
- Keduanya bergantung pada **abstraksi** (LimbahRepository ABC)
- **Dependency Injection** via constructor:
  ```python
  def __init__(self, limbah_repository: LimbahRepository):
      self.__limbah_repository = limbah_repository
  ```

---

## Design Patterns yang Digunakan

### 1. Repository Pattern

- Memisahkan business logic dari data access logic
- Interface `LimbahRepository` sebagai kontrak
- Implementasi dapat diganti tanpa mengubah service layer

### 2. Dependency Injection

- Dependencies di-inject melalui constructor
- Meningkatkan testability dan loose coupling

### 3. Layered Architecture

- **Presentation Layer**: `main.py` (CLI interface)
- **Service Layer**: Business logic di `services/`
- **Data Access Layer**: `repositories/`
- **Domain Layer**: `models/`

---

## Fitur Quality Assurance

### 1. Unit Testing (58+ Test Cases)

- **test_models.py**: 25+ tests untuk validasi OOP concepts
- **test_repositories.py**: 7 tests untuk data access
- **test_services.py**: 18 tests untuk business logic
- **test_utils.py**: 8 tests untuk utility functions

### 2. Logging

- **INFO**: Aktivitas normal (registrasi, pengangkutan berhasil)
- **WARNING**: Kondisi yang perlu perhatian (data tidak ditemukan)
- **ERROR**: Kesalahan yang dapat ditangani (validasi gagal)
- **EXCEPTION**: Error tidak terduga dengan full traceback

### 3. Error Handling

- **ValueError**: Validasi input gagal
- **LookupError**: Data tidak ditemukan
- **Exception**: Fallback untuk error tidak terduga
- Semua error di-log untuk audit trail

### 4. Input Validation

- Validasi tipe data (str, int, float)
- Validasi range (volume > 0, tingkat minimal 1)
- Validasi tidak kosong (strip whitespace)
- Reusable validator di `utils/validator.py`

---

## Dokumentasi

### Docstring Style: Google

Semua class dan method menggunakan Google-style docstring:

```python
def registrasi_limbah_organik(self, id: str, volume: float, tingkat_pembusukan: int) -> LimbahOrganik:
    """
    Membuat dan menyimpan objek LimbahOrganik ke repository.

    Args:
        id (str): ID limbah.
        volume (float): Volume limbah.
        tingkat_pembusukan (int): Tingkat pembusukan limbah.

    Returns:
        LimbahOrganik: Objek LimbahOrganik yang berhasil dibuat dan disimpan.

    Raises:
        ValueError: Jika validasi input gagal.
    """
```

### Type Hints

Semua function dan method menggunakan type hints untuk better IDE support:

```python
def get_by_id(self, id: str) -> Optional[Limbah]:
    ...
```

---

## Teknologi yang Digunakan

- **Python 3.9+**: Language utama
- **abc (Abstract Base Classes)**: Untuk abstraction dan interface
- **typing**: Type hints untuk better code quality
- **logging**: Audit trail dan debugging
- **datetime**: Timestamp management
- **unittest**: Framework testing

---

## Keunggulan Sistem

1. **Modular dan Terstruktur**: Separation of concerns yang jelas
2. **Mudah di-maintain**: Code yang clean dan well-documented
3. **Mudah di-extend**: Tambah fitur baru tanpa merusak yang lama
4. **Testable**: Comprehensive unit tests
5. **Type-safe**: Type hints di semua function/method
6. **Robust**: Error handling dan validasi yang ketat
7. **Auditable**: Logging lengkap untuk tracking aktivitas

---
