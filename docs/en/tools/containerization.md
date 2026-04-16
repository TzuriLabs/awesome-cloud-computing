# Containerization

> Containerization is a technology that enables packaging applications
> and their dependencies into isolated containers, allowing consistent
> deployment across different environments.

## Container Engines

> Tools responsible for building, running, and managing containers at the runtime level.
> These engines handle image execution, isolation, and container lifecycle.

| Name | Description | Link | Tutorial |
|------|-------------|------|----------|
| **Docker** | Platform for building, testing, and running applications using containers. | [Docker](https://www.docker.com) | [Docker Get Started](https://docs.docker.com/get-started) |
| **Podman** | Daemonless container engine for managing OCI containers with a Docker-compatible CLI. | [Podman](https://podman.io) | [Podman Getting Started](https://podman.io/get-started) |
| **containerd** | Industry-standard container runtime used by Docker, Kubernetes, and other systems. | [containerd](https://containerd.io) | [Getting started with containerd](https://github.com/containerd/containerd/blob/main/docs/getting-started.md) |
| **Kata Containers** | Open-source project combining lightweight virtual machines with container workflows for stronger isolation. | [Kata Containers](https://katacontainers.io) | [Kata Containers Docs](https://katacontainers.io/docs) |
| **Firecracker** | Lightweight microVM technology for running container and serverless workloads. | [Firecracker](https://firecracker-microvm.github.io) | [Firecracker Getting Started](https://github.com/firecracker-microvm/firecracker/blob/main/docs/getting-started.md) |

## Container Orchestration

> Platforms for scheduling, scaling, and managing containerized workloads
> across multiple hosts and environments.

| Name | Description | Link | Tutorial |
|------|-------------|------|----------|
| **Kubernetes** | Open-source system for automating deployment, scaling, and management of containerized applications. | [Kubernetes](https://kubernetes.io) | [Kubernetes Tutorials](https://kubernetes.io/docs/tutorials) |
| **OpenShift** | Kubernetes-based platform providing tools for deploying and managing containerized applications. | [OpenShift](https://www.redhat.com/en/technologies/cloud-computing/openshift) | [OpenShift Documentation](https://docs.redhat.com/en/documentation/openshift_container_platform) |
| **Nomad** | Flexible workload orchestrator supporting containerized and non-containerized workloads. | [Nomad](https://developer.hashicorp.com/nomad) | [Nomad Tutorials](https://developer.hashicorp.com/nomad/tutorials) |
| **Docker Swarm** | Native Docker clustering and orchestration solution. | [Docker Swarm](https://docs.docker.com/engine/swarm) | [Swarm Mode Overview](https://docs.docker.com/engine/swarm/key-concepts) |
| **AWS Fargate** | Serverless compute engine for running containers without managing servers. | [AWS Fargate](https://aws.amazon.com/fargate) | [Getting Started with Fargate](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html) |
| **AWS EKS** | Managed Kubernetes service on AWS. | [AWS EKS](https://aws.amazon.com/eks) | [EKS Workshop](https://www.eksworkshop.com) |
| **K3s** | Lightweight Kubernetes distribution for edge, IoT, and development use cases. | [K3s](https://docs.k3s.io) | [K3s Quick Start](https://docs.k3s.io/quick-start) |
| **MicroK8s** | Lightweight Kubernetes distribution designed for local development and edge environments. | [MicroK8s](https://canonical.com/microk8s) | [MicroK8s Tutorials](https://canonical.com/microk8s/docs/tutorials) |

## Management Tools

> Tools that simplify container operations through packaging, configuration,
> visualization, and cluster management.

| Name | Description | Link | Tutorial |
|------|-------------|------|----------|
| **Docker Compose** | Tool for defining and running multi-container Docker applications. | [Docker Compose](https://docs.docker.com/compose) | [Compose Get Started](https://docs.docker.com/compose/gettingstarted) |
| **Helm** | Package manager for Kubernetes applications. | [Helm](https://helm.sh) | [Helm Quickstart](https://helm.sh/docs/intro/quickstart) |
| **Portainer** | Web-based container management interface. | [Portainer](https://www.portainer.io) | [Portainer Docs](https://docs.portainer.io) |
| **Rancher** | Platform for managing Kubernetes clusters across environments. | [Rancher](https://www.rancher.com) | [Rancher Documentation](https://ranchermanager.docs.rancher.com) |

## Container Benefits

### Development

- **Consistency** - Same environment from development to production
- **Isolation** - Applications run independently
- **Portability** - Run across different platforms
- **Efficiency** - Lower overhead compared to virtual machines

### Operations

- **Scalability** - Supports horizontal scaling
- **Resource Utilization** - Improved hardware usage
- **Deployment Speed** - Fast startup and rollout
- **Rollback Capability** - Easier version rollback

---

*Have any suggestions, additions, best-practices or references? Please [contribute](../contributing.md) to help others learn!*

[:material-arrow-left: Multi-cloud Management](multi-cloud-management.md){ .md-button }
[:material-arrow-right: Serverless Frameworks](serverless-frameworks.md){ .md-button .md-button--primary }
