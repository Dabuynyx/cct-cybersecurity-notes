# Module 07: Network Security Controls - Technical Controls

> **Source Material:** Authentic CCT Study Notes & Slide Deconstructions (Pages 280 – 384)  
> **Author:** [@Dabuynyx](https://github.com/Dabuynyx)  
> **Related Hands-on Lab:** [lab-04-snort-nids-rule-crafting.md](../../labs/lab-04-snort-nids-rule-crafting.md)  
> **Quick Reference:** [cct-exam-quick-reference.md](../../cheatsheets/cct-exam-quick-reference.md)

---

## 🧭 My Complete Study Notes & Slide Walkthroughs

### Slide / Page 280

Module 7- Network Security Controls: Technical Controls 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
 
Remote Authentication Dial-in User Service (RADIUS): 
 
Clear text vs encrypted text: 
 
Clear text is easily parsed (analyzed) by any source of packing capturing utility if you can 
gain access to network traffic. RADIUS deals with authentication, authorization, and 
accounting (AAA) for remote access servers to communicate with a central server. 
 
Authentication in RADIUS: 
 
1. The client starts a connection by sending the access-request packet to the server 
 
2. Once the server receives the access request from the client, the server checks if the 
credentials of the client matches; if the credentials match it sends an access- accept 
message along with the access-challenge to the client for additional authentication.


### Slide / Page 281

3. Client sends the accounting-request to the server to specify the accounting 
information about user activity and system events and sends it to the RADIUS server 
for specified events. The accounting-request is connected to network access server 
(NAS) to provide information about user sessions.


### Slide / Page 282

Terminal Access Controller Access Control System Plus (TACACS+) 
 
TACACS+ is a network security protocol used for AAA of network devices through one or 
more centerlized servers 
 
TACACS+ encrypts the entire communication between the client and the server. The 
protection includes the user’s password which protects it from sniffing attacks. 
 
It is a client-server model approach where the client requests from the server, and the 
server authenticates the user by their credentials.


### Slide / Page 283

Kerberos 
Authentication method for access the network 
 
1. A user sends their credentials to an Authentication Server (AS) 
 
2. AS hashes the password of the user and verifies the credentials in the Active Directory 
Base (ADD). If the credentials matches then the AS sends TGS and generates a TGT to 
the user to create a session 
 
3. The TGT requests a server ticket for access the services 
 
4. TGS authenticates the TGT and grants a service ticket to the user. 
 
Challenge handshake involves challenge string and a response, the challenge string can be 
mathematically manipulated using the password hash. The hacker could eavesdrop and 
collect the challenge and the response then brute force until it matches the challenge 
response.


### Slide / Page 284

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Secure EBs
> - Email
> - Services
> - Secure SMTP (SMTPS)
> - ~ Astandard protocol that provides
> - entication ices for
> - messages sent from one email
> - server to another email server
> - over the transport layer
> - yr Itisnotan extension of SMTP; it
> - is used to convert insecure SMTP
> - communication to s
> - Secure POP POPSs) MN
> - iti iy
> - ET
> - | iH|
> - | H
> - af Wind ON
> - i "Secure IMAP CMAPS)
> - i | NN I Hil
> - Ht i i
> - th) \ Whit
> - WAT NNW HAHAH
> - ‘|i | AAO iH |
> - NN itll Hi AN ME
> - INNA
> - POP3S (POP 4 over Tis/ss rl ANNAN Ahh en imap i isia jt protocol
> - provides encrypl rand i ee
> - the email client and email |
> - server
> - it establishes TeBtonnectidgs
> - over the secufe port 995 by]
> - default
> - ih iil
> - MAN
> - iis to retrieve messages from
> - Ai Se mailbox, Similarlytag eens
> - email coritnianlestiee between Nil
> - mn IMAPS (IMAP ovigg TLS/SS})
> - uses. asecure channel to
> - incrypt the ll traffic in
> - transit
> - yr \tuses'the secure TP j
> - by default
> - Copyright © by EC-Gaimnnll, Adi Rights Reserved. Reproduction is Strictly Pi


### Slide / Page 285

SSL (Secure Sockets Layer)/ TLS (Transport Layer Security): 
 
An encryption-based internet security protocol developed by Netscape for the purpose of 
ensuring privacy, authentication, and data integrity in internet communications. 
 
Encryption-based internet security protocol, implements HTTPS in its URL 
 
Hypertext transfer protocol secure which is more secure than HTTP  
 
HTTPS encrypts communications using TLS; this protocol secures communications by using 
a asymmetric public key infrastructure. 
 
 
HTTP is broken into packets that can be sniffed using free software.


### Slide / Page 286

````````````````````````````````````````````````````````````````````````````````````````````````````````````````


### Slide / Page 287

Secure Shell protocol (SSH): 
 
Method for securely sending commands to a computer over an unsecured network. 
 
SSH uses cryptography to authenticate and encrypt connections between devices. SSH also 
enables tunnelling 
```````````````````````````````````````````````````````````````````````````````````````````````````````````````` 
IPsec: 
Group of networking protcols used for setting up secure encrypted connections, such as 
VPNs, across publicly shared networks


### Slide / Page 288

Pretty Good Privacy (PGP) 
 
PGP is an application layer protocol which provides cryptographic privacy and 
authentication communications. 
 
Authenticity comes from the private key as a signature 
 
Symmetric key: same key is used to encrypt and decrypt à if one side is compromised the 
other side is compromised 
 
Asymmetric: Public key and private key à Private key can only decrypt the public key


### Slide / Page 289

Secure/ Multipurpose Internet Mail Extensions (S/MIME) 
S/MIME is an ALP used for sending digitally signed and encrypted email messages. 
Certificate’s purpose was to bind a public key to an owner’s identity. Uses RSA system. 
Network defenders enable S/MIME-based security for mailboxes in their organization.


### Slide / Page 290

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - a
> - ee es  o waeee
> - caves RAuitiperpose Internet Mail Extensions
> - (S/IMIMIE) (Cont’d)
> - Alice | 7 Sete - _] © Bob
> - (a)
> - [mes ae a <Q ) Public Key
> - zk etl neal >($3) Alice
> - Message
> - . : Private Key
> - : 4 Alice
> - Vv Vv
> - : Digital 6) Signature
> - SE UNE «6<<cicnineldl(é‘C‘C ee CUBE aia mel ne |
> - : | a) Signing | Signature Checking < 3
> - 7 > 2) Encryption (DES) [rtttsttttttttttrttrts ae senerverererand > e— Decryption (DES) lS A
> - j Message | |
> - Vv Secret Key . - Secret Key
> - j 3) Encryption say J sonraasszeccesseeep>| ff BGOORR feet ssn cramrenne > | @ Decryption (RSA)
> - Publickey | (SO) <r Or nes aie Que’ Private Key
> - Bob ‘ : Bob


### Slide / Page 291

DNSSEC 
Domain name secure extensions (DNSSEC) used for securing certain types of information 
provided by DNS. 
 
DNSSEC enables DNS to have cryptographic verification for authenticity and integrity of DNS 
data by digitally siyning records for DNS lookup with the help of Public-Key. 
 
- Prevents cache poisoning where an attacker can redirect traffic to malicious sites by 
corrupting DNS data. 
 
DNSSEC does not provide confidentiality nor protects against DoS 
 
Working of DNSSEC 
 
DNSSEC works with the concept of asymmetric key; it adds digital signatures to 
authenticate DNS information; The digital signature must match the value on the file


### Slide / Page 292

Secure- HTTP 
 Encrpyts web communications carried over HTTP and secures data transmission of 
individual messages. SSL secures connection between two entities thus ensuring security of 
the entire communication. 
 
 
HTTPS 
Secures communication between two computers over HTTP; connection is encryted using 
TLS or SSL protocol. HHTPS is often used in confidential online transactions. Portects against 
MITMA since the data is transmitted over an encrypted channel.


### Slide / Page 293

Transport Layer Security (TLS): 
 Ensures a secure communication between client-server applications over the internet. 
Prevents the network communitcation from being eavesdropped or tampered. 
 
TLS handshake protocol 8ensures connection security with encryption and ensures server 
and client authentication. 
 
TLS record protocol ensures connection security with encryption


### Slide / Page 294

Secure Real-time Transport Protocol (SRTP) 
 
SRLTP is an advanced version of RLP. 
 
SRLTP provides encryption, confidentiality, integrity, authentication, and defense against 
replay attacks and DoS for RTP messages


### Slide / Page 295

SRTP and RTCP are secure versions of RTP and RTCP used for media transmission between 
connected devices. 
 
 
Lightweight Directory Access Protcol over SSL (LDAPS) 
 
LDAPS establishes a more secure connection using SSL/TLS, and ensures data packers being 
transferred between LDAP client and LDAP server are encrypted. 
 
Port 636 is encrypted, not 389. 
 
 
 
 
IPsec 
 
IPsec is developed by IETF for securing IP communications by authenticating and encrypting 
each IP packet of coummunication session


### Slide / Page 296

IPsec implements VPNs and for remote user access through dial-up connection to private 
networks. 
 
IPsec does not use Port numbers, instead it uses layer 3. Internet key exchange establishes 
the connection in UDP Port 500.


### Slide / Page 297

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Sd Dow - [CC Vodu'c O’ Ndecn fecurty Careniss Trcte 8 oO “99 Pose
> - Internet Protocol Security (IPsec) (Cont’d)
> - © Components of IPsec
> - © 1|Psec Driver
> - Benefits of IPsec
> - © Network-level peer
> - authentication
> - cA internet Key Exchange
> - (IKE) ) (<0)
> - OF iniicomet: Security
> - Association Key
> - Management Protocol
> - wh coictiiey ad
> - Did -
> - © |Psec Policy Agent
> - © Data origin authentication
> - © Data integrity
> - © Data confidentiality
> - (encryption)
> - © Replay protection


### Slide / Page 298

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Te? Module 07 Netaork Security Com Mog tenis Conte's ppt | - lowerPex
> - Internet Protocol Security (IPsec) (Cont’d)
> - Modes of IPsec
> - *?
> - teeaee
> - Transport — mode encapsulation
> - Transport data
> - (TCP, UDP, etc.)
> - ——————- enn
> - <—— encrypted ———>
> - 5. Network t : : Internet = S Network 2 :
> - dow 1 owt ows Hont > §
> - Re nweeeneneccuce ‘ Wa ewwececeecceset
> - Tunnel — mode encapsulation
> - —encwrypie —————>
> - <—— — ercrypted —  ->
> - IPsec Architecture
> - aretereees IPsec Architecture avereswes
> - AH  narrtecot | ESP rotost Protocol
> - “authentication . .
> - x Encryption Algorith
> - Algorithm "vP aida
> - Gree
> - aoe
> - IPsec Domain of
> - Interpretation (DO1)
> - Se Policy + >| Keymanage Key Management
> - )
> - Por
> - +>
> - Ul


### Slide / Page 299

IPsec Authentication and Confidentiality 
 
Authentication Header (AH): provides Authentication of the sender 
 
Encapsulation Security Payload (ESP):  
Provides both authentication and encryption (CONFIDENTAILITY) of the sender 
 
 
Secure File Transfer Protocol (SFTP) 
 
Secure version of FTP and an extension SSH2 protocol. Used for secure file transmission and 
file access over a reliable data stream. TCP port 22.


### Slide / Page 300

SNMPv3 
 
SNMPv3. Improved security for network management activites. Provides encryption, 
authenticationm and remote configuration of SNMP entities. 
 
User-based security model (USM) for authentication and encryption as well as a view-based 
access control model for defining access control policies


### Slide / Page 301

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - oo ide
> - j Data Confidentiality
> - 1 ah epee ge ee
> - Beeb nbeS ne icua ble e ee
> - Data (Ori gin
> - Authentication
> - Message Integrity
> - fe po oe be uN aman ge F val


### Slide / Page 302

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - SSH is another network management
> - protocol primarily used in Unix and
> - Linux environments
> - It is mainly used for secure remote login
> - It builds a secure, encrypted tunnel for
> - exchanging information between the
> - network management software and
> - devices
> - In SSH, administrators should provide a
> - combination of username, password,
> - and port number for authentication
> - Secure Shell (SSH)
> - SSH Authentication Mechanism
> - eA authentication: Authentication is performed based on the
> - user’s password
> - 2. Key-based authentication: SSH allows key-pair-based authentication
> - * The user needs to generate a public and a private key
> - " The keys are generated using ssh-keygen -t rsa or ssh-keygen -t dsa
> - = The private keys are used by the users the next time they attempt to
> - establish a connection
> - * The public key must be saved in ~/.ssh/authorized_keys
> - 3. Host-based authentication: If host-based authentication is enabled on
> - the target machine, then users on a trusted host can login to the
> - target machine using the same username. To enable this feature, the
> - setuid bit must be set on /usr/lib/ssh/ssh-keysign (32-bit systems)
> - or/usr/lib64/ssh/ssh-keysign (64-bit systems)
> - y 4


### Slide / Page 303

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - OAuth
> - QO OAuth is an authorization protocol that allows a user to grant limited access to their resources on
> - one site from another site, without having to expose their credentials
> - Q) OAuth does not transfer user credentials between applications; instead, it uses authorization tokens
> - to verify an identity between the client and server
> - Client H ) Resource
> - Application 34 Server
> - } Authorization and
> - } authentication
> - > Access
> - Auth, o--.
> - horizon. Sa
> - ode 7"
> - e
> - > server
> - Resource Authorization
> - Owner fit Server
> - fi I Grant Access


### Slide / Page 304

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - OpenID/Connect (OIDC)
> - alten babtbna ie +i scons
> - QO OIDCis an authentication
> - protocol that is built as a
> - thin layer on the OAuth 2.0 Resource provider
> - protocol :
> - Authorization server
> - i ‘ 4 : User authentication, authorization, and scope
> - QO It provides authentication
> - functions such as login,
> - profiling information, and
> - Resource Relying party/
> - end-user identity owner/user OIDC application URL
> - ape 4 ait
> - verification redirect>
> - User accesses
> - OQ It creates a secure ID token the application TiDERREE\ ~_AVRARILAG PRE REDLINE SUE estore
> - using JSON that contains
> - basic information such as
> - name, phone number, and ba
> - address User info request and response


### Slide / Page 305

UNDERSTANDING SECURITY BENEFITS OF NETWORK SEGMENATION 
 
 
Network Segmentation: Splitting up the network into small segments with separating 
groups of systems or applications from each other. 
 
In a segmented network groups of systems will have different sections such as a proxy 
server, email server, web server… etc…  
 
Security benefits of Network Segmentation: 
 
> Improved security 
 
> Better Access Control 
 
> Improved Monitoring 
 
> Improved Performance


### Slide / Page 306

> Better Containment 
 
 
Types of Network Segmentation 
 
Physical segmentation is a process of splitting the network into smaller physical 
components that could communicate via intermediary devices. Easy to divide but it is an 
expensive way. 
 
Logical segmentation creates VLANS that communicates as their own isolated network. 
In this approach firewalls are shared, and switches handle the VLAN infrastructure.  
 
Network Virtualization comines all networks to enable security professionals to share 
resources with other network users using a single admin unit. NV enables each user to 
access available network resources from their system.


### Slide / Page 307

Bastion Host 
 
01. A computer system designed and configured to protect network resources from 
attacks. 
 
02. A baston host is the only computer that can be addressesed directly from the public 
network 
 
03. Provies a limited range of services such as website hosting, and mail to ensure 
security 
 
Baston Host minimizes prenetrations by intruders, creates logs to identify attacks or 
attempts to attack, acts as a scapegoat, provides an additional level of security.


### Slide / Page 309

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Positioning the
> - Bastion Host
> - ‘suitable environmental controls
> - ntilation, cooling, and ae :
> - QO) Should be located on an additional layer
> - known as a perimeter network
> - CY Attach packet filtering router


### Slide / Page 310

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - TN WN\\ f i,
> - ip ANS, . A t |
> - oS
> - Bastion
> - "Hosts
> - gee Exterior
> - ; Firewall
> - Internet seanssvensnaesenneonnnenvenensnnaninn sya pegenanennhaned ian nngranneenense
> - : DMZ or Perimeter Network
> - a
> - eats Interior Firewall
> - Intranet
> - errrereeer eter terry


### Slide / Page 311

Types Of Bastion Hosts:  
 
Single-Homed:- 
 
One network interface – firewall device. All traffic is routed through the bastion host. Tests 
data against security guidelines and acts accordingly. 
 
 
Multi-Homed: 
 
Two network interfaces that seperates internal networks from external networks  
à this increases security 
 
   Internal Basition host: 
 
Resides inside the internal network of an organization. It can be both single/multi- homed. 
Communicates with the internal bastion host.


### Slide / Page 312

Network Segmentation Example: Demilitarized Zone (DMZ) 
 
A computer subnetwork is placed between the organization’s private network such as LAN 
and outside public network such as the internet to act as an additional security layer.


### Slide / Page 313

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Contains the servers that need to be accessed
> - joke an outside network
> - = Web servers
> - = ‘Email servers
> - . DNS servers
> - DMZ configurations
> - * Both internal and external networks can connect to the
> - DMZ hs
> - «Hosts in the DMZ can connect to external networks
> - 's But hosts in the pMz can not t connect to internal
> - networks :


### Slide / Page 314

Creating a DMZ 
 
WAY 01 
DMZ is included in three network interfaces. 
 
First network interface connects the ISP to the firewall that forms the external the network. 
The second interfaces forms the internal network. The third forms the DMZ. 
 
 
WAY 02 
 
Dual firewalls creating the DMZ, the first firewall only sanitizes traffic meaning that the 
segment filtrates and controls data flow between untrusted networks (For example the 
internet and the internal organization). Helps prevent unauthorized access and protects 
sensitive data by managing the flow of information between different network zones. 
 
The second firewall double checks.  
 
THE MOST SECURE APPROACH FOR DMZ


### Slide / Page 316

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - —
> - North-South
> - network traffic
> - <—
> - = =
> - aent I /I\ \
> - AOOO & Aooo &
> - External
> - Network
> - Internal Network
> - Data Center
> - network traffic


### Slide / Page 317

Zero Trust Networks 
 
ZNM model is a security implementation assumes that every user trying to access the 
network is not trusted and must undergo a verification for every incoming connection 
before access. 
 
 
Strictly follows the principle “TRUST NO ONE AND VERIFY”  
 
 
ZNM enforces strict access control and monitors the network traffic flow 
 
 
 
History: The Jericho Forum (2000s), Edward Snowden incident (NSA), Google’s 
BeyondCorp (2014-2015), Forrester's John Kindervag (2009, Standardized Cyber Rule).


### Slide / Page 318

LESSON 03 
Identifying different Types of Firewalls and their role:- 
 
What is a firewall? 
A firewall is a software/ hardware generally used to separate a protected network from an 
unprotected network. 
 
- Monitors and filters in and out traffic and prevents unauthorized access 
Hardware Firewalls: 
 
01. Form: Stand-alone hardware device or part of the router. 
 
02. Networkwork traffic ios filtered using packet filtering technique (predefined rules such 
as Destinations of IP addresses. Port numbers, protocol types, traffic direction, and 
TCP flags) 
 
03. Separates network traffic


### Slide / Page 319

Software Firewalls filters only for the installed device and not the entire network. 
 
Host-based firewalls: 
 
- Installed firwall that filters out inbound/outbound traffic of an individual computer 
 
- Software-based 
 
- Part of Os 
 
Network-based Firewalls: 
 
- Filters out traffic from internal LAN 
 
- Hardware-based 
 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
 
External Firewall:


### Slide / Page 320

à Limits the access between protected and public network 
à Provides AC and protection of DMZ systems. 
Internal Firewalls: 
 
à Protects a network segment from others in internal networks 
 
à Used for different types of access and specific services or information, and security 
 
à Sits between two network segments from the same organization or different 
 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
 
Packet Filtering firewall 
 
Layer 03 in the OSI mode à Network layer 
 
Packt filtering fire wall is usally part of a router. Each packet is compared to a set of rules 
before it is forwarded.


### Slide / Page 321

Circuit-Level Gateway 
 
Session layer of the OSI (layer 05) or the TCP layer. Circuit-level Gateway monitors TCP 
handshake between packets to determine whether a requested session is real.   
 
The information passed to a Remote computer through the CGL appears as if it came  
from the gateway itself, meaning the remote computer sees the gateway’s IP address as 
the source and it hides its original sender’s IP addressees. 
 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
Application Layer Gateways: 
 
Filters packets in Layer 07 in the OSI model. Filters application-specific commands such as 
http:post and get. Application layer gateways can be configured to be a web proxy which 
will not allow any FTP, gopher, Telnet, or other traffic through 
 
Gopher and Telnet are different protocls used for accessing information and remote 
systems over a network.


### Slide / Page 322

Gopher: Used to access and retrieve information organized in a hierarchical, menu-driven 
structure. 
 
Telnet: Used to establish a remote connection with another computer, allowing command-
line interface access as if you were physically present at the machine. 
 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
 
Stateful Multilayer Inspection Firewall is an advanced firewall that combines both stateful 
inspection (state of active traffic such as TCP)  and multilayer inspection to provide robust 
security. 
  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
 
Application Proxy 
 
- Filters connections for specific services based on services and protocols


### Slide / Page 323

Network Address Translation (NAT) 
 
NAT separates IP addresses into two sects and enables the LAN to use the IP for internal 
and external traffic 
 
- Works with the router and does packet filteing; Modifies the packets. 
 
- Changes addresses of the packet 
 
- Limits the number of public IPs 
 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
 
VPN 
 
- A private network used for the internet.


### Slide / Page 324

- Establishes a secure transmission using Encapsulation and Encryption 
 
- Dedicates connections 
 
- Specific for only the computer software of where it is running 
 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


### Slide / Page 325

Firewall Access Control Lists (ACLs) 
- Collection of rules to allow or deny in and out traffic


### Slide / Page 326

- Restricts unauthorized access 
 
Standard ACLs verifies from the Source IP 
 
Extended ACLs verifies by source IP, dentenation IP, Mac Address, and Port Numbers 
 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


### Slide / Page 327

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - foe aikegpelce-virealteachies: -hacktop QS
> - r 1-feeshtesS Aptaples -A
> - iptables v1.4.3
> - : erage! eet [Ath] chain rale-specttication [options]
> - tptaaled -0 chain [rulesen) rule-apectficatten (options)
> - tptasles -A chein rolenos ra eg Topticra} ed:
> - : iptebles -A INPUT +p tcp | —syn -m state --siate
> - Apiales -b chain relenae [op Fitering non T¢ 7 : :
> - Aptasles -[15] [ebatn rat etre Fees i
> - { = - NEW -) OROP i
> - {chain} [options] . = z ae
> - eid-chalninate frorechein «pane = ‘ nl
> - -P chain ta options) =
> - -b (print this belp isfornstion) = a
> - Blackie AS scan Attack iptables -A INPUT -p tep —tep-flags ALL -j DROP
> - Append to chain
> - Check for the extaterce cf a ret
> - Selere rarching rule tres chala Drop any NULL packets iptables -A INPUT -*-j DROF
> - +B chale rulestn
> - telete rule ruleres (i = first)
> - -3 chate feuletin)
> - Fn a ee ta iptables -A INPUT -# +4 DROP
> - Drep any fragmented packets


### Slide / Page 328

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Firewall Tools
> - A free network firewall distribution, based an the FreeBSD operating: system with a
> - pfSense custom kernel and including third party free software ‘cone for additional
> - Functionality fee
> - Smoothwall Firewall
> - https: {/wiew.smocthwallcons
> - | ‘
> - SE a liare
> - ZoneAlarm Free Firewall
> - | Alfpetewewsconeninem.coc
> - ; ManageEngine Firewall Analyzer
> - \ - httpd aro monaqeengite.com
> - ae * i Sophes Firewall
> - i" a aa Attys ifaw sonfios.cam
> - x : da
> - fee Comodo Firewall
> - dtp trong Finewnl coenana cert
> - fal Fights Reserved


### Slide / Page 329

DIFFERENT TYPES OF IDS/IPS and their role 
7.4 
 
Intrusion Detection and Prevention System (IDS/IPS) 
 
An IDS/IPS is a network security monitor that inspects all network traffic 
(Inbound/outbound) for suspicious patterns that might indicatate a security breach. 
 
àIf found, IDS will alert the admin about the suspicious activities 
 
à IDS checks the network traffic for signatures that much known intrusion patterns and 
triggers an alarm if found. 
 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
 
How does IDS work? 
 
1. Signature-Based detection: identifies threats by comparing incoming data to a 
database of attack patterns (signatures)


### Slide / Page 330

2. Anomly-based detection: identifies changes from normal behaviour which may 
indicate a threat 
 
3. Hybrid Detection: Combines both SB and AB methods for improved detection 
 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
 
Roles of an IDS in Network Defence: 
 
IDS works from inside the network. IDS is placed behind the firewall inspecting all traffic- 
looks for heuristic (examining for suspicious codes) and a pattern match for intrusions 
 
How an IDS detects an Intrusion? 
 
Signature Recognition aka misuse detection tries to identify events that indicate an abuse. 
 
Protocol Annomaly Detection built to explore inconsistency with the TCP/IP specification 
 
Anomaly Detection detects intrusion based on the fixed behaviour characteristics


### Slide / Page 331

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
 
General indications of intrustions: 
 
File System Intrusions: 
 
- New unfamiliar files/ programs 
 
- Changes in file permissions 
 
- Unauthorized files 
 
- Missing files 
 
 
 
 
 
 
Network Intrusions:


### Slide / Page 332

- Multiple probe requests sending requests to different network services or ports to see 
which ones are active or vulnerable 
 
- Connections from unknown locations 
 
- Repeated login attempts from remote hosts 
 
- Sudden influx of log data 
 
System Intrusions: 
 
- Short or incomplete logs 
 
- Unusual slow system performance  
 
- Missing logs or logs with incorrect permissions 
 
- Modifications to system software and configuration files


### Slide / Page 333

- Unusual graphic displays or text messages 
 
- Gaps in system accounting for system intrusions making it difficult to detect, trace or 
respond to unauthorized events. 
 
- System crashes  
 
- Unfamiliar processes 
 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
 
Approach-based IDS 
 
Signature-based detection aka misuse monitors patterns of data packets in the network 
and compares them to ready-to-use attack patterns known as signatures. 
 
Advantages: 
- Detects attacks with minimal false alarms 
 
- Quickly identifies the use of a specific way


### Slide / Page 334

- Assists admins to track any potential security issues and initiate incident handling 
procedures 
 
Disadvantages: 
 
- Only detects known threats based on the database (must be updated constantly) 
 
- Uses not fixed defined signatures making it ineffective at detecting common variations 
of the attactls 
 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


### Slide / Page 335

Anomaly-based detection: 
 
Evaluates network patterns (includes bandwidth type, what protocols are used, what 
ports are used, and what devices are connected to each other).  
 
An IDS monitors normal activity for a particular time interval then builds the statistics for 
the network traffic. 
 
Advantages: 
 
- Identifies unnormal behaviour in the network and detects symtpons for attacks 
 
- Further defines signatures for misuse detecors 
 
Disadvantages: 
 
- False alarms is high due to behaviour of users and networks


### Slide / Page 336

- Extensive set of system events in order to know normal behaviour patterms  
 
 
Stateful Protocol Analysis 
 
Compares examined events with predetermined profiles based on accepted definitions of 
harmless activities for each protocol to identify any variation of the protocol state 
 
- This method can identify unpredictable sequence of commands. 
 
- Detecs variation  
 
- For any protocol performing authentication, the IDS/IPS will monitor the track of the 
authenticator for each session used and will record the authenticator if involved in 
suspicious activities


### Slide / Page 337

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Timing
> - information
> - A typical misuse detection system
> - Modify existing rules
> - Add rew rule


### Slide / Page 338

Behaviour-based IDS 
 
An IDS is based on how it reacts to a protential intrusion. 
 
Active IDS: Detects and responds to detected intrusions 
 
Passive IDS: Only detects intrusions 
 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
 
Protection-based IDS 
 
- IDS is classified based on the system/ network. I 
 
If IDS protects the network then it is called network intrusion detection system (NIDS) 
 
If IDS protects a host then it is called a host intrusion detection system (HIDS) 
 
If IDS protects both a network and a host then it is called a hybrid detection system 
(Hybrid IDS)


### Slide / Page 339

A hybrid IDS combines the strength of both NIDS and HIDS to provide security. 
 
1. Low False-Positive wats of NIDS: False alarms are low since it based on known attack 
patterns 
 
2. Anomaly-Based detection of HIDS: Each individual host (such as servers or 
computers) is monitored and can detect deviations from normal behaviour. Identifies 
unknown or new types of attacks. 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
 
Structure-based IDS (AKA Centralized IDS or a Distributed IDS): 
 
All data is sent to a central location for analysis. Several IDS are deployed over a large 
network and each IDS communicates with each other for traffic analysis


### Slide / Page 340

Analysis Timing-based IDS: 
 
Analysis time is time elapsed between events occurring and the analysis of what happened 
 
 
Interval-Based IDS- 
 information about an intrusion detection is stored and forwarded 
  
Analysis of the detected intrusion is offline 
 
Real-Time-based IDS- 
 
Information about an intrusion flows continuously from monitoring points to analysis 
engines


### Slide / Page 341

Source Data Analysis-based IDS: 
 
IDS is based on the type of data source. IDS uses data sources to audit trail and network 
packets to detect intruions 
 
 
USING AUDIT TRAILS: 
 
- Audit trails help the IDS detect performance problems, security violations, and flaws in 
applicatons 
 
USING NETWORK PACKETS: 
 
- Capturing and analyizing network packets help an IDS detect well-known attacks


### Slide / Page 342

Command Console 
 
- Software that runs a separate system for the IDS 
 
- Provides user interface to an admin for the purpose of receiving and analyzing security 
events, alert messages, and log files 
 
- Evalutes security events 
 
- 
Caution: if you install the CC software on a non-dedicated system it may result in 
slower responses to security, because the non-dedicated system has to handle other 
tasks (such as manging firewalls, rules, backups….) in aditon to running the software.


### Slide / Page 343

Network Sensors are hardware and software components that monitor network traffic and 
trigger alarms if any unknown activity is detected. 
 
Network sensors placements and locations: 
 
- Internet gateways 
 
- In between LAN connections 
 
- Remote access servers used to receive dial-up connections 
 
- VPN devices 
 
- Either side of the firewall 
 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
 
Alert Systems:


### Slide / Page 344

- Alert messages when any anomaly or misuse is detected 
 
Response System: 
 
Countermeasures against any intrusion that is detected. 
 
- Involvement in decisions during incident repsone is important and should have the 
ability to respond alone. Decisions are needed on how to deal with false postivies and 
when a response needs an escalation 
 
- You should not rely only on IDS for an intrusion response 
 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
Attack Signature Database: 
 
An IDS only maintains a database of attack signatures and patterns 
 
à Network traffic is compared against known attack signatures, then a decision can be 
made


### Slide / Page 345

à If any matches are found, the IDS will raise an alert and block the suspicious traffic 
 
à IDS attack signature database must always be updatd


### Slide / Page 346

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Deploying Network-based IDS |
> - Consider ell possible options and its associahed
> - advantages/disadvantages woer placing a
> - nebwork-besed IDS
> - Kat re: Pessereed, Megrrch action by Stricthy 2aclkl


### Slide / Page 347

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - ___\, Deploying Network-based IDS (Cont’d)_
> - Ineemet | iemwa Rourer ~
> - Location @
> - bane eet tll een A
> - Ama
> - THM al st abowwert
> - Cagright © ey B-Qeuerth Ad Rigtrn Recereed. Saprcahiction be Stricthy @e r


### Slide / Page 348

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Deploying a Host-based IDS"
> - i, comialen ies rman aes sere from. iargte nuniber of hone
> - Cogpprigit ry Bi-Gammiclh, 4 Rigten Resaread, Gepecehacticon be Stricthy


### Slide / Page 349

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - What is an IDS Alert?
> - It sends the
> - atificatien, indicating
> - Hat sarnething is
> - owrongand requires
> - Immediate attention
> - a land manitering
> - ticular event
> - a specified
> - ole and needs
> - jeractionbya


### Slide / Page 350

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Q An IDS raises an alarm when
> - a
> - legit


### Slide / Page 351

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Intrusion Detection with Snort
> - Snort is a open-source eosark intrusion
> - detection system, capable of performin |-time
> - traffic analysis and packet fogging on IP networks
> - arid comtirrul
> - liganoerform protecal analysis
> - searchingmatching. anc
> - ofattacks and probes, 51
> - sherk, parte) yes "
> - erprritiig aluernpls
> - snoule collector
> - seer th Lert
> - Sg Le elie amet cama
> - oe Tnltisticing Seort ++--
> - acti] leg Oeteet elgg t
> - ae fil: oertigered t# aisien:
> - ‘B4Q vernon does set tepomct relesd.
> - dleg tite tee fe ener Meeps) bv 8rd r- ereerard)
> - ting Cttorect
> - soe teltislisetice complete 2x--
> - tr Sacre 4
> - Herplic 7.0.18 M1817 EEE Chai la 7)
> - $e Seria Geesth 4 Ter Seart Trem: ether J Fee aor ere rerterteee
> - tappetgi: t Seis-date (Sire: udjor ts aeitilres. iz} vigets receracd.
> - pW Remitdiee, Tot, et al
> - Sieg POR vertion: 0.Ub thee
> - ‘Gilag ditt wwudca: 3.2.7
> - ATE Ab eee
> - emer cing packet orocemting Crit-dtot)
> - nee ate ee erat
> - Rruasiiete el adage [2p [Dredts®) WV; (SEE Wah [=] fleet lection, Setenttalty Red Trsftic] FLarsig,
> - irad ep dietlitete tetas a
> - 1 Sacer {ttl Contig are tees em () Klasctibiecion: peteacialie met aiic) lenin
> - Usa wT aaa [tp Cette) rw care a (=) KleacHissiion: Pofeatiialty Sil TraHtie] F-Lerity
> - ALE) Lee,
> - = Rie shat eaina Show Eats feeb (1 Hleeettieerion: seteecial by bed effi] brie)
> - CMe) ware ee (| Leet: Pee Ret WELL) Le
> - Ege lilee
> - Te ELAR [OD CG eas] CH CE PL] Kleen bection: Pelenbtal hy Bed Weitin] Poisritg)
> - CR ate ne
> - Lis bad Ha? PE CTE) A GE RS Khoo testi: Geter fet TeefVicl Priori
> - ee are ere Esty


### Slide / Page 352

Understanding Different Types of Honeypots 
7.5 
 
What is a honeypot? 
 
A honeypot is an information system recourse used to set up traps and attract people to 
penetrate an organization’s network. 
 
- Any traffic is likely to be a probe, attack, or compromise. 
 
- Honeypot can log access attempts or monitor an attacker’s keystroke. 
 
Types of Honeypots (DESGNED): 
 
01.  Low-interaction honeypots: Simulates only a limited number of services and 
applications of a target system or network 
 
02.  Medium-Interaction honeypots: Simulates a real operating system, applications, 
and services of a target network


### Slide / Page 353

03.  High-Interaction Honeypots: simulates all services and applications of a target 
network 
 
04.  Pure Honeypots: Emulates the real production network of a target organization 
 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
 
Honeypots based on Deployment Strategy  
 
Production Honeypots: 
 
- Deployed inside the production network. 
 
- Helps find internal flaws and attackers within an organization 
 
Research Honeypots: 
 
- Gains detailed knowledge about the actions of the intruder 
 
- Deployed by research institutes, government, or military organization


### Slide / Page 354

Honeypot tools 
 
à HoneyBOT: medium interaction for widows


### Slide / Page 355

7.6 
Understanding Different Types of Proxy Servers and Their Benefits 
 
What are Proxy Servers? 
A proxy server is a dedicated system virtually located between a client and the actual server 
 
à It is a shield between internal network and the open network 
 
à it serves clients requests on behalf of actual servers, thereby preventing actual servers 
from exposing themselves to the outside world 
 
à  Provides an additional layer of defence and can protect against OS and web server 
specific attacks 
 
à A proxy server is needed to be deployed to intercept malicious, offensive web content, 
computer viruses…etc… hidden in the client’s requests


### Slide / Page 356

Transparent Proxy 
 
à  Intercepts and redirects network traffic to a server without its knowledge 
 
à Configured to be entirely invisible to an end user 
 
à All the web clients must be configured manually 
 
 
Non-Transparent Proxy 
 
à Requires client software to be configured to use the proxy server 
 
à Client is aware of the Proxy 
 
à Difficult to configure as each client program must be configured to route all requests to a 
single port


### Slide / Page 357

Proxy Features and Functions: 
 
- Group Annotation: Groups and manages traffic for different sets for handling and 
monitoring 
 
- Services: Caching, content filtering, and load balancing to enhance network perfroamces 
and security 
 
 
- Media type: Handles different types of media and optimizes their delivery 
 
- Transformation: Modifies content of data packets such as removing ads, adjustment, or 
alerting headers 
 
- Proctol reduction: Simplifies communication protocols, reducing overhead and 
improving efficiency by converting data from one protocol to another 
 
- Anonymity Filtering


### Slide / Page 358

SOCKS Proxy: 
 
- Internet Egineering Task Force (IETF) standard 
 
- Does not allow external network components to collect information on the client  
 
SOCKS package includes a specificied OS system, a client program such as FTP, Telnet, or an 
internt browser, and a client library 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
 
Anonymous Proxy does not transfer information about the IP addresses of its user, theby 
hides information about the user and their surfing interests 
 
Pros: 
- A user has privacy 
- A user is able to access censored websites


### Slide / Page 359

Cons: 
- May decrease the speed of loading web pages 
- Bypass internet censorship is illegal in some countries 
 
Reverse Proxy 
 
Forwards client requests to appropriate backend (data access layer) server and then returns 
the server’s response to the client 
 
- This improves performance and reliability since it distributes incoming traffic to multiple 
backend servers. 
 
- Increases security acting as a barrier between clients and backend servers to protect 
against attacks by masking the backend infrastructure. (includes SSL encryption, firewall 
protection, DDoS attack mitigation. 
 
- Caching 
 
- Compression


### Slide / Page 360

7.7 
Overview of VPN and its importance in network security 
 
What is a VPN? 
Virtual Private Network are used to securely communicate with different computers over 
insecure channels 
 
- A VPN ensures that there is security within a communication for distant officers or users 
within the enterprise’s network.


### Slide / Page 361

How VPN works:- 
 
01.  A client connects to the internet 
 
02.  The client intiates a VPN connection with the company’s server 
 
03.  Before connection, end points must be authenticated through security measures.


### Slide / Page 362

04. The client can securely access the company’s network 
 
 
VPN Concentrators 
- 
Acts as a VPN router generally used to create a remote access or site-to-site VPN. 
 
- Creates secure VPN connections  
 
- 
Uses tunnelling protocols to negotiate security parameters, creates and manges 
tunnels, encapsulate (isolating harmful resources within a secure environment) , or 
receive packets through the tunnel, and de-encapsulate them 
   
Client-to-Site (Remote-access) VPNs 
 
- Allows users to establish a secure communication to a company’s network over the VPN 
 
- Each host contains VPN client software or web-based. 
 
- VPN encrypts the data packets that are forwarded over the internet to the VPN gateway


### Slide / Page 363

- A VPN gateway receives the packets and closes the communication after transfer is 
complete 
 
 
Site-to-Site VPNS: 
 
Two types-  
 
01. Internal-based: between sites of a single organization 
 
02. External-based: between different organizations 
 
- Extends the Company’s network, and allows access of an organization’s network 
resources from different locations 
 
- Connections different locations to the company’s HQ network 
 
- AKA LAN-to-LAN or L2l VPns


### Slide / Page 364

Hardware VPNs 
 
- Connects routers and gateways to ensure communication over an insecure channel 
 
- Designed to serve as VPN endpoint and can connect to multiple LANs


### Slide / Page 365

Software VPNs 
 
- Installed and configured on routers, servers, and firewalls or as a gateway that functions 
as a VPN 
 
Pros: 
 
- No extra devices needed to install 
 
- Easy and low-cost to deploy a VPN and does not change the target network 
 
Cons: 
- Extra processing 
- Less secure 
VPN Core Functionality: Encapsulation- 
 
- Packets over a VPN are surrounded within another packet which has a different IP 
source and destination


### Slide / Page 366

- Hides the sources and the destination of packets in cause to protect its integrity of the 
data sent 
 
Common VPN protocols: 
 
- Point-to-Point Tunnelling Protocol (PPTP) 
 
- Layer to tunnelling Layer Protocol (L2TP)   
 
-  Secure Shell (SSH) 
 
- Secure (SOCKS) 
 
 
 
 
Encryption 
 
- Packets sent over a VPN are encrypted to maintain confidentially of the information


### Slide / Page 367

- Packets are read by decryption the encryption key from the sender 
 
Common VPN Encryption technologies: 
 
- Tripple Data Encryption Standard (3DES)  
 
- Secure Sockets Layer (SSL) 
 
- OpenVPN 
 
 
Authentication 
- Users are authenticated by using digital certificates. 
 
Techniques: 
IPsec, MS-CHAP, Kerberos 
 
Hub-and-Spoke VPN Topology


### Slide / Page 368

- Each spoke connected to the remote office communicates securely with the central 
device (hub) 
 
- A separate and secure tunnel is established between the hub and each scope 
 
- A continuous connection is established between the organization’s main office and their 
branches using a third-party network or the internet 
 
 
 
Point-to-Point VPN Topology 
 
01.  Different locations can directly communicate without IPsec Failover 
 
02.  Two endpoints are treated as two peer devices  
 
03.  Only regular IPsec/GRE can be assigned for the tunnel as any peer device can start 
the communication 
 
Full Mesh VPN Topology


### Slide / Page 369

- Suitable for complicated networks where all peers communicate with one another 
 
- Device to device communication in the network with a unique IPsec tunnel 
 
- Prevents a bottleneck at the VPN gateway (each device is directly connected to every 
other device, reduces the chances of overcrowded with traffic) 
 
- Saves an encryption/ decryption overhead (less need for repeated 
encryption/decryption of data at CP à reduces loading on any single device à makes 
network more efficient) 
 
- Reliable and offers redundancy (the network can still function even if a connection fails 
because there are multiple alternative paths for data to travel


### Slide / Page 371

Star Topology 
 
- 
Allows remote branches to securely communicate with cooperate headquarters 
 
- 
Does not allow interconnection between branches 
 
- 
Deployed in a bank network, preventing one branch from compromising another 
branch 
 
- 
Attacks must first compromise the central network, before another branch. 
 
- 
New sites can be added easily and only the central site needs to be updates 
 
- 
The central site is a major role. if it fails, then all connections goes down.


### Slide / Page 372

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - w)
> - STAR
> - TOPOLOGY


### Slide / Page 373

Jump Servers aka Jump box aka jump host 
 
- Acts as an intermediary gateway inside a secure environment in a network that is used 
to connect or access to devcies located in another security zone such as DMZ 
 
 
7.8 
Overview of Other Network Security Controls 
 
User Behaviour Analytics (UBA): 
 
- Process of tracking user behaviour to detect malicious attacks, potential threats, and 
financial fraud 
 
- Provides advanced threat detection in an organization to monitor specific behavioural 
characteristics of employees  
 
- Identifies variations in traffic patterns


### Slide / Page 374

Network Access [or admission] Control (NAC) 
 
- Solutions that attempts to protect the network by restricting the connection of an end 
user to a network based on a security policy 
 
- Preinstalled software agent might inspect serval items before accepting the advice and 
might restrict  
 
What does NAC do? 
 
- Authenticates users connected to network resources 
 
- Identifies connections 
 
- Defines a connection point of network devices 
 
- Develops and applies security policies


### Slide / Page 375

Web Content Filter 
 
- A software or hardware that blocks browsing of harmful websites and undesirable 
content on the WWW 
 
- Prevents the network from malware, phishing, and pharming attacks 
 
- Filters content 
 
- Provides additional protection other than traditional network (firewalls and antivirus 
software) 
 
Unified Threat Management (UTM) 
 
- Network security management solution which allows an administrator to monitor and 
manage an organization’s network security through a centralized management console


### Slide / Page 376

- Provides firewalls, intrusion detection, anti-malware, spam filter, load balancing, content 
filtering, data loss prevention, and VPN using a single UTM appliance


### Slide / Page 377

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - S& wallarm
> - UTM A single appliance Blended threats protection
> - VPN
> - Gateway AV
> - Antisryware
> - o&
> - Email/Antispam
> - filtering
> - N\
> - =
> - Web security IPs
> - QoS/Bandwidth
> - management


### Slide / Page 378

Security Incident and Event Management (SIEM) 
 
- Performs real-time SOC (Security Operation Center) functions like identifying, 
monitoring, recording, auditing, and analysing security incidents 
 
- Provides security by tracking suspicious end-user behaviour activities within a real-time 
IT environment 
 
- Provides security management services combining Security Information Management 
(SIM) and Security Event Management (SEM) 
 
 
SIM supports permeant storage, analayis, and reporting of log data 
 
SEM deals with real-time monitoring, correlation of events, notifications amd console views


### Slide / Page 379

Security Orchestration Automation, and Response (SOAR) 
 
  +---------------------------------+ 
  | Security Orchestration          | 
  | - Integrates various tools      | 
  | - Coordinates workflows         | 
  +---------------------------------+ 
                | 
                v 
  +---------------------------------+ 
  | Security Automation             | 
  | - Automates repetitive tasks    | 
  | - Reduces manual intervention   | 
  +---------------------------------+ 
                | 
                v 
  +---------------------------------+ 
  | Security Response               | 
  | - Manages incident responses    | 
  | - Ensures timely actions        |


### Slide / Page 381

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Security Orche:
> - and Automati
> - Security Inc
> - Response Platform


### Slide / Page 382

7.9 
Understanding Importance of Load balancing in Network Security 
 
Load balancer 
 
- A device responsible for distributing network traffic across multiple servers in a 
distributed system 
 
- it can control the number of requests to protect against rate-based attacks such as DoS 
and DDoS 
 
Types of Load Balancing Algorithms 
 
Session Affinity: tracks the session cookie 
 
Round-robin: Distributes incoming requests 
 
Least connections: chooses the server with the least number of active connections to 
request connection


### Slide / Page 383

Random Connections: Selects two servers randomly and sends requests to the one chosen 
by applying the least-connection algorithm 
 
 
7.10 
Understanding Various Antivirus/Anti-malware Software 
 
Anti-Trojan Software 
 
Kaspersky Internet Security provides protection against Trojans, viruses, spyware, 
ransomware, phishing, and dangerous websites


### Slide / Page 384

Bitdefender Antivirus Plus 
 
Works against all threats – from viruses, warms, and trojans to ransomware, zero-day 
exploits, rootkits, and spyware



---

## 🛠️ Connecting Theory to Practice
- **Execute the Lab:** Open [`labs/lab-04-snort-nids-rule-crafting.md`](../../labs/lab-04-snort-nids-rule-crafting.md) to work through the practical workshop reinforcing this module.
- **Reference Card:** Check [`cheatsheets/cct-exam-quick-reference.md`](../../cheatsheets/cct-exam-quick-reference.md) for rapid command syntax, formulas, and port mappings.
