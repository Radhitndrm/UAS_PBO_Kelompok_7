"""
Main entry point aplikasi Manajemen Limbah.

Aplikasi ini menyediakan menu berbasis CLI (Command Line Interface)
untuk:
- Menambahkan data limbah (Organik, Medis, B3)
- Melihat seluruh data limbah
- Melakukan proses pengangkutan limbah

Penyimpanan data menggunakan InMemory Repository
(sementara, selama program berjalan).
"""

import logging
from utils.logging_config import setup_logging

from repositories.in_memory_limbah_repository import InMemoryLimbahRepository
from services.limbah_service import LimbahService
from services.pengangkutan_service import PengangkutanService
from models.petugas import Petugas
from models.lokasi import Lokasi

logger = logging.getLogger(__name__)


def main():
    """
    Fungsi utama aplikasi.

    Fungsi ini:
    - Menginisialisasi logging
    - Menyiapkan repository dan service
    - Menyediakan menu interaktif untuk pengguna
    - Menangani input user dan memanggil service terkait

    Program akan terus berjalan sampai user memilih menu keluar.
    """

    # Setup logging aplikasi
    setup_logging()
    logger.info("Aplikasi Manajemen Limbah dimulai")

    # Inisialisasi repository dan service
    limbah_repository = InMemoryLimbahRepository()
    limbah_service = LimbahService(limbah_repository)
    pengangkutan_service = PengangkutanService(limbah_repository)
    logger.info("Repository dan service berhasil diinisialisasi")

    # Loop utama menu
    while True:
        print("\n=== MENU MANAJEMEN LIMBAH ===")
        print("1. Tambah Limbah Organik")
        print("2. Tambah Limbah Medis")
        print("3. Tambah Limbah B3")
        print("4. Lihat Semua Limbah")
        print("5. Angkut Limbah")
        print("0. Keluar")

        pilihan = input("Pilih menu: ")

        try:
            # Tambah Limbah Organik
            if pilihan == "1":
                logger.info("User memilih menu: Tambah Limbah Organik")
                id_limbah = input("ID limbah: ")
                volume = float(input("Volume (kg): "))
                tingkat_pembusukan = int(input("Tingkat pembusukan: "))

                # Data lokasi (sebagai konteks)
                nama_lokasi = input("Nama lokasi: ")
                alamat = input("Alamat lokasi: ")
                jenis_bencana = input("Jenis bencana: ")
                lokasi = Lokasi(nama_lokasi, alamat, jenis_bencana)
                logger.info("Lokasi bencana: %s", lokasi)

                limbah_service.registrasi_limbah_organik(
                    id_limbah, volume, tingkat_pembusukan
                )

                print("Limbah organik berhasil ditambahkan.")
                logger.info("Limbah organik berhasil ditambahkan: %s", id_limbah)

            # Tambah Limbah Medis
            elif pilihan == "2":
                logger.info("User memilih menu: Tambah Limbah Medis")
                id_limbah = input("ID limbah: ")
                volume = float(input("Volume (kg): "))
                tingkat_infeksi = int(input("Tingkat infeksi: "))

                nama_lokasi = input("Nama lokasi: ")
                alamat = input("Alamat lokasi: ")
                jenis_bencana = input("Jenis bencana: ")
                lokasi = Lokasi(nama_lokasi, alamat, jenis_bencana)
                logger.info("Lokasi bencana: %s", lokasi)

                limbah_service.registrasi_limbah_medis(
                    id_limbah, volume, tingkat_infeksi
                )

                print("Limbah medis berhasil ditambahkan.")
                logger.info("Limbah medis berhasil ditambahkan: %s", id_limbah)

            # Tambah Limbah B3
            elif pilihan == "3":
                logger.info("User memilih menu: Tambah Limbah B3")
                id_limbah = input("ID limbah: ")
                volume = float(input("Volume (kg): "))
                kandungan_kimia = input("Kandungan kimia: ")

                nama_lokasi = input("Nama lokasi: ")
                alamat = input("Alamat lokasi: ")
                jenis_bencana = input("Jenis bencana: ")
                lokasi = Lokasi(nama_lokasi, alamat, jenis_bencana)
                logger.info("Lokasi bencana: %s", lokasi)

                limbah_service.registrasi_limbah_b3(
                    id_limbah, volume, kandungan_kimia
                )

                print("Limbah B3 berhasil ditambahkan.")
                logger.info("Limbah B3 berhasil ditambahkan: %s", id_limbah)

            # Lihat Semua Limbah
            elif pilihan == "4":
                logger.info("User memilih menu: Lihat Semua Limbah")
                semua_limbah = limbah_service.get_semua_limbah()
                if not semua_limbah:
                    print("Belum ada data limbah.")
                else:
                    print("\n--- DAFTAR LIMBAH ---")
                    for l in semua_limbah:
                        print(l)

            # Angkut Limbah
            elif pilihan == "5":
                logger.info("User memilih menu: Angkut Limbah")
                id_limbah = input("ID limbah yang akan diangkut: ")

                id_petugas = input("ID petugas: ")
                nama_petugas = input("Nama petugas: ")
                keahlian = input("Keahlian petugas: ")

                petugas = Petugas(id_petugas, nama_petugas, keahlian)
                logger.info("Petugas dibuat: %s", petugas)

                kendaraan = input("Nama/jenis kendaraan: ")
                tujuan = input("Tujuan pengangkutan: ")

                catatan = pengangkutan_service.angkut_limbah(
                    id_limbah=id_limbah,
                    kendaraan=kendaraan,
                    tujuan=tujuan
                )

                print("Pengangkutan berhasil.")
                logger.info("Pengangkutan limbah berhasil: %s", id_limbah)
                print("Petugas bertanggung jawab:")
                for k, v in petugas.get_info().items():
                    print(f"  {k}: {v}")

                print("Catatan pengangkutan:")
                for k, v in catatan.items():
                    print(f"  {k}: {v}")

            # Keluar Program
            elif pilihan == "0":
                print("Program dihentikan.")
                logger.info("Aplikasi dihentikan oleh user")
                break

            else:
                print("Pilihan tidak valid.")
                logger.warning("Pilihan menu tidak valid: %s", pilihan)

        except ValueError as e:
            print(f"Error input: {e}")
            logger.error("ValueError: %s", e)
        except LookupError as e:
            print(f"Error pencarian: {e}")
            logger.error("LookupError: %s", e)
        except Exception as e:
            print(f"Terjadi kesalahan tidak terduga: {e}")
            logger.exception("Exception tidak terduga: %s", e)


if __name__ == "__main__":
    """
    Entry point program.

    File akan dijalankan langsung sebagai program utama.
    """
    main()
