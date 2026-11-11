# Module 10: Virtualization and Cloud Computing Security

> **Source Material:** Authentic CCT Study Notes & Slide Deconstructions (Pages 459 – 475)  
> **Author:** [@Dabuynyx](https://github.com/Dabuynyx)  
> **Related Hands-on Lab:** [lab-07-aws-cloud-kms-envelope-encryption.md](../../labs/lab-07-aws-cloud-kms-envelope-encryption.md)  
> **Quick Reference:** [cct-exam-quick-reference.md](../../cheatsheets/cct-exam-quick-reference.md)

---

## 🧭 My Complete Study Notes & Slide Walkthroughs

### Slide / Page 459

Chapter 10 
Virtualization and Cloud Computing 
 
10.1- Overview of Virtualization Essential Concepts and OS Virtualization Security 
 
Virtualization: A software-based virtual representation of an IT infrastructure that includes network, 
devices, applications, storage, etc 
 
- Virtual Architecture divides physical resources that are restricted to hardware into multiple individual 
simulated environments 
 
Virtualization Components 
 
01.  Hypervisor/ VM monitor: An application or firmware that enables multiple guest Os to share 
hardware resources 
 
02.  Guest Machine/ VM:  Standalone system of Os created by VM monitor  
 
03.  Host Machine/Physical Machine: Provides computing resources to support the VM 
 
04.  Management Server: Virtualization platform used to directly manage VMs


### Slide / Page 460

05.  Management Console: Interface used to access, configure, and manage the Virtualization 
product 
Virtualization Enablers 
 
- Software Defined Network (SDN): Separates network control from hardware 
 
- Network Virtualization (NV): Creates multiple virtual networks on the same physical hardware 
 
- Network Function Virtualization (NFV): Replaces network devices with software running on standard 
hardware 
 
Virtual Desktop Infrastructure: Allows users to access desktop environments on a central server that 
enables remote access and centralized management 
 
Container: OS that allows multiple isolated applications to run on the same host while sharing  
kernal (core of an OS that manages hardware resources and software)  
 
Container Engine: Manages an individual container 
 
Container Orchestration: Manages multiple containers as cohesive application.  
This includes Docker Swarm, OPENSHIFT, and Kubermetes 
 
Types of Containers:


### Slide / Page 461

- OS containers: An OS and runs multiple servers. Examples:  LXS, OpenVZ, LinuxVZ, BDS Jails, Solaris 
Zones 
- Application Containers: A single application that contains its dependencies and hardware requirement 
file. Examples: Docker, Rocket 
Docker: An open-source technology used for developing, packaging, and running applications in the form 
of containers for a seamless environment. It provides a Platform-as-a-Service (PaaS) through OS-level 
Virtualization and delivers software packages 
 
Microservices Vs. Docker 
  
Microservices: A monolithic application (All software system components are in one place) broken into a 
cloud-hosted sub-application. 
 
- Each microservice is packaged into a docker container along with its configurations and directories 
belonging to a single application that can develop and manage using multiple platforms 
 
Kubernetes: 
 
- Open-source, portable, extensible, orchestration platform developed by google for managing 
containerized applications and microservices 
 
- Provides a resilient framework for managing distributed containers, generating deployment patterns, 
and performing failover and redundancy for the application.


### Slide / Page 462

Docker Security Threats: 
Escaping: Gaining Root access to host server 
 
Cross-Container Attacks: Gaining access to a container and utilizing it to attack other containers that is 
same host and within the local network 
 
Examples: DDoS, malicious remote access, unpatched exploits 
 
Inter-Container Attacks: Gaining unauthorized access to a single container 
 
Docker Registry: Gaining access to dock registry 
 
Serverless Computing: Function-as-a-service (FaaS) is a cloud-based application architacure for application 
infrastructure and supporting services by cloud vendors. Eliminates the need for managing and hardware 
 
- Frameworks: Microsoft Azure Functions- allows to run code without provisioning and managing servers


### Slide / Page 464

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - PR INN EEE eS “NE Tee Peer he ee . een
> - Docker Security Tools
> - A script that enables checking:
> - Docker Bench
> - ; # Host Configuration
> - for Security ‘
> - =» Docker Daemon Configuration
> - HiTASS] 5.19 - Do not set nount propagat fon node to shared :
> - Bo not share the host’s UTS mnespace |
> - Bo not disable default secconp profile
> - Do nat docker exec commands uith privileged option
> - Bo not docker exec coanands uith user option
> - Confirn cgroup usage
> - Restrict container fron acquiring additional privileges
> - a Privileges not restricted: docker-nginx \
> - q .26 = Check container health at runtine
> - eae Health check not set: docker—nyinx
> - Sale oie aiate
> - ea
> - - Ensure docker connmands aluays get the latest version af the Inage \
> - | ; .28 — Use PIDs cgroup Linit
> - wR = PIDs linit not set: docker-nginx
> - 5.29 - Do not use Docker’s default bridge dockerO
> - » Container in dockerO netuork:
> - i 315.30 - Do not share tho host’s user parespaces
> - cP PASS) §.31 - Do not nount tho Docker socket inside any containers
> - Docker Security Operations
> - 6
> - 6.
> - 6.2 -~- Honitor Docker containers usage, performance and nactering
> - 6
> - 6 = fiwold inage spraul
> - # There are currently: 17 inagces
> - # Only 2 out of 1? are in use
> - 6.5 —- fivoid container spraul
> - « There ore currently a total of 2 containers, uith 1 of then currently running
> - Jlual len@ubuntu:7/docker-bench-security$ —
> - AERELE LG
> - https://gitbub.com
> - 1 - Perforn regular security audits of your host systen and containers |
> - 2
> - -3 — Backup container data
> - 4
> - Docker Daemon Configuration Files
> - Container Images and Build Files
> - Container Runtime
> - | Twistlock
> - https://github.com
> - am Aqua
> - https://vawve.aquasec.com
> - Anchore
> - https://anchore.com
> - Se NeuVector
> - wee https://neuvector.com
> - EJ CloudPassage Halo
> - https://veww, cloudpassage.com
> - Copyright © by Ee-fammell, AS) Rights Reserved. Reproduction Is Strictly Pro i:


### Slide / Page 465

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - oe
> - VM Escape Protection
> - SRV CE eet rh VA nt PRP HP EEN ard Bes API CET EAE PG hay Pane?
> - VM escape attack attempts can be minimized by placing VMs that offer web services and other services
> - (such as database services) on independent security zones with the corresponding physical hosts
> - Security Zone 1
> - : Protection against VM Escape Attacks
> - ay | =
> - es. Se )
> - sana Firewall | Web Host — © Frequently update or patch the VM
> - Services : a. software
> - rent Firewall
> - aed. p-
> - & Install only the required resources
> - — VM2
> - Fnswcall a el Minimize software installations because
> - ciienmmeai eae VRouter each program could have its own exploit:
> - Security Zone 2
> - Copyright © by EC-Cammell. All Rights Reserved. Reproduction is Strictly Prot


### Slide / Page 466

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - VM Sprawl] Avoidance
> - © VM sprawl occurs because of a lack of proper policy implementation for
> - provisioning/deprovisioning VMs, when leaving VMs idle for a long duration, or when the
> - administrator overlooks/fails to handle or control all the VMs in the network
> - VM Sprawl Avoidance Methods | | :
> - > Perform an audit | Mi Mi f i i Remove unnecessary backups
> - > Protect idle resources i i ma aes ie —} Clean up junk
> - » Identify the appropriate size for the VMs
> - a i “buia standards and processes
> - > Clear orphaned snapshots i
> - Ma i oh ti ie
> - ean an effective VM
> - _ Management tool f
> - > Archive the VMs a i | i i ae ae hy lel :
> - > Employ well-organized naming conventions


### Slide / Page 467

10.2- Overview of Cloud Computing Fundamentals 
Introduction to Cloud Computing: Delivery of various IT Capabilities over the internet without the need of 
physical hardware. 
 
Characteristics of Cloud Computing: 
- On-Demand self-service 
- Distributed storage 
- Rapid Elasticity 
- Broad Network Access 
- Resource Pooling 
- Virtualization Technology 
 
Types of Cloud Computing Services 
 
SYS Admins: Infrastructure-as-a-Service (IaaS): Virtualized computer resource (AWS, Google Cloud) 
 
Developers: Platform-as-a-Service (PaaS0): Offers platforms for development, configuration and 
management for applications (Google App Engine, Microsoft Azure)


### Slide / Page 468

End Customers:  
Software-as-a-Service (SaaS): offers software applications of the internet (Google Workspace, Salesforce) 
 
Identity-as-a-Service (IDaaS): manages user identity and access (Single Sign-On -SSO-, Multi-Factor 
Authentication -MFA-) 
 
Security-as-a-Service (SECaaS) 
 
Function-as-a-Service (FaaS): Provides developing, running, and managing functionalises for microservices 
(AWS Lambda, Google Cloud Functions). 
 
Anything-as-a-Service (XaaS): Provides a broad category of services over the internet based on the user’s 
demand like digital products, food transportation, medical consultations, etc… (Salesforce, AWS, Google 
Compute Engine, Azure,… ) 
 
Key Concept: 
When using cloud services, the responsibility for managing different layers of the technology stack is 
shared between the customer and the cloud service provider (CSP). This varies depending on the type of 
cloud service you're using (On-Premise, IaaS, PaaS, or SaaS). 
 
1. On-Premise:


### Slide / Page 469

• Customer Responsibility: The customer manages everything, from the physical servers and data 
storage to applications and data. 
• Complexity: You need to handle hardware, security, and software. 
 
2. Infrastructure as a Service (IaaS): 
• Customer Responsibility: Manages data, applications, operating systems, and virtual machines. 
• CSP Responsibility: Manages the underlying network, servers, storage, and physical data centers. 
• Simplified: You don’t need to worry about hardware or network management. You focus on your 
applications and data. 
 
3. Platform as a Service (PaaS): 
• Customer Responsibility: Only responsible for data and applications. 
• CSP Responsibility: Handles everything else, like middleware, operating systems, and infrastructure. 
• Simplified: You focus on building and deploying your apps, without worrying about the underlying 
platform. 
 
4. Software as a Service (SaaS): 
• Customer Responsibility: Only manages their data and how they interact with the software (e.g., user 
interfaces). 
• CSP Responsibility: Everything else is managed by the CSP, including applications, security, and 
infrastructure. 
• Simplified: This is the easiest—just use the software. Everything else is handled for you.


### Slide / Page 470

Simplified Chart: 
1. 
On-Premise: You manage everything. 
2. 
IaaS: You manage apps, OS, and data; CSP manages infrastructure. 
3. 
PaaS: You manage only the apps and data. 
4. 
SaaS: CSP manages everything, you just manage your data. 
 
Cloud Deployment Models 
Public Cloud: Open for public Source & Private Cloud: Single organization/ Private Use 
Community Cloud: Several Organizations from a specific cloud  
 
Hybrid Cloud: Combination of two or more clouds (private, community, or public) 
Multi-Cloud: Combines multiple workloads across multiple cloud vendors via a single proprietary interface. 
 
NIST Cloud Deployment Reference Architecture:  
Cloud Consumer: Use of Cloud Computing 
 
Cloud Provider 
Cloud Carrier: An intermediary for providing connectivity and transport service between consumers and 
providers 
 
Cloud Auditor: Responsible for reviewing and evaluating the use of cloud by organizations 
Cloud Broker: Manges cloud services use, performance, delivery, and maintains the relationship between 
providers and consumers.


### Slide / Page 471

Fog Computing (aka intelligent gateway): A distributed and independent digital environment that brings 
data processing, storage, and cloud services locally. 
 
è Acts as an intermediary between hardware and remote access  
 
è Used for enhanced data processing, storage, and quick analysis. 
 
Edge Computing: Distributed decentralized computing model. Helps in building automation systems that 
perform fast  processing and enables efficiency for real-time models.  
 
10.3- Understanding the insights of Cloud Security and Best Practices: 
 
Cloud Security- Shared Responsibility: 
 
01. “Cloud Security and Compliance of the cloud Provider and the Consumer” à shared responsibility 
 
02.  Security responsibilities are divided based on the shared responsibility model 
 
03.  If the consumer do not secure their function, then the entire cloud security model will fail


### Slide / Page 473

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Shared Responsibility Model for Security in the Cloud:
> - laaS PaaS SaaS
> - On-Premises (Infrastructure- (Platform-as- (Software-as-
> - Responsibility (for reference) as-a-Service) a-Service) a-Service)
> - User Access Customer Customer Customer Customer
> - Responsibility Responsibility Responsibility Responsibility
> - Data Customer Customer Customer Customer
> - Responsibility Responsibility Responsibility Responsibility
> - Applications Customer Customer Customer Cloud Provider
> - Responsibility Responsibility Responsibility Responsibility
> - Operating Customer Customer Cloud Provider Cloud Provider
> - System Responsibility Responsibility Responsibility Responsibility
> - Network Customer Cloud Provider Cloud Provider Cloud Provider
> - Traffic Responsibility Responsibility Responsibility Responsibility
> - Infrastructure Customer Cloud Provider Cloud Provider Cloud Provider
> - Responsibility Responsibility Responsibility Responsibility
> - Physical Customer Cloud Provider Cloud Provider Cloud Provider
> - Responsibility Responsibility Responsibility Responsibility


### Slide / Page 474

AWS Identity and Access Management: 
 
- IAM enables users to securely control the AWS service and resources. 
 
- AWS IAM allows to establish access rules and permissions for specific users and applications 
 
Security Assertion Language (SAML) 
 
- Popular open-source protocol used for authentication and authorization between both communicating 
parties 
 
- SaaS installed at the ISP and IdP to simply the federated authorization and authentication mechanisms 
for users 
 
Cloud Network Security: 
Virtual Private Cloud (VPC):  
 
- Secure and independent private cloud environment within the public cloud.  
 
- Clients can execute programs, save data, host applications, and perform anything using their individual 
accounts on their private network 
 
Public and Private Subnets:


### Slide / Page 475

- Can be both public and private. VM in the public subnet can transmit 
outbound traffic over web. Private Subnet can communicate via the internet 
using a NAT Gateway. 
Transit Gateways: Network routing that establishes and manages 
communication an on-premises consumer network and VPCs via a centralized 
unit 
 
VPC Endpoint: Private connection between a VPC and another cloud service without access to the internet, 
external gateways, NAT solutions, VPN connections, or public addresses 
 
Cloud Application Security: Set of protocols and techniques used to administer all data exchange between 
collaborative cloud platforms 
 
High Availability Across Zones: Available during intentional or unintentional network downtimes 
 
Cloud Access Security Broker (CASB): Responsible for enforcing security, compliance, and governance 
policies for the cloud applications. Placed between consumer and providers (services). Azure Security 
services include CASB Functionality 
 
Next-Generation Secure Web Gateway (NG SWG): Protects an organization’s network from cloud-based 
attack activities and allows clients to securely access cloud services. 
 
Module 10 lab: implement Key Management Services in AWS, Secure Amazon Web Services Storage



---

## 🛠️ Connecting Theory to Practice
- **Execute the Lab:** Open [`labs/lab-07-aws-cloud-kms-envelope-encryption.md`](../../labs/lab-07-aws-cloud-kms-envelope-encryption.md) to work through the practical workshop reinforcing this module.
- **Reference Card:** Check [`cheatsheets/cct-exam-quick-reference.md`](../../cheatsheets/cct-exam-quick-reference.md) for rapid command syntax, formulas, and port mappings.
