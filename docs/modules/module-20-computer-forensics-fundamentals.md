# Module 20: Computer Forensics Fundamentals

> **Source Material:** Authentic CCT Study Notes & Slide Deconstructions (Pages 725 – 803)  
> **Author:** [@Dabuynyx](https://github.com/Dabuynyx)  
> **Related Hands-on Lab:** [lab-09-linux-incident-triage-forensics.md](../../labs/lab-09-linux-incident-triage-forensics.md)  
> **Quick Reference:** [cct-exam-quick-reference.md](../../cheatsheets/cct-exam-quick-reference.md)

---

## 🧭 My Complete Study Notes & Slide Walkthroughs

### Slide / Page 725

Chapter 20 Computer Forensics 
Understanding the Fundamentals of Computer Forensics 
20.1


### Slide / Page 726

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - 2
> - °
> - ~
> - > 1:17/12:33


### Slide / Page 728

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Types of Cybercrimes
> - Cybercrime is defined as any illegal act involving
> - a computing device, network, its systems, or its
> - applications
> - Cybercrime can be categorized into two
> - types based on the line of attack
> - Internal/Insider Attack External Attack
> - C itis an attack performed on a corporate Q) This type of attack occurs when an
> - network or on a single computer by an attacker from outside the organization —
> - entrusted person (insider) who has
> - tries to gain unauthorized access to its
> - authorized access to the network computing systems or informational :
> - assets ‘
> - O) Such insiders can be former or current
> - employees, business partners, or QO These attackers exploit security
> - contractors loopholes or use social engineering
> - techniques to infiltrate the network
> - Copyright © by tame 8


### Slide / Page 729

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Impact of
> - Cybercrimes at the
> - Organizational
> - Level
> - \
> - ol
> - [
> - 03.
> - Sudden disruption of business activit
> - 04
> - 05
> - 06
> - 07
> - eas
> - Loss of confidentiality, integrity and avail ability of information
> - stored in organizational systems
> - Theft of s sitive data
> - ules
> - Loss of customer and sta
> - ccnorder
> - Substantial reputational damage
> - ge
> - Huge financial losses
> - Penalties arising from the failure to comply with regulations
> - Copyright © by EC-Coumelll. All Rights Reserved. Reprod


### Slide / Page 730

20.2  
Understanding Digital Evidence


### Slide / Page 731

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Intro
> - D dence ed as “any information of
> - probative valu her stored or transmitted
> - wv —
> - nd leav
> - leave


### Slide / Page 732

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Types of Digital Evidence
> - Volatile Data wi
> - OQ Data that are lost as soon as the
> - device is powered off; examples
> - includesystem time, logged-on
> - user(s), open files, network
> - information, process information,
> - process-to-port mapping, process
> - memory, clipboard contents,
> - service/driver information,
> - command history, etc.
> - -
> - Non-volatile Data
> - Q Permanent data stored on
> - secondary storage devices such
> - as hard disks and memory cards;
> - examples include hidden files,
> - slack space, swap file, index.dat
> - files, unallocated clusters,
> - unused partitions, hidden
> - partitions, registry settings,
> - event logs, etc.


### Slide / Page 733

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Sources of Potential Evidence
> - Computer-Created
> - User-Created Files Files
> - User-Protected Files
> - = Address books = Backup files
> - = Compressed files
> - * Database files Log files
> - = Media (images, graphics, = Configuration files
> - audio, video, etc.) files = Encrypted files
> - = Printer spool files
> - = Documents (text,
> - spreadsheet,
> - presentation, etc.) files
> - = Password-protected files ® Cookies
> - . fil
> - * Hidden files silica
> - = Internet bookmarks, = System files
> - favorites, etc. * Steganography * History files
> - '
> - 1
> - '
> - \
> - 1
> - 1
> - 1
> - '
> - 1
> - '
> - '
> - :
> - | ©  Misnamed files
> - :
> - '
> - 1
> - '
> - '
> - '
> - 1
> - '
> - 1
> - ‘
> - '
> - '
> - '
> - '
> - 1
> - 1
> - Temporary files
> - 9
> - Copyright © by Al Rights Reserved. Reproduction bs Strictly Pro "v


### Slide / Page 734

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Sources of Potential
> - Evidence (Cont’d)
> - Device
> - i Hard Drive Text, picture, video, multimedia, database, and computer program files
> - | Thumb Drive Text, graphics, image, and picture files
> - Memory Card Event logs, chat logs, text files, image files, picture files, and internet browsing history
> - Smart Card
> - Evidence is found by recognizing or authenticating the information of the card and the user,
> - Dongle dj i \
> - 8 through the level of access, configurations, permissions, and in the device itself
> - Biometric Scanner
> - Hy a Voice recordings such as deleted messages, last called number, memo, phone numbers,
> - _ Answering Machine Baeaous
> - Digital Camera/Surveillance
> - Images, removable cartridges, video, sound, time and date stamp, etc.
> - cameras
> - Learhapetoaarenrae nena Evidence is located and can be acquired f; t i f tt
> - (RAM) and Volatile storage € acquired from the main memory of the computer


### Slide / Page 735

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Rules of Evidence
> - QO Digital evidence collection must be governed by five basic rules
> - that make it admissible in a court of law:
> - Understandable
> - Evidence must be clear and understandable to the judges
> - § Admissible
> - 5 Evidence must be related to the fact being proved
> - Authentic
> - Evidence must be real and appropriately related to the incident
> - Reliable
> - There must be no doubt about the authenticity or veracity of the evidence
> - | Complete
> - The evidence must prove the attacker's actions or his/her innocence
> - Copyright © by EC-Gomncal All Rights Reserved. Reproduction fs Strictly Prohil


### Slide / Page 736

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Best Evidence Rule
> - It states that the court only allows the original
> - evidence of a document, photograph, or
> - recording at the trial rather than a copy.
> - However, the duplicate can be accepted as
> - evidence, provided the court finds the party’s
> - reasons for submitting the duplicate to be
> - genuine
> - The principle underlying the best
> - evidence rule is that the original
> - evidence is considered as the best
> - ri evidence :
> - ————————>


### Slide / Page 737

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Federal Rules of Evidence (United States)
> - These rules shall be construed to secure fairness in administration, elimination of unjustifiable expense
> - and delay, and promotion of growth and development of the law of evidence to the end that the truth
> - may be ascertained and proceedings justly determined
> - htten J /waw ruteso!
> - Copyright © by E€-Goumell All Rights Reserved. Reproduction & Strictly Prohil


### Slide / Page 738

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Scientific Working Group on Digital Evidence (SWGDE)
> - Principle 1
> - = Inorder to ensure that the digital evidence is
> - collected, preserved, examined, or transferred
> - in a manner safeguarding the accuracy and
> - reliability of the evidence, law enforcement
> - and forensic organizations must establish and
> - maintain an effective quality system
> - Standards and Criteria 1.2
> - = Agency management must review the SOPs on an
> - annual basis to ensure their continued suitability
> - and effectiveness
> - Standards and Criteria 1.1
> - All agencies that seize and/or examine digital
> - evidence must maintain an appropriate SOP
> - document. All Rements of an agency's policies
> - and procedures concerning digital evidence
> - must be clearly set forth in this SOP document,
> - which must be issued under the agency's
> - management authority.
> - : ‘Standards and Criteria 1.3
> - Procedures used must be generally accepted in
> - the field or supported by data gathered and
> - recorded in a scientific manner


### Slide / Page 739

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - | Scientific Working Group®
> - on Digital Evidence


### Slide / Page 740

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Scientific Working Group on Digital Evidence (SWGDE)
> - Principle 1 Standards and Criteria 1.1
> - = In order to ensure that the digital evidence is * All agencies that seize and/or examine digital
> - collected, preserved, examined, or transferred evidence must maintain an appropriate SOP
> - in a manner safeguarding the accuracy and document. All elements of an agency's policies
> - reliability of the evidence, law enforcement and procedures concerning digital evidence
> - and forensic organizations must establish and must be clearly set forth in this SOP document,
> - maintain an effective quality system : Rwhich must be issued under the agency's
> - management authority.
> - Standards and Criteria 1.2 Standards and Criteria 1.3
> - = Agency management must review the SOPs on an = Procedures used must be generally accepted in
> - annual basis to ensure their continued suitability the field or supported by data gathered and
> - and effectiveness recorded in a scientific manner
> - ce


### Slide / Page 741

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - The Association of Chief Police Officers
> - (ACPO) Principles of Digital Evidence
> - | Principle 1: No action taken by law enforcement agencies or their agents should
> - change data held on a computer or storage media which may subsequently be relied
> - upon in court
> - Principle 2: In exceptional circumstances, where a person finds it necessary
> - | to access original data held on a computer or on storage media, that persay
> - must be competent to do so and be able to explain his/her actions and the
> - impact of those actions on the evidence, in the court
> - Principle 3: An audit trail or other record of all processes applied to computer based
> - electronic evidence should be created and preserved. An independent third party
> - should be able to examine those processes and achieve the same result
> - Principle 4: The person in charge of the investigation (the case officer)’ has overall
> - responsibility for ensuring that the law and these principles are adhered to i wily it
> - ‘itl
> - HEC
> - Atte //wiew dated gf
> - q


### Slide / Page 742

Identify the Roles and Responsibilities of a Forensic Investigator 
20.3


### Slide / Page 743

20.3 
Understanding the Forensic Investigation Process and Its Importamce


### Slide / Page 744

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Importance of the Forensic L ,
> - Investigation Process 7 z
> - a
> - Ss
> - \
> - "
> - Uj
> - |
> - |
> - S82)
> - =N\
> - 2
> - As digital evidence is fragile in nature, following strict bee S ie '
> - g re , aaa ‘ c o ‘a | a "
> - 6: guidelines and thorough forensic investigation process ' / — |
> - that ensures the integrity of evidence is critical to ah, Y/, 2
> - prove a case in the court of law | “on ‘
> - ~
> - 6100 1000 ih
> - ) Y TNOOD 4)
> - The forensics investigation process to be i“ 7 (7 \ “=
> - followed should comply with local laws and ‘| pee ta,
> - established precedents. Any breach/deviation
> - may jeopardize the complete investigation
> - The investigators must follow a repeatable and well-
> - yo documented set of steps such that every iteration of
> - ©) analysis provides the same findings; else, the findings il 4 LNG ‘ er q@. ft
> - of the investigation can be invalidated during the cross
> - Fo Uh Irae itr ab
> - examination in a court of law


### Slide / Page 745

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Phases Involved in the Forensics Investigation Proces:
> - ©
> - Pre-investigation
> - Phase
> - QO Deals with tasks to be
> - performed prior to the
> - commencement of the actual
> - investigation
> - O Involves setting up a computer
> - forensics lab, building a
> - forensics workstation,
> - developing an investigation
> - toolkit, setting up an
> - investigation team, getting
> - approval from the relevant
> - authority, etc.
> - Q The main phase of the
> - computer forensics
> - investigation process
> - Q Involves acquisition,
> - preservation, and analysis of
> - evidentiary data to identify the
> - source of the crime and the
> - culprit behind it
> - Post-investigation
> - Phase
> - Q Includes documentation of all
> - actions undertaken and all
> - findings uncovered during the
> - investigation
> - Q Ensures that the report is easily
> - explicable to the target
> - audience and that it provides
> - adequate and acceptable
> - evidence


### Slide / Page 746

Understanding Various Forensic Investigation Phases 
20.5


### Slide / Page 747

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Pre-investigation Phase: Setting Up a Computer Forensics Lab
> - A Computer Forensics Lab (CFL) is a location that houses instruments, software and hardware tools, and forensic
> - workstations required for conducting a computer-based investigation with regard to the collected evidence
> - 1
> - Planning & budgeting
> - considerations
> - Number of expected cases *
> - Type of investigation
> - Manpower
> - & & &*&
> - Equipment and software requirement
> - 4
> - EEE SEE SERRE EE
> - Physical security considerations
> - ¥ Electronic sign-in
> - Y Intrusion alarm systems
> - ~ Fire suppression systems
> - 2
> - Physical & Structural design
> - considerations
> - ¥ tabsize
> - Y Access to essential services
> - ~ Space estimation for work area and
> - evidence storage
> - ~. Heating, ventilation, and air-conditioning
> - BE)
> - Human resource considerations
> - ¥ Number of required personnel
> - Vv Training and certification
> - 3
> - Work area considerations
> - Workstation requirement
> - Ambience
> - Internet, network and communication line
> - SRE
> - Lighting systems and emergency power
> - 6
> - Forensic lab licensing
> - Y ASCLD/LAB accreditation
> - ¥ ISO/IEC 17025 accreditation


### Slide / Page 748

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Pre-investigation Phase: Understanding the Hardware and
> - Software Requirements of a Forensic Lab
> - QO Adigital forensic lab should have all the necessary hardware and software tools to support the investigation process,
> - starting from searching and seizing the evidence to reporting the outcome of the analysis
> - |, @=sse Ss
> - Hardware | ! Software
> - H |
> - > Two or more forensic workstations with godd | : | > OSes
> - processing power and RAM : | & Data discovery tools
> - > Specialized cables | : | > Password-cracking tools
> - > Write-blockers and drive duplicators | : | & Acquisition tools
> - > Archive and Restore devices | : | > Data analyzers
> - > Media sterilization systems | : | > Data recovery tools
> - > Other equipment that allow forensic software | ' > File viewers (Image and graphics)
> - rola wor : > File type conversion tools
> - > Computer Forensic hardware toolkit, such as : > s : d Utiliti f
> - Paraben's First Responder Bundle, DeepSpar : Pre eCUn Menon uIDess onace
> - Disk Imager, FRED forensic workstation etc. : > Computer forensic software tools such as
> - o
> - Wireshark, Access Data’s FTK etc.


### Slide / Page 749

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Investigation Phase: Computer Forensics Investigation
> - Methodology
> - -Documenting the >|... pe =—Search ed Evidence
> - _ Electronic Crime Scene | and Seizure Preservation
> - é= ©
> - Case Analysis | | Data pee Data Acquisition
> - @
> - “J
> - €9 |!
> - Reporting . Expert Witness
> - ' bab = atat
> - Copyright © by Ee Commcil All Rights Reserved. Reproduction la Sirkcthy Pro Le
> - > oven | (


### Slide / Page 750

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Investigation Phase: Planning the Search and Seizure
> - K search and seizure plan should contain the following detaiz:
> - © (Cese name or title of the incident = Details of equipment to be seized


### Slide / Page 751

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Investigation Phase: Data
> - Acquisition
> - Forensic data acquisition is a process of imaging or collecting
> - information from various media in accordance with certain
> - standards for analyzing its forensic value
> - Investigators can then forensically process and
> - examine the collected data to extract information
> - relevant to any particular case or incident while
> - protecting the integrity of the data
> - It is one of the most critical steps of digital forensics as
> - improper acquisition may alter data in evidence media,
> - and render it inadmissible in the court of law
> - Investigators should be able to verify the accuracy of acquired
> - data, and the complete process should be auditable and
> - acceptable to the court


### Slide / Page 752

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Understanding Various Forensic Investigation Phases


### Slide / Page 753

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Post-investigation Phase: Gathering and Organizing Information
> - Identification
> - Following are the procedures for gathering end organizing the
> - required documentation:
> - = Gather all notes from different phases of the investigation process
> - = identify the facts to be included in the report for supporting the
> - condusions *
> - * List all the evidence to submit with the report
> - ® lst the conclusions that need to be in the report
> - * Organize and classify the information gathered to create a concise
> - and accurate report


### Slide / Page 754

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - [=> H forensics investigation report template contains the following: alee |
> - O Executive summary i
> - Y Casenumber AH AY \
> - ¥ Names and $8tkal Security Numbers of authors, investigators, and examiners
> - Y Purpose of investigation
> - Y Significant findings
> - Y Signature analysis
> - QO Investigation objectives {
> - Q Details of the incident
> - Y Date and time the incident allegedly occurred “
> - Y Date and time the incident was reported to the agency’s personnel b
> - ~ Details of the person or persons reporting the incident
> - Q Investigation process
> - Y Date and time the investigation was assigned
> - ~ Allotted investigators
> - ¥ Nature of the claim and information provided to the investigators
> - Copyright © by £C-Gemmell. All Rights Reserved. Reproduction is Strictly Probilil


### Slide / Page 755

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Forensics Investigation Report Template (Cont’d)
> - QO Evidence information \f QO Relevant findings
> - Q Supporting Files
> - Y Attachments and appendices
> - Y Location of the evidence
> - Y List of the collected evidence
> - Y Tools involved in collecting the evidence
> - ienemnions) Y Full path of the important files
> - Y Preservation of the evidence F veecesteeui sb ioers
> - —_ xpert reviews and opinion
> - Q Evaluation and analysis Process
> - Q Other supporting details
> - Y Initial evaluation of the evidence
> - o% Y Attacker’s methodology
> - aCe anes Y User's applications and Internet
> - Y Analysis of the computer evidence activity
> - (Tools involved)
> - ¥ Recommendations


### Slide / Page 756

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Post-investigation Phase: Testifying as an Expert Witness
> - a. Presenting digital evidence in the court requires knowledge of new, specialized, evolving, and
> - ditt sometimes complex technology
> - Familiarize the expert witness with the usual procedures that are
> - followed during a trial \
> - Things that
> - take place
> - in the court
> - The attorney, introduces the Spee witness
> - xoorn
> - The opposing counsel may try to discredit the expert witness
> - ——
> - The attorney leads the expert witness through the evidence
> - Later, it is followed by the opposing counsel's cross-examination
> - a


### Slide / Page 757

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - p
> - } a
> - SOUrces: Log Elles pes OO ECO!
> - v
> - = Se Log files are system generated reports that contain information related to user activities or events that
> - occur in software applications, OSes, servers, or network communication
> - Network Logs System Logs Application Logs
> - > Network logs record events related to > System log files (Syslog) provide details >» An application log records all events or
> - system or user activities such as of process success state, devices, actions generated during the runtime o:
> - accessing a resource, performing warnings, system failures, debugs, an application
> - authentication, and details of errors, and alerts, etc. that contain
> - communication with remote hosts that critical information for investigatingan  _* +These records can be investigated to
> - contain critical information such as IP incident identify the behavior of server and
> - addresses, date, timestamp, details of details of entities (who, when, and
> - request, and response messages how) accessing the server


### Slide / Page 758

Understadning Digital Foresnic Evidence Sources to Support Foresnic Investigation 
20.6


### Slide / Page 759

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Digital Evidence Sources: Log Files (Cont’d)
> - Security logs store data related to failed logins, passwords,
> - resources accessed and allocated, date/time, and user identity
> - that help investigators in tracking the events that led to the
> - incident
> - Security Logs
> - Web access logs record information such as IP address,
> - Web Access Logs date/time of a request, client ID, request type, status code,
> - and the application used to send the request
> - DNS logs record all activities on a server, including host
> - communications with spoofed IP, unexpected spikes, and
> - inconsistent DNS lookups, which can help investigators in
> - analyzing DNS conversions bd (


### Slide / Page 760

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Digital Evidence Sources: Log Files (Cont’d)
> - Dump Files
> - Dump files are compressed
> - versions of system log files that
> - are recorded when a system
> - crashes or is turned off
> - unexpectedly
> - Processes, profiles, and other
> - security events are logged in this
> - file; this information enables
> - security teams to identify the
> - reasons for unexpected
> - shutdowns or terminations
> - Authentication
> - Logs
> - QO Authentication logs record the
> - events that occur during the
> - authentication process such as
> - verifying and granting
> - permission to access a network
> - or any restricted resource
> - QO These records help investigators
> - to identify malicious attempts
> - made by attackers
> - SIP Logs
> - Q Session Initiation Protocol (SIP)
> - logs record details about
> - connections that are established, ©
> - maintained, or disconnected for
> - applications used for
> - communication such as live
> - conferences, chats, and voice
> - calls
> - These logs contain information
> - such as request/response
> - messages, invitees, and
> - acknowledgment that helps in
> - investigating illegal or suspicious f
> - activities


### Slide / Page 761

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - SIEM Dashboards
> - SIEM dashboards visualize actionable data from various log events that
> - assist investigators in analyzing current log data and identifying abnormal
> - behavior patterns
> - »
> - Sensors
> - Sensors aggregate logs from various neighboring sources and correlate them
> - with device data, which are then used by investigators to identify patterns
> - that deviate from the normal activities of a user or the usual traffic flow in a
> - network
> - Sensitivity
> - .
> - Security specialists apply correction rules to assign sensitivity levels to
> - aggregated data; it can also be achieved by implementing Al and ML P
> - capabilities in security solutions a
> - This type of segregation based on the sensitivity level facilitates log anal’
> - during investigations \ gee


### Slide / Page 762

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - A
> - Digital Evidence
> - Automated Alerts Wi Correlation
> - Y Alerts are generated by the sensors implemented in _.¥%. Security solutions apply correlation rules to integrate
> - security solutions and network hardware appliances multiple log sources and transform the data into useful
> - when they encounter attack signatures information
> - Y They are classified based on the threat severity level
> - (low, medium, and high), which includes warning
> - alert, critical level alert, compliance alert, action
> - object alert, alert overview, and alert rules
> - Y Correlated logs help investigators to track the timeline of
> - the events that led to.a security incident , 4
> - / BE Commell All Rights Resor


### Slide / Page 763

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - sy
> - of
> - Vv.
> - Digital Evidence Sources: Bandwidth
> - Monitors and Metadata
> - Bandwidth Monitors
> - Network traffic analysis using
> - bandwidth monitors provides insights
> - into incidents and evidence, discovers
> - the footprints of attackers, and
> - identifies the degree of damage
> - Using tools such as SolarWinds
> - Network Bandwidth Analyzer Pack,
> - investigators can perceive the events
> - in a network by comparing the
> - network behavior with the standard
> - baseline
> - Metadata
> - The metadata present in file system
> - snapshots can provide easy
> - understanding of incidents during the
> - investigation process, which might
> - include unapproved deletion and
> - modification of files
> - Metadata can be acquired from
> - various data sources such as email,
> - mobile, web, and file systems
> - Investigators can use tools such as
> - Metadata Assistant, Paraben P2
> - Commander, and Metashield to 4
> - analyze metadata 4


### Slide / Page 764

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - > §:17/7:19
> - NetFlow-enabled
> - Device
> - Source/Destination IP {
> - addresses
> - IP version
> - Source/Destination
> - port numbers
> - Source Interface
> - Packets or bytes
> - Traffic flow
> - NetFlow cache
> - Packet Bytes
> - Maree bs ports.. |11003 \1435
> - ae a ae
> - )


### Slide / Page 765

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Digital Evidence Sources: Vulnerability Scan Output
> - QO Vulnerability scan reports consist of detected vulnerabilities, bugs, and configuration weaknesses, which can be exploited to
> - launch cyberattacks
> - Q The output of a vulnerability scan acts as an important evidence source during forensic investigation
> - Q It provides information on how the attack might have been performed by mapping it with the exploit database of identified
> - vulnerabilities .
> - betes //wwrer.tenatse com ; ki


### Slide / Page 766

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Digital Evidence Sources: Protocol Analyzer Output
> - Q Security solutions such as SIEM capture the network traffic from every corner and aggregate the packets to analyze them using protocol
> - analyzers
> - 3
> - Q The results of protocol analyzers can be used to troubleshoot network issues, identify the behavioral patterns of an entity by reviewing
> - the protocols used, and identify and restrict the protocols used by malicious IPs
> - } WEAR
> - i
> - oi
> - $
> - ren
> - era
> - saa wn anne
> - &ORGGHREEEEY


### Slide / Page 767

Collectiving the Evidence 
20.7


### Slide / Page 768

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Collecting and
> - Preserving
> - Evidence
> - r must have
> - eH
> - | experience toserthe
> - | Gi) Prior toiinitiating the
> - Q Applicable jurisdiction and relevant legislation
> - Q Chain of custody documentation \ ‘ee
> - * 4
> - QO Details of the equipment containing evidence: +
> - Q Approval of authorities and local management
> - SEERA
> - ‘
> - + Structure type and size 4 44 1 ‘a!
> - %
> - > Location (alli in ong Su takny the building or floors)
> - 4
> - va Type of device | . + \ eae a
> - ‘ \ ’ ;
> - + Model ALAA
> - + ‘ uA q a ee
> - > Powered status ‘ ,k4
> - »
> - Network status and type of network
> - Vv
> - ’
> - Backups (if any), intervals of SHEE last time and date, and the
> - location % \ ‘
> - Y> If necessary, take the server down and measure the business impact
> - f


### Slide / Page 769

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Collecting Physical Evidence
> - O Collect electronic devices or any other media found at the crime scene
> - Q To preserve the integrity of the physical evidence, all the pieces of evidence collected should be
> - handled carefully
> - OQ Physical evidence includes:
> - \
> - Removable media
> - Cables
> - NE
> - > Publications
> - > All computer equipment, including peripherals
> - Items taken from the trash
> - Vv
> - Miscellaneous items
> - Vv
> - QO Tag all objects identified as evidence and mention all the required details on the tag, such as the time,
> - date, incident responder’s name, and control number


### Slide / Page 770

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Dealing with Powered On Computers. =
> - Investigators must perform the following steps while
> - collecting evidence from powered on computers:
> - If a computer is switched ON and the screen is viewable, photograph
> - the screen and document the running programs |
> - If a portable computer wakes up, record the time and date at which
> - this occurs, take a photograph of the screen, and document a brief
> - explanation of all running programs
> - if a computer is ON and the monitor shows'a screensaver, move the
> - mouse slowly without pressing any mouse button and then
> - photograph and document the programs |
> - After collecting all volatile data, turn off the devices
> - For portable computers, press down the power switch for 30 seconds: : s
> - to force the power off
> - For portable computers, remove the battery and unplug the power
> - cord from the wall socket
> - If the computer is switched OFF, leave it in that state
> - Copyright © by EC-Coumell. All Rights Rese


### Slide / Page 771

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Dealing with Powered Off Computers
> - Q At this point in the investigation, do not change the state of any electronic devices or equipment:
> - > If the device/equipment is switched OFF, leave it OFF
> - QO If a monitor is switched OFF and the display is blank:
> - > Turn the monitor ON, move the mouse slightly, observe the changes from a blank screen to another
> - screen and note the changes
> - > Photograph the screen
> - QO) If a monitor is switched ON and the display is blank:
> - > Move the mouse slightly
> - = If the screen does not change after moving the mouse slightly, do not press any keys
> - > Photograph the screen +
> - Copyright © by (6-Geumcll. All Rights Reserved. Reproduction is Strictly Pro


### Slide / Page 772

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Dealing with Networked Computers
> - Unplug the network cable from the router and modem in
> - order to prevent further attacks
> - Photograph all devices connected to the victim's compute i
> - Particularly the router and modem, from several angles Hi i
> - If any devices, such as a printer or a scanner, are present |
> - near the computer, then also take photographs of those
> - devices
> - Hi ‘onicomputers: Heil
> - Unplug all cords and devices connected to the computer and
> - label them for identification


### Slide / Page 773

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Dealing with Open Files and Startup Files
> - O When malware attacks a computer system, some files are created in the startup folder to run the malware program
> - Document the date and time of the files oF) ©
> - Examine the open files for sensitive data such as
> - passwords or images
> - O The investigator can get vital information from these files
> - Open any recently created documents from the startup or
> - system32 folder in Windows and the rc.local file in Linux
> - Search for unusual MAC (modified, accessed, or changed) times
> - on vital folders and startup files
> - Use the dir command for Windows or the Is command for Linux
> - to locate the actual access times on those files and folders
> - All Rights Reserved. Reproduction bs Strictly Prohil


### Slide / Page 774

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Operating System Shutdown Procedure
> - Q Incase the investigators need to shut the systems down, they must either collect or wait for the collection of the
> - volatile data from the systems, as the system deletes it after shutting down, making it impossible to retrieve
> - O The investigators must follow the predefined shutdown procedure; otherwise, data may be lost as the hard
> - drives may crash
> - Windows Operating System
> - Mac OS X Operating System
> - UNIX/Linux Operating Systems.
> - Y Click on the Windows button
> - Y Click the Apple icon loc:
> - don he Y Right click on the Desktop and select the
> - top left-hand side Terminal option
> - ~ Click the Power (f@j)option . : ¥ 1 A s 5 ;
> - root user’s prompt is set to #sign mode:
> - i Y Select the Shut Down o
> - ~ Select the Shut Down option
> - * Enter the password if available and type
> - sync;sync;halt to shut down the system
> - * If password is not available, unplug the
> - power cord from the wall socket
> - v If itis set to console sign mode:
> - = Enter the user’s ID and press Enter
> - = if the user ID is root, type sync;sync;halt to
> - shut down the system


### Slide / Page 775

20.8  
Securing Evidence

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Evidence Management
> - OQ) Evidence management helps protect the true state of the evidence
> - QO) This is achieved by proper handling and documentation of the evidence
> - QO At the time of evidence transfer, both sender and receiver need to provide information about the
> - date and time of the transfer in the chain of custody record
> - OQ The procedures used to protect the evidence and
> - document it while collecting and shipping are:
> - e@ The logbook of the project
> - @ A tag to uniquely identify any evidence
> - @  Achain of custody record


### Slide / Page 776

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Chain of Custody
> - Chain of custody is a legal document that demonstrates the progression of evidence as it travels from the
> - original evidence location to the forensic laboratory
> - The chain of custody administers the collection, handling, storage, testing, and disposition of evidence
> - Chain of custody documentation should list all the people involved in the collection and preservation of
> - evidence and their actions, with a stamp for each activity
> - Chain of custody document contains the complete information about the obtained evidence, such as:
> - ®* Case number ,
> - = Name and title of the person from whom the evidence was received
> - * Address and telephone number
> - * Location from which the evidence was obtained
> - = Date/time of evidence
> - = Item number/quantity/ description of items ta


### Slide / Page 777

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Simple Format of the Chain of Custody
> - Document
> - Chain of Custody Document
> - rs
> - Ba Laboratory or Agency Name: 5] Case Number:
> - Date and Time
> - = Evidence Was
> - Obtained:
> - Reason Evidence Was
> - Obtained:


### Slide / Page 778

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Chain of Custody Form (Co
> - Chain of Custody Form
> - Name/Agency
> - Name/Agemy
> - Sapnature
> - Spnature
> - Name/Agency
> - Signature
> - Name/Apency
> - Name/Agemy
> - Signature
> - Signature
> - Name/Agemy
> - Namne/Agency
> - Signature
> - Signature
> - Name/Agemy Name/Agency
> - ‘Signature Signalure
> - Name/Agens ¥
> - Signature
> - Copyright © by §C-Commell. All Rights Reserved. Reproduction bs Strictly Pr


### Slide / Page 779

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Package #’ s
> - Chain of Custody Form
> - Date/Time Released By |
> - Received By
> - ie Reason
> - Date Name/Agency Name/Apency
> - Tame Signature Signature i
> - Date Name/Agency | Name /Ageucy i
> - titpe Signature Signature), : i
> - Date Name/Agency | Name/Agency
> - | tw Signature Signature
> - Date igneiigens Name/Agoncy j
> - : Sign anuie Signature j
> - X
> - ‘Date Name /Agency Nome /Agoncy f
> - } Time Sugnature Signature :
> - Date Name/Ageney Name/Agency ce i
> - Tene Signature Signature f
> - oduction bs Strictly Prohi


### Slide / Page 780

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Evidence Bag Contents List
> - The panel on the front of evidence bags
> - must, at the very least, contain the following
> - details:
> - Date and time of seizure HY
> - Investigator who seized the evidence —
> - Exhibit number ~
> - Site from which the evidence was seized a
> - Details of the contents of the evidence ba
> - oOo fn ®& WwW DN
> - Submitting agency and its address _


### Slide / Page 781

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Packaging, Transporting, and Storing Electronic Evidence
> - er Ngsetees must package, store, and transport all physical evidence for further analysis after collecting all vo
> - tion. More specifically, they must:
> - Pack all available physical evidence equipment and components
> - Label and list all devices and components
> - Avoid turning the computer upside down or putting it-on its side during transportation
> - Keep the electronic evidence collected from the crime scene away from magnetic sources such as radio
> - transmitters, speaker magnets, and heated seats
> - Store the evidence in a safe area, away from extreme heat, cold, or moisture
> - Avoid storing electronic evidence in vehicles for a long period of time
> - Maintain proper chain of custody of the transported evidence
> - Take special precautions while storing wireless and portable devices, such as laptops, mobiles, and PDAs ,
> - f
> - Ensure that these devices do not connect to networks by storing them in signal-blocking containers
> - 999900000)


### Slide / Page 782

20.9 
Overview of Data Aquisition

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Acquisition
> - Q Data acquisition is the use of established methods to extract Electronically Stored Information (ESI) from suspect
> - computer or storage media to gain insight into a crime or an incident
> - O Investigators must be able to verify the accuracy of acquired data, and the complete process should be auditable
> - and acceptable in the court
> - ‘Live Acquisition Dead Acquisition (Static Acquisition)
> - Data Acquisition
> - Categories It involves collecting data from It involves collecting data from a system that
> - a system that is powered ON is powered OFF


### Slide / Page 783

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - _Live baa Secieinio
> - ‘Volatile Information assists in determining the logic:
> - users | responsible
> - suspec Machine, removes the Wena! disk and then’ acquires its sens image
> - Types of data captured during live acquisition
> - pee
> - = ae a Sar.
> - *- Current configuration . Running processes ' 2 Routing tables
> - Running state = Logged on users ARP cache
> - Date and time . DLLs or shared libraries Network configuration
> - Current system uptime Swap files and temp files Network connections
> - P> 1:10 / 21:57
> - aD ——— | ee


### Slide / Page 784

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Live Acquisition
> - @) Liveldata)acquisition involves collecting volatile data fromiailive system
> - @) Volatile information assists in determining the logical timeline of the security incident, and the possible
> - Usersiresponsible
> - 1) Gil Live acquisition’can then)be followed by static/dead acquisition, where an investigator shuts down the
> - suspect machine) removes the harddisk and then acquires its forensic image
> - Types of data captured during live acquisition
> - Network Data
> - "Current configuration © Running processes = Routing tables
> - = Running state * Logged on users * ARP cache
> - = Date and time = DLLs or shared libraries = Network configuration Ly
> - =  Currentsystem uptime = Swap files and temp files = Network connections
> - Copyright © by [C-Cammell, Al Rights Reserved. Reproduction fs Strictty Prohibit


### Slide / Page 785

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Q When collecting evidence, an investigator needs to evaluate the order of
> - volatility of data depending on the suspect machine and the situation
> - Order of
> - Volatility According to the RFC 3227, below is an example of the order of
> - volatility for a typical system:
> - Ol = Registers and cache
> - 02 = Routing table, process table, kernel statistics, and memory
> - 03 Temporary system files
> - 04 ‘Disk or other storage media
> - Remote logging and monitoring data that is relevant to the system in
> - question
> - Physical configuration, and network topology
> - Archival media
> - Copyright © ty EC-Commell. All Rights Reserved. Reproduction fs Strictly


### Slide / Page 786

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Types of Data Acquisition
> - Logical Acquisition
> - Q Logical acquisition allows an
> - investigator to capture only selected
> - files or files types of interest to the
> - case
> - Q_ Examples of logical acquisition
> - include:
> - = Email investigation that requires
> - collection of Outlook .pst or .ost
> - files
> - * Collecting specific records froma
> - large RAID server
> - Sparse Acquisition
> - Sparse acquisition is similar to
> - logical acquisition, which in addition
> - collects fragments of unallocated
> - data, allowing investigators to
> - acquire deleted files
> - Use this method when inspection of
> - the entire drive is not required


### Slide / Page 787

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Types of Data Acquisition (Cont’d)
> - Bit‘Stream Bit-stream imaging creates a bit-by-bit copy of a suspect drive, which is a cloned copy of the
> - entire drive including all its sectors and clusters, which allows forensic investigators to retrieve
> - deleted files or folders
> - Imaging \
> - Bit-stream disk-to-image file Bit-stream disk-to-disk
> - O Itis the most common method used by forensic
> - Q Disk-to-image copying is not possible in situations where
> - investigators
> - The suspect drive is very old and incompatible with the
> - imaging software
> - QO The created image file is a bit-by-bit replica of the suspect
> - drive * Investigator needs to recover credentials used for websites
> - and user accounts
> - O Tools used: R-Drive Image, ProDiscover, EnCase, FTK, The Q To overcome this situation, investigators can create a disk-
> - Sleuth Kit, X-Ways Forensics, etc. to-disk bit-stream copy of the target media
> - 6 Tp | O While creating a disk-to-disk copy, investigators can adjust
> - | the target disk’s geometry (its head, cylinder, and track
> - configuration) to align with the suspect drive. This results Sy
> - smooth data acquisition process.
> - Q Tools used: Encase, Tableau Forensic Imager, etc.


### Slide / Page 788

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Step 1: Determine the Best Data Acquisition Method
> - O Aninvestigator needs to identify the best data acquisition method
> - suitable for the investigation, depending on the situation the
> - investigator is presented with
> - YY
> - are: required to acquire the image
> - Q These situations include: Logical/Sparse
> - = Size of the suspect drive
> - i . Whether the investigator can retain the suspect drive: an
> - O Example: =
> - = Incase the original evidence drive needs to be returned to the owne
> - as in the case of a discovery demand for a civil litigation c case, check.
> - with the requester (lawyer or supervisor) whether logical acquisit tion
> - of the disk is acceptable. If not, you may have togo back tothe —
> - requester. <= Full Image
> - Ls
> - Q Investigators need to acquire only the data that is intended tobe”
> - acquired


### Slide / Page 789

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Step 2: Select the Data Acquisition Tool
> - Mandatory Requirements
> - The tool should not change the original content
> - o* tool should log /O errors in an accessible and readable form,
> - >» 2 investigators need to :
> - ‘ cluding the tyj f th and locati f thi
> - ch athe : et i > inclucing: type of ye error an ation oO! e error
> - The tool must have the ability to pass scientific and peer review.
> - based on the type of Results must be repeatable and verifiable by a third party if
> - acquisition technique * necessary
> - they choose. When it
> - s to imaging alee ee source is larger than the
> - tools, they need to 7
> - choose the tools that
> - satisfy certain
> - requirements.
> - The tool should create a bit-stream copy of the original content
> - : when there are no errors in accessing the source media
> - The tool should create a qualified bit-stream copy (a qualitied he
> - @ stream copy is defined as a duplicate except in identified areas of the
> - bit-stream) when /O errors occur while accessing the source media
> - __ ee, ee ee


### Slide / Page 790

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Step 3: Sanitize the Target Media
> - Investigators must properly sanitize the target media
> - in order to any prior data residing on it, before it is
> - used for collecting forensic data
> - Post investigation, they must dispose this media by
> - following the same standards, so as to mitigate the risk
> - of unauthorized disclosure of information, and ensure
> - its confidentiality
> - The following are some standards for sanitizing media:
> - * Russian Standard, GOST P50739-95
> - * German: VSITR
> - . American: NAVSO P-5239-26 (MFM)
> - American: DoD 5220.22-M.
> - = American: NAVSO P-5239-26 (RLL)
> - = NIST SP 800-88


### Slide / Page 791

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Step 4: Acquire Volatile Data
> - (2) Volatile data acquisition involves collecting data that is lost when the computer Is shut down or resta
> - Gi This data usually corresponds to running processes, logged onjusers, registries) DLLs, clipboard/data, openifiles, etc.
> - @ Forensic tools such as Belkasoft Live RAM Capturer and PsTools can be used to extract the entire contents of the’computer’s
> - volatile memory,
> - Acquire Volatile Data from a Windows Machine
> - QO Belkasoft Live RAM Capturer is a forensic tool th,
> - allows extracting the entire contents of a compifter’s
> - volatile memory
> - Q It saves the image files in.mem format
> - Note: While performing live acquisition, an investigator must be aware | -
> - of the fact that wor ona live system may alter the contents of RAM
> - or processes running on the system. Any involuntary action performed
> - on the system may potentially make the system inaccessible.


### Slide / Page 792

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Step 5: Enable Write Protection on
> - the Evidence Media
> - It is necessary to write protect the suspect dri using write blockers
> - to preserve and protect the evidence contained in it
> - blocker is a hardware device or softwa:
> - s data acquisition from the storage media v
> - contents
> - application that
> - ithout altering its
> - It blocks write commands, thus allowing read-only access to the
> - storage media
> - = If hardware write blocke
> - > Installa
> - 7 Bootthe
> - 7 Examples of hard:
> - Tableau Forensic Brid
> - If softwar
> - y Boot the
> - s of software applications: SAFE Block, MacFore
> - Pm 11:16 / 21:57


### Slide / Page 793

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Step 6: Acquire Non-volatile
> - Data
> - Non-volatile data can be acquired in both live acquisition
> - and dead acquisition. It mainly involves acquiring data
> - from a hard disk
> - There is no significant difference in the amount of data
> - acquired from a hard disk between the live and dead
> - acquisition methods
> - Live Acquisition of a hard disk is performed by using
> - remote acquisition tools (e.g. netcat), and bootable CDs or
> - USBs (e.g. CAINE); while dead acquisition involves
> - removing the hard disk from the suspect drive, connktting
> - it to a forensic workstation, write-blocking the hard disk,
> - and running a forensic acquisition tool on the disk f


### Slide / Page 794

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Step 6: Acquire Non-volatile Data (Using a Windows
> - Forensic Workstation)
> - O To acquire forensic image of a hard disk during dead acquisition, remove the hard disk, connect it to a forensic
> - workstation, enable write-blocker, and run a forensic imaging tool (e.g. AccessData FTK Imager) on the workstation
> - O AccessData FTK Imager is a disk imaging program which can preview recoverable data from a disk of any kind and also
> - Vr create copies, called forensics images, of that data
> - nit Lfouerudora com


### Slide / Page 795

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Step 7: Plan for Contingency
> - 2 Investigators must prepare for contingencies such as when the hardware or software does not work,
> - ora failure occurs during acquisition
> - Hard Disk Data Acquisition
> - Investigators must create at least two images of the
> - digital evidence collected, in order to preserve it. If one
> - copy of the digital evidence recovered becomes corrupt,
> - investigators can then use the other copy
> - Imaging Tools
> - If you possess more than one imaging tool, such as Pro-
> - DiscoverForensics or AccessData FTK Imager, it is
> - recommended to create the first image with one tool
> - and the second image with the other tool. If you posses
> - only one tool, make two or more images of the drive
> - using the same tool
> - 4
> - * First Copy of
> - ~ ay Deal idence
> - a) Me sediecsiver
> - Pro Discover Forensics Eas Digital fvidence


### Slide / Page 796

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Step 7: Plan for Contingency (Cont’d)
> - Hardware Acquisition Tool H Drive Decryption
> - Consider using a hardware acquisition tool H Be prepared to deal with encrypted drives
> - (such as UFED Ultimate or IM SOLO=4 G3 IT : that need the user to provide the decryption
> - 69) RUGGEDIZED) that can access the drive at e key for decrypting. Microsoft includes a full
> - the BIOS level to copy data in the Host disk encryption feature (BitLocker) with select
> - Protected Area (HPA) i editions of Windows Vista and later


### Slide / Page 797

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Step 8: Validate Data
> - Acquisition
> - 20.9
> - Overview of Dat
> - Validating data acquisition involves calculating the hash
> - value of the target media and comparing it with its forensic
> - counterpart to ensure that the data is completely acquired
> - The unique number (hash value) is referred to as a
> - “digital fingerprint”
> - As hash values are unique, if two files have the same hash
> - value, they are 100% identical even if the files are named
> - differently
> - Utility algorithms that produce hash values include CRC-32,
> - MDS, SHA-1, and SHA-256
> - aa ?
> - ® 19:10/21:57 ad


### Slide / Page 798

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Step 8: Validate Data Acquisition —-Windows Validation Methods
> - Windows computers come with PowerShell utility, which has the ability to run emdlet
> - The Get-FileHash cmdlet computes the hash value for an evidence file by using the specified hash algorithm
> - This hash value is used throughout the investigation for validating the integrity of the evidence
> - oooo0
> - Investigators can also use commercial computer forensics programs, which have built-in validation features that can
> - be used to validate the evidence files
> - Oo
> - For instance:
> - * ProDiscover’s .eve files contain metadata in
> - segmented files or acquisition files, including the
> - hash value for the original media
> - = When you load the image to ProDiscover, it compares
> - the hash value of this image to the hash value of the
> - original media
> - * Ifthe hashes do not match, the tool notifies that the
> - image is corrupt, implying that the evidence cannot
> - be considered reliable = =
> - Note: In most computer forensics tools, raw format image files do not contain metadata. For raw acquisitions, therefore, a separate
> - manual validation is recommended during analysis.


### Slide / Page 799

20.10  
Performing Evidence Analysis


### Slide / Page 800

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Evidence Analysis: a RRS
> - G O The first responder needs to prepare rand | Sek Sean peered hisites such as the availability of tools,
> - reporting requirement, and legal clearances in order to conduct a successful investigation
> - QO Asa part of an evidence analysis, the first responders will perform following preparations: aa
> - \ | Understand the investigation
> - } requirement and scenario
> - Transport evidence to a secure location
> - or forensic investigation lab
> - ‘Check with the lawyer/organization for »
> - Check the lab facilities before starting the
> - any specific analysis requirements —_~
> - analysis
> - Prepare the evidence analysis toolkit
> - containing imaging, recovery, and
> - analysis tools
> - a8 > ~
> - Rey \ Have a copy of the organization's Qe
> - i Be forensic investigation policy .3 Be
> - ta


### Slide / Page 801

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Forensic Analysis Tools
> - The Volatility Framework The Sleuth Kit/Autopsy
> - . The Volatility, a forensic framework, can be utilized by > The Sleuth Kit (TSK) allows you to investigate disk
> - investigators to analyze RAM contents and retrieve images and enables you to analyze volume and file
> - information, such as processes and executable files running system data
> - in the system, open ports, IP addresses, and user login > Autopsy is a digital forensics platform and graphical
> - information interface to The Sleuth Kit
> - = sowyiyten Tym eve = Be eaneee event =
> - +——— 6 —— 5 ES Se.
> - 2\Users\. \OneOrive\Desktop\volatility_2.6>volatility.exe -f ramdusp.me= imsgeinfo s —!
> - folatility foundation Volatility Framework 2.6
> - : wolatility.debug = Determining profile based on KDEG search.
> - Suggested Profile(s) = Min7SPIxG4, Win7SPOx64, NINIOOERISPOKGS, WinZOOIAISPInE
> - Hs 23418, win2008K2591n04, win?sPixcd_23418
> - aS Layert MindowsAMOC4APage@temory (Kernel AS)
> - AS Layer? = fileadéressSpace (C=\Users\ | | \OneDeive\Desktop\wolat
> - |iLity_2.6\rancump.sea)
> - No PAE
> - OxIS7OOOL
> - Oxf 20001420301
> - Number of Processors : 1
> - Image Type (Service Pack) : 1
> - ICR for CUO : Oxt ff ff Eo00164{ coer
> - KUSER_SHARED_OATA = Oxf ff F#7E0000000001
> - Image Cate ond tine : 2020-03-11 14
> - Image local date and tise : 2020-03-21 07
> - IC: \Users \winwi \OneDrive\Desktop\volati lity 2.6>


### Slide / Page 802

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - ndhdecetonteetatinlovinlld hentia. tnatter telecine tu dlnveinitented
> - Forensic Analysis Tools (Cont’d)
> - °
> - Forensic Recovers and analyzes hidden system files, deleted
> - Explorer _ files, slack space, and unallocated clusters
> - °
> - Forensic ~ Acomputer forensic investigation tool
> - Toolkit that delivers cutting edge analysis,
> - (ETK) =, decryption, and password cracking
> - mn Chm Dermees Drmten.. Daimn. Dawe Sieve Barer Cun
> - $289 Daa a2 d
> - ome
> - IR pai esc ans prey atcseszets adh isab ies fpsesgasaagsas EPR eSIAEEAA Ag AIT ADS IREAER
> - Not mine
> - ee ee ee ee ee
> - Att //octdataforenucs com Ntton //wwww entero. com


### Slide / Page 803

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Forensic Analysis Tools (Cont’d)
> - An easy-to-use cyber security solution integrated into
> - your network that gives you visibility across your entire
> - infrastructure and reveals malicious activities such as
> - Internet abuse, data sharing, and harassment
> - Event Log Explorer
> - Attps://eventlogxp.com
> - OSForensics
> - hitps://www.osforensics.com
> - OpentText EnCase Forensic
> - https-//security opentext.com
> - WinHex
> - Attps://ewoys.net
> - Belkasoft Evidence Center 0
> - https.//deikosoft.com q.



---

## 🛠️ Connecting Theory to Practice
- **Execute the Lab:** Open [`labs/lab-09-linux-incident-triage-forensics.md`](../../labs/lab-09-linux-incident-triage-forensics.md) to work through the practical workshop reinforcing this module.
- **Reference Card:** Check [`cheatsheets/cct-exam-quick-reference.md`](../../cheatsheets/cct-exam-quick-reference.md) for rapid command syntax, formulas, and port mappings.
