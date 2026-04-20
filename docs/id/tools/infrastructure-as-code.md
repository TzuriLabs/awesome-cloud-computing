# Infrastructure as Code

> Infrastructure as Code (IaC) adalah praktik mengelola dan menyediakan
> infrastruktur melalui file konfigurasi yang dapat dibaca mesin, bukan
> melalui proses manual atau interaktif.

| Nama | Deskripsi | Dokumentasi | Tutorial |
|------|-----------|-------------|----------|
| **Ansible** | Alat otomasi open-source yang umum digunakan untuk manajemen konfigurasi dan otomasi infrastruktur. | [Docs](https://www.redhat.com/en/ansible-collaborative?intcmp=7015Y000003t7aWQAQ) | [Getting Started](https://docs.ansible.com/projects/ansible/latest/getting_started/index.html) |
| **AWS CDK** | Kerangka kerja open-source untuk mendefinisikan infrastruktur cloud menggunakan bahasa pemrograman dan menyediakannya melalui AWS CloudFormation. | [Docs](https://aws.amazon.com/cdk) | [CDK Workshop](https://cdkworkshop.com) |
| **Chef** | Platform open-source untuk manajemen konfigurasi dan otomasi infrastruktur. | [Docs](https://docs.chef.io) | [Chef Tutorials](https://www.chef.io/training/tutorials) |
| **Pulumi** | Platform Infrastructure as Code yang memungkinkan pendefinisian sumber daya cloud menggunakan bahasa pemrograman umum. | [Docs](https://www.pulumi.com/docs) | [Getting Started](https://www.pulumi.com/docs/get-started) |
| **Terraform** | Alat untuk menyediakan dan mengelola sumber daya infrastruktur di seluruh penyedia cloud dan pusat data. | [Docs](https://developer.hashicorp.com/terraform/docs) | [Terraform Tutorials](https://developer.hashicorp.com/terraform/tutorials) |
| **OpenTofu** | Fork open-source Terraform yang digerakkan komunitas, kompatibel dengan konfigurasi dan penyedia Terraform yang ada. | [Docs](https://opentofu.org/docs) | |
| **Azure ARM / Bicep** | Alat Infrastructure as Code Azure bawaan untuk mendefinisikan dan mendeploy sumber daya Azure menggunakan template deklaratif. | [Docs](https://learn.microsoft.com/en-us/azure/azure-resource-manager) | [Bicep Getting Started](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/learn-bicep) |
| **Google Cloud Deployment Manager** | Layanan Infrastructure as Code Google Cloud bawaan untuk mendefinisikan dan mendeploy sumber daya menggunakan template deklaratif. | [Docs](https://docs.cloud.google.com/deployment-manager/docs) | [Getting Started](https://docs.cloud.google.com/deployment-manager/docs) |
| **AWS CloudFormation** | Layanan Infrastructure as Code AWS bawaan untuk memodelkan dan menyediakan sumber daya menggunakan template deklaratif. | [Docs](https://docs.aws.amazon.com/cloudformation/) | [Getting Started](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/GettingStarted.html) |

---

## Perbandingan Alat

### Deklaratif vs Imperatif

- **Deklaratif** - Mendefinisikan kondisi akhir yang diinginkan (Terraform, Pulumi, AWS CDK, Azure ARM / Bicep, Google Cloud Deployment Manager)
- **Imperatif** - Mendefinisikan langkah-langkah yang diperlukan untuk mencapai kondisi (Ansible, Chef)

### Dukungan Bahasa

- **HCL** - Terraform, OpenTofu
- **YAML** - Ansible
- **JSON / YAML** - AWS CloudFormation
- **YAML (config) / Python, Jinja2 (template)** - Google Cloud Deployment Manager
- **Bicep / JSON** - Azure ARM, Bicep
- **Bahasa Pemrograman** - Pulumi (Python, TypeScript, Go, C#), AWS CDK (TypeScript, Python, Java, C#)
- **Ruby** - Chef

### Dukungan Penyedia Cloud

- **Multi-cloud** - Terraform, Pulumi, Ansible
- **Berfokus AWS** - AWS CDK, CloudFormation
- **Berfokus Azure** - Azure ARM, Bicep
- **Berfokus Google** - Google Cloud Deployment Manager
- **Tidak terikat penyedia** - Chef, Ansible

---

*Punya saran, tambahan, praktik terbaik, atau referensi? Silakan [berkontribusi](../contributing.md) untuk membantu orang lain belajar!*

[:material-arrow-left: Alat & Perangkat Lunak](index.md){ .md-button }
[:material-arrow-right: Manajemen Multi-cloud](multi-cloud-management.md){ .md-button .md-button--primary }
