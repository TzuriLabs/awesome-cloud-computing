# Kontainerisasi

> Kontainerisasi adalah teknologi yang memungkinkan pengemasan aplikasi
> dan dependensinya ke dalam container yang terisolasi, memungkinkan deployment
> yang konsisten di berbagai lingkungan.

## Mesin Container

> Alat yang bertanggung jawab untuk membangun, menjalankan, dan mengelola container di level runtime.
> Mesin ini menangani eksekusi image, isolasi, dan siklus hidup container.

| Nama | Deskripsi | Tautan | Tutorial |
|------|-----------|--------|----------|
| **Docker** | Platform untuk membangun, menguji, dan menjalankan aplikasi menggunakan container. | [Docker](https://www.docker.com) | [Docker Get Started](https://docs.docker.com/get-started) |
| **Podman** | Mesin container tanpa daemon untuk mengelola container OCI dengan CLI yang kompatibel dengan Docker. | [Podman](https://podman.io) | [Podman Getting Started](https://podman.io/get-started) |
| **containerd** | Runtime container standar industri yang digunakan oleh Docker, Kubernetes, dan sistem lain. | [containerd](https://containerd.io) | [Getting started with containerd](https://github.com/containerd/containerd/blob/main/docs/getting-started.md) |
| **Kata Containers** | Proyek open-source yang menggabungkan mesin virtual ringan dengan alur kerja container untuk isolasi yang lebih kuat. | [Kata Containers](https://katacontainers.io) | [Kata Containers Docs](https://katacontainers.io/docs) |
| **Firecracker** | Teknologi microVM ringan untuk menjalankan beban kerja container dan serverless. | [Firecracker](https://firecracker-microvm.github.io) | [Firecracker Getting Started](https://github.com/firecracker-microvm/firecracker/blob/main/docs/getting-started.md) |

## Orkestrasi Container

> Platform untuk penjadwalan, scaling, dan mengelola beban kerja yang dikontainerisasi
> di berbagai host dan lingkungan.

| Nama | Deskripsi | Tautan | Tutorial |
|------|-----------|--------|----------|
| **Kubernetes** | Sistem open-source untuk mengotomatisasi deployment, scaling, dan manajemen aplikasi yang dikontainerisasi. | [Kubernetes](https://kubernetes.io) | [Kubernetes Tutorials](https://kubernetes.io/docs/tutorials) |
| **OpenShift** | Platform berbasis Kubernetes yang menyediakan alat untuk men-deploy dan mengelola aplikasi yang dikontainerisasi. | [OpenShift](https://www.redhat.com/en/technologies/cloud-computing/openshift) | [OpenShift Documentation](https://docs.redhat.com/en/documentation/openshift_container_platform) |
| **Nomad** | Orkestrator beban kerja fleksibel yang mendukung beban kerja yang dikontainerisasi dan non-kontainerisasi. | [Nomad](https://developer.hashicorp.com/nomad) | [Nomad Tutorials](https://developer.hashicorp.com/nomad/tutorials) |
| **Docker Swarm** | Solusi klastering dan orkestrasi Docker native. | [Docker Swarm](https://docs.docker.com/engine/swarm) | [Swarm Mode Overview](https://docs.docker.com/engine/swarm/key-concepts) |
| **AWS Fargate** | Mesin komputasi serverless untuk menjalankan container tanpa mengelola server. | [AWS Fargate](https://aws.amazon.com/fargate) | [Getting Started with Fargate](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html) |
| **AWS EKS** | Layanan Kubernetes terkelola di AWS. | [AWS EKS](https://aws.amazon.com/eks) | [EKS Workshop](https://www.eksworkshop.com) |
| **K3s** | Distribusi Kubernetes ringan untuk kasus penggunaan edge, IoT, dan pengembangan. | [K3s](https://docs.k3s.io) | [K3s Quick Start](https://docs.k3s.io/quick-start) |
| **MicroK8s** | Distribusi Kubernetes ringan yang dirancang untuk pengembangan lokal dan lingkungan edge. | [MicroK8s](https://canonical.com/microk8s) | [MicroK8s Tutorials](https://canonical.com/microk8s/docs/tutorials) |

## Alat Manajemen

> Alat yang menyederhanakan operasi container melalui pengemasan, konfigurasi,
> visualisasi, dan manajemen klaster.

| Nama | Deskripsi | Tautan | Tutorial |
|------|-----------|--------|----------|
| **Docker Compose** | Alat untuk mendefinisikan dan menjalankan aplikasi Docker multi-container. | [Docker Compose](https://docs.docker.com/compose) | [Compose Get Started](https://docs.docker.com/compose/gettingstarted) |
| **Helm** | Manajer paket untuk aplikasi Kubernetes. | [Helm](https://helm.sh) | [Helm Quickstart](https://helm.sh/docs/intro/quickstart) |
| **Portainer** | Antarmuka manajemen container berbasis web. | [Portainer](https://www.portainer.io) | [Portainer Docs](https://docs.portainer.io) |
| **Rancher** | Platform untuk mengelola klaster Kubernetes di berbagai lingkungan. | [Rancher](https://www.rancher.com) | [Rancher Documentation](https://ranchermanager.docs.rancher.com) |

## Manfaat Container

### Pengembangan

- **Konsistensi** - Lingkungan yang sama dari pengembangan ke produksi
- **Isolasi** - Aplikasi berjalan secara independen
- **Portabilitas** - Berjalan di berbagai platform
- **Efisiensi** - Overhead lebih rendah dibandingkan mesin virtual

### Operasi

- **Skalabilitas** - Mendukung horizontal scaling
- **Utilisasi Sumber Daya** - Penggunaan perangkat keras yang ditingkatkan
- **Kecepatan Deployment** - Startup dan rollout yang cepat
- **Kemampuan Rollback** - Rollback versi yang lebih mudah

---

*Punya saran, tambahan, praktik terbaik, atau referensi? Silakan [berkontribusi](../contributing.md) untuk membantu orang lain belajar!*

[:material-arrow-left: Manajemen Multi-cloud](multi-cloud-management.md){ .md-button }
[:material-arrow-right: Kerangka Kerja Serverless](serverless-frameworks.md){ .md-button .md-button--primary }
