# Kerangka Kerja Serverless

> Kerangka kerja dan alat untuk membangun, mendeploy, dan mengelola aplikasi
> serverless di berbagai penyedia cloud.

| Nama | Deskripsi | Tautan |
|------|-----------|--------|
| **Serverless Framework** | Kerangka kerja untuk mendefinisikan dan mendeploy aplikasi serverless di beberapa penyedia cloud. | [Serverless Framework](https://www.serverless.com) |
| **AWS SAM** | AWS Serverless Application Model untuk mendefinisikan dan mendeploy aplikasi serverless di AWS. | [AWS SAM](https://aws.amazon.com/serverless/sam) |
| **Azure Functions Core Tools** | Alat baris perintah untuk mengembangkan dan menguji Azure Functions secara lokal. | [Azure Functions Core Tools](https://learn.microsoft.com/en-us/azure/azure-functions/functions-run-local) |
| **Google Cloud Functions Framework** | Kerangka kerja untuk menulis fungsi serverless portabel dalam beberapa bahasa. | [Functions Framework](https://docs.cloud.google.com/run/docs/local-dev-functions) |
| **Zappa** | Alat untuk mendeploy aplikasi web Python ke AWS Lambda dan API Gateway. | [Zappa](https://github.com/zappa/Zappa) |
| **Chalice** | Kerangka kerja Python untuk membuat dan mendeploy aplikasi serverless di AWS. | [Chalice](https://chalice.readthedocs.io/en/latest/) |

## Karakteristik Serverless

> Karakteristik umum komputasi serverless sebagaimana dijelaskan dalam
> praktik industri dan dokumentasi penyedia cloud.

### Model Biaya

- **Bayar per penggunaan** - Tagihan berdasarkan waktu eksekusi atau permintaan
- **Tidak ada sumber daya idle** - Tidak ada biaya saat fungsi tidak berjalan
- **Penskalaan otomatis** - Skala berdasarkan permintaan
- **Manajemen infrastruktur berkurang** - Tidak perlu provisi server

### Pengalaman Pengembangan

- **Berfokus pada aplikasi** - Kekhawatiran infrastruktur diabstraksikan
- **Iterasi cepat** - Siklus deployment dan umpan balik yang singkat
- **Berbasis event** - Cocok untuk beban kerja reaktif dan asinkron

### Pertimbangan Operasional

- **Ketersediaan ditangani oleh platform** - Redundansi bawaan
- **Pembaruan runtime terkelola** - Patch yang dikelola platform
- **Observabilitas terintegrasi** - Log dan metrik disediakan oleh platform
- **Eksekusi global** - Fungsi dapat berjalan di beberapa wilayah

## Perbandingan Kerangka Kerja

### Kerangka Kerja Multi-Cloud

- **Serverless Framework** - Mendukung beberapa penyedia cloud
- **Pulumi** - Infrastructure as Code dengan dukungan serverless
- **Terraform** - Provisi infrastruktur dengan sumber daya serverless

### Kerangka Kerja Spesifik Penyedia

- **AWS SAM** - Kerangka kerja serverless bawaan untuk AWS
- **Chalice** - Kerangka kerja Python berfokus AWS
- **AWS CDK** - Infrastructure as Code dengan konstruksi serverless

### Alat Berfokus Bahasa

- **Zappa** - Aplikasi web Python di AWS Lambda
- **Functions Framework** - Kerangka kerja serverless multi-bahasa untuk Google Cloud

---

*Punya saran, tambahan, praktik terbaik, atau referensi? Silakan [berkontribusi](../contributing.md) untuk membantu orang lain belajar!*

[:material-arrow-left: Kontainerisasi](containerization.md){ .md-button }
[:material-arrow-right: Migrasi Cloud](cloud-migration.md){ .md-button .md-button--primary }
