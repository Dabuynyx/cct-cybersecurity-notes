# Module 08: Network Security Assessment Techniques and Tools

> **Source Material:** Authentic CCT Study Notes & Slide Deconstructions (Pages 385 – 423)  
> **Author:** [@Dabuynyx](https://github.com/Dabuynyx)  
> **Related Hands-on Lab:** [lab-05-nmap-recon-and-vulnerability-scan.md](../../labs/lab-05-nmap-recon-and-vulnerability-scan.md)  
> **Quick Reference:** [nmap-and-wireshark-commands.md](../../cheatsheets/nmap-and-wireshark-commands.md)

---

## 🧭 My Complete Study Notes & Slide Walkthroughs

### Slide / Page 385

Module 8 
Network Security Assessment Techniques and Tools:- 
Lesson 1 
Overview of Threat Hunting: 
 
Threat hunting is the continuious approach of searching networks, devices, endpoints, and 
databases to identify and isolate the cyber threats that have entered a network by evading 
the current security systems


### Slide / Page 386

Types of threat hunting 
 
A. Data-driven Hunting:  
- Analyzing large volumes of data to identify patterns that may indicate threats 
 
- Uses data analytics, machine learning, and statistical analysis 
 
B. Intel-Driven Hunting:


### Slide / Page 387

- Based on threat intelligence information used by attackers such as indicators of 
compromise (IOSs) and tactics, techniques, and procedurers (TTPs) 
 
- Relies on external threat feeds and internal intelligence sources 
 
C. Entity-Driven Hunting:  
 
- Focuses on specific entities 
 
- Monitors behaviour and activity of these entities to detect unusual or malicious action  
 
 
D. TTP-Driven Hunting:  
  
- Centers on identifying threats based on tactics, techniques, and procedurs used by 
attackers 
 
- Uses frameworks like MITRE ATT&CK to understand and hunt for specific attack patterns


### Slide / Page 388

E. Hybrid Hunting:  
 
- Combines elements from multiple hunting methodologies (e.g. data-driven, intel-driven, 
TTP- driven). 
 
- Leaverges the strengths of different hunting strategies


### Slide / Page 389

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - LEVEL
> - L oa 2
> - oo : PROCEDURAL
> - 2 MINIMAL ays sie pe
> - porates threat
> - INITIAL
> - »
> - a
> - 3
> - INNOVATIVE oucomset (| igh
> - : Shalyare janes
> - hgh ca aera
> - Hightsewer: Sign js\eh eae
> - ile ee


### Slide / Page 390

Threat Hunting Considerations: 
 
à Intelligence Fusion:  Combines security with threat intelligence and other cyber 
intelligence sources 
 
à Threat Feeds: Continuous data stream that collects information from real-time attacks. 
Includes Incident of Compromise (IoC), Potential Threats, Vulnerabilities, existing risks. 
 
à Advisories and Bulletins: Informative blogs that provide information about the latest 
security threats and attacks 
 
à Maneuver:  Strategic actions and techniques used to continuously detect, investigate, 
and respond to potential security threats


### Slide / Page 391

Lesson 2: 
Understanding Various Threat Intelligence Feeds and Sources- 
 
Cyber Threat Intelligence (CTI): 
 
- The collection and analysis of information about threats, adversaries, and drawing 
patterns that provide an ability to make knowledgeable decisions against cyber-attacks. 
 
- CTI help organizations to identify and mitigate various business risks by implementing 
various advanced and proactive defence strategies.


### Slide / Page 392

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Se wallarm
> - Long-term Use
> - Strategic
> - High level information on
> - hanging risks
> - IT Service Administrators
> - and SOC Managers
> - Technical
> - Spesific OC
> - ming attack


### Slide / Page 393

Layers of Threat Intelligence: 
 
- An intelligence provide can be an open-source community, or movement, or a private, 
or a commercial body that provides threat intelligence as sources, TI feeds, platforms, 
and professional service 
 
TI Feeds: 
 
- Continuous streams of packaged data related to potential or current threats to an 
organization. 
-  
Examples of websites providing freely available TI feeds: 
• SHODAN 
• Threat Connect 
• Virus Total 
• AlienVaults Open Threat Exchange (OTX) 
• Zeus Tracker 
• The dark web 
 
TYPES OF SOURCES:


### Slide / Page 394

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - ‘Commercial Services:
> - lligence provided
> - lized vendors that
> - offer paid services and
> - subscriptions for detailed |
> - ‘and curated data.
> - Vertical Communities:
> - Data shared within
> - industry-specific groups
> - ‘and forums where
> - members exchange
> - Types of Threat
> - Intelligence
> - Dark Web: Intelligence
> - gathered from hidden
> - parts of the internet
> - ‘where cybercriminals
> - operate and trade
> - information.
> - Open Source: Information
> - gathered from publicly
> - available sources such as
> - news articles, blogs, and
> - social media.
> - Sources
> - In-House: Intelligence
> - collected and
> - analyzed intermally by
> - an organization's
> - security team.


### Slide / Page 395

Open-Source Intelligence (OSINT): 
 
- Public available sources such as the media, internet, Public Government data, corporate-
funded sources, and literature are analyzed to obtain rich information 
 
 
Human Intelligence (HUMINT): 
 
- Information is collected from others 
 
Signals Intelligence (SIGINT): 
 
- Gathered by intercepting communication signals such as communication intelligence, 
electronic intelligence, and foreign instrumentation signal intelligence. 
 
 
Technical Intelligence (TECHINT): 
 
- Information is gathered by adversary’s equipment


### Slide / Page 396

Social Media intelligence (SOCMINT) 
 
Cyber Counterintelligence (CCI): 
 
- Information is gathered by established security infrastructure by implementing threat 
manipulation techniques as traps. 
 
CCI Sources: 
 
- Honeypots 
- Passive DNS monitors 
- Online Web Trackers 
- Sock puppets (Fake Profiling) on online forums 
- Publishing false reports


### Slide / Page 397

Indicators of Compromise (IoCs): 
 
- Information is gathered from network security threats and breaches 
 
IoCs Sources: 
 
- Commercial and industrial sources 
- Free IoC specific sources 
- Online security-related sources 
- Social media and news feeds 
- IoC buckets 
 
Industry Association and Vertical Communities 
 
- Information is gathered from organizations that share intelligence among each other 
 
Vertical Community sources:


### Slide / Page 398

- Financial Service Information Sharing and Analysis Center (FSI-IFAC) 
 
- Malware Information Sharing Platform (MSIP) 
- Information Technology – Information sharing and Analysis Center (Information 
Technology (IT-ISAC) 
 
Commercial Sources: 
 
- Information is gathered from commercial entities and security vendors 
 
Sources: 
 
- Kaspersky Threat Intelligence 
- McAfee 
- Avast 
- FortiGuard 
- SecureWorks 
- Cisco 
 
Government and Law Enforcement Sources:


### Slide / Page 399

- US Computer Emergency Response Team (US-CEMT) 
- European Union Agency for Network and information security (ENSIA) 
- FBI Cyber Crime 
- StopThinkConnect 
- CERIAS Blog 
 
 
Deep and Dark Web Searching 
 
Surface Web: Online Cyberspace via simple browsers like Google, Firefox, and Opera 
 
Deep Web: Hidden and unlisted web pages that cannot be accessed via simple browsers. 
Accessible by search engines like DeeperWeb and Surfwax 
 
Dark Web/ Dark Net:   
Enables anyone to navigate anonymously 
Accessible by browsers like TOR Browser, Freenet, GNUnit, I2P, OneSwarm, and Retroshare


### Slide / Page 400

Deep and Dark Web Searching Tools:  
A VPN is used and bounces network IP address through several servers before interacting 
with web 
 
AI and Predictive Analysis for Threat Hunting: 
 
AI-based correction in cybersecurity involves using machine learning to detect, analyze, and 
automatically remediate security threats and vulnerabilities in real-time, ensuring 
continuous protection and compliance. 
 
Threat Intelligence Frameworks: 
 
MISP is used for sharing, storing, and identifying IoC 
 
Sources: 
 
- TC Identify 
- Yeti 
- ThreatStream 
- IBM X-Force Exchange


### Slide / Page 401

- IntelMQ 
 
 
 
Standards and Formats for Sharing Threat Intelligence: 
 
CybOX: Cyber Observable eXpression is a standardized language for encoding and 
communicating high-precision information about cyber observables 
 
Structure Threat Information Expression 
 
Trusted Automated Exchange of intelligence information: 
 
Application Layer Protocol for the communication of CTI in a simple and scannable manner


### Slide / Page 402

8.3 Overview of vulnerability Research 
 
Vulnerability Research: 
 
- Process of analyzing the network system to discover vulnerabilities and design flaws that 
will expose an OS to an attack 
 
Security level is ranged from Low → Medium → High 
 
01.  Gathering information concerning security concerns, attack vectors, and techniques 
 
02.  To discover weaknesses in the system and alert the network administrator before a 
network attack 
 
03.  Gathering information to prevent security issues


### Slide / Page 403

04.  To know how to recover from a network attack 
 
 
Vulnerability Assessment: 
 
The process analyzing vulnerabilities in an infrastructure to detect and examine security 
weaknesses that could be exploited by attackers 
  
This recognizes, measures, and classifies security vulnerabilities in a computer system, 
network, and communication channels 
 
→ Identifies weaknesses 
 
→ Predict the effectiveness of additional security measures 
 
Vulnerability scanning information: 
 
- OS Version 
-  Open ports and running services


### Slide / Page 404

-  Application and service vulnerability 
-  Application and service configuration errors 
-  Accounts with weak passwords 
- Missing patches and hotfixes 
 
Vulnerability Scanning Approaches: 
 
Active scanning (AKA Intrusive scanning): 
-  Attacker Interacts directly with the target network to find vulnerability 
- Example: An attacker sends probes and specific requests to the target host to identify 
vulnerabilities 
 
Passive Scanning (AKA Non-intrusive scanning): 
 
- Attacker does not directly interact with the target network 
 
- Example: Observing the data that’s being transmitted by others such as MAC addresses, 
Network traffic patterns, and unencrypted data being transmitted.


### Slide / Page 405

- HARDER TO DETECT & DOES NOT DISRUPT NETWORK 
 
Vulnerability Scoring Systems and Databases: 
 
- A quantitative method used for finding characteristics and impacts of IT Vulnerabilities.  
 
- It also allows users to view underlaying vulnerability characteristics used to generate 
values 
 
Common Vulnerabilities and Exposures (CVE):  
 
- Public database of information security issues 
 
National Vulnerability Database (NVD):  
 
- U.S. Government repository of vulnerability management data using the Security 
Content Automation Protocol 
 
- NVD includes security analytics


### Slide / Page 406

Common Weakness Enumeration (CWE) 
 
- Category for software vulnerabilities and weaknesses 
 
- Over 600 catagories of vulnerabilitieis used as a baseline for weakness, identification, 
mitigation, and prevemtion 
 
Types of Vulnerability Assessment: 
 
  Active Assessment: Network scanner to find hosts, services, and vulnerabilities 
 
  Passive Assessment: Used to sniff network traffic to observe the network system and 
vulnerabilities 
 
External Assessment: Assesses the network from a hacker’s view for the outside world 
 
Internal Assessment: Scans the internal infrastructure to discover exploits and 
vulnerabilities


### Slide / Page 407

Host-based Assessment: Conducts a configuration-level check to identify system 
configurations, user directories, file systems, and registry settings. 
 
Network-based Assessment: Determines possible network security attacks that may occur 
on the network’s system 
 
Application Assessment: Examines the elements of the web infrastructure for any 
vulnerabilities 
 
Database Assessment: Tests database for the presence of data exposure or injection type 
vulnerabilities 
 
 Wireless Network Assessment 
 
Credentialed Assessment: Obtains the credentials of all machines present in the network 
 
Manual Assessment


### Slide / Page 408

Distributed Assessment: Accesses distributed assets such as client and server application, 
simultaneously through synchronization techniques  
Non-Credentialed Assessment 
 
Automated Assessment: Ethical hacker employs several vulnerability assessment tools such 
as Nessus, Qualys, GFI LanGuard, etc…  
 
 Vulnerability-Management Life Cycle 
 
1. Identify Assets and Create a Baseline 
 
2. Vulnerability Scan 
 
3. Risk Assessment 
 
4. Remediation 
 
5. Verification


### Slide / Page 409

6. Monitor 
 
 
 
Overview of Ethical Hacking concepts 
Lesson 4 
 
What is Ethical Hacking? 
 
- Use of hacking tools, tricks, and techniques to identify vulnerabilities and ensure system 
security 
 
- Simulates the techniques used by hackers to check exploitable vulnerabilities in a system 
 
- Ethical hackers have permission to preform security assessments 
 
Scope and Limitations of Ethical Hacking 
 
Scope: EH plays a key role in risk assessment, auditing, and information security. It helps 
identify risks, highlights solutions and reduces ICT costs by fixing vulnerabilities


### Slide / Page 410

Limitations: Ethical hacker can only help the organization to better understand its security 
systems; its up to the organization to place the right safeguards on the network 
Understanding Fundamentals of Penetration Testing and Benefits 
Lesson 5 
 
What is Penetration Testing? 
 
- Type of security testing that evaluates an organization’s ability to protect its 
infrastructure against internal and external threats 
 
- Effective way to determine the efficacy of the organization’s security policies, controls, 
and technologies 
 
- Simulates a similar attack to real attackers to conduct an evaluation of the organization’s 
security 
 
Return on Investment (RO) For Penetration testing: 
 
- Penetration tests help identify, understand, and address any vulnerabilities


### Slide / Page 411

- Companies spend resources only if they know the pen test has known benefits 
ROI = (Benefits – Cost / Cost) x 100 
Rules of Engagement 
 
- Pen test requires formal permission 
 
- ROE provides “top-level” guidance 
 
- ROE helps testers overcome legal, federal, and policy-related restrictions to use various 
pen test tools and techniques 
 
- Scoping and ROE need to be handled independently while engaging in a pen test 
assignment 
 
- Scooping defines what should be tested 
 
- ROE defines on how the test should be performed within certain limitations and rules 
during pen testing


### Slide / Page 412

- ROE specifies the manner of how the pen test will be conducted 
 
 
 
Security Audit: 
 
- Assures the organization follows standard policies and procedures 
 
Vulnerability Assessment: 
 
- Focuses on discovering the vulnerabilities in an information system without indicating if 
it could be exploited or the amount of damage 
 
 
 Blue Teaming: 
 
- Analysis of how sufficient the necessary controls are in place to meet the basic 
requirements and address the expected risks and how efficient is the security measures 
implemented in terms of use, cost and performance.


### Slide / Page 413

- Blue team has access to all organizational resources and information  
 
- Primary role is to detect and reduce red team (attackers) activities, and to predict how 
surprise attacks might occur 
 
Red Teaming: 
 
- An approach where Ethical hackers perform penetration test on information system 
with no or very limited access to the organization’s internal resources 
 
- Can be conducted with or without warning 
 
- Primary role is to detect network system vulnerabilities and check security from an 
attacker’s prespective approach to network, system, or information access. 
 
Purple Teaming: 
 
- A purple team includes both the blue team and red team members


### Slide / Page 414

- Knowledge comes from both blue and red 
 
- Purple team can establish continuous communication, provide real-time feedback, 
preform frequent security auditing and threat hunting, implement latest defensive 
techniques, etc…  
 
 
phis Teaming: 
 
- White team acts as a negotiator for an engagement between a red team and blue team 
 
- Only monitors the activities of both the blue team and red team 
 
- Responsible for gaining insight by conduct post-engagement activities such as 
debriefing, reviewing performance, reporting, and providing recommendations. 
 
Strategies of Penetration testing: 
 
Black Box: No knowledge of the target network


### Slide / Page 415

White Box: Everything is known of the target network 
 
Gray Box: Some knowledge is known 
 
Each test strategy has different approach to assess security of the organization’s 
infrastructure. 
 
Penetration Testing Process: 
 
Defining the Scope 
 
• Extent of testing 
• What will be tested 
• Where testing will be performed from 
• Who will perform testing 
 
Performing the Penetration Test 
 
• Involves gathering all information significant to security vulnerabilities


### Slide / Page 416

• Involves testing the targeted environment such as network configuration, topology, 
hardware, and software 
 
Reporting and Delivering Results 
 
• Listing vulnerabilities 
• Categorizing risks as high, medium, or low 
• Recommending repairs if vulnerabilities are found 
 
Phases of Penetration Testing: 
 
01 → Pre-Attack Phase: Research (Information Gathering) 
 
02 → Attack Phase: Testing/ Exploitation 
 
03 → Post-Attack Phase: Documentation and Reporting 
 
Penetration Testing Methodologies:


### Slide / Page 417

- Various pen test frameworks and methodologies exist to help organziations choose the 
best method to conduct a successful penetration test 
 
Most used methodologies: 
- Proprietary Methodologies 
- EC-Council's LPT 
- IBM 
- ISS 
- McAfee Foundstone 
 
 
Open-source Methodologies 
- OSSTMM 
- ISSAF 
- NIST 
- OWASP 
- CREST 
 
 
Understanding the Fundamentals of Configuration Management and Asset


### Slide / Page 418

Management 
8.6 
 
What is Asset management? 
- Process of maintain organization’s assets (internal and external devices) which helps in 
the growth of the organization and in fulfilling business goals 
 
- Tracks all the information about tangibles (physical assets) and intangibles (non-physical 
assets) involved in business development 
 
 
 
Asset Identification Methods 
 
Standard Naming Conventions: 
 
- Identifies each asset individually with a unique name 
 
- Example: Barcode or RFID tag with a unique code


### Slide / Page 419

Internet Protocol (IP) Schema: 
 
- Subset information of an IP address space and the range of IP’s used in each subset 
 
 
Configuration Management: 
- Management of technical and administrative process employed to build and ensure the 
stability of a product, track real-time information, and keep the product updated. 
 
 
 
 
 
 
Elements: of Configuration Management:- 
 
- Configuration Management and Planning: Establishes guide to all actions and decisions 
within a process for managing system changes, setting guidelines for how the 
framework will be implemented and maintained.


### Slide / Page 420

- Configuration Identification: Equips the settings and baselines that determine the shape 
of the systems/subsystems, items, and development 
 
- Configuration Control: Assigns the change for recommendations, requests, and the 
tracking of the approval/disapproval status 
 
- Configuration Status Accounting: Record and reports baselines for individual 
configuration items at a point in time 
 
- Configuration Verification and Audit: Reviews independently of software and hardware 
to assess their compliance with standards, product baselines, performance 
requirements, and policies 
 
 
 
 
 
Configuration Review:


### Slide / Page 421

- Process of verifying the configuration settings of hardware and software 
devices/components such as systems, servers, and firewalls in an organization 
 
- The Security Content Autonomation Protocol (SCAP) is a standard evaluation process 
used to validate the security standard of an organization’s network and devices 
connected to the network 
 
Standard Components of SCAP: 
 
Open Vulnerability Assessment Language (OVAL):-  
 
- International information security community (I.ISA) for evaluating and reporting system 
condition 
 
- Uses XML schema to expose vulnerabilities in a system 
 
Extensible Configuration Checklist Description Format (XCCDF) 
- Language used for writing security contents such as checklists, system configuration 
procedures, and benchmarks (standards) 
Change Management:


### Slide / Page 422

- Process of managing the changes to an organization’s Information Technology systems 
and infrastructure  
 
- Main purpose is to enforce an appropriate plan for implementing and controlling 
changes, and assisting induvial to adapt 
 
1. Request Changes  
2. Analyze Impacts 
3. Approve or Deny Changes 
4. Implement Changes 
5. Document or Report Changes


### Slide / Page 423

Change Management Tools 
 
Sunview ChangeGear is an IT change management software that allows the automation of 
the capture and processing of all IT change records across an enterprise 
 
   ManageEngine ServiceDesk Plus https://www.manageengine.com 
   StarTeam https://www.microfocus.com 
   Freshservice IT Asset Management Software https://freshservice.com 
   SolarWinds Service Desk https://www.solarwinds.com 
   SysAid https://www.sysaid.com 
 
Module Summary 
- This module discussed the concepts of threat hunting. 
- It introduced cyber threat intelligence as well as various feeds and sources of threat 
intelligence. 
- This module also explained concepts related to ethical hacking and penetration testing. 
- Finally, this module presented an overview of asset management and configuration 
management.



---

## 🛠️ Connecting Theory to Practice
- **Execute the Lab:** Open [`labs/lab-05-nmap-recon-and-vulnerability-scan.md`](../../labs/lab-05-nmap-recon-and-vulnerability-scan.md) to work through the practical workshop reinforcing this module.
- **Reference Card:** Check [`cheatsheets/nmap-and-wireshark-commands.md`](../../cheatsheets/nmap-and-wireshark-commands.md) for rapid command syntax, formulas, and port mappings.
