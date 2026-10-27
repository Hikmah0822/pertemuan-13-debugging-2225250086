# Pertemuan 13 - Debugging dan Testing

**Nama:** Hikmah Azizah  

**NIM:** 2225250086

**Kelas:** 3B

## Kasus

Praktik ini bertujuan untuk mengidentifikasi dan memperbaiki bug pada program Python yang menghitung rata-rata nilai, menentukan status kelulusan, dan mencari nilai tertinggi.

## Test Case

| ID | Input | Expected | Actual Awal | Status Retest |
|---|---|---|---|---|
| T1 | [80, 60, 90, 70] | 75.0 | 60.0 | PASS |
| T2 | [100, 80] | 90.0 | 36.0 | PASS |
| T3 | Status nilai 60 | Lulus | Tidak lulus | PASS |
| T4 | Status nilai 59 | Tidak lulus | Tidak lulus | PASS |
| T5 | [80, 60, 90, 70] | 90 | 0 | PASS |
| T6 | List kosong | 0 | Belum ditangani | PASS |

## Bug Report

**B01 - Bug rata-rata**

Akar penyebab: pembagi menggunakan angka tetap 5 sehingga hasil salah untuk list dengan jumlah data berbeda.

Perbaikan: mengganti pembagi dengan `len(nilai)` dan menambahkan penanganan list kosong.

**B02 - Bug status kelulusan**

Akar penyebab: penggunaan operator `>` menyebabkan nilai 60 tidak dinyatakan lulus.

Perbaikan: mengganti operator menjadi `>=`.

**B03 - Bug nilai tertinggi**

Akar penyebab: kondisi perbandingan terbalik dan nilai awal ditetapkan 0.

Perbaikan: menggunakan elemen pertama list sebagai nilai awal dan membandingkan dengan operator `>`.

## Retest

Seluruh enam test case dijalankan kembali setelah perbaikan. Hasilnya sesuai dengan nilai yang diharapkan.

## Cara Menjalankan

Jalankan perintah berikut di terminal dari folder utama:

`python praktik/praktik_4_debugging.py`

Jika menggunakan Python Launcher di Windows, gunakan `py praktik/praktik_4_debugging.py`.

## Refleksi

Teknik tracing dan test case membantu menemukan penyebab kesalahan secara bertahap. Debugger VS Code juga membantu melihat perubahan variabel sehingga perbaikan dapat dilakukan pada bagian kode yang tepat.