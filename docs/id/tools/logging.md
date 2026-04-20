# Logging

> Logging mengacu pada pengumpulan, pemrosesan, dan analisis data log
> yang dihasilkan oleh sistem cloud dan cloud-native, memungkinkan pemecahan masalah,
> audit, dan visibilitas operasional di lingkungan terdistribusi.

| Nama | Deskripsi | Tautan |
|------|-----------|--------|
| **ELK Stack** | Adalah akronim yang merupakan singkatan dari Elasticsearch, Logstash, dan Kibana. Bersama-sama, ketiga komponen ini menyediakan solusi terintegrasi yang kuat untuk mengelola volume data besar, menawarkan wawasan real-time dan rangkaian analitik yang komprehensif. Stack logging terpusat dan analitik yang umum digunakan di lingkungan cloud dan terdistribusi. | [ELK](https://www.elastic.co/elastic-stack) |
| **Fluentd** | Adalah proyek perangkat lunak pengumpulan data open-source lintas platform yang awalnya dikembangkan di Treasure Data. Pengumpul dan forwarder log cloud-native yang dirancang untuk container dan infrastruktur dinamis. | [Fluentd](https://www.fluentd.org) |

## Dasar-dasar Logging

### Level Log

- **<span style="color:#6c757d;">DEBUG</span>** - Informasi terperinci untuk mendiagnosis masalah
- **<span style="color:#0d6efd;">INFO</span>** - Informasi umum tentang operasi sistem
- **<span style="color:#f0ad4e;">WARN</span>** - Pesan peringatan untuk situasi yang berpotensi berbahaya
- **<span style="color:#dc3545;">ERROR</span>** - Kejadian error yang mungkin masih memungkinkan aplikasi untuk terus berjalan
- **<span style="color:#7a1f1f;">FATAL</span>** - Kejadian error yang sangat parah yang mungkin menyebabkan aplikasi berhenti

### Jenis Log

- **Log aplikasi** - Log yang dihasilkan oleh aplikasi dan layanan cloud-native
- **Log sistem** - Kejadian tingkat sistem operasi dan runtime
- **Log keamanan** - Kejadian terkait autentikasi, otorisasi, dan keamanan
- **Log audit** - Pelacakan kepatuhan dan tata kelola
- **Log akses** - Catatan akses API gateway, load balancer, dan layanan

## Arsitektur Logging

### Pengumpulan Log

- **Agen log** - Mengumpulkan log dari berbagai sumber
- **Penerusan log** - Mengirim log ke sistem terpusat
- **Penguraian log** - Menstrukturkan data log yang tidak terstruktur
- **Pengayaan log** - Menambahkan konteks dan metadata

### Pemrosesan Log

- **Penyaringan** - Menghapus entri log yang tidak relevan
- **Transformasi** - Mengonversi format log
- **Agregasi** - Menggabungkan entri log terkait
- **Korelasi** - Menghubungkan kejadian terkait di seluruh sistem

### Penyimpanan Log

- **Penyimpanan terpusat** - Satu lokasi untuk semua log
- **Pengindeksan** - Memungkinkan pencarian log yang cepat
- **Kebijakan retensi** - Mengelola siklus hidup log
- **Kompresi** - Mengoptimalkan penggunaan penyimpanan

### Analisis Log

- **Pencarian dan kueri** - Menemukan entri log tertentu
- **Visualisasi** - Membuat grafik dan dasbor
- **Peringatan** - Memberi tahu pada pola log tertentu
- **Pelaporan** - Menghasilkan laporan log secara berkala

---

*Punya saran, tambahan, praktik terbaik, atau referensi? Silakan [berkontribusi](../contributing.md) untuk membantu orang lain belajar!*

[:material-arrow-left: Pemantauan](monitoring.md){ .md-button }
[:material-arrow-right: Praktik Terbaik](../best-practices/index.md){ .md-button .md-button--primary }
