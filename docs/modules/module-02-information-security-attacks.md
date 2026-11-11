# Module 02: Information Security Attacks

> **Source Material:** Authentic CCT Study Notes & Slide Deconstructions (Pages 66 – 148)  
> **Author:** [@Dabuynyx](https://github.com/Dabuynyx)  
> **Related Hands-on Lab:** [lab-02-network-attacks-arp-poisoning.md](../../labs/lab-02-network-attacks-arp-poisoning.md)  
> **Quick Reference:** [cct-exam-quick-reference.md](../../cheatsheets/cct-exam-quick-reference.md)

---

## 🧭 My Complete Study Notes & Slide Walkthroughs

### Slide / Page 66

A security professional must have the required knowledge to find vulnerabities on exploit 
sites and further mitigate them to enhance the organization's security infrastructure. 
 
 
 
 
 
 
 
 
 
 
 
 
MODULE  02- Information Security Attacks 
 
ATTACKS = Motive + Method + Vulnerability 
 
A motive comes from the reason of attack.


### Slide / Page 67

The target system may contain something valuable and this leads to a threat 
 
Motives behind ISA: 
 
 
 
 
 
 
 
 
 
 
 
• Disrupting business continuity: 
 
Attackers often aim to disrupt/ disturb the normal operations of an organization. 
 
Types of attacks:


### Slide / Page 68

• DoS: Denial of service attack is a type of cyber attack that aims to render a device 
unavailable by interrupting the device’s normal functioning. 
 
• DDoS: multiple DoS 
• Ransomware 
 
• Wiper attacks: malware based attacks designed to permanently delete or corrupt data 
on target systems which could destroy access to files and data 
 
 
 
 
 
 
 
 
• Causing Financial Loss to the Target: 
 
• Cyber fraud and theft


### Slide / Page 69

• Intellectual Property Theft: stealing trade secerts to reduce competitive advantage 
 
• Extortion: ransom 
 
 
 
 
 
 
 
 
 
 
 
 
 
• Damaging the reputation of the target 
 
- Defacement: Replacing content with the attacker’s message


### Slide / Page 70

- Information Leaks 
 
- Social engineering and Phishing

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - These motives often overlap, with a single attack achieving multiple objectives. For
> - instance, a ransomware attack can disrupt business continuity, cause financial loss, and
> - damage reputation simultaneously. Understanding these motives is crucial for
> - developing effective cybersecurity strategies and defenses.


### Slide / Page 71

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Disrupting Business Continuity: Attackers often aim to halt the operations of businesses
> - through methods like Distributed Denial of Service (DDoS) attacks, which overwhelm systems
> - and cause downtime. This disruption can have severe operational and financial consequences
> - for the targeted company (Crayon Data) IT Governance).
> - 2. Stealing Information and Manipulating Data: A significant portion of cyberattacks focus on
> - stealing sensitive information, such as personal data, financial details, and intellectual property.
> - This stolen data can be sold on the black market, used for identity theft, or manipulated to cause
> - further harm to the organization (Crayon Data) (Visual Capitalist).
> - 8. Creating Fear and Chaos by Disrupting Critical Infrastructures: Cybercriminals may target
> - critical infrastructures like power grids, water supply systems, and healthcare facilities to create
> - widespread fear and chaos. Such attacks can have far-reaching consequences, impacting public
> - safety and national security (Visual Capitalist).
> - 4, Causing Financial Loss to the Target: Many cyberattacks are financially motivated. Ransomware
> - attacks, where hackers encrypt data and demand a ransom for its release, are a prime example.
> - ‘These attacks can lead to significant financial losses for businesses that either pay the ransom
> - or invest in costly recovery efforts (Visual Capitalist) (Crayon Data).
> - 5. Damaging the Reputation of the Target: Attacks can also be almed at tarnishing an
> - organization's reputation. Data breaches, especially those involving customer data, can erode
> - trust and lead toa loss of business. Publicly exposing vulnerabilities or spreading
> - misinformation can further damage a company's standing (Visual Capitalist)
> - Understanding these motives helps in developing better defensive strategies and responding more
> - effectively to cyber threats. For more detailed insights and statistics on cybersecurity attacks, you
> - can explore resources like Visual Capitalist's infographics and IT Governance's reports on cyber,
> - security trends (Visual Capitalist) (Visual Capitalist) (IT Governance).


### Slide / Page 72

Classifications of Attacks 
 
• Passive attacks: 
 
Does not tamper with the data and involves surveillance the network and data flow on the 
target. 
 
• Active attacks: 
 
Tampers with the data to manipulate the data also to break into secured systems 
 
Examples  
 
DoS, Man-in-the-middle, session hijacking, injection.


### Slide / Page 73

Research tasks: 
 
Man-in-the-middle: 
 
A cyberattack where an attacker intercepts and could change the communication between 
both parties without their knowledge 
 
Types of MITM attacks: 
 
1. Eavesdropping 
 
2. Session Hijacking: 
The attacker takes over a user’s session by stealing session cookies/ tokens to 
impersonate the user and gain unauthorized access to their accounts 
 
3. SSL Stripping:  
The attacker decrypts a secure HTTPS connection to a HTTP connection, making it easier to 
get data and manipulate data that is being transmitted


### Slide / Page 74

4. DNS Spoofing 
The attacker provides false DNS responses that will redirect the victim to a malicious 
website that looks like the intended destination. 
 
DNS  
Domain Name system provides a name for computers, services, and other resources in the 
internet or other internet protocol networks. 
 
DNS is the phonebook of the internet. 
 
DNS translates IP addresses to load internet resources.


### Slide / Page 75

Injection:  
An attack that injects malicious code or a command into a program to change its excitation 
code and potentially gain unauthorized access to data or systems. 
 
Types of injections: 
A. Strcuted Query Language (SQL): standard language for database creation and 
manipulation 
 
B. Cross-Stie Scripting (XXS): 
Malicious scripts are injected into benign and trusted websites. 
 
 
C. Command injection 
 
D. Code Injection 
 
E. LDAP Injection:


### Slide / Page 76

Lightweight Directory Access Protocol (LADP): Directory service Protocol that runs on a 
layer above TCP/IP stack. It provides a mechanism used to connect to, search, and modify 
internet directories. 
 
Close-in Attacks: 
Close- physical proximity with the target system or network to gather, modify, or disrupting 
access. 
 
 
 
Insider Attacks: 
Privileged access inside the perimeter to intentionally cause a threat to the organization’s 
information/ its systems. 
 
Examples: 
Theft of physical device 
Planting Keyloggers 
Backdoors 
Malware


### Slide / Page 77

Distribution Attacks: 
 
Dealing with the distribution/ supply chain 
 
• Occurs when attackers tamper with hardware or software prior to installation 
What is hacking? 
 
Hacking is learning how something works then manipulating it in a way that is unexpected 
by the system to make it do something that is not made to do. 
 
Hacking is like bending the rules and manipulating the system to achieve a result other 
than system’s original intent. 
 
 
Exploits system vulnerabilities and compromises security controls to gain access to a 
system’s resources. 
 
Hacking can be used to steal and redistribute intellectual property. 
 
RESEARCH TASK: RCE


### Slide / Page 78

Phase 1- Foot printing and Reconnaissance:  
 
Reconnaissance is when an attacker seeks to gather information about a target to launch 
an attack. 
 
Types: 
Passive and Active Reconnaissance. 
 
Phase 2- Scanning: 
 
Pre-Attack phrase when the attacker scans the network for specific information based on 
reconnaissance to gather information.


### Slide / Page 79

Types: 
 
Diallers: 
A malicious program that is installed on a computer and tries to use the dialing features 
to call other numbers. 
 
 
 
Port scanners 
A technique used to discover open doors or weak points in a network. 
 
A port scan attack helps cyber criminals find open ports to figure out if it is receiving or 
sending data. It could revel active security devices ..such as firewalls.. that are being used 
by an organization 
 
 
Network mappers: 
 
Tools that help identify active devices, open ports, and the services running on them, 
providing critical information for network security management and vulnerabilities.


### Slide / Page 80

Helps discover and map the devices and services within a network. 
 
Ping tools: 
Checks if a host is reachable on a Internet Protocol (IP) network and measures round-trip 
time for messages sent from the originating host to a destination computer. 
 
Uses of Ping Tools 
 
Connectivity Testing: Checking if a host is reachable across the network. 
 
Latency Measurement: Determining the time, it takes for a packet to travel to the 
destination and back. 
 
Network Diagnostics: Identifying network issues such as packet loss or high latency. 
 
Network Configuration: Verifying network configurations and ensuring devices are properly 
connected.


### Slide / Page 81

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Phase 2 - Scanning
> - Scanning refers te the pre-attack phase when the attacker scans the network for specific information
> - ) based on information gathered during reconnaissance
> - Scanning can include the use of dialers, port scanners, network mappers, ping tools, and vulnerability
> - Stanners
> - \ Attackers extract information such as live machines, port, port status, OS details, device type, and
> - _/ system uptime to launch attack
> - Sands
> - TCP/IP probes
> - 6 hues chi eeoes dieeesaree DS on
> - Gat Aetwork —— ied
> - information
> - Network
> - Attacker


### Slide / Page 82

Phase 3- Gaining Access 
 
PHASE 4- MAINTAINING ACCESS 
 
PHRASE 4- CLEARING TASKS


### Slide / Page 83

Cyber Kill Chain Methodology 
 
A component of intelligence-driven defence for the identification and prevention of 
malicious intrusion activities 
 
It helps security professionals understand the adversary’s tactics, techiques, and 
procedures to be steps ahead of an attack. 
 
1. Reconnaissance: Gathers data 
 
2. Weaponization: Creates a malicious payload using an exploit or a backdoor 
 
3. Delivery  
 
4. Exploration 
 
5.   Installation  
 
6. Command and Control to pass data back and forth


### Slide / Page 84

7. Actions on objectives  
Tactics, Techniques, and Procedures (TTPs) 
 
Patterns of activities and methods associated with specific/ groups of threat actors. 
 
Tactics: 
Guidelines that describe how an attacker preforms from beginning to the end 
 
Procedures: 
Organizational approaches that TA follow to launch an attack


### Slide / Page 85

MITRE Attack Framework 
 
Knowledge network based on adversary tactics and techniques based on real-world 
obvervations. 
 
The ATT&CK knowledge base is used as a foundation for the development of specific threat 
models and methodologies in the private sector, in government, and in the cybersecurity 
product and service community.


### Slide / Page 86

Diamond Model of intrusion Analysis 
 Cybersecurity framework that helps organizations analyse cyber intrusion. 
 
The main objectives of the diamond model are to identify specific attackers, understands 
the techniques, threats, and procedures they use, to effectivity respond to cyber incidents.  
 
Its main attribution is to identify those responsible for a cyber incident. 
 
Composes of: 
 
Adversary: The Opponent “Who” was behind the attack 
 
Victim: the target or “Where” the attack was preformed  
 
Capability: The attack strategies or “How” the attack was preformed


### Slide / Page 87

Infrastructure: “What” the adversary used to reach the victim 
 
 
NOTE: there is AVCAI and adversary- AVCAI


### Slide / Page 88

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Meta Features of Diarmond Model
> - =
> - i |
> - x


### Slide / Page 89

The Benefits: 
 
Holistic understanding: Examines the techniques of both the cyber attack and the human 
also the organzaional aspects (of both the adversary and the victim) 
 
Structured Analysis: Structures and processes data relating to cyber threats and attacks, 
making it easier to collaborate and share information. 
 
Incident response and threat intelligence 
 
Adversary elements: 
The adversary’s identity, name, or pseudonym. 
 
The adversary’s motivations and objectives (e.g., financial gain or corporate espionage). 
 
The adversary’s technical capabilities, skills, and knowledge. 
 
The adversary’s tactics, techniques, and procedures (TTPs).


### Slide / Page 90

The adversary’s attribution indicators (pieces of evidence that link the adversary to a 
particular group, such as code similarities or similar tactics). 
 
 
 
Infrastructure element: 
 
The geographic locations, IP addresses, and domains of servers in the adversary’s command 
and control infrastructure. 
 
The communication protocols used (e.g., HTTPS or DNS). 
 
Domain registration details (e.g., the registration date and name of the registering party). 
 
The websites or servers hosting malware or phishing scams. 
 
Abnormal traffic patterns indicating communication with the adversary’s command and 
control systems.


### Slide / Page 91

Diamond Model Of Intrusion Analysis (Cont’d)

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - ee SS ee eee a eae ey eee ae fae ee
> - Diamond Mode! of Intrusion Analysis (Cont'd)
> - Meta-Features of the Extended
> - Diarmmond Model
> - L] Describes the relationship between
> - the adversary and victim and used
> - to determine “why” the attack was
> - performed -
> - Technology Wieta-Feature
> - _| Connects the infrastructure and
> - capability for better
> - communication and operation
> - ‘Social-Political Veta -Foatereaae
> - Extended Diamond Model of Intrusion Analysis
> - ~y
> - Adversary
> - Sacial-Palitieal
> - Infrastructure
> - Capability
> - Technology
> - Wietim
> - Tap ight O by A-£ pM LE Fdgtis A=sersnerl Raperetictinn fs tinatly or .


### Slide / Page 92

Reconnaissance Attacks: 
Attackers gain as much information as they can to estibalish an attack. 
 
Reconnaissance Techniques for Attacks: 
 
Social Engineering: Manipulating the target into addressing specific information or to 
preform a specific action 
 
Port Scanning: Discovering open doors or weak points in a network to figure out whether 
data is being transmitted or receiving. 
 
DNS Footprinting: Gathering information about a target dominain name and associaited 
resources 
 
Ping Sweeping: determines a range


### Slide / Page 93

Network information obtained: 
 
• Domain name 
 
• Internal Domain Name controlled by one’s organization 
 
• Network Blocks: Storage 
 
• IP Addresses of the reachable systems  
 
• Private Websites 
 
• Open Ports 
 
• Versions running Oses 
 
• Running TCP and UDP Service  
 
• Access Control Mechanisms and  ACL


### Slide / Page 94

• Network Protocols 
 
• VPN Points 
 
• Running Firewalls 
 
• Analog/ Digital Telephone Numbers 
 
• Authentication Mechanisms 
 
• System Enumeration: process of extraction


### Slide / Page 95

Network Scanning 
 
Running a series of crafted probs to gather a lot of useful informations. 
 
Identifies hosts, ports, and services in a network 
 
New definitions: 
 
Hosts: any device that is connected to a network and can send or receive data. 
 
Packets: Small segment of a larger message 
Network scanning is part of intelligence gathering which can be used by an attacker to 
create a profile of the target organization.


### Slide / Page 96

Objectives of Network Scanning 
• Discovers live hosts, IP address, and open ports 
• Discovers Os and system Architecture 
• Discovers services running on hosts 
• Discovers vulnerabilities in live hosts


### Slide / Page 97

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Saerects
> - CHEAMEA EEDA PN NO MI IR ere et Pee >
> - + } Qf vt rrins CEE KREBS EEN EEE G7 EEE TA E SS EER SANSA L_]
> - Attacker Network


### Slide / Page 98

DNS Foot-printing: 
 
DNS records provide information about the location and types of servers 
 
Attackers can gather DNS information to determine key hosts in the network and can 
preform social engineering attacks.


### Slide / Page 99

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Record Description
> - A Arrecord is an address mapping record, also known as a DNS host record.
> - Mx The mail server record specifies an SMTP email server
> - Ns It specifies the authoritative Name Server.
> - CNAME Conical Name record, alias record used to alias a hostname to another hostname
> - SOA Start of Authority is the authoritative Name server for the current DNS zone.
> - PTR Pointer records, It allows a DNS resolver to provide an IP address and receive a hostname
> - xT Text Record, It contains machine-readable data such as DKIM.
> - HINFO Host information record includes CPU type and OS
> - SRV
> - Service Records


### Slide / Page 100

Procedures: 
 
NSLOOKUP: network administration command-line tool for searching DNS to obtain the 
mapping between domain name and IP address or other DNS records


### Slide / Page 101

Packet Sniffing 
 
Process of monitoring and capturing all data packets passing through a given network in a 
system. 
 
It allows attacks to capture traffic in the entire network and gather sensitive information 
such as telnet passwords, email traffic, syslog, etc.


### Slide / Page 102

Man-in-the-middle 
 
An attack where the attacker lies in the middle between the victim and the victim’s target, 
intercepting the messages being exchanged.


### Slide / Page 103

DNS Posioning: 
 
Misleading victims into connecting to nonlegitimate resource to preform illegal activities.


### Slide / Page 104

It can manipulate IP addresses in the DNS cache without authorizations. 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Domain Hijacking 
 
The domain ownership of a server is changed to come the attacker’s server without the 
consent of the actual owner/


### Slide / Page 105

The attacker attempts to infiltrate the domain registrar account using social engineering 
and others… 
 
It misleads victims to malicious DNS server. 
 
 
 
 
 
 
 
 
 
 
 
 
ARP Spoofing Attack


### Slide / Page 106

Address Resolution Protocol is used for mappin an IP addres to a physical machine address 
which recongized in LAN 
 
2-Layer attack used to intercept traffic on a switch network. It can impersonate responses 
and achieve MITMA. 
 
ARP spoofing involves sending a larger number of forged entries to the target machine’s 
ARP cache 
 
  DHCP Starvation Attack


### Slide / Page 107

Dynamic Host Configuration Protocol is DoS attack by impersonating maliciously falsifying 
DHSCP client discovery request for purchases of consuming an address skill 
 
DHCP automatically provides an IP host with its IP address and other related configuration 
information such as subnet mask and default gateway


### Slide / Page 108

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - DHCP Server
> - User will be Pee Ks Lig 4° ne “tp Server runs out of IP
> - unable tof. ae ia x Fa Se > @ ig 2 “45. “SS, \s accreasses to allocate
> - valid [P address AS we we Rg 3 PR 8 HB, ey % to valid users
> - yO we 7a a a
> - SHE SS PE BE
> - Po Ass” =; ° 5  ? DHCP Scope
> - Evans | a a a a 10.10.10.1
> - 10.10.10.2
> - Attacker sends many 10.10.10.3
> - different DHCP requests :
> - with many source MACs
> - 10,10.10.254
> - Attacker
> - EG-Gxxzt §. All Rights Reserved. Reproduction is Strictly Prohibit¢
> - Copyright © by G-G0mE


### Slide / Page 109

DHSCP Spoofing attack 
 
The attacker impersonated a DHSCP server and does that to mislead clients to wrong 
gateways, wrong DNS servers, or IP. 
 
Research “Gateway” 
 
A gateway is a network node used in telecommunications that connect two networks with 
different transmission protocols together 
 
 
The attacker sets up a rogue DHCP server on the network and responds to DHSCP requests 
with fake IP addresses which is a compromised network access 
 
The attacker works by connecting the DHSCP requests with DHCP starvation attack.


### Slide / Page 110

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - ae Snes 6 ee a a ee eee 2 ee
> - DHCP Spoofing Attack
> - The attacker sets up a on
> - the network and responds to DHGP requests
> - This attack works in oncneten Wi et
> - DHCP starvation attack; th ne attack ker sends Sa
> - him/her out from the genuine DHGP server
> - with bogus IF addresses resulting in
> - DHCPDISCOVERY (IPv4) / SOLICIT (IPv6) (Broadcast)
> - < DHCPOFFER (IPv4) / ADVERTISE (IPv6) (Unicast) from Rogue Server
> - DHCPREQUEST (IPv4) / REQUEST (IPv6) (Broadcast) — ————, —
> - To 2 DOooOre eee Eee eee mm ‘|
> - = Chetan DHCP Server
> - ~ ——* < DHCPACK (IPv4) / REPLY (IPv6) (Unicast) from Rogue Server . ®
> - User Geccccnescccccccucccccucccccccecuceccusecuasacazags : : :
> - : A) : @ By running a rough DHCP server, an attacker
> - IP Address: 10.0.0.20 ; . =. £ « can send incorrect TCP/IP setting
> - Subnet Mask: 255.255.255.0 | -_ . 7 :
> - ES ee i ae : Wrong Default Gateway > Attacker is the gateway
> - DNS Servers: 192.168.168.2, |], — . ;
> - 192.168.168.3 | (a> : = Wrong DNS server > Attacker is the DNS server
> - - Le Time: 24 ; . ) <4 ee .
> - — =a ,o~weeeee . ja Wrong IP Address > DoS with spoofed IP
> - Internet Rogue Server
> - eayane © by EG-Semmeil_ All Rights Reserved. Reproduction is Strictly Prohib


### Slide / Page 111

MAC Spoofing/ Duplicating/ Cloning 
 
A MAC cloning attack is launched by sniffitng a network for mac Addresses of clints who are 
activicly connected with a switch port or re-using one of those addresses. 
 
Attackers can be listening to the network traffic, a malicious user can intercept and use a 
legitimate user’s mac address to receive all the traffic destined for the user 
 
This attack allows an attacker to gain access to the network and take over someone’s 
identity of that network. 
 
Spoofing is falsifying information. 
 
Mac Spoofing is typically used to circumvent filtration controls on a wireless access point or 
to hide physical address and avoid detection 
 
- Messaging DHCP servers


### Slide / Page 112

Mac Flooding: 
 
Sniffing a switch network by flooding the switch’s CAM Table with misaddressed frames, 
flashing out legitmitte entries 
 
DIFFINATIONS: 
 
Sniffing: process of monitoring and capturing all data packets passing through a given 
network 
 
Two types of Sniffing: 
 
Active sniffing: A switch is a point to point 
network device. The switch takes control of the 
flow of data between its ports actively 
monoriting the MAC addresses only for its 
intended target


### Slide / Page 113

In order to capture traffic between target sniffers has to actively inject taffic into the LAN. 
 
 
 
 
Passive Sniffng: Any traffic that is passing through a non- switched network or unbridged 
network segement   
 
 
 
CAM Table: 
 
Content Addressable Memory is used on ethernet switches to determine where to forward 
traffic on a LAN


### Slide / Page 114

IP Address Spoofing 
 
Changing the source of IP addresses to appear that the attack appears to be coming from a 
different source and not the attacker 
 
Attackers modify the address information in the IP packet header and sources the address 
to bypass the IDS and firewall 
 
You cannot three-way handsake and do a TCP connection with a spoofed IP Address 
 
 
Steps of a three-way handshake


### Slide / Page 115

TCP is responsible for ensuring data is delivered correctly between computers on an 
internet network. The three-way handshake involves the following three steps: 
synchronize (SYN), synchronize-acknowledge (SYN-ACK), and acknowledge (ACK) 
 
 
 
 
DoS  
Denial of Service 
 
DoS attack can be as simple as logging out a user out of their account or unplugging 
network cables…etc… 
 
 
Attackers flood the victim system with non-legitimate service requests or traffcic to overload 
its resoruces 
 
Attackers use tools such as hping3 to preform a DoS attack. 
 
DDos is multiple of DoS via”zombies”


### Slide / Page 116

DRDosS Attack 
Disturbed Reflected Denial-of-Service Attack 
 
 
Spoofing an IP address with the primary target and sending requests to intermediary 
victims then back to the target 
 
DRDoS involves use of multipe intermediary target and secondary machines that works with 
actual DDoS attack against the target 
 
Attackers launch this attack by sending requests to intermediary hosts which then redirect 
the requests to the secondary machines which then reflects the attack traffic to the target


### Slide / Page 117

The primary target seems to be directly attacked by the secondary victim rather than the 
actual target 
 
Multiple intermidary will result in an increase of attack bandwidth 
 
 
 
Definitions 
Bandwidth attack 
Ethical hacking a targets maximum amount of data transmitted over an intenet connection 
in a given amount of time 
 
 
Malware Attacks 
 
Software Progams or malicious codes that are installed on a system without the user’s 
knowledge 
 
A malware attack disrupts services, damages, systems, gather sensitive information…etc…


### Slide / Page 118

Examples of malware: Viruses, Trojans, Adware, Spyware, Rootkits, and Backdoors. 
 
 
 
 
 
 
APTs  
Advanced Persistent Threats 
 
APTs are a type of network attack, where an attacker gains unauthorized access to a 
target’s network and remains undetected for a long period of time. 
 
 
Main objective is to obtain sensitive information  
 
Unknown compromised system on a network that continues to provide access for an 
extended period of time


### Slide / Page 119

OR 
 
A ultraskill hacker group moving forwar an iconic role 
 
Infects the system internally, remains undetected for a period of time and keeps sending 
information back and forth to the attacker. 
 
 
 
Physical Attacks 
 
Malicious USB cable: USB cable with a small wifi chip that excutes commands from the 
attacler’s system 
 
Malicious Flash Drive  
 
Card Clonning 
 
Skimming


### Slide / Page 120

Adversarial AI 
 
Attackers with malicious intent to mislead machine learning models 
 
Attackers leveragae flaws in ML systems and infects malicious traffic to control over their 
network


### Slide / Page 121

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Tainted Training Data for
> - Machine Learning |
> - - Rigorithms
> - ¢* The primary task in securing ML algorithms
> - involves securing the dataset used for training
> - the ML system. The potential ML security risks —
> - include:
> - contaminating the training data of machine |
> - |
> - Y Confidentiality of Data
> - |
> - |
> - |
> - |
> - |
> - |
> - “* Tainted training data means infecting or |
> - |
> - learning models |
> - +
> - ¢.
> - ¢
> - Attackers can contaminate the data with |
> - malicious inputs that can disrupt the system |
> - performance and cause disturbances in
> - retraining
> - ¥ Manipulating the Online System
> - Vv Making False Predictions
> - Y Poisoning the Data
> - ea
> - Y Transfer Learning Attack


### Slide / Page 122

Injection Flaws 
 
Web application vulnerabilities that allow untrusted data to be interpreted and executed as 
part of a command or query 
 
Attackers exploit injection flaws by constructing malicious commands or queries that result 
in data loss or corruption, lack of accountability, or DoS. 
  
 
An injection is inserting an unexpected code through any input field  
 
 
Types of Injection Flaws: 
 
SQL Injection: Structured query language that stores and processes information in the 
database 
 
Command Injection: Malicious code through a web application


### Slide / Page 123

LDAP Injection: Lightweight Directory Access Protocol used to lookup information or 
devices within a network 
 
Cross-Site Scripting XXS 
 
Exploits vulnerabilities in dynamically generated web pages, enabling hackers to inject 
clinet-side scripts into into web pages 
 
It occurs when unvalidated input data is included in dynamic content that is sent to a user’s 
web browser for rendering.


### Slide / Page 124

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - How XSS Attacks Work
> - Normal Request
> - http: //certifiedhacker.com
> - This example uses a vulnerable
> - page, which handles requests |
> - for nonexistent pages: a classic
> - ra /jason file.html 404 error page
> - 404 Not found :
> - az Vv ~~. (Handles requests
> - /jason_file.html . Sarver Codeuan popes
> - 2 dered Response @ <7 hem > page: a classic 404
> - , <body> error page) |
> - 3 <? php
> - ——— — Server Response </body>
> - 404 Not nec as [27 </html>
> - PAVE ie acpicazben
> - hat erxounternd an e7o~
> - Copyright © by EG-Geamedl. All Nts Reserved. Reproduction is Sse Prohity
> - http: //certifiedhacker.com/<seript>
> - alert (“WARNING: The application has
> - encountered an error") ;</script>
> - REQUEST URI"}])
> - print “Not found: "=
> - XSS Attack Code urldecode ($_SERVER[" =


### Slide / Page 125

Parameter Tampering Attack 
 
Manipulation of parameters exchanged between clinet and server to modify application 
data. 
 
Exploits vulnerabilities in integrity and logic validation mechanisms that may result in 
XSS,SQL injection, etc… 
 
Attackers use tools such as Burp Suite to perfom parameter tampering attack. 
 
 
 
Directory Traversal Attacks: 
 
Attackers use “ ../ ” to access restricted directories outside the web server root directory 
 
Attackers can use the trial and error method to navigate outside the root directory and 
access sensitive information in the system.


### Slide / Page 126

CRSF Attack 
Cross- Site Request Forgery Attack 
 
Exploits web page vulnerabilities that allow an attacker to force an unsuspecting user’s 
browser to unintended send malicious requests. 
 
The victim holds an active session with a trusted site and simultaneously visits a malicious 
site which injects an HTTP request trusted site into the victim user’s session. 
 
 
Holding an active session then visiting a malicious site then it sends a transactional request 
that isn’t authorized


### Slide / Page 127

DNS Amplification Attack 
 
DRDoS Attack in which the attacker leverages the functionality of an open DNS resolvers to 
overwhelm a target with an amplified amount of traffic, rendering the server, making it 
inaccessible to users. 
 
 
Attackers exhaust available server resources by sending hundreds of resource- intensive 
requests. 
 
 
Application-level DoS attacks use the same request as the target making it undetectable by 
existing DoS protection measures.


### Slide / Page 128

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Targets
> - CPU, Memory, and Sockets
> - ts
> - “ Disk Bandwidth
> - “ Database Bandwidth
> - * Worker Processes
> - Why are Applications Vulnerable
> - to DoS? |
> - * Reasonable Use of Expectations
> - a
> - Pat
> - * Application Environment Bottlenecks
> - Pig
> - * Implementation Flaws
> - ate
> - * Poor Data Validation


### Slide / Page 129

XML External Entity (XXE) Injection 
 
 
Server-side request forgery (SSRF) attack that can occur when a misconfigured XML parser 
allower from an unreliable source 
 
 
Unauthorized Request and your injecting an input. 
 
XML Parser allows access to protected files and services 
 
Parsing: a technique used to analyse and interprets syntax (the structure) of information and 
breaks down a complex set of data structures into smaller, more manageable components 
that can be analysed and understood. 
 
 
The victim’s web application can refer to an external entity that includes the malicious XML 
input


### Slide / Page 130

Extensible Markup Language (XML) defines and stores data in a sharable manner.  
Watering Hole Attack 
 
Attacking a website that is frequent by the victim 
 
The attacker identifies frequent visited websites of the victim, then the attacker identifies 
any possible vulnerabilities of that specific site. 
 
Once identified the attacker can inject a malicious code that can redirect the webpage and 
download malware onto the victim’s machine, which then compromises the network. 
 
The attacker waits for the victim to fall into the trap


### Slide / Page 131

Application Level Session Hijacking: Session Replay Attack 
 
The attacker steals a session token from an authictencated user to reply it to the web 
server as if you were that victim to get unauthorized access to the server.  
 
An authication token is generated after log-in.


### Slide / Page 132

Application Progamming Interface (API) Attacks 
 
 
APIs are meant to be accessed by progamming software rather than humans. 
 
Whenever you want to attack something, you need to be able to know how to talk to it and 
get into that input field.  
 
Types of API Attacks: 
 
1. Fuzzing: automated software method that inkected invalid inputs into a system to 
reveal system defects and vulnerabilities. 
 
2. Injection Attacks 
  
3. Invalid Input Attacks 
 
4. Insecure SSL Configuration


### Slide / Page 133

5. 
Insecure Direct Object Reference: Whwne an application provides direct access to 
objects based on user-supplied input 
 
6. 
Insecure Session/ Authentication handling 
 
7. 
Login/ Credential Stuffing: credentials obtained from a data breach on one service 
are used to attempt to log in to another unrelated service 
 
 
8. 
API DoS Attack


### Slide / Page 134

Secure Socket Layer (SSL) Stripping 
 
Method of turning an encrypted web session into unencrypted  
 
Malicious Code or Script Excutation 
 
PowerShell: Powerful command and scripting utility that helps admins automate  
complicated tasks 
 
à Attackers use fireless malware that can be made to run applications using PowerShell 
script 
 
Python


### Slide / Page 135

Password Cracking 
 
 
Dictonary, Brute-Force, and Rule-Based attack 
 
 
Hash injection/ Pass-the-Hash (PtH) Attack 
 
When you login into a system your password hash and credientials is stored in an access 
token. 
 
That access token contains user hash and password hash which can be rewritten


### Slide / Page 136

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Hash Injection/Pass-the-Hash (PtH) Attack
> - A hash injection/PtH attack allows an attacker to inject a compromised hash
> - into a local session and use the hash to validate network resources
> - (2) The attacker finds and extracts a logged-on domain admin account hash
> - The attacker uses the extracted hash to log on to the domain controller (FS })
> - ai
> - Compromises server
> - Logged-on hashes are using a local/remote exploit
> - stored In the SAM file bir eee rere irre rene
> - Extracts a logged-on domain
> - User Server admin account hash
> - (Domain Controller)
> - Inject a compromised hash into a local session @


### Slide / Page 137

Rainbow Table Attack 
 
A precomputed hash table that creates the cracking process using the table. 
 
 
Buffer Overflow 
 
A vulnerability in software where a program writes more data to buffer (a temporary 
storage area) that it can hold. 
 
 
Attacks use this buffer overflow vulnerability to inject malicious code.


### Slide / Page 138

Privilege Escalation 
 
An attacker gains access to the network using a non-admin user account and then would try 
to gain administrative privileges. 
 
The attacker looks for vulnerabilities in the system such as design flaws, programming 
errors, bugs, and configuration oversights to gain admin access. 
 
Two types: 
 
Horizontal: Same permission line 
 
Vertical: Higher permission line 
 
 
DLL Hijacking/ Injection 
Dynamic Link Library Files contain resources an application needs to run successfully 
 
Tools such as Robber/ PowerSploit can detect hijackable DLL on the the target system


### Slide / Page 139

Driver Manipulation 
 
A driver is a software that interfaces hardware devices 
 
Refactoring is the process of modifying the mom-functional code of driver software, the 
attacker modifies parts and can hide their malicious programs and evade antiviruses. 
 
Application Shimming inserts a small piece of code between the layer of an application and 
the operating system on which it runs. This code can modify the system’s behaviour 
without the system being aware. 
 
Tools such as RedirectEXE, InjectDLL, and GetProcAddress 
 
 
Social Engineering such as impersonation, vishing (over the phone) 
 
Eavesdropping, shoulder surfing, and dumpster diving


### Slide / Page 140

Reverse Social Engineering: Attack presents themselves as an authority. 
 
Tailgating & Piggybacking: falling for a trap without a valid ID


### Slide / Page 141

Module 2 Lab 
 
Information Security

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - CQ) Emails that i issue warnings to the user
> - about new viruses, Trojans, or worms g
> - that may harm the user’s system | ,
> - © Gathering p sonal nf
> - @---s2-.->-4
> - ha Spam Email
> - ©) Irrelevant, unwanted, and unsolicited
> - !/ emails that attempt to collect
> - financial information, social security
> - numbers, and network information
> - chatting with a =
> - ‘information SUED as _
> - Copyright © by BB-Bommelll All Rights Resen


### Slide / Page 142

Refers to the protection or safeguarding of information and information systems that 
use,store, and transmit information from unauthorized access, disclosure, alteration, and 
destruction. 
 
If sensitive information goes to the wrong hands, it could cause a dangerous impact on the 
network 
 
Information security relies on confidentiality, integrity, availability, authenticity and 
 non-repudation. 
 
 
 
 
 
 
 
 
 
Perform a Man-in-the-Middle (MITM) Attack using Cain & Abel


### Slide / Page 143

Perform MAC Flooding using macof 
 
Perform a DoS Attack on a Target Host using hping3 
 
Perform an SQL Injection Attack Against MSSQL to Extract Databases using sqlmap 
 
Perform Parameter Tampering using Burp Suite 
 
Audit System Passwords using John-the-Ripper 
 
Perform Social Engineering using Various Techniques to Sniff Users' Credentials 
 
Crack a WPA2 Network using Aircrack-ng 
 
Hack an Android Device by Creating Binary Payloads 
 
Exploit Open S3 Buckets using AWS CLI 
 
 
EXERCISE 01 MITM


### Slide / Page 144

MITM: An attacker can information by capturing data packets. 
 
An MITM is used to intrude an existsing conection that is between systems in various ways 
that include splitting the TCP connection, a clinit-to-attacker connection, and an attacker-
to-server connection. 
 
 
After successfully intercepting the TCP connection the attacker can access the 
communication and intercept it. 
 
MITM can be preformed on LAN


### Slide / Page 145

EXERCISE 02: Mac Flooding using Macof 
MAC flooding is a technique used to compromise the security of network switches in the 
network system. 
 
Attackers use MAC flooding so they can sniff the traffic easilia via making the switch into a 
hub (C & C) 
 
 
For demonstration purposes, we are using the same machine. However, you can use 
multiple machines connected to the same target network. macof sends the packets with 
random MAC addresses and IP addresses to all active machines in the local network. 
 
 
In the terminal window, type macof -i eth0 -n 10 and press Enter. 
 
-i: specifies the interface and -n: specifies the number of packets to be sent (here, 10). 
 
A single system can also be targeted by issuing the command macof -i eth0 -d [Target IP 
Address] (-d: specifies the destination IP address).


### Slide / Page 146

EXERCISE 03: DoS Attack on target Host using hping3 
 
A DoS attack is an attack on a computer or network that reduces, restricts, or prevents 
access to system resources for legitimate users 
 
In DoS attack, attackers flood victim’s system with false service requests or traffic to 
overload its resources and collapse the system, leading to the unavailability or even the 
reduction of the system’s performance. 
 
 
The goal of DoS is to prevent legitimate users access to the system. 
 
 
DoS attacks may result in the over consumption of resources, bandwidth, disk space, CPU 
time, or data structures; they may also cause the actual physical destruction or alteration of 
network components or the destruction of programming and files in a computer system. 
 
 
-S: sets the SYN flag; -a: spoofs the IP address; -p: specifies the destination port; and --flood: 
sends a huge number of packets.


### Slide / Page 147

EXERCISE 04: SQL Injection Attack 
 
A technique used to take advantaged of vulnerabilities to pass SQL commands to gain 
unauthorized access to a database or to retrieve information from the database, directly. 
 
 
In this query, -u specifies the target URL (the one noted down in Step 6), --cookie specifies 
the HTTP cookie header value, and --dbs enumerates DBMS databases. 
 
 
 
EXERCISE 05: Parameter Tampering 
 
A web parameter tampering attack involves the manipulation of parametrs exchanged 
between clinet and the server to modify data. 
 
This attack directly targets an application’s business logic. 
 
A PTA explits vulnerabilities that may result in XSS, SQL Injection, etc…


### Slide / Page 148

Exercise 10: Exploit Open S3 Buckets using AWS CLI 
 
S3 buckets are used by customers and end users to store text documents, PDFs, videos, 
images, etc.



---

## 🛠️ Connecting Theory to Practice
- **Execute the Lab:** Open [`labs/lab-02-network-attacks-arp-poisoning.md`](../../labs/lab-02-network-attacks-arp-poisoning.md) to work through the practical workshop reinforcing this module.
- **Reference Card:** Check [`cheatsheets/cct-exam-quick-reference.md`](../../cheatsheets/cct-exam-quick-reference.md) for rapid command syntax, formulas, and port mappings.
