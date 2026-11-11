# Module 13: IoT and OT Security

> **Source Material:** Authentic CCT Study Notes & Slide Deconstructions (Pages 516 – 536)  
> **Author:** [@Dabuynyx](https://github.com/Dabuynyx)  
> **Related Hands-on Lab:** [lab-03-tcp-wireshark-deep-dive.md](../../labs/lab-03-tcp-wireshark-deep-dive.md)  
> **Quick Reference:** [cct-exam-quick-reference.md](../../cheatsheets/cct-exam-quick-reference.md)

---

## 🧭 My Complete Study Notes & Slide Walkthroughs

### Slide / Page 516

IoT and OT Security 
Chapter 13 
 
 
13.1 
 
What is IoT 
 
IoT aka IoE (internet of everything) refers of devices having IP addresses and the capability to sense, 
collect, and send data using embedded sensors, communication hardware and processors. 
 
 
IoT “thing” is used to refer to objects that can communicate over the network 
 
 
Organizations and IoT-Enabled Environments 
 
IoT devices work on a 3D-plane offering connectivity anytime, anywhere 
 
IoT Architecture 
A gateway is responsible for collecting data from IoT and preforming processed data before sending to the 
cloud


### Slide / Page 518

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - | Buildings
> - Energy
> - Consumer
> - and Home
> - Healthcare
> - and Life Science
> - Transportation
> - Commercial/institutional
> - Industrial
> - Supply/Oemand
> - Alternative
> - Oil/Gas
> - Infrastructure
> - Awareness & Safety
> - Convenience & Entertainment
> - Care
> - In Vivo/Home
> - Research
> - Non-Vehicular
> - Vehicles
> - Trans Systems
> - Airports, Stadiums
> - Process, Clean Room, Campus
> - Power Gen, Trans & Dist, Low Voltage, Power
> - Quality, Energy management
> - Solar Wind, Co-generation, Electrochemical
> - Rigs, Derricks, Heads, Pumps, Pipelines
> - Wiring, Network Access, Energy management
> - Security/Alerts, Fire Safety, Elderly, Children, Power
> - Protection
> - HVAC/Climate, Lighting, Appliance, Entertainment
> - Hospital, ER, Mobile, POC, Clinic, Labs, Doctor
> - Office
> - Implants, Home, Monitoring Systems
> - Orug Discovery, Diagnostics, Labs
> - Air, Rail, Marine
> - Consumer, Commercial, Construction, Off-Highway
> - Tolls, Traffic mgmt., Navigation
> - Office, Education, Retail, Hospitality, Healthy
> - Turbines, Windmills, UPS, Batteries, Generators,
> - Meters, Drills, Fuel Cells, etc.
> - Digital Cameras, Power Systems, MID, e-Readers,
> - Dishwashers, Desktop Computers, Washing
> - Machines/Oryers, Meters, Lights, TVs, MP3
> - Devices, Games Consoles, Alarms, etc.
> - MRI Machines, PDAs, Implants, Surgical
> - Equipment, Pumps, Monitors, Telemedicine, etc.
> - Vehicles, Lights, Ships, Planes, Signage, Tolls, etc.


### Slide / Page 519

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - oo0oogoogoogoogoogoagoo0o0
> - IoT Technologies and Protocols
> - Short-range
> - Wireless
> - Communication
> - Bluetooth Low Energy (BLE)
> - Light-Fidelity (Li-Fi)
> - Near Field Communication (NFC)
> - QR Codes and Barcodes
> - Radio Frequency Identification (RFID)
> - Thread
> - Wi-fi
> - Wi-Fi Direct
> - Z-wave
> - ZigBee
> - ANT
> - Communication
> - Q Ha-Low i
> - Q LTE-Advanced
> - Q GLoWPAN
> - Q auic
> - ong-range
> - Wireless
> - Communication
> - \
> - Q Low-power Wide-area Networking
> - (LPWAN)
> - o LoRaWAN
> - © Sigfox
> - © Neul
> - Q Very Small Aperture Terminal (VSAT)
> - Q Cellular
> - Q mattT
> - Q NB-loT


### Slide / Page 520

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - IoT Technologies and Protocols (Cont’d)
> - Wired
> - IoT Application
> - Communication byes ‘Operating tsHRhANAtit Protocols
> - =a! sernaEAAMUSNNERSTTANIAEENTS AAOREMEURN SY]
> - .O Ethernet O Windows 10107 ARM mbed 0s Q CoaP
> - Q Multimedia over Coax OQ. Amazon FreeRTOS \ Gizeptyr Q Edge
> - Alli MoCA
> - Meneoreny Q Contiki O Nucleus RTOS O wm
> - QO Power-line : d
> - Gommunication tlc) Q Fuchsia Q Nuttx RTOS Q Physical Web
> - QO RIOT Q Integrity RTOS Q xmpe
> - Q Ubuntu Core Q Mihini/M3DA
> - Copyright © by Eo Council) All Rights Reserved. Reproduction suicty Prony Fi


### Slide / Page 521

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Layers of the
> - IloT Architecture
> - RERESES REA AR EAN Applications Processes, Practices,
> - User _Device(s) _ Gateway Connection Cloud (CRM, ERP, SCM) PLM) __and Policies
> - Device Layer Communication Layer Cloud Platform Layer Process Layer


### Slide / Page 522

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - IoT Communication Models
> - Device-To-Cloud Model
> - Application
> - aieest "Service Provider
> - fo aS eee
> - ¥ VEE 802.25.4 (LR-WPRAN)
> - se
> - ©
> - Light Bulb from Wireless Network Light Switch from ws
> - manufacture manufacturer B +f o hve
> - ¥ Bluetooth Device with Hi af
> - v 2wave Device with
> - Temperature
> - Y Tigbee pasta Carbon Monoxide
> - Sensor
> - im Device-to-Gateway Model {} 4 _ Cloud-to-Cloud (Back-End Data-Sharing Model)
> - Application y { Protocol Stack
> - ~ ure Service Provider CoAP ike Application
> - CMS ee 4 944.7 OTS a Service Provider #2
> - er" > 1Pva/IPV6 hancoee ' hase porate
> - ! a" 4 10 ¢ ~ upp ' | 4 lgdebitadted eth Application an” HTTPS
> - \ Y V6 W/ ¥ IPV6 i &) } add il Service Provider #1, Oauth 2.0
> - — : LocalGateway =: pt kaneett hice JSON
> - Device witl f ! : vee ian
> - inte ere Local Protec! b// soaihow atch Sensor sn  Apptication
> - Snpersture ¥ Bluetooth smort Carbon Monoxide Service Provider #3 f
> - Sensor ~ (EE 802.12 (Wi-Fi) Sensor \
> - Copyright © by EG-Coumcil. All Rights Reserved. Reproduction is Strictly Pro!


### Slide / Page 523

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - With no or inadequate focus on loT device security by manufacturers,
> - security measures used to harden the IoT device are often insufficient
> - Therefore, organizations should focus on countering attack scenarios in
> - loT-enabled environments. Organizations should focus on securing
> - network devices and routers in an loT-enabled environment. This helps
> - restrict the attacker from accessing other parts of the network and
> - performing targeted attacks
> - The organization should use multilayered management. An overarching
> - multilayered security plan and constant maintenance are necessary to
> - effectively secure all these disparate loT devices
> - Company-wide collaboration and synchronization are required to secure
> - an loT-enabled environment


### Slide / Page 524

Overview of Security in IoT-Enabled Environments 
13.2 
 
IoT System Management 
 
Device Management 
 
è Ensures secure data transmission  
 
User Management 
 
è Provides control over the users and their access protocols on an IoT System. 
 
Security Monitoring 
 
è Detects and prevents potential threats in an IoT system


### Slide / Page 525

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - SiSck wise IoT Security Principles
> - WANS | Applications Processes, Practices,
> - User Device(s) _ Gateway Connection, |) Cloud {cana Ene, Sc SCM, PLM) and Policies
> - —_—_ eee ea GEe LEAL SRARARE EAT ee
> - oll = a sl 7 \\ amt
> - = oS
> - S
> - Baa vi
> - Secure Device Layer Secure Communication Secure Cloud Layer Secure Process
> - Layer Layer


### Slide / Page 526

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - EDGE
> - Communications encryption
> - Storage encryption
> - Update components
> - No default passwords
> - GATEWAY
> - Multi-directional encrypted
> - communications
> - Strong authentication of all
> - the components
> - Automatic updates
> - CLOUD PLATFORM
> - Encrypted communications
> - Secure web interface
> - Authentication
> - Encrypted storage
> - Automatic updates
> - IoT
> - Framework
> - Security
> - Considerations
> - MOBILE
> - * Local storage security
> - = Encrypted communications
> - channels
> - * Multi-factor authentication
> - = Account lockout mechanism +
> - f
> - f


### Slide / Page 527

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - IoT Device Management
> - QO) loT device management helps in supporting loT solutions by using any software tools
> - and processes and helps in onboarding latest devices securely and promptly
> - IoT Device
> - Management Solutions
> - ~ Oracle loT Asset Monitoring Cloud
> - hitps://www.orocle.com
> - > Predix
> - hittps://www.ge.com
> - ~ Cloud loT Core
> - https://cloud.google.com
> - ~ 18M Watson loT Platform
> - https-//www.ibm.com
> - ~ AT&T loT Connectivity Management
> - https://www.business.ctt.com
> - https fannie murosott col


### Slide / Page 528

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - IoT Security Best Practices
> - 1
> - Disable the “guest”
> - and “demo” user
> - accounts if enabled
> - )
> - Implement IPS and
> - IDS in the network
> - 2
> - Use the “Lock Out”
> - feature to lock out
> - accounts for excessive
> - invalid login attempts —
> - 6
> - Implement end-to-end
> - encryption and use
> - Public Key
> - Infrastructure (PKI)
> - 3
> - ‘Implement strong
> - authentication
> - “mechanisms
> - ; f;
> - Use VPN architecture
> - for secure
> - communication
> - 4
> - Locate control system
> - networks and devices
> - behind firewalls and
> - isolate them from the
> - business network
> - 8
> - Deploy security as a
> - unified, integrated
> - system


### Slide / Page 529

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - SeaCat.io
> - https://teskalabs.com
> - Digicert loT Security Solutions
> - https://vaww.digicert.com
> - FortiNAC
> - https://www.fortinet.com
> - er
> - a
> - _ Cisco loT Threat Defense
> - https://vaww.cisco.com


### Slide / Page 530

Understanding OT Concepts, Devices, and Protocols 
13.3 
 
What is OT 
 
Operational technology is the software and hardware designed to detect or cause changes in industrial 
operations through direct monitoring or controlling indus. Physical devices 
 
For the purpose to monitor and control the industrial operations 
 
TERMINOLOGY 
 
Asset: Physical Assets  
 
Zones and Conduits: Network segregation technique to isolate networks and assets to have a strong access 
control mechanisms 
 
Industrial Network: Automated Control systems that connects devices and systems in manufacturing and 
industrial to enable communication and control 
 
Business Network: Information infrastructure to the business


### Slide / Page 531

Indus. Protocols: Serial communication and communication over standard ethernet 
 
Network Perimeter: Boundary that separates an organization’s internal network from external networks 
through protected security measures 
 
Cloud Infrastructure: Virtualized hardware and software provided over the internet for cloud computing 
services 
 
Electronic Security Perimeter: Boundary between secure and insecure zones 
 
Critical Infrastructure: Collection of physical or logical systems and assets that would impact the security, 
safety, economy, or public health. 
 
 
IIOT: 
 
Combination of IT computing systems and OT operation monitoring systems to fill up the gap between 
IT/OT technologies for improving overall security, efficiency, and productivity. 
 
Enables IT/OT convergence can enable smart manufacting aka indus. 4.0 where IoT applications are used in 
indus. Operations


### Slide / Page 532

Introduction to ICS: 
Collection of different types of control systems and their associated equipment. 
 
Several Types of Control: SCADA, DCS, BPCS, SIS, HMI, PLCs, RTU, IED,…  
 
 
 
 
Supervisory Control and Data Acquisition (SCADA): 
 
è Centralized supervisory control system that used to control and monitor indus. facilities and 
infrastructure of multiple inputs and outputs with the data transmission system and Human 
Machine Interface (HMI) software 
Programming Logic Controller (PLC): 
 
è Small solid-state control computer where instructions can be customized to perform a specific task 
 
CPU Module: Central processor and its mem component 
 
Power Supply Module: Provides a neccassry supply of power required for the CPU and I/O  
 
I/O Modules:  Connects sensors and acquator  with the system for sensing and controlling RT values such 
as pressure, temp, and flow


### Slide / Page 533

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - International OT Security Organizations
> - Q Global cybersecurity organizations such as OTCSA and OT-ISAC are committed to providing appropriate
> - security policies and insights into improving the security resilience of critical infrastructures
> - Operational Technology Cyber
> - Security Alliance (OTCSA)
> - > OTCSA educates operators and manufacturers | ” Wea Operstiond Factations Ofcet Sects Amanee
> - with constant technical awareness and provides . 4 Meeting the security
> - guidelines to apply essential changes, updates, i] ai challenges of a digital world
> - integrations, etc. } a ° é
> - Pa
> - March 31,2021
> - MITRE ATT&CK for ICS: How OT Stakeholders Can Benefit
> - Copyright © by EC-Camncil. Al Rights Reserved. Reproduction fs Strictly Prohiliie


### Slide / Page 534

Overview of Security in OT-Enabled Environments 
13.4


### Slide / Page 535

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Firewalls
> - ti Unified Identity
> - i and OT Access
> - 5 Management
> - Asset Inventory
> - and Device
> - Kuthorization
> - j } Hii i
> - {jjor Network
> - ‘Monitoring and
> - / Bnomaly Detection
> - Decoys to
> - fee] Deceive
> - ooo Attackers
> - Firewalls are used in the network for monitoring and controlling the incoming and outgoing network
> - traffic
> - You can use firewall solutior:s such as SCADAWall, and Waterfall for securing the OT network
> - Access management helps industries to centralize certain operations like adding, securing, changing, and
> - removing user access to the OT systems
> - You can use tools such as OTaccess, and FireEye for identifying and managing access to industrial systems
> - Asset inventory helps in SonneCenE, only euthorized devices to the network and detect vulnerabilities
> - in the devices OY
> - You can use tools such as scapsfence, and cyberten for asset inventory and device authorization
> - : OT network monitoring employs machine tearing algorithms for easy detection and identification of
> - malicious behaviors
> - - You can use tools such as Claroty, and OT ThreatFeed for OT network monitoring and anomaly detection
> - Decoys are honeypots used in OT environments to lure attackers to reveal their presence and activities
> - You can use decoy tools such as ThreatDefend, Conpot, and GasPot for protecting the network f
> - {


### Slide / Page 536

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - OT Security Tools
> - ; Flowmon empowers manufacturers and utility companies to ensure the
> - © Flowmon reliability of their industrial networks to avoid downtime and disruption
> - _ of service continuity
> - | fro meere mmeneeena ryren tenable.ot
> - atasnchtaded https://wwwetenable.com
> - Forescout
> - https://www.forescout.com
> - UR,
> - to: \ PA-220R
> - Yast )  https://www.paloattonetworks.com
> - te
> - D> Pats er tae ete emtern et
> - Nozomi Networks Guardian™
> - https://www.nozominetworks.com
> - Fortinet ICS/SCADA solution
> - hitps://www.fortinet.com
> - ?



---

## 🛠️ Connecting Theory to Practice
- **Execute the Lab:** Open [`labs/lab-03-tcp-wireshark-deep-dive.md`](../../labs/lab-03-tcp-wireshark-deep-dive.md) to work through the practical workshop reinforcing this module.
- **Reference Card:** Check [`cheatsheets/cct-exam-quick-reference.md`](../../cheatsheets/cct-exam-quick-reference.md) for rapid command syntax, formulas, and port mappings.
