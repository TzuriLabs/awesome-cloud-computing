# Identity & Access Management (IAM)

> Tools and services for managing user identities, access permissions, and authentication across cloud environments.

| Name | Description | Link |
|------|-------------|------|
| **AWS IAM** | Manage access to AWS services and resources securely with fine-grained permissions. | [AWS IAM](https://aws.amazon.com/iam) |
| **Azure Entra ID** | Microsoft's unified identity and access solution, formerly known as Azure Active Directory. | [Azure Entra ID](https://www.microsoft.com/en-us/security/business/identity-access/microsoft-entra-id) |
| **Google IAM** | Provides fine-grained access control and visibility for Google Cloud resources. | [Google IAM](https://docs.cloud.google.com/iam/docs) |

## IAM Fundamentals

### Core Components

- **Identities** - Users, groups, roles, and service accounts
- **Authentication** - Verifying identity (who you are)
- **Authorization** - Granting permissions (what you can do)
- **Policies** - Rules that define permissions
- **Resources** - Cloud services and data being protected

### Identity Types

- **Human users** - Individual people accessing resources
- **Service accounts** - Applications and services
- **Groups** - Collections of users with similar access needs
- **Roles** - Sets of permissions that can be assumed

### Cloud-Specific Considerations

- **Ephemeral credentials** - Prefer short-lived credentials over static access keys
- **Service-to-service identity** - Use roles and service accounts instead of shared secrets
- **Federated identity** - Integrate external identity providers where possible
- **Audit logging** - Enable identity and access audit logs by default

## IAM Best Practices

### Principle of Least Privilege

- **Minimal permissions** - Grant only necessary access
- **Regular reviews** - Periodically audit permissions
- **Just-in-time access** - Temporary elevated permissions
- **Separation of duties** - Divide critical operations

### Strong Authentication

- **Multi-factor authentication (MFA)** - Additional security layer
- **Strong passwords** - Complex, unique passwords
- **Passwordless authentication** - Biometrics, hardware keys
- **Single sign-on (SSO)** - Centralized authentication

### Access Management

- **Role-based access control (RBAC)** - Permissions based on roles
- **Attribute-based access control (ABAC)** - Context-aware permissions
- **Conditional access** - Access based on conditions
- **Zero trust model** - Verify every access request

---

*Have any suggestions, additions, best-practices or references? Please [contribute](../contributing.md) to help others learn!*

[:material-arrow-left: Security](index.md){ .md-button }
[:material-arrow-right: Threat Detection](threat-detection.md){ .md-button .md-button--primary }
