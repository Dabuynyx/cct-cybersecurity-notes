# Module 01: Information Security Threats & Vulnerabilities

> **Source Material:** Authentic CCT Study Notes & Slide Deconstructions (Pages 4 – 65)  
> **Author:** [@Dabuynyx](https://github.com/Dabuynyx)  
> **Related Hands-on Lab:** [lab-01-malware-analysis-mechanics.md](../../labs/lab-01-malware-analysis-mechanics.md)  
> **Quick Reference:** [cct-exam-quick-reference.md](../../cheatsheets/cct-exam-quick-reference.md)

---

## 🧭 My Complete Study Notes & Slide Walkthroughs

### Slide / Page 4

Module 01 - Information 
Security Threats and Vulnerabilities 
 
• What is a threat? 
A threat is the potential occurrence of an undesirable event that can damage and 
disrupt a system. 
 
Threatens the confidentially, integrity, vulnerability of a data/ computer resource 
 
“CIV” 
Confidentially: Privacy 
Integrity: Ethics 
Vulnerability: Weakness  
 
• Attackers use cyber threats to infiltrate and steal data such as personal information, 
financial information, and login credentials.


### Slide / Page 5

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Threat Sources
> - Threat Sources
> - Natural Unintentional Intentional
> - Unskilled
> - administrators I
> - * Floods
> - ial a ‘eens | inert
> - Lazy or untrained 5
> - employees * Fired employee
> - * Fires a
> - External
> - Hackers
> - * Disgruntled * Criminals
> - employee + Terrorists
> - * Service providers * Foreign intelligence
> - * Contractors agents
> - Corparate raiders


### Slide / Page 6

Three Actors/Agents: 
 
• Black Hats “bad guys”: 
 
Who don’t have any “main” connection with the establishment. 
 
They are generally influenced by financial structures. 
 
• White Hats “Security Analysist”: 
 
Attacks for defensive purposes.  
 
• Gray hats “Two Face”: 
 
Both offensive and defensive. 
 
• Suicide hackers “Treasure hunter”: 
 
Main aim is to bring down critical infrastructure for a “cause”.


### Slide / Page 7

• Script kiddies ”fakers”: 
 
copy and pasting tools that were developed by real hackers


### Slide / Page 8

Attributes of Threat Actors 
 
Internal:  
Insiders who have permission and authorization into the organization’s network, system, 
and physical resources. 
 
External: 
Outsiders who are authorised to access the organization’s network, system, and physical 
resources. 
 
Level of sophistication: 
 
“Highly successful” threat actors. 
 
Resources/ funding: 
Determines how a threat actor supports an attack financially / with his “tools”.


### Slide / Page 9

Intent/ motivation: 
Highly motivated actors are more likely to launch an attack- their attack may be linked to 
political or personal goals. 
Threat vector 
 
The medium (“pathway”) used by the attacker to gain access to a system by exploiting 
identified vulnerabilities.


### Slide / Page 10

Introduction to malware: 
 
Malware: Malicious software that damages or disables computer systems and gives limited 
or full control of the system for the purpose of threat and fraud.


### Slide / Page 11

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Malware programmers develop and
> - malware to:
> - CE] Attack browsers and track websites visited


### Slide / Page 12

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Different Ways for Malware to Enter a System
> - =
> - \nstant Messenger applications ®
> - Portable hardware
> - media/removabla devices ®
> - Browser and email software bugs iz)
> - Untrusted sites and freeware a
> - web applications/ software
> - Downloading files fram the
> - Internet,
> - Email attachments
> - Installation by other malware
> - Bluetooth and wireless networks


### Slide / Page 13

The design of the attack comes in many different forms and may be hard to distinguish  
 
Forms: 
SEO where malware websites are high in the search results 
 
Social engineered clickjacking 
 
Spear-phishing sites 
 
Malvertising- disguising ads into malware 
 
Compromised legitimate websites 
 
Drive-by Downloads 
 
Spam emails


### Slide / Page 14

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - evelat ars es
> - = —
> - SS ees
> - Crypter
> - Downloadar
> - Dropper
> - Exploit
> - Injector
> - Obfuseator
> - Packer
> - Payload
> - Malicious Code
> - a eae
> - Software that protects malware from undergoing reverse engineering or analysis
> - A type of Trojan that dawnloads other malware from the Internet on to the PC
> - A type of Trojan that covertly installs other malware files on to the system
> - A malicious code that breaches the system security via software vulnerabilities to access information or
> - install malware
> - 4 program that Injects its code inte other vulnerable running pracesses and changes haw they execute to
> - hide of prevent its removal
> - A program that conceals Its code and intended purpose via various techniques, and thus, makes it hard for
> - security mechanisms to detect or remove it
> - A program that allows all files ta bundle together into a single executable file vla compression to bypass
> - security software detection
> - A, piece of software that allows control aver a computer system aiter it has been exploited
> - & command that defines malyrare’s basic functionalities such as stealing data and creating backdoors
> - Coperigsht © by Hommel AS ficiits Bocere


### Slide / Page 15

Crème, downloaders, dropper, obfuscator, packers are not the malware itself, but it is the 
“companion” which is meant to download the file to the system or to encode It in a way that 
avoids signature based or reversed analysis 
 
Some companion files assists on not getting detected. 
 
Payload is generally the malisicious code that excutes


### Slide / Page 16

Trojan 
 
   
   
Unknown/ unauthorized program of where its code is harmful and is contained inside a 
harmless program which can later gain and cause damage 
 
Trojans create a covert communication channel between the victim computer and the 
attacker for transferring sensitive data.


### Slide / Page 17

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - What is a Trojan?
> - It is a program in which the malicious Trojans get activated Trojans create a covert
> - or harmful code Is contained Inside when a user performs communication channel
> - an apparently harmless program or certain predefined é between the victim come
> - data, which can later gain control actions and the attacker for
> - transferring sensitive dat;
> - and cause damage
> - sicdauscueneiee
> - CRGCAS OR AERAAPBAR SH SRS eK ES LAR HEL ATLA ES
> - Downloads
> - Mazicinus Files
> - .
> - aanases dsccceseses SPACED TKR GBA dae
> - Intornat
> - Al lather
> - prepagates Trojan
> - r
> - s222se2020 Ge Bee 1b cb ass
> - Victim infectad with Trojan
> - Caprpregte © ty E-Sammll An Rages Roureed Feces & Sr


### Slide / Page 18

Types of Trojans: 
 
1. Remote access trojans  
The use of gaining full administrative privileges and remote control of a target computer 
 
2. Backdoor Trojans 
Software program designed to grant unwanted access for a remote attack


### Slide / Page 19

3. Botnet Trojans 
A network of infected computers that work together to carry out an attacker’s goal 
 
 
4. Rootkit trojans 
Installs malicious software which allows unotherized access while being hidden and hard to 
remove


### Slide / Page 20

5. E-Banking Trojans 
Designed to target online banking uses and collect their online banking credentials and 
other sensitive information from infected machines 
 
6. Point-of-Sale Trojans 
 
7. Defacement Trojans 
Designed to modify the appearance of websites by replacing the original content with 
the attacker’s message or imagery 
 
8. Service Protocol Trojans 
Uses vulnerabilities in network service protocols to gain unauthorized access to computer 
systems or to preform malicious activities 
 
9. Mobile Trojans 
Designed to target mobile devices by tricking users to install apps or software for 
purpose to access sensitive information, or even take control of the device remotely 
 
 
10. IoT Trojans


### Slide / Page 21

11. Security software disabler trojans 
 
Designed to bypass security software installed on a computer or network. 
 
12. Destructive Trojans 
Designed to cause damage such as deleting files, corrupt data, modify system setting, or 
even disabling the system 
 
This is unique because unlike the other trojans this is designed to damage and delete data 
from an entire system. 
 
13. DDoS Attack Trojans 
 
14. Command Shell Trojans


### Slide / Page 22

Creating a trojan


### Slide / Page 23

What is a Virus?

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - nm kits help attackers to construct Trojai
> - Creating a Trojan
> - . horses of their choice
> - @ The tools in these kits can be dangerous and can backfire if not properly executed
> - Trojan Horse
> - Construction Kits
> - DarkHorse Trojan Virus Maker
> - Trojan Horse Construction Kit
> - Senna Spy Trojan Generator
> - Batch Trojan Generator
> - Umbra Loader - Botnet Trojan
> - Maker
> - | (> Theefv¥.2:.10
> - Computer Information
> - | User name: Administrator
> - Compuler name: SERVER2016
> - Registered organisation:
> - Registered owner. Windaws User
> - YWorkgroup: [Unknoven]
> - Available memory: 1042 hib of 2046 Iib
> - Processor. Genuinelniel Intel64 Family 6 INodel $8 Stepping 9 (2991 Iih2)
> - Display res: 1024 x 7638
> - | Printer [Unknown]
> - Hard drives:
> - | C:\ (41,123 hib of 61,109 Ib free)
> - +1 PC Details} 2 OS Info {$98 Home = | Network |
> - # { | eh - iy i s
> - Reply "PCDetaas® received.
> - Theef RAT Trojan
> - Theef is a Remote
> - written in Delphi. It
> - allows remote
> - attackers access to
> - the system via port
> - 9871
> - Copyright © by EG-Semmel. All Rights Reserved. Reproduction is Strictly Prohiby


### Slide / Page 24

A virus is a self-replicating program that causes an “infection” to a computer 
 
Viruses are generally transmitted through file downloads, infected disks/ drives, and email 
attachments. 
 
 
 
 
 
 
Types of viruses


### Slide / Page 25

1. System or boot sector virus 
 
A type of malware that infects a system’s boot partition or the Master Boot Record (MBR). 
 
These viruses typically targetthe area of the disk responsible for booting which can allow it 
to take over the system and install its code. 
 
 
 
MBR: 
MBR contains a partition table which stores information. 
 
MBR is the first sector of a hard disk that identifies how and where the system’s operating 
system (OS) is located in order to be booted (loaded) into the main computer’s main 
storage or RAM. 
 
 
 
2. file and multipartite virus


### Slide / Page 26

Combines features of both boot sector virus and a file infector virus. 
 
Multipartite virus known for its fast speed in the infected computer. 
 
Multipartite virus causes the most damages than any other computer virus 
 
The Multipartite virus makes the computer very inoperable which can cause the user not 
being able to even complete simple tasks.


### Slide / Page 27

3.  Marco and cluster virus 
 
Marco “stoned” virus was one of the earliest boot sector virus to spread widely. 
 
It infected the MBR. 
 
“it would typically display a message such as "Your PC is now Stoned!" It didn't cause much 
harm beyond displaying the message, but it was one of the first viruses to gain 
significant attention in the early PC era.” 
 
 
Cluster virus infects individual files that alter their directory (location) to execute the virus 
code. 
 
Once executed, the virus can reproduce into other files on the system causing further 
damage. 
 
The virus code resides in a single location.


### Slide / Page 28

4. Stealth/ tunnelling virus 
Designed to hide its presence and its actions on a system  
 
Stealth virus achieve this by actively intercepting and modifying system responses to 
antivirus software. 
 
The techniques are code encryption, polymorphism (changing their appearance with each 
infection), and rootkit-like behaviours to evade detection. 
 
Tunnelling viruses focus more on the transmission of data secretly between compromised 
systems or networks. 
 
Tunnelling viruses are often associated with advanced persistent threats (APTs) and 
targeted attacks aimed at stealing data or maintaining long-term access to compromised 
systems.


### Slide / Page 29

Detecting and mitigating these types of malware often requires advanced security 
measures, including behaviour-based analysis, network monitoring, and regular security 
updates. 
 
 
5. Encryption virus aka ransomware 
Encrypts files on a victim’s computer or network and demans a ransom for the decryption 
key needed to unlock the files. 
 
These typically uses strong encryption algorithims to make the victim’s file inaccessible until 
the ransom paid. 
 
6. Sparse infector virus 
 
Designed to infect only specific few files on the system make it harder to detect and 
potentially increasing its time frame. 
 
 
7. Polymorphic virus


### Slide / Page 30

Designed to change its code to avoid detection 
 
 
 
 
8. Metamorphic Virus 
 
Designed to transformable and rewriting its own code. 
 
9. Overwriting or Cavity Virus 
Designed to overwrite parts of files they infect which could cause irreparable damages 
 
10. Companion virus 
Designed to attach themselves to legitimate files and execute when the legitimate file is 
executed 
 
11. Shell and File Extension virus 
Designed to infect system files or file extensions modifying their behaviour/ appearance


### Slide / Page 31

12. File and Logic Bomb Virus 
File viruses infect executable files, while LBV are trigged by specific events/ condition 
 
 
 
 
13. Web Scripting Virus 
Designed to exploit vulnerabilities in web scripting languages to infect websites/ web 
applications. 
 
 
14. Email and Armored Virus 
Email viruses spread via attachments or links 
 
Armoured viruses use encryption or obfuscation to avoid detection 
 
 
15. Add-on and Intrusive Virus 
Add-on is designed by adding program code to infect the computer.


### Slide / Page 32

16. Direct Action or Transient Virus 
 
17. Terminate & Stay Resident Virus 
Loads its virus into memory and remains active even after the initial startup has finished


### Slide / Page 33

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Creating a Virus (Cont’d)
> - i]
> - JPS Virus Maker
> - Virus Maker Tools
> - © DELmE’s Batch Virus Maker
> - » Bhavesh Virus Maker SKW
> - Using Virus > Deadly Virus Maker
> - Maker Tools
> - > SonicBat Batch Virus Maker
> - > TeraBlT Virus Maker
> - > AndreinickO5's Batch Virus
> - Maker,


### Slide / Page 34

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Atiachos
> - Rarisermwvere
> - ai in e-mail Misia oe cit ota Victim pays ranson ‘Attacker unboces and syicthigins actece
> - and pate wateled twegat access provides accuss ic Mes


### Slide / Page 35

Computer worms 
Spread on their own, unlike a virus, they do not have to infect an executable file and they 
may deliver an alternative payload: viral, backdoor, etc… 
 
Rootkits: 
They hide their presence from detection  
 
Rootkits are patch OS which means they can falsify file system, directory listings, 
running…etc… 
 
It is known for its main function to hide and maintain stealth in the system. 
 
Potentially Unwanted Application(s) – PUAs 
 Harmful applications that may pose severe risks to security and privacy of data (PoD) in the 
system of where they are installed. 
 
Installed when downloading and installing a freeware using third-party installer or when 
accepting a misleading license agreement. 
 
It functions can secretly monitor and alter the data or settings in the system.


### Slide / Page 36

Types of PUAs 
 
1. Adware: 
• Generates unsolicited ads and pop-ups 
 
• Tracks the cookies and user patterns for marketing purposes and collects user data 
Indications of Adware 
• Frequent system lag 
• Inundated advertisements 
• Incessant system crash 
* Disparity in the default browser homepage 
• Presence of new toolbar or browser add-ons 
• Slow Internet


### Slide / Page 37

2. Torrent 
 
3. Marketing 
 
4. Cryptomining 
 
5. Diallers


### Slide / Page 38

Spyware 
 
A program that spies on user activities and may record the user’s interaction and the with 
the user’s computer and internet without the user’s knowledge and sends the information 
to the remote attacks. 
 
Hides its process, files, and other objects in order to avoid detection and removal


### Slide / Page 39

Desktop spyware, keystroke, etc…  
 
 
Keylogger 
 
Progams/ hardware devices that monitor each keystroke as the user types.


### Slide / Page 40

Allows the attacker to gather confidential information about the victim 
 
 
 
Files malware: 
 
Infects legitimate software, applications, and other protocols existing in the system to 
preform various malicious activities.


### Slide / Page 41

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Leverages any existing vulnerabilities te infect the system
> - Resides in the system’s RAN
> - Injects malicious code inte the running processes
> - such as Microsoft Word, Flash, Adele POF Reader,
> - Javaycripl, and PowrerShell QS;
> - =
> - |


### Slide / Page 43

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Infection through lateral
> - mavement
> - Fileless
> - Propagation
> - © Techniques
> - Script-based Injection —
> - Maliciaus websites
> - Mative applications
> - Copprett © ty Rehan Ap sight: Sescreed Foprosicinn S Skis Pra |


### Slide / Page 44

Anything that is weak and can lead to a security breach. 
Risks


### Slide / Page 45

Potential loss or damage that can occur if a threat could happen 
 
Risk = Asset + Threat + Vulnerability


### Slide / Page 46

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - iWabccountievientiqne/ Default
> - ESCO Lratimns Z “ : :
> - = Installstians, Application Poor Patch :
> - Weak | Desien Flaws
> - eS Default Flaws Management |
> - Conftir tions a. gaa
> - Confleurations
> - © oF
> - Vulnerability
> - Operating System Betault
> - ferp Ge — System Sprawl! [Pn proper
> - a ni A _ seein Undocumented Certificate and Key Third-party Risks
> - Vulnerabalrties Yulmerabilities
> - Assets, Management :
> - Ceopareatt & ty Bema, AR Sietre Seeman Sep reticinn 5 Sorbets Pros
> - ua


### Slide / Page 47

Misconfiguration/ Weak configurations 
 
Most common vulnerability and is mainly caused by human error. 
 
It allows attackers to break into a network and gain unauthorized access to systems  
 
 Network misconfigurations:  
 
• Insecure protocols 
 
• Open ports and services  
 
• Erros 
 
• Weak encryption 
 
Host misconfigurations: 
• Open permissions


### Slide / Page 48

• Unsecured root accounts 
 
   
Application flaws examples: 
 
1. Butterfly overflow 
 
Occurs when a program exceeds the amount of data a buffer. 
 
2. Memory leaks 
 
3. Integer overflow 
 
4.  Null pointer/ object dereference: 
Occurs when a program attempts to access or manipulate memory using a null pointer/ 
object reference.


### Slide / Page 49

Attackers can use this flaw to crash the program or excute a code 
 
 
 
5. DLL Conditions 
Involves Inserting malicious dynamic link library (DDL) code into a real process allowing 
attackers to start an ACE. 
 
It can bypass security mechanisms and gain unauthorized access to system resources 
 
6. Race Conditions 
 
7. Improper Input Handling 
 
8. Improper Error Handling


### Slide / Page 51

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - aS See eal (ir — nates ae poe eee SO AE ae elt 5 Re Pee = —— ae
> - ie aa a i a Maa SS a a
> - Poor Patch Management !
> - ts
> - LI A patch is a small piece of software designed to fix problems, security vulnerabilities, and bugs as well
> - 2 orove the usabllity or performance of a computer program or Its supporting data
> - Cs are vendors provide patches that prevent exploitatians and reduce the probability of threats
> - exploiting a specific vulnerability
> - L] Unpatched software can make an application, server, or device vulnerable to various attacks
> - Examples of Poor Patch Management
> - Unpatched Servers
> - Unpatched Firmware
> - _ Unpatched os
> - ©) Unpatched Applications
> - Ceqyaigtt © ty Pe-bomeell An eegtrs Reseed. Sere & Seti Pro i


### Slide / Page 52

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - ros
> - ;
> - O) Design vulnerabilities
> - such as incorrect
> - encryetion oar the
> - flaws in the
> - Tumectionality of the
> - systern that attackers
> - exploit to bypass the
> - detection mechanism
> - and acquire access toa
> - a secure system


### Slide / Page 53

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Operating System Flaws
> - J.
> - QI Due to vulnerabilities in the ez OPERATING SYSTEM is L} These attacks use malicious code,
> - —— = eyeTpins F me ri cr =
> - operating systems, applications such AERTS R UN Oe
> - script, or unwanted software, vehich
> - results in the lass of sensitive
> - information and cantral of computer
> - aperations 4
> - as Trojans, worms, and viruses pose
> - threats
> - Copyitett © try (Gemmell 20 Ristrs Stree Beoqiockition & Streth rok


### Slide / Page 54

Zero-Day Vulnerabilities

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - * Manufacturers
> - provide users
> - with default
> - passwords ta
> - access the
> - Cevice during
> - its inttial set-up,
> - which users
> - must change
> - for future use
> - Default Passwords
> - ty
> - ssa
> - > When users
> - forget to update
> - the passwords
> - and continue
> - using the
> - default
> - passwords, they
> - Make devices
> - and systems
> - yulneranle ta
> - various attacks,
> - such as brute
> - ferce and
> - dictionary
> - attacks


### Slide / Page 55

“no defence” and are unpatched since they are new and unknown


### Slide / Page 56

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - zp Hl beth De teh vt UA vita ew ew ere ey Gee _p> ~<—_-« aa tn ee elf
> - Improper Certificate and Key
> - Management
> - Improper certificate and key management may lead ta rany vulnerabilities that
> - allow attackers to perform password cracking and data exfiltration attacks
> - Storing or retaining legacy or outdated keys also poses major threats ta
> - organizations
> - Privale keys used with certificates rust be stored in a highly
> - secured enviranment; otherwise, an unauthorized individual
> - can intercept the keys ard gain access to confidential data or
> - critical systems


### Slide / Page 57

Third -party risks  
 
Third-party services or products can have access to priviligied systems and applications 
which can include financial information, customer and employee data, and enterprise 
supply chain. 
 
This all can be compromised 
 
Examples of Third-Party risks: 
 
1. Vendor Management 
The processes an organization uses to manage their suppliers- vendors. 
 
It includes activities such as selecting vendors, negotiating contracts, controlling costs, 
reducing vendor-related risks and ensuring service delivery.


### Slide / Page 58

2. Data Storage 
Includes senestive data which can be posed as a risk in cases of data breaches, data loses, 
or unauthorized accesses 
 
3. Outsourced Code Development 
TP may introduce vulnerabilities or malicious codes during development 
 
4. Supply-chain Risks 
 
 
6. Cloud-based vs. On-premises Risks


### Slide / Page 59

Module 01 exercises 
Part 1 
No system or network is immune to attacks. 
 
 
A compromised system can affect other systems on the network. 
 
An intruder may be able to record sensitive informations 
 
Overview of Trojan: 
 
Attackers use remote access trojans (RATs) to infect the target machine to gain admin 
access. 
 
RATs help an attacker remotely access the complete GUI of the victim without their 
awareness  
 
They can preform sceening and camera capature


### Slide / Page 60

Trojan infects victims via phishing attacks and drive-by downloads and propagates through 
infected USB keys or networked drives. 
Part 2 Exercise 
Create a virus to infect the target system 
 
 
 
A computer virus is a self- replicating program that repdoruces its code by attaching itself to 
other locations without consent or knowledge 
 
A security professional must have the required knowledge to create a virus and infect a 
machine in the local network to test the security infrastructure.


### Slide / Page 61

Module 03- CREATING AN INTERNET WORM 
 
Worms are standalone malicious programs that replicate, excute, and spread across 
network connections alone without the act of humans. 
 
 
A worm is the subtype of viruses. 
 
• 
A worm does not require a host to replicate


### Slide / Page 62

Research tasks: Payload 
A payload is ia malware that acts as a threat actor for the victim. 
 
For example: 
 A cybercriminal sends out an email with a malicious attachment- ransomware. 
 
The victim gets infected with the ransomware.


### Slide / Page 63

Ransomware is the payload 
 
Not the email or the document. 
 
 
 
 
 
 
 
 
EXERCISE 04- SPYWARE 
 
 
 
Spyware is a stealthy computer monitoring software that allows you to record all user 
activities on a target computer.


### Slide / Page 64

It automatically delivers logs to the remote attacker using the internet (via email, FTP, 
command and control through encrypted traffic, HTTP, DNS, etc.) 
 
The delivery includes all logs. 
 
Note: The target machine is only accessible when the monitor is on.


### Slide / Page 65

EXERCISE 05- FINDING VULNERABILIRES ON EXPLOIT SITES 
 
Vulnerability research is the process of analysing protocols, services, and configurations to 
discover vulnerabilities and design flaws that will expose a system to exploit, attack, or 
misuse.



---

## 🛠️ Connecting Theory to Practice
- **Execute the Lab:** Open [`labs/lab-01-malware-analysis-mechanics.md`](../../labs/lab-01-malware-analysis-mechanics.md) to work through the practical workshop reinforcing this module.
- **Reference Card:** Check [`cheatsheets/cct-exam-quick-reference.md`](../../cheatsheets/cct-exam-quick-reference.md) for rapid command syntax, formulas, and port mappings.
