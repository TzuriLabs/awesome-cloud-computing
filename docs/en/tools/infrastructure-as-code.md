# Infrastructure as Code

> Infrastructure as Code (IaC) is the practice of managing and provisioning
> infrastructure through machine-readable configuration files rather than
> manual or interactive processes.

| Name | Description | Documentation | Tutorial |
|------|-------------|---------------|----------|
| **Ansible** | Open-source automation tool commonly used for configuration management and infrastructure automation. | [Docs](https://www.redhat.com/en/ansible-collaborative?intcmp=7015Y000003t7aWQAQ) | [Getting Started](https://docs.ansible.com/projects/ansible/latest/getting_started/index.html) |
| **AWS CDK** | Open-source framework for defining cloud infrastructure using programming languages and provisioning it through AWS CloudFormation. | [Docs](https://aws.amazon.com/cdk) | [CDK Workshop](https://cdkworkshop.com) |
| **Chef** | Open-source platform for configuration management and infrastructure automation. | [Docs](https://docs.chef.io) | [Chef Tutorials](https://www.chef.io/training/tutorials) |
| **Pulumi** | Infrastructure as Code platform that allows defining cloud resources using general-purpose programming languages. | [Docs](https://www.pulumi.com/docs) | [Getting Started](https://www.pulumi.com/docs/get-started) |
| **Terraform** | Tool for provisioning and managing infrastructure resources across cloud providers and data centers. | [Docs](https://developer.hashicorp.com/terraform/docs) | [Terraform Tutorials](https://developer.hashicorp.com/terraform/tutorials) |
| **OpenTofu** | Community-driven open-source fork of Terraform, compatible with existing Terraform configurations and providers. | [Docs](https://opentofu.org/docs) | |
| **Azure ARM / Bicep** | Native Azure Infrastructure as Code tools for defining and deploying Azure resources using declarative templates. | [Docs](https://learn.microsoft.com/en-us/azure/azure-resource-manager) | [Bicep Getting Started](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/learn-bicep) |
| **Google Cloud Deployment Manager** | Native Google Cloud Infrastructure as Code service for defining and deploying resources using declarative templates. | [Docs](https://docs.cloud.google.com/deployment-manager/docs) | [Getting Started](https://docs.cloud.google.com/deployment-manager/docs) |
| **AWS CloudFormation** | Native AWS Infrastructure as Code service for modeling and provisioning resources using declarative templates. | [Docs](https://docs.aws.amazon.com/cloudformation/) | [Getting Started](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/GettingStarted.html) |

---

## Tool Comparison

### Declarative vs Imperative

- **Declarative** - Define the desired end state (Terraform, Pulumi, AWS CDK, Azure ARM / Bicep, Google Cloud Deployment Manager)
- **Imperative** - Define the steps required to reach a state (Ansible, Chef)

### Language Support

- **HCL** - Terraform, OpenTofu
- **YAML** - Ansible
- **JSON / YAML** - AWS CloudFormation
- **YAML (config) / Python, Jinja2 (templates)** - Google Cloud Deployment Manager
- **Bicep / JSON** - Azure ARM, Bicep
- **Programming Languages** - Pulumi (Python, TypeScript, Go, C#), AWS CDK (TypeScript, Python, Java, C#)
- **Ruby** - Chef

### Cloud Provider Support

- **Multi-cloud** - Terraform, Pulumi, Ansible
- **AWS-focused** - AWS CDK, CloudFormation
- **Azure-focused** - Azure ARM, Bicep
- **Google-focused** - Google Cloud Deployment Manager
- **Provider-agnostic** - Chef, Ansible

---

*Have any suggestions, additions, best-practices or references? Please [contribute](../contributing.md) to help others learn!*

[:material-arrow-left: Tools & Software](index.md){ .md-button }
[:material-arrow-right: Multi-cloud Management](multi-cloud-management.md){ .md-button .md-button--primary }
