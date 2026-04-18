# Edge Computing

> Platform dan alat untuk mendeploy dan mengelola aplikasi lebih dekat
> ke pengguna akhir dan sumber data, sering di luar wilayah cloud terpusat.

| Nama | Deskripsi | Tautan |
|------|-----------|--------|
| **AWS Wavelength** | Layanan edge computing 5G yang membawa infrastruktur AWS ke jaringan telekomunikasi. | [AWS Wavelength](https://aws.amazon.com/wavelength) |
| **AWS Local Zones** | Deployment infrastruktur AWS yang ditempatkan lebih dekat ke pusat populasi. | [AWS Local Zones](https://aws.amazon.com/about-aws/global-infrastructure/localzones) |
| **Azure Edge Zones** | Layanan infrastruktur Azure yang dideploy lebih dekat ke pengguna akhir dan perangkat. | [Azure Edge Zones](https://learn.microsoft.com/en-us/azure/extended-zones/overview) |
| **Google Distributed Cloud Edge** | Infrastruktur Google Cloud yang dideploy di lokasi pelanggan atau edge. | [Distributed Cloud Edge](https://cloud.google.com/distributed-cloud/edge) |
| **AWS IoT Greengrass** | Layanan untuk menjalankan komputasi lokal, pesan, dan manajemen data pada perangkat IoT. | [AWS IoT Greengrass](https://aws.amazon.com/greengrass) |
| **Azure IoT Edge** | Platform untuk mendeploy beban kerja terkontainerisasi ke perangkat edge IoT. | [Azure IoT Edge](https://azure.microsoft.com/en-us/products/iot-edge) |
| **K3s** | Distribusi Kubernetes ringan yang dirancang untuk lingkungan edge dan sumber daya terbatas. | [K3s](https://k3s.io) |
| **OpenYurt** | Kerangka kerja edge computing berbasis Kubernetes yang memperluas pola cloud-native ke edge. | [OpenYurt](https://openyurt.io) |

## Pertimbangan Edge Computing

### Performa

- **Latensi berkurang** - Memproses data lebih dekat ke tempat data dibuat
- **Waktu respons lebih baik** - Interaksi aplikasi yang lebih cepat
- **Pemrosesan real-time** - Dukungan untuk beban kerja yang sensitif terhadap waktu
- **Optimasi bandwidth** - Meminimalkan transfer data ke cloud terpusat

### Keandalan

- **Toleransi offline** - Operasi berlanjut saat koneksi terputus
- **Eksekusi terdistribusi** - Ketergantungan berkurang pada sistem terpusat
- **Redundansi lokal** - Beberapa node edge untuk ketersediaan

### Pertimbangan Biaya

- **Transfer data berkurang** - Penggunaan bandwidth lebih rendah
- **Penggunaan cloud selektif** - Memindahkan pemrosesan dari wilayah pusat
- **Penskalaan efisien** - Skalakan komputasi lebih dekat ke permintaan

---

*Punya saran, tambahan, praktik terbaik, atau referensi? Silakan [berkontribusi](../contributing.md) untuk membantu orang lain belajar!*

[:material-arrow-left: FinOps & Manajemen Biaya](finops-cost-management.md){ .md-button }
[:material-arrow-right: Pemantauan](monitoring.md){ .md-button .md-button--primary }
