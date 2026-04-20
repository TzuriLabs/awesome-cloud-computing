# Manajemen Identitas & Akses (IAM)

> Alat dan layanan untuk mengelola identitas pengguna, izin akses, dan autentikasi di berbagai lingkungan cloud.

| Nama | Deskripsi | Tautan |
|------|-----------|--------|
| **AWS IAM** | Kelola akses ke layanan dan sumber daya AWS secara aman dengan izin yang mendetail. | [AWS IAM](https://aws.amazon.com/iam) |
| **Azure Entra ID** | Solusi identitas dan akses terpadu Microsoft, sebelumnya dikenal sebagai Azure Active Directory. | [Azure Entra ID](https://www.microsoft.com/en-us/security/business/identity-access/microsoft-entra-id) |
| **Google IAM** | Menyediakan kontrol akses yang mendetail dan visibilitas untuk sumber daya Google Cloud. | [Google IAM](https://docs.cloud.google.com/iam/docs) |

## Fundamental IAM

### Komponen Inti

- **Identitas** - Pengguna, grup, peran, dan akun layanan
- **Autentikasi** - Memverifikasi identitas (siapa Anda)
- **Otorisasi** - Memberikan izin (apa yang dapat Anda lakukan)
- **Kebijakan** - Aturan yang mendefinisikan izin
- **Sumber Daya** - Layanan cloud dan data yang dilindungi

### Jenis Identitas

- **Pengguna manusia** - Individu yang mengakses sumber daya
- **Akun layanan** - Aplikasi dan layanan
- **Grup** - Kumpulan pengguna dengan kebutuhan akses serupa
- **Peran** - Kumpulan izin yang dapat diasumsikan

### Pertimbangan Spesifik Cloud

- **Kredensial sementara** - Utamakan kredensial berumur pendek daripada kunci akses statis
- **Identitas layanan-ke-layanan** - Gunakan peran dan akun layanan daripada rahasia bersama
- **Identitas federasi** - Integrasikan penyedia identitas eksternal jika memungkinkan
- **Pencatatan audit** - Aktifkan log audit identitas dan akses secara default

## Praktik Terbaik IAM

### Prinsip Hak Akses Minimal

- **Izin minimal** - Berikan hanya akses yang diperlukan
- **Tinjauan berkala** - Audit izin secara periodik
- **Akses just-in-time** - Izin yang ditingkatkan secara sementara
- **Pemisahan tugas** - Bagi operasi kritis

### Autentikasi Kuat

- **Multi-factor authentication (MFA)** - Lapisan keamanan tambahan
- **Kata sandi kuat** - Kata sandi yang kompleks dan unik
- **Autentikasi tanpa kata sandi** - Biometrik, kunci perangkat keras
- **Single sign-on (SSO)** - Autentikasi terpusat

### Manajemen Akses

- **Role-based access control (RBAC)** - Izin berdasarkan peran
- **Attribute-based access control (ABAC)** - Izin yang sadar konteks
- **Akses kondisional** - Akses berdasarkan kondisi
- **Model zero trust** - Verifikasi setiap permintaan akses

---

*Punya saran, tambahan, praktik terbaik, atau referensi? Silakan [berkontribusi](../contributing.md) untuk membantu orang lain belajar!*

[:material-arrow-left: Keamanan](index.md){ .md-button }
[:material-arrow-right: Deteksi Ancaman](threat-detection.md){ .md-button .md-button--primary }
