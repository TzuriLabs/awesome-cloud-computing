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

#### Basic Concepts

- [AWS](https://aws.amazon.com/what-is-cloud-computing/?nc1=h_ls) - Basic definition, benefits and types of cloud computing from AWS (Amazon Web Service).
- [GCP](https://cloud.google.com/learn/what-is-cloud-computing?hl=en) - Basic definition, types, deployment models and use case from GCP (Google Cloud Platform).
- [Linux Foundation](https://training.linuxfoundation.org/blog/perspectives-in-cloud-computing/) - Perspectives In Cloud Computing.
- [NIST](https://nvlpubs.nist.gov/nistpubs/legacy/sp/nistspecialpublication800-145.pdf) - Basic definition and models of cloud computing from NIST (National Institute
of Standards and Technology).

#### Books

- [Cloud Native Patterns by Cornelia Davis.](https://www.manning.com/books/cloud-native-patterns)
- [The Cloud at Your Service: The When, How, and Why of Enterprise Cloud Computing.](https://www.amazon.com/Cloud-Your-Service-Enterprise-Computing/dp/1935182528)

#### Tutorials

##### Amazon Web Service

- [Getting Started with AWS.](https://aws.amazon.com/getting-started/)
- [Hands-on Tutorials](https://aws.amazon.com/getting-started/hands-on/?getting-started-all.sort-by=item.additionalFields.content-latest-publish-date&getting-started-all.sort-order=desc&awsf.getting-started-category=*all&awsf.getting-started-content-type=*all)

##### Azure

- [Getting started with Azure.](https://azure.microsoft.com/en-us/get-started)
- [Getting started with Azure App Service](https://learn.microsoft.com/en-us/azure/app-service/getting-started?pivots=stack-python)

##### DigitalOcean

- [Getting Started With DigitalOcean Cloud Computing.](https://www.digitalocean.com/community/tutorial-series/getting-started-with-cloud-computing)
- [DigitalOcean Community Tutorials](https://www.digitalocean.com/community/tutorials)

##### Google Cloud Platforms

- [Google Cloud quickstarts and tutorials.](https://cloud.google.com/docs/tutorials)
- [Get started with Google Cloud](https://cloud.google.com/docs/get-started)

#### Certifications

##### Free Certifications

- [AWS Educate](https://aws.amazon.com/education/awseducate/)
- [Google Cloud Skills Boost](https://www.cloudskillsboost.google/)

##### Paid Certifications

- [AWS Certifications](https://aws.amazon.com/certification/)
- [Google Cloud Certification](https://cloud.google.com/learn/certification?hl=en)
- [CompTIA Cloud+](https://www.comptia.org/certifications/cloud)

### Platforms

> Public, private or hybrid platforms. Open source or enterprise platforms.

- [AWS](https://aws.amazon.com/console/) - Cloud platform offering over 200 services for computing, storage, databases, machine learning, and more.
- [Azure](https://azure.microsoft.com/en-us) - Cloud computing platform providing a wide range of integrated services, particularly excelling in hybrid cloud solutions and seamless integration with Microsoft's ecosystem.
- [GCP](https://cloud.google.com/?hl=en) - Cloud platform offering over 200 services for computing, storage, databases, machine learning, and more.
- [DigitalOcean](https://www.digitalocean.com/) - Developer-friendly platform with simple tools and predictable pricing.
- [Vultr](https://www.vultr.com/) - Cloud computing platform offering SSD-powered hosting, bare metal servers, and globally distributed data centers focused on delivering simplicity and reliable performance.
- [OpenStack](https://www.openstack.org/) - An open-source cloud computing platform enabling organizations to create and manage their own private clouds, providing Infrastructure-as-a-Service through a set of interrelated services.

### Tools & Software

> Collections of tools or software to manage cloud infrastructure.

#### Infrastructure as Code

> IaC is the process of managing and provisioning infrastructure through machine-readable configuration files, rather than physical hardware or interactive configuration tools. It helps achieve consistency, scalability, and automation in cloud environments.

- [Ansible](https://www.ansible.com/) - An open-source automation tool for configuration management and application deployment, widely used for IaC.
- [AWS CDK](https://aws.amazon.com/cdk/) - Is an open-source software development framework for defining cloud infrastructure in code and provisioning it through [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).
- [Chef](https://www.chef.io/) - An open source systems management and cloud infrastructure. automation platform
- [Pulumi](https://www.pulumi.com/) - Is an infrastructure-as-code platform for full-stack developers and cloud engineers who are interested in using a general-purpose programming language for their cloud resources.
- [Terraform](https://www.terraform.io/) - IAC tool to provision and manage resources in any cloud or data center.

#### Containerization

> Is a technology that enables the packaging of applications and their dependencies into isolated containers, facilitating consistent deployment across different environments.

##### Container Engines

- [Docker](https://www.docker.com/) - Is a software platform that allows you to build, test, and deploy applications quickly using containers.
- [Podman](https://podman.io/) - A daemonless container engine for managing OCI containers, providing a Docker-compatible CLI.

##### Container Orchestration

- [Kubernetes](https://kubernetes.io/) - Is an open source system for automating deployment, scaling, and management of containerized applications.
- [OpenShift](https://www.openshift.com/) - A Kubernetes-based platform offering enterprise-grade security, monitoring, and tools.
- [Nomad](https://www.nomadproject.io/) - A simple, flexible workload orchestrator that supports containers and non-containerized applications.
- [Docker Swarm](https://docs.docker.com/engine/swarm/) -  Is an advanced feature for managing a cluster of Docker daemons.

##### Management Tools

- [Docker Compose](https://docs.docker.com/compose/) - A tool for defining and running multi-container Docker applications.
- [Helm](https://helm.sh/) - A package manager for Kubernetes to deploy pre-configured applications as charts.
- [Portainer](https://www.portainer.io/) - A container management software.
- [Rancher](https://rancher.com/) - A complete software stack for teams deploying containers, particularly Kubernetes clusters.

#### Monitoring

> Collections of tools or software used to monitor your cloud services.

- [Grafana](https://grafana.com/) - Is a multi-platform open source analytics and interactive visualization web application.
- [Prometheus](https://prometheus.io/) - Is an open-source systems monitoring and alerting toolkit.
- [VictoriaMetrics](https://victoriametrics.com/) - Is a fast, cost-saving, and scalable solution for monitoring and managing time series data by Nokia.

#### Logging

> Logging refers to the systematic recording of events and activities in a cloud environment to monitor performance, troubleshoot issues, and enhance security by providing a historical record of system behavior.

- [ELK](https://www.elastic.co/elastic-stack) - Is an acronym that stands for Elasticsearch, Logstash, and Kibana. Together, these three components provide a powerful, integrated solution for managing large volumes of data, offering real-time insights and a comprehensive analytics suite.
- [Fluentd](https://www.fluentd.org/) - is a cross-platform open-source data collection software project originally developed at Treasure Data.

### Best Practices

> Best Practices encompass established guidelines and strategies that help optimize cloud resource, enhance performance, and ensure security and compliance in cloud environments.

#### Cost Optimization

- [Cost Optimization with AWS](https://aws.amazon.com/aws-cost-management/cost-optimization/)
- [Cost Optimization with Google Cloud](https://cloud.google.com/architecture/framework/cost-optimization)
- [Optimizing OpenStack Cost](https://superuser.openinfra.dev/articles/7-best-practices-for-optimizing-openstack-costs/)

#### Scalability and Performance

- [AWS Auto Scaling](https://aws.amazon.com/autoscaling/)
- [Google Cloud Autoscaler](https://cloud.google.com/compute/docs/autoscaler)
- [OpenStack Autoscaling](https://docs.openstack.org/auto-scaling-sig/latest/theory-of-auto-scaling.html)

### Security

> Implementing measures and practices to protect cloud resources, data, and applications from threats, ensuring compliance with regulations, and safeguarding user privacy.

#### Identity & Access Management (IAM)

- [AWS IAM](https://aws.amazon.com/iam/)
- [Azure Entra ID](https://www.microsoft.com/en-us/security/business/identity-access/microsoft-entra-id)
- [Google IAM](https://cloud.google.com/security/products/iam)

#### Threat Detection

- [AWS GuardDuty](https://aws.amazon.com/guardduty/)
- [Google Cloud Security Command Center](https://cloud.google.com/security/products/security-command-center?hl=en)
- [OpenStack Threat Analysis](https://wiki.openstack.org/wiki/Security/Threat_Analysis)

#### Secret Management

- [AWS Secret Manager](https://aws.amazon.com/secrets-manager/)
- [Azure Key Vault](https://learn.microsoft.com/en-us/azure/key-vault/)
- [HashiCorp Vault](https://www.vaultproject.io/)

#### Compliance & Governance

- [AWS Artifact](https://aws.amazon.com/artifact/)
- [Azure Policy](https://learn.microsoft.com/en-us/azure/governance/policy/overview)
- [OpenStack Compliance](https://docs.openstack.org/security-guide/compliance.html)

### Community and Conferences

> Collections of communities or conferences, with focus on cloud computing.

#### Community

- [AWS Community BUilder](https://aws.amazon.com/developer/community/community-builders/) - Program offers technical resources, education, and networking opportunities to AWS technical enthusiasts and emerging thought leaders who are passionate about sharing knowledge and connecting with the technical community.
- [Google Cloud Community](https://cloud.google.com/communities) - Meet industry peers, ask questions, collaborate to find answers, and connect with Googlers who are making the products you use every day.
- [DevOps Exchange](https://www.devops-exchange.io/) - Global community that ignites the passion for DevOps.
- [OpenStack](https://www.openstack.org/community/) - The Community Team helps developers and users of OpenStack find information relevant for them. The group is made by staff of the OpenStack Foundation and volunteers around the world.

#### Conferences

- [AWS re:Invent](https://reinvent.awsevents.com/) - Is a learning conference hosted by AWS for the global cloud-computing community.
- [Microsoft Ignite](https://ignite.microsoft.com/en-US/home) - Is an annual conference for developers, IT professionals and partners, hosted by Microsoft.
- [OpenInfra](https://openinfra.dev/summit/) - a global collaboration of 110,000 people across 187 countries, builds and operates infrastructure powered by open source software (likes Linux, OpenStack, etc).

#### Emerging Trends

> As cloud computing continues to evolve, new trends are shaping the future of how businesses and organizations leverage cloud technologies. Here are some key trends to watch:

- [Serverless Computing](https://aws.amazon.com/serverless/) - Allows you to build and run applications and services without thinking about servers.
- [Multicloud Strategy](https://cloud.google.com/learn/what-is-multicloud?hl=en) - Multicloud is when an organization uses cloud computing services from at least two cloud providers to run their applications.
- [Edge Computing](https://aws.amazon.com/what-is/edge-computing/) - Is the process of bringing information storage and computing abilities closer to the devices that produce that information and the users who consume it.
- [Artificial Intelligence (AI) Integration](https://aws.amazon.com/ai/services/) - AI and machine learning are increasingly integrated into cloud services, allowing for smarter data analysis and automation of business processes.

## Contributing

Your contributions are always welcome! Please take a look at the [contribution guidelines](CONTRIBUTING.md) first.
