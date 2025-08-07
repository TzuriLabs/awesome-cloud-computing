# Awesome Cloud Computing [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of concepts, cloud platforms, tools, practices and resources to learn, improve cloud computing knowledge.

## Content

- [Learning Resources](#learning-resources)
    - [Basic Concepts](#basic-concepts)
    - [Books](#books)
    - [Tutorials](#tutorials)
    - [Certifications](#certifications)
- [Platforms](#platforms)
- [Tools and Software](#tools--software)
    - [Infrastructure as Code](#infrastructure-as-code)
    - [Containerization](#containerization)
        - [Container Engines](#container-engines)
        - [Orchestration](#orchestration)
        - [Management Tools](#management-tools)
    - [Monitoring](#monitoring)
    - [Logging](#logging)
- [Best Practices](#best-practices)
    - [Cost Optimazation](#cost-optimazion)
    - [Scalability and Performances](#scalability-and-performances)
- [Security](#security)
    - [Identity & Access Management (IAM)](#identity--access-management-iam)
    - [Threat Detection](#threat-detection)
    - [Secret Management](#secret-management)
    - [Compliance & Governance](#compliance--governance)
- [Community and Conferences](#community-and-conferences)
    - [Community](#community)
    - [Conferences](#conferences)
- [Emerging Trends](#emerging-trends)
- [Contributing](#contributing)

### Learning Resources

> Collections of learning resources such as basic concepts of cloud computing, books, tutorials, and certifications.

#### > Basic Concepts

| Source | Description| Link |
|----------|------------|------|
| Amazon Web Service    | Basic definition, benefits and types of cloud computing from AWS (Amazon Web Service). | [What is cloud computing?](https://aws.amazon.com/what-is-cloud-computing/?nc1=h_ls)|
| Google Cloud Platform | Basic definition, types, deployment models and use case from GCP (Google Cloud Platform). | [What is cloud computing?](https://cloud.google.com/learn/what-is-cloud-computing?hl=en)|
| Linux Foundation | Perspectives In Cloud Computing. | [Perspectives In Cloud Computing](https://training.linuxfoundation.org/blog/perspectives-in-cloud-computing/) |
| National Institute of Standards and Technology | Basic definition and models of cloud computing from NIST (National Institute of Standards and Technology). | [The NIST Definition of Cloud Computing](https://nvlpubs.nist.gov/nistpubs/legacy/sp/nistspecialpublication800-145.pdf) |

#### > Books

| Name | Description | Author |
|------|-------------|--------|
| Cloud Native Patterns: Designing Change-tolerant Software | Cloud Native Patternsis your guide to developing strong applications that thrive in the dynamic, distributed, virtual world of the cloud. This book presents a mental model for cloud-native applications, along with the patterns, practices, and tooling that set them apart. | Cornelia Davis |
| The Cloud at Your Service: The When, How, and Why of Enterprise Cloud Computing | Cloud Computing is here to stay. As an economically viable way for businesses of all sizes to distribute computing, this technology shows tremendous promise. But the intense hype surrounding the Cloud is making it next to impossible for responsible IT managers and businessdecision-makers to get a clear understanding of what the Cloud really means, what it might do for them, when it is practical, and what their future with the Cloud looks like. | Jothy Rosenberg and  Arthur Mateos |

#### > Tutorials

##### Amazon Web Service

| Name | Description | Link |
|------|-------------|------|
| Getting Started with AWS. | Learn the fundamentals and start building on Amazon Web Services | [Getting Started with AWS](https://aws.amazon.com/getting-started)|
| Hands-on Tutorials | Get started with step-by-step tutorials to launch your first application. | [Hands-on Tutorials](https://aws.amazon.com/getting-started/hands-on/?getting-started-all.sort-by=item.additionalFields.content-latest-publish-date&getting-started-all.sort-order=desc&awsf.getting-started-category=*all&awsf.getting-started-content-type=*all) |

##### Azure

| Name | Description | Link |
|------|-------------|------|
| Get started with Azure. | Get started with the Azure Quickstart Center. | [Azure Portal Quickstart Center](https://learn.microsoft.com/en-us/azure/azure-portal/azure-portal-quickstart-center) |
| Getting started with Azure App Service. | *Azure App Service* enables you to build and host web apps, mobile back ends, and RESTful APIs in the programming language of your choice without managing infrastructure. | [Azure App Service](https://learn.microsoft.com/en-us/azure/app-service) |

##### DigitalOcean

| Name | Description | Link |
|------|-------------|------|
| Getting Started With Cloud Computing Series. | This curriculum introduces open-source cloud computing to a general audience along with the skills necessary to deploy applications and websites securely to the cloud. | [Getting Started With Cloud Computing](https://www.digitalocean.com/community/tutorial-series/getting-started-with-cloud-computing) |
| DigitalOcean Community Tutorials | Tutorial Series page on DigitalOcean’s community platform. It features a collection of in-depth, multi-part guides covering various topics related to cloud computing, software development, system administration, DevOps, and other tech-related fields. Each series is designed to help users build practical skills step by step. | [Digital Ocean Tutorial Series](https://www.digitalocean.com/community/tags/tutorial-series) |

##### Google Cloud Platforms

| Name | Description | Link |
|------|-------------|------|
| Google Cloud quickstarts and tutorials. | Tutorials section of Google Cloud's documentation. It provides a wide range of step-by-step guides and tutorials covering different Google Cloud services and solutions, such as machine learning, data analytics, cloud infrastructure, Kubernetes, and serverless computing. | [Google Cloud quickstarts and tutorials](https://cloud.google.com/docs/tutorials) |
| Get started with Google Cloud | Get hands-on experience with free usage of 20+ products, including popular products like AI APIs, Compute Engine, BigQuery, and more. | [Get started with Google Cloud](https://cloud.google.com/docs/get-started) |

#### > Certifications

##### Free Certifications

| Name | Description | Link |
|------|-------------|------|
| AWS Educate | AWS Educate is a free global program by Amazon that provides students and educators with resources, training, and tools to learn and build skills in cloud computing.| [AWS Educate](https://aws.amazon.com/education/awseducate) |
| Google Cloud Skills Boost | Google Cloud Skills Boost is a learning platform offering hands-on labs, courses, and certifications to help individuals build expertise in Google Cloud technologies. | [Google Cloud Skills Boost](https://www.cloudskillsboost.google) |

##### Paid Certifications

| Name | Description | Link |
|------|-------------|------|
| AWS Certifications | AWS Certifications validate expertise in Amazon Web Services, offering globally recognized credentials across various roles like cloud practitioner, architect, developer, and operations.| [AWS Certifications](https://aws.amazon.com/certification) |
| Google Cloud Certification | Google Cloud Certification validates expertise in Google Cloud technologies, offering globally recognized credentials for roles like cloud engineer, architect, data engineer, and more. | [GCP Certification](https://cloud.google.com/learn/certification?hl=en)|
| CompTIA Cloud+ | CompTIA Cloud+ is a vendor-neutral certification that validates the skills needed to deploy, secure, and optimize cloud infrastructure services in multi-cloud environments. | [CompTIA Cloud+](https://www.comptia.org/certifications/cloud)|

### Platforms

> List of public, private or hybrid cloud computing platforms. Open source or enterprise platforms.

| Name | Description | Link |
|------|-------------|------|
| Ansible | An open-source automation tool for configuration management and application deployment, widely used for IaC. | [Ansible](https://www.ansible.com/) |
| AWS CDK | Is an open-source software development framework for defining cloud infrastructure in code and provisioning it through [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html). | [AWS CDK](https://aws.amazon.com/cdk/) |
| Chef | An open source systems management and cloud infrastructure. automation platform | [Chef](https://www.chef.io/) |
| Pulumi | Is an infrastructure-as-code platform for full-stack developers and cloud engineers who are interested in using a general-purpose programming language for their cloud resources. | [Pulumi](https://www.pulumi.com/) |
| Terraform | IAC tool to provision and manage resources in any cloud or data center. | [Terraform](https://www.terraform.io/) |

### Tools & Software

> Collections of tools or software to manage cloud infrastructure.

#### > Infrastructure as Code

> IaC is the process of managing and provisioning infrastructure through machine-readable configuration files, rather than physical hardware or interactive configuration tools. It helps achieve consistency, scalability, and automation in cloud environments.

| Name | Description | Link |
|------|-------------|------|
| Ansible | An open-source automation tool for configuration management and application deployment, widely used for IaC. | https://www.ansible.com/ |
| AWS CDK | Is an open-source software development framework for defining cloud infrastructure in code and provisioning it through [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html). | https://aws.amazon.com/cdk/ |
| Chef | An open source systems management and cloud infrastructure. automation platform | https://www.chef.io/ |
| Pulumi | Is an infrastructure-as-code platform for full-stack developers and cloud engineers who are interested in using a general-purpose programming language for their cloud resources. | https://www.pulumi.com/ |
| Terraform | IAC tool to provision and manage resources in any cloud or data center. | https://www.terraform.io/ |

#### > Containerization

> Is a technology that enables the packaging of applications and their dependencies into isolated containers, facilitating consistent deployment across different environments.

##### Container Engines

| Name | Description | Link |
|------|-------------|------|
| Docker | Is a software platform that allows you to build, test, and deploy applications quickly using containers. | [Docker](https://www.docker.com/) |
| Podman | A daemonless container engine for managing OCI containers, providing a Docker-compatible CLI. | [Podman](https://podman.io/) |
| containerd | An industry-standard core container runtime used by Docker, Kubernetes, and other systems to manage container lifecycle. | [containerd](https://containerd.io/) |

##### Container Orchestration

| Name | Description | Link |
|------|-------------|------|
| Kubernetes | Is an open source system for automating deployment, scaling, and management of containerized applications. | [Kubernetes](https://kubernetes.io/) |
| OpenShift | A Kubernetes-based platform offering enterprise-grade security, monitoring, and tools. | [OpenShift](https://www.openshift.com/) |
| Nomad | A simple, flexible workload orchestrator that supports containers and non-containerized applications. | [Nomad](https://www.nomadproject.io/) |
| Docker Swarm | Is an advanced feature for managing a cluster of Docker daemons. | [Docker Swarm](https://docs.docker.com/engine/swarm/) |
| AWS Fargate | A serverless compute engine for containers that works with Amazon ECS and EKS, eliminating the need to manage servers. | [AWS Fargate](https://aws.amazon.com/fargate/) |

##### Management Tools

| Name | Description | Link |
|------|-------------|------|
| Docker Compose | A tool for defining and running multi-container Docker applications. | [Docker Compose](https://docs.docker.com/compose/) |
| Helm | A package manager for Kubernetes to deploy pre-configured applications as charts. | [Helm](https://helm.sh/) |
| Portainer | A container management software. | [Portainer](https://www.portainer.io/) |
| Rancher | A complete software stack for teams deploying containers, particularly Kubernetes clusters. | [Rancher](https://rancher.com/) |

#### > Monitoring

> Collections of tools or software used to monitor your cloud services.

| Name | Description | Link |
|:---|:---|:---|
| Grafana | Is a multi-platform open source analytics and interactive visualization web application. | [Grafana](https://grafana.com/) |
| Prometheus | Is an open-source systems monitoring and alerting toolkit. | [Prometheus](https://prometheus.io/) |
| VictoriaMetrics | Is a fast, cost-saving, and scalable solution for monitoring and managing time series data by Nokia. | [VictoriaMetrics](https://victoriametrics.com/) |

#### > Logging

> Logging refers to the systematic recording of events and activities in a cloud environment to monitor performance, troubleshoot issues, and enhance security by providing a historical record of system behavior.

| Name | Description | Link |
|------|-------------|------|
| ELK | Is an acronym that stands for Elasticsearch, Logstash, and Kibana. Together, these three components provide a powerful, integrated solution for managing large volumes of data, offering real-time insights and a comprehensive analytics suite. | [ELK](https://www.elastic.co/elastic-stack) |
| Fluentd | Is a cross-platform open-source data collection software project originally developed at Treasure Data. | [Fluentd](https://www.fluentd.org/) |

### Best Practices

> Best Practices encompass established guidelines and strategies that help optimize cloud resource, enhance performance, and ensure security and compliance in cloud environments.

#### > Cost Optimization

| Name | Description | Link |
|------|-------------|------|
| AWS Cost Optimization | Best practices for optimizing your AWS costs using AWS-native tools. | [Link](https://aws.amazon.com/aws-cost-management/cost-optimization/) |
| Google Cloud Cost Optimization | Ttips to optimize your Google Cloud spend. | [Link](https://cloud.google.com/architecture/framework/cost-optimization) |
| OpenStack Cost Optimization | Guide for optimizing OpenStack costs. | [Link](https://superuser.openinfra.dev/articles/7-best-practices-for-optimizing-openstack-costs/) |

#### > Scalability and Performance

| Name | Description | Link |
|------|-------------|------|
| AWS Auto Scaling | Automatically adjusts your Amazon EC2 capacity to maintain performance and control costs. | [AWS Auto Scaling](https://aws.amazon.com/autoscaling/) |
| Google Cloud Autoscaler | Dynamically resizes virtual machine instances to match demand in Google Cloud. | [Google Cloud Autoscaler](https://cloud.google.com/compute/docs/autoscaler) |
| OpenStack Autoscaling | Theory and implementation guide for auto-scaling in OpenStack environments. | [OpenStack Autoscaling](https://docs.openstack.org/auto-scaling-sig/latest/theory-of-auto-scaling.html) |

### Security

> Implementing measures and practices to protect cloud resources, data, and applications from threats, ensuring compliance with regulations, and safeguarding user privacy.

#### > Identity & Access Management (IAM)

| Name | Description | Link |
|------|-------------|------|
| AWS IAM | Manage access to AWS services and resources securely with fine-grained permissions. | [AWS IAM](https://aws.amazon.com/iam/) |
| Azure Entra ID | Microsoft’s unified identity and access solution, formerly known as Azure Active Directory. | [Azure Entra ID](https://www.microsoft.com/en-us/security/business/identity-access/microsoft-entra-id) |
| Google IAM | Provides fine-grained access control and visibility for Google Cloud resources. | [Google IAM](https://cloud.google.com/security/products/iam) |

#### > Threat Detection

| Name | Description | Link |
|------|-------------|------|
| AWS GuardDuty | Threat detection service that continuously monitors for malicious activity and unauthorized behavior. | [AWS GuardDuty](https://aws.amazon.com/guardduty/) |
| Azure Defender | Advanced threat protection for workloads in Azure, now part of Microsoft Defender for Cloud. | [Azure Defender](https://azure.microsoft.com/en-us/products/defender-for-cloud/) |
| Chronicle Security (Google) | Google Cloud’s threat detection and response platform. | [Chronicle Security](https://chronicle.security/) |

#### > Secret Management

| Name | Description | Link |
|------|-------------|------|
| AWS Secrets Manager | Securely stores and manages secrets such as API keys, database credentials, and tokens. | [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/) |
| AWS Systems Manager Parameter Store | Alternative to Secrets Manager, supports secure string parameters. | [Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html) |
| Azure Key Vault | Securely stores secrets, keys, and certificates for use by cloud apps and services. | [Azure Key Vault](https://learn.microsoft.com/en-us/azure/key-vault/general/overview) |
| Google Secret Manager | Securely stores API keys, passwords, certificates, and other sensitive data. | [Google Secret Manager](https://cloud.google.com/secret-manager) |

#### > Compliance & Governance

| Name | Description | Link |
|------|-------------|------|
| AWS Artifact | Provides access to AWS compliance reports and security/compliance documentation. | [AWS Artifact](https://aws.amazon.com/artifact/) |
| Azure Compliance Manager | Helps manage compliance activities and provides assessments and actionable insights. | [Azure Compliance](https://learn.microsoft.com/en-us/compliance/regulatory/) |
| Google Assured Workloads | Supports compliance requirements like FedRAMP, HIPAA, and CJIS in Google Cloud. | [Assured Workloads](https://cloud.google.com/assured-workloads) |

### Community and Conferences

> Collections of communities or conferences, with focus on cloud computing.

#### > Community

- [AWS Community BUilder](https://aws.amazon.com/developer/community/community-builders/) - Program offers technical resources, education, and networking opportunities to AWS technical enthusiasts and emerging thought leaders who are passionate about sharing knowledge and connecting with the technical community.
- [Google Cloud Community](https://cloud.google.com/communities) - Meet industry peers, ask questions, collaborate to find answers, and connect with Googlers who are making the products you use every day.
- [DevOps Exchange](https://www.devops-exchange.io/) - Global community that ignites the passion for DevOps.
- [OpenStack](https://www.openstack.org/community/) - The Community Team helps developers and users of OpenStack find information relevant for them. The group is made by staff of the OpenStack Foundation and volunteers around the world.

#### > Conferences

- [AWS re:Invent](https://reinvent.awsevents.com/) - Is a learning conference hosted by AWS for the global cloud-computing community.
- [Microsoft Ignite](https://ignite.microsoft.com/en-US/home) - Is an annual conference for developers, IT professionals and partners, hosted by Microsoft.
- [OpenInfra](https://openinfra.dev/summit/) - a global collaboration of 110,000 people across 187 countries, builds and operates infrastructure powered by open source software (likes Linux, OpenStack, etc).

#### > Emerging Trends

> As cloud computing continues to evolve, new trends are shaping the future of how businesses and organizations leverage cloud technologies. Here are some key trends to watch:

- [Serverless Computing](https://aws.amazon.com/serverless/) - Allows you to build and run applications and services without thinking about servers.
- [Multicloud Strategy](https://cloud.google.com/learn/what-is-multicloud?hl=en) - Multicloud is when an organization uses cloud computing services from at least two cloud providers to run their applications.
- [Edge Computing](https://aws.amazon.com/what-is/edge-computing/) - Is the process of bringing information storage and computing abilities closer to the devices that produce that information and the users who consume it.
- [Artificial Intelligence (AI) Integration](https://aws.amazon.com/ai/services/) - AI and machine learning are increasingly integrated into cloud services, allowing for smarter data analysis and automation of business processes.

## Contributing

Your contributions are always welcome! Please take a look at the [contribution guidelines](CONTRIBUTING.md) first.
