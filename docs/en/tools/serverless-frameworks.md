# Serverless Frameworks

> Frameworks and tools for building, deploying, and managing serverless
> applications across different cloud providers.

| Name | Description | Link |
|------|-------------|------|
| **Serverless Framework** | Framework for defining and deploying serverless applications across multiple cloud providers. | [Serverless Framework](https://www.serverless.com) |
| **AWS SAM** | AWS Serverless Application Model for defining and deploying serverless applications on AWS. | [AWS SAM](https://aws.amazon.com/serverless/sam) |
| **Azure Functions Core Tools** | Command-line tools for developing and testing Azure Functions locally. | [Azure Functions Core Tools](https://learn.microsoft.com/en-us/azure/azure-functions/functions-run-local) |
| **Google Cloud Functions Framework** | Framework for writing portable serverless functions in multiple languages. | [Functions Framework](https://docs.cloud.google.com/run/docs/local-dev-functions) |
| **Zappa** | Tool for deploying Python web applications to AWS Lambda and API Gateway. | [Zappa](https://github.com/zappa/Zappa) |
| **Chalice** | Python framework for creating and deploying serverless applications on AWS. | [Chalice](https://chalice.readthedocs.io/en/latest/) |

## Serverless Characteristics

> Common characteristics of serverless computing as described in
> industry practice and cloud provider documentation.

### Cost Model

- **Pay-per-use** - Charges based on execution time or requests
- **No idle resources** - No cost when functions are not running
- **Automatic scaling** - Scale based on demand
- **Reduced infrastructure management** - No server provisioning

### Development Experience

- **Application-focused** - Infrastructure concerns are abstracted
- **Fast iteration** - Short deployment and feedback cycles
- **Event-driven** - Well-suited for reactive and asynchronous workloads

### Operational Considerations

- **Availability handled by platform** - Built-in redundancy
- **Managed runtime updates** - Platform-managed patches
- **Integrated observability** - Logs and metrics provided by the platform
- **Global execution** - Functions can run in multiple regions

## Framework Comparison

### Multi-Cloud Frameworks

- **Serverless Framework** - Supports multiple cloud providers
- **Pulumi** - Infrastructure as Code with serverless support
- **Terraform** - Infrastructure provisioning with serverless resources

### Provider-Specific Frameworks

- **AWS SAM** - Native serverless framework for AWS
- **Chalice** - AWS-focused Python framework
- **AWS CDK** - Infrastructure as Code with serverless constructs

### Language-Focused Tools

- **Zappa** - Python web applications on AWS Lambda
- **Functions Framework** - Multi-language serverless framework for Google Cloud

---

*Have any suggestions, additions, best-practices or references? Please [contribute](../contributing.md) to help others learn!*

[:material-arrow-left: Containerization](containerization.md){ .md-button }
[:material-arrow-right: Cloud Migration](cloud-migration.md){ .md-button .md-button--primary }
