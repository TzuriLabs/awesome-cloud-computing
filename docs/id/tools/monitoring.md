# Pemantauan

> Alat dan praktik untuk mengamati sistem cloud dan cloud-native,
> termasuk metrik, log, dan jejak di lingkungan dinamis dan terdistribusi.

| Nama | Deskripsi | Tautan |
|------|-----------|--------|
| **Grafana** | Platform visualisasi dan analitik yang umum digunakan untuk dasbor pemantauan cloud-native. | [https://grafana.com](https://grafana.com) |
| **Prometheus** | Sistem pengumpulan metrik dan peringatan cloud-native yang dirancang untuk lingkungan dinamis. | [https://prometheus.io](https://prometheus.io) |
| **VictoriaMetrics** | Database deret waktu yang skalabel dan dioptimalkan untuk beban kerja pemantauan cloud bervolume tinggi. | [https://victoriametrics.com](https://victoriametrics.com) |

## Dasar-dasar Pemantauan Cloud

### Jenis Pemantauan

- **Pemantauan infrastruktur** - Sumber daya komputasi, jaringan, dan penyimpanan
- **Pemantauan aplikasi** - Aplikasi cloud-native dan terdistribusi
- **Pemantauan layanan** - Layanan terkelola dan API
- **Pemantauan keamanan** - Sinyal terkait postur keamanan cloud

## Komponen Stack Pemantauan

### Pengumpulan Data

- **Pengumpulan metrik** - Pengukuran numerik dari waktu ke waktu
- **Agregasi log** - Pengumpulan dan penyimpanan log terpusat
- **Pelacakan terdistribusi** - Aliran permintaan di seluruh layanan
- **Pemantauan sintetis** - Pengujian dan pemantauan proaktif

### Penyimpanan Data

- **Database deret waktu** - Dioptimalkan untuk data metrik
- **Penyimpanan log** - Solusi penyimpanan log yang skalabel
- **Retensi data** - Kebijakan untuk manajemen siklus hidup data
- **Kompresi data** - Pemanfaatan penyimpanan yang efisien

### Visualisasi dan Peringatan

- **Dasbor** - Representasi visual dari metrik
- **Sistem peringatan** - Notifikasi masalah secara proaktif
- **Pelaporan** - Laporan kinerja berkala
- **Deteksi anomali** - Identifikasi masalah otomatis

## Praktik Terbaik

### Strategi Metrik

- **Pilih metrik yang bermakna** - Fokus pada indikator yang relevan dengan bisnis
- **Hindari ledakan metrik** - Jangan memantau semua hal
- **Gunakan label dengan bijak** - Atur metrik dengan label yang sesuai
- **Siapkan SLI/SLO** - Definisikan indikator dan tujuan tingkat layanan

### Desain Dasbor

- **Dasbor berfokus pengguna** - Rancang untuk audiens tertentu
- **Struktur hierarkis** - Dari tampilan tingkat tinggi hingga tampilan terperinci
- **Gaya yang konsisten** - Gunakan warna dan tata letak yang konsisten
- **Optimasi kinerja** - Pastikan dasbor dimuat dengan cepat

### Strategi Peringatan

- **Beri peringatan pada gejala, bukan penyebab** - Fokus pada dampak pengguna
- **Kurangi kelelahan peringatan** - Minimalkan false positive
- **Prosedur eskalasi** - Jalur eskalasi yang jelas
- **Integrasi runbook** - Tautkan peringatan ke panduan pemecahan masalah

## Stack Pemantauan Populer

### Prometheus + Grafana

- **Prometheus** - Pengumpulan dan penyimpanan metrik
- **Grafana** - Visualisasi dan dasbor
- **Alertmanager** - Penanganan dan perutean peringatan
- **Exporters** - Pengumpulan metrik dari berbagai sumber

### Solusi Cloud-Native

- **AWS CloudWatch** - Pemantauan bawaan AWS
- **Azure Monitor** - Platform pemantauan Azure
- **Google Cloud Monitoring** - Solusi pemantauan GCP
- **Datadog** - Platform pemantauan SaaS

### ELK Stack

- **Elasticsearch** - Mesin pencarian dan analitik
- **Logstash** - Pipeline pemrosesan data
- **Kibana** - Visualisasi dan eksplorasi
- **Beats** - Pengirim data ringan

### TICK Stack

- **Telegraf** - Agen pengumpulan data
- **InfluxDB** - Database deret waktu
- **Chronograf** - Visualisasi dan dasbor
- **Kapacitor** - Pemrosesan data streaming real-time

---

*Punya saran, tambahan, praktik terbaik, atau referensi? Silakan [berkontribusi](../contributing.md) untuk membantu orang lain belajar!*

[:material-arrow-left: Edge Computing](edge-computing.md){ .md-button }
[:material-arrow-right: Logging](logging.md){ .md-button .md-button--primary }
