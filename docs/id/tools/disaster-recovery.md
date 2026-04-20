# Pemulihan Bencana

> Solusi dan alat untuk pencadangan, pemulihan bencana, dan kelangsungan bisnis
> di lingkungan cloud dan hybrid.

| Nama | Deskripsi | Tautan |
|------|-----------|--------|
| **AWS Backup** | Layanan pencadangan terpusat untuk melindungi layanan AWS dan beban kerja hybrid yang didukung. | [AWS Backup](https://aws.amazon.com/backup) |
| **Azure Site Recovery** | Layanan pemulihan bencana untuk mereplikasi beban kerja antar wilayah atau lokasi. | [Azure Site Recovery](https://azure.microsoft.com/en-us/products/site-recovery) |
| **Google Cloud Backup and DR** | Layanan pencadangan dan pemulihan bencana terkelola untuk Google Cloud dan lingkungan hybrid. | [Backup and DR](https://cloud.google.com/backup-disaster-recovery) |
| **Veeam Backup & Replication** | Solusi pencadangan dan replikasi enterprise dengan dukungan cloud dan hybrid. | [Veeam](https://www.veeam.com/products/veeam-data-platform/backup-recovery.html) |
| **Commvault** | Platform perlindungan data enterprise untuk pencadangan, pemulihan, dan pemulihan bencana. | [Commvault](https://www.commvault.com) |
| **Rubrik** | Platform manajemen data cloud untuk kasus penggunaan pencadangan, pemulihan, dan pengarsipan. | [Rubrik](https://www.rubrik.com) |

## Komponen DR

### Tujuan Pemulihan

- **RTO (Recovery Time Objective)** - Waktu henti maksimal yang dapat diterima
- **RPO (Recovery Point Objective)** - Kehilangan data maksimal yang dapat diterima
- **RCO (Recovery Consistency Objective)** - Persyaratan konsistensi data setelah pemulihan
- **RLO (Recovery Level Objective)** - Granularitas dan cakupan pemulihan

### Pola DR

- **Backup and Restore** - Biaya terendah, waktu pemulihan tertinggi
- **Pilot Light** - Infrastruktur minimal yang tetap berjalan
- **Warm Standby** - Lingkungan yang diperkecil namun tetap fungsional
- **Hot Standby / Multi-Site** - Replika yang sepenuhnya aktif dengan waktu henti minimal

---

*Punya saran, tambahan, praktik terbaik, atau referensi? Silakan [berkontribusi](../contributing.md) untuk membantu orang lain belajar!*

[:material-arrow-left: Migrasi Cloud](cloud-migration.md){ .md-button }
[:material-arrow-right: FinOps & Manajemen Biaya](finops-cost-management.md){ .md-button .md-button--primary }
