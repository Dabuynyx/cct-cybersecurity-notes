# Module 15: Data Security & Protection

> **Source Material:** Authentic CCT Study Notes & Slide Deconstructions (Pages 578 – 626)  
> **Author:** [@Dabuynyx](https://github.com/Dabuynyx)  
> **Related Hands-on Lab:** [lab-08-openssl-cryptography-pki.md](../../labs/lab-08-openssl-cryptography-pki.md)  
> **Quick Reference:** [cct-exam-quick-reference.md](../../cheatsheets/cct-exam-quick-reference.md)

---

## 🧭 My Complete Study Notes & Slide Walkthroughs

### Slide / Page 578

Understanding Data Security and Its Importance 
15.1 
 
Business Critical Data 
Data is the heart of any organization 
 
à Identification and classification is the first step to securing an organization’s data 
 
 
 
Data Security 
Based on CIA trad to prevent any destruction 
 
è Data at Rest 
è Data in Use 
è Data in Transit


### Slide / Page 579

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Example: “Data at Rest” vs “Dat
> - in Use” vs “Data in Trar
> - a
> - Proper implementati
> - required in
> - aoe Inactive data stored in d
> - mecuption) | Physical location
> - Customer bank balanc
> - An email be
> - Examples in database
> - Data encryption
> - . Tight con
> - Security Password protection seh CO
> - accessibility
> - Controls Tokenization
> - ryption
> - Data federation 5
> - Strong identity mar
> - >» 5:42/18:01
> - -_ »


### Slide / Page 580

Information Management Lifecyle 
Helps organizations meet legal, compliance, and competitive requirements 
 
è Monitors and tracks information from creation to destruction 
è Reduces risks and cost; enhanced services, and effective governance


### Slide / Page 581

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Data Controller
> - Data Processor
> - Data Steward
> - Custodian
> - Privacy
> - Officer
> - Data Protection
> - Officer (DPO)
> - > 8:57/18:01


### Slide / Page 582

Data Classification 
Assigning sensitivity levels to data

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - oN
> - Highly
> - Data can be
> - classified into five Proprietary informatic
> - levels:
> - Information for interna
> - Public d
> - Copyright © by E€-Ceuncil. ali Rights Reserved. Reproduction is Strictly Pro


### Slide / Page 583

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Protectin
> - with rat t ct or
> - Making a cate copy of critical data th
> - tore and recovery purpos N
> - or corrupted either accidentally or on pu
> - so that it cannot be
> - wrong moti\


### Slide / Page 584

Understanding Various Data Security Controls 
15.2

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - ACL: Setting Access Controls and Permissions to Files
> - and Folders in Windows
> - Coprright © by EC-Cemnell. All Rights Reserved. Reproduction is Strictly Pro
> - > 0:47 / 33:43
> - _


### Slide / Page 585

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - > 3:08 / 33:43
> - re
> - APES


### Slide / Page 586

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Q allce@allce-VirtualMachine: ~
> - allcegalice-Virtual-machtne:-$§ Us -2
> - root root 7 Feb o @
> - Foot root 85 Feb deno. txt .9p9
> - altce altce 4096 Feb Desktop ootgalice-Virtual-Machtne:/hone/altces setfacl -m uraltce:r
> - alice altce 4096 Feb jocunents hone/alice/deno. txt
> - altce alice 4096 Feb oun loads ° Uice-Virtual-Machine:/hone/altces ff
> - altce alice 8980 Feb eons a
> - alice alice 4096 Feb
> - altce altce 4096 Feb
> - druxe-xr-x 2 altce allce 4096 Feb
> - ldrwxr-xe-x 2 alice altce 4096 Feb
> - drwxe-x-x 2 alice altce 4096 Fed
> - alicegalice-Virtual-machtne:-§ ff
> - rootGallce-virtualMachine: /home/alice = o ®
> - ot@alice-Virtual-Mac!
> - file: demo. txt
> - thine: /hone/altces getfact deno. txt
> - > 7:11/ 33:43
> - Ra


### Slide / Page 587

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - v
> - | Disk
> - Encryption
> - I
> - Encryption of data
> - stored in files/folders
> - > 9:58 / 33:43
> - i
> - Encrypting “Data at Rest”
> - ‘Data at Rest” Encryption
> - f
> - -
> - |” File-level. | | Removable Media | \ Database
> - |_Encryption Encryption Encryption
> - 1 1
> - v 1
> - V
> - Encryption of data
> - Encryption of data in
> - stored in file
> - removable media
> - devices
> - Encryption of data
> - folders
> - stored in databases


### Slide / Page 588

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - ttribute:
> - i Windows \System32>cipher /e “d:\Oeno\Sample.txt™
> - Encrypting fLlesain d:\Demo\,
> - Sample.txt fox)
> - } File(s) [or directorie(s)} mithin 2 dinectorie(s) were encrypted.
> - ‘onverting files fron plaintext to ciphertext may leave sections of old
> - plaintext on the disk volune(s). It 1s recomended to use comand
> - TOMER /M:directory to clean up the disk after all converting 1s done,
> - Ic: Windows \System32>
> - > 12:20 / 33:43
> - io... a


### Slide / Page 589

Database Encryption 
Conversion of plain text database into ciphertext data base using encryption. 
 
Transparent/ External Encryption: Symmetric key 
 
Collumn-level Encryption: Ecnrypts individual collums within database using different encryption keys 
 
 
Symmetric Database Encryption: Enhanced transparent key that Remains encrypted till the database is not 
opened or accessed 
 
 
Asymmetric data encryption


### Slide / Page 590

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - DP 16:03 / 33:43
> - esc


### Slide / Page 591

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Secure HTTP Con
> - The browser connects to a web server t nding a message indicating that a secure session (SSL) is requeste
> - Web server respon y B of its root certificate along with server's public key
> - Browser verifies the certificate b king whether it is valid and has been signed by a certificate authority (CA). It also
> - and sends a one-time session key along with the server's public key
> - rivate key to decrypt the sess and sends back an acknowledgement encrypted with the s k C inan
> - 2 Now, the browser v Z rely transmit data with the session key
> - Standard SSL rtificate
> - » 17:03 / 33:43
> - renee ee


### Slide / Page 592

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Viewing a Digital Certificate
> - Viewing Digital Certificate in Firefox Browser
> - ° €>¢ 4 a
> - Viewing Digital Certificate in Google Chrome
> - > 17:44 / 33:43
> - Se ee eae ‘


### Slide / Page 593

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Install and Configure SSL Certificate on |
> - Windows Server |
> - > 18:04 / 33:43
> - oct eee ae .


### Slide / Page 594

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Encrypt all outgoing Outlook
> - eee x


### Slide / Page 595

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - > 27:15 / 33:43
> - on


### Slide / Page 596

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - > 27:35 / 33:43
> - aii


### Slide / Page 597

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Masking
> - > Itis the process of ace
> - 1 fovecess of replacing sensitive data ina
> - in database fields with special characters such as field | | with arbitrary tokens. These tokens act as
> - asterisks (*) and hashes (#) a replacement for encryption keys
> - on™ Hashing/Salting
> - > Itisthe pia of replacing unnecessary
> - > Hashing is the process of transforming any type
> - information with some common values of
> - ‘data with a unique fixed string length using
> - hashing algorithms such as MDS. and SHA
> - > Salting is the process of }random
> - (salt) to a hashed field in a table. It
> - increases complexity and the difficulty of
> - retrieving the hashes
> - > 29:17 / 33:43
> - oO 380 Q
> - OSC FI
> - F2
> - re
> - G
> - B
> - Fo ay
> - = / ;


### Slide / Page 598

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Public Notifications and
> - Disclosures
> - Notifications of Data Breach Escalation of Data Breach
> - Initial escalation:
> - such as the IT desk, administ
> - lication managers
> - el; Notify teams such as the
> - s such
> - > 31:52 / 33:43


### Slide / Page 599

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Interconnectio
> - > 32:13 / 33:43
> - n Security Agreement (ISA)
> - provider and receiver, which contair
> - han
> - ared and how the data need to be
> - level of service that an orge a vendor
> - levels are
> - 7 and Non-disclosure Agreement (CNDA)
> - 2en two individuals or companie r maintainin


### Slide / Page 600

Overview of Data Backup, Retention, and Destruction 
 
Data Backup 
Process of duplicating a copy of data  
 
Purpose 
Reinstate a system to normal working state after damage; to recover data and information from corruption 
 
This avoids severe damage


### Slide / Page 601

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Data Backup Strategy/Plan
> - 2
> - a
> - Identifying the Selecting the backup Selecting a backup Selecting the
> - critical business data media technology appropriate RAID
> - levels
> - 3 ) v4 8
> - — : =
> - Selecting an Selecting the backup Choosing the right Conducting a
> - appropriate backup types backup solution recovery drill test
> - method


### Slide / Page 602

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Examples of Data Backup Media Devices
> - Several manual disk swaps may be
> - Feardabl red because of the limited
> - ~200 GB hy ane y to store and
> - transport
> - Recordin


### Slide / Page 603

Redundant Array of Independent Disks (RAID) Technology 
 
è  A method of combining multiple HDD into a single unit and writing data across several disk drives to 
have a fault tolerance (if one drive fails, the system will still be able to run) 
 
è RAID disks enables a balanced overlap of I/O operations. Improves system performance, simplifies 
storage management, and protects against data loss 
 
è Works as a secondary storage 
 
è 6 LEVELS depending on storage techniques: Stripping, Parity, and Mirroring 
 
RAID Storage Architecture 
 
è RAID Controller: Physical Disk drives and presents them to the computer as logical units 
 
è IDE, SATA, or SCSI Interface: Connection to the server  
 
è Multiport Memory Controller: Access to a memory bank and helps achieve a high efficiency with 
RAM 
 
è SDRAM: Synchronized with the CPU Clock speed


### Slide / Page 605

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - é RAID Level 0 splits data into blocks that are written
> - It improves 1/0 performance by spreading the I/O load across several channels and disk drives
> - Data recovery is not possible if a drive fails
> - It requires a minimum of two drives
> - It does not provide data redundancy
> - evenly across multiple hard drives
> - Copyright © by EC-Couneill. All Rights Reserved


### Slide / Page 606

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - RAID Level 1: Disk Mirroring i
> - Multiple copies of data are written to multiple drives at crm,
> - the same time wt »
> - © It provides data redundancy by duplicating the drive data ——
> - in multiple drives
> - If one drive fails, data recov ver
> - Copyright © by EG-Goumell. all Rights Reserved. Reproduction is Strictly Prohit


### Slide / Page 607

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - “ RAID Level 3: Disk Striping with Parity
> - B 3% w
> - 0 | Data is striped at the byte level across multiple drives. One drive
> - per set is taken up for parity information
> - 02 If a drive fails, data recovery and error correction is possible
> - using the parity drive in the set
> - The parity drive stores the information on multiple drives


### Slide / Page 608

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - RAID Level 5: Block Interleaved Distributed Parity
> - The data is striped at the byte level across multiple drives,
> - and the parity information is distributed among all the
> - member drives
> - The data writing process is slow
> - 00 0
> - This level requires a minimum of three drives to be set up


### Slide / Page 609

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - RAID Level 10: 23
> - Blocks Striped
> - and Mirrored :
> - : cI-
> - y RAID 1+0
> - RAID 10 is a combination of RAID 0 (striping volume wank
> - data) and RAID 1 (disk mirroring), and its implementation MNO
> - requires at least four drives none IO. seaasetcsennmeostrensctteneelecsnae ieee ean
> - It has the same fault tolerance as RAID level 1, and the same A1 ! A1. a
> - mirroring overhead as Raid 0 Aa i) Aal re. > aa |
> - AS! ! ASI ] nel)
> - It stripes the data across mirrored pairs. The mirroring provides aw | al | a
> - (03) redundancy and improves performance. The data striping provides I
> - . isk O Di: Disk 2
> - maximum performance bi) is 3


### Slide / Page 610

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - RAID Level 50: Mirroring and Striping across Multiple
> - RAID Levels
> - 0101010101 O RAID 50 is acombination of RAID 0 striping and the distributed parity of RAIDS
> - : ey a OQ Itis more fault tolerant than a RAID 5 but uses twice the parity overhead
> - Q Aminimum of six drives are required for setup. A’ drive from each segment can
> - Q This RAID level offers better reads and writes than a RAID 5 and the highest levels
> - i€
> - sl
> - fail and the array will recover, If more than one drive fails in. a segment, the array
> - will stop functioning.
> - of redundancy and performance
> - ,
> - ; RAID 5+0
> - RAID O


### Slide / Page 611

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Ecialized, dedicated, and discrete high-speed network th
> - arrays, tapes,
> - -Fconnect (Fiber Channel,
> - speed I/O inte
> - at
> - Servers, etc ) witha
> - SAS, Ethernet, etc.)
> - disk
> - € preferred in large enterprises because of reliable data transfer
> - and flexible sc alability
> - A
> - SAN s: Apports
> - data archival, backup,
> - from one storag:
> - restore, transfer, retrie
> - and Mirroring
> - ‘Val, migration,
> - € device to another
> - The comm Anication infrastructure layer provides the physical connections
> - to the network de vices
> - The management layer organizes the connections, storage elements, and
> - computer systems
> - The storage layer hosts the Storage devices
> - 1 Network ( SAN)
> - ?
> - [mu]
> - Communication
> - Infrastructure
> - Use
> - Database Servers
> - Layer
> - Application Servers NAS Filter
> - Fiber Channel Fiber Channel
> - Fiber
> - Management
> - ~ Channel” ww
> - layer
> - Storage Layer


### Slide / Page 612

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - NAS isa file-based
> - ata storage
> - shared over the
> - service anda dedicated Computer appliance
> - network
> - NAS is a high-performance file server Optimized for storing, retrieving, and
> - Serving files
> - NAS servers contain pro
> - Optimized for file serving
> - Users with different Operatin
> - ig systems can
> - share files with no compatibi
> - lity issues
> - ANAS can be conn
> - ed toa LAN using the
> - plug and play feature
> - > Data transfer is inefficie t as it uses TCP/IP
> - Minimal administration required, unlike Uni Protoco
> - or NT file serve
> - 26:06
> - Gf Sammy
> - PD)
> - 2600 = <a
> - Py
> - be


### Slide / Page 613

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Selecting
> - Select a backup method based On its cost and ability acc
> - Ls
> - Cold Backup (Offline)
> - application,
> - database, or system unning and
> - available to users
> - Q Backup the data when the application,
> - database, or system is not running
> - (shutdown) and is not available to users
> - Q A combination of both hot and cold
> - backups
> - vel down time is O) Used when a service level down time is Advantages:
> - allowed and a full backup is required
> - ¥ | Less expensive than a h.
> - Advantage: Advantage: (
> - not allowed
> - ackup switch over is Y Least expensive
> - Disadvantage:
> - itchin a backup
> - quires additional time
> - " 13:40 / 26:06
> - a
> - ry
> - be


### Slide / Page 614

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - -hoosing the
> - &) x
> - Onsite Data Backup | Offsite Data Backup | Cloud Data Backup
> - Q Storing backup data at Q Storing backup data in Storing backup data on
> - onsite data storage only remote locations in fire- storage provided by an
> - proof, indestructible safes online backup provider
> - ¥ Onsite backup data can be v Data is secured from Y The data is encrypted and
> - easily accessed and restored physical security threats free from physical
> - i a such as fire, floods, etc. security threats
> - Y Data can be accessed
> - from anywhere
> - Y Data loss risk is greater Y Problems with a regular
> - data backup schedule
> - Y No direct control of the
> - backup data
> - vY More time to backup


### Slide / Page 615

Types of Backup 
 
Full/Normal Backup: All system data is copied 
 
Differential Data Backup: All data has been changed since the last backup 
 
Incremental Data Backup: Only files that has been changed or created are copied to the backup media


### Slide / Page 616

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - r
> - ckup loo
> - ® File History is in Windows
> - ® \t regularly backs up important folders like Desktop, Documents, Downloads, Music, ©
> - Picture, Videos, and parts of AppData folder
> - BullGuard Backup
> - Attps:/
> - NTI Backup Now Ez
> - https://www.nticorp.com
> - Power2Go 13
> - https://www.cybe:
> - roy
> - ba
> - 26:06


### Slide / Page 617

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - ® of storing and maintaining important information f
> - lival requirements
> - Q Data retent
> - compliance req
> - ion pc
> - dards
> - ta retention 2ment team
> - he applic Sanizati
> - to be include
> - ata retentic
> - Ensure that al employees unde tand the >Fganization’s data re
> - > 20:19 / 26:06


### Slide / Page 618

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Data destruction is the process of destroying
> - data stored on tapes, hard disks, and other forms
> - of electronic Media, so that it is completely
> - unreadable and cannot be accessed or used for
> - unauthorized Purposes
> - The main Purpose of data destruction is to
> - restrict unauthorized disclosure of information
> - through Proper disposal and destruction of
> - devices, equipment, computers, and media that
> - store sensitive data


### Slide / Page 619

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Data Destruction Policy
> - Q Data destruction policy ensures that th
> - 1 data stored on unused tapes, hard VA
> - disks, and other forms of electronic media is deleted or destroyed such |
> - that they are unreadable and cannot be accessed
> - Q Every organization must implement a d:
> - DP 21:22 / 26:06


### Slide / Page 620

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Data Destruction Techniques
> - Technique Description
> - Methods
> - Clearing ‘
> - ‘ar data in all user
> - Overwr ting
> - e media
> - Purging
> - - 10\ permanently from a stora
> - tic fields can damage nearby devices
> - lestroyi
> - Bayne Technique to d
> - estroy data by destroying the storage
> - Gm medium
> - Best method
> - itive data


### Slide / Page 621

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Disk Wipe
> - Windows Diskpart Utility
> - fticrosoft DiskPart version 10.0.18362.1
> - Opyright (C) Microsoft Corporation.
> - Cosputer: VM-W10-1903
> - > 25:17/ 26:06
> - —_,._


### Slide / Page 622

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - EaseUS Data EaseUS data recovery software can quickly
> - ecovery Wizard
> - s after deletion
> - OF Emptying the recycle bin
> - Puran File
> - http
> - 25:38 / 26:06
> - i


### Slide / Page 623

Overview of Data Loss Prevention Concepts 
15.4 
 
DLP 
Processes that do not allow users to send confidential data to the outside.


### Slide / Page 624

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Vee eee? Lek UY TIVE CHU WY VOLTS (UU SETI COT IQer iit
> - data outside the organization
> - it is used by organizations to:
> - Y Discover sources of data leaks
> - ¥ Monitor the sources of data leakage
> - Protect organization assets and resources
> - ¥ Prevent accidental disclosure of sensitive
> - information to unintended parties
> - ¥ Manage resources with business rules,
> - security policies, and software


### Slide / Page 626

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Types of Data Loss Prevention (DLP) Solutions
> - EndpointDLP 3 J i
> - yi!
> - A solution that monitors and protects PC-based systems such as tablets, laptops, ete. !
> - It is used for preventing data leakage through clipboards, removable devices, and eh applications
> - Ne
> - A solution that monitors, protects, and reports all data in transit |
> - It is installed at the “perimeter” of an organization's network
> - It helps the security professionals in scanning all data moving through the|ports and protocols within the organizati
> - : i ‘
> - Storage DLP
> - A solution that monitors and protects data at rest, that is, the data stored in an Organization's data center infrastruc
> - such as file servers, SharePoint, and databases |
> - It identifies the location where sensitive information is stored and helps users in determining whether it is stored se



---

## 🛠️ Connecting Theory to Practice
- **Execute the Lab:** Open [`labs/lab-08-openssl-cryptography-pki.md`](../../labs/lab-08-openssl-cryptography-pki.md) to work through the practical workshop reinforcing this module.
- **Reference Card:** Check [`cheatsheets/cct-exam-quick-reference.md`](../../cheatsheets/cct-exam-quick-reference.md) for rapid command syntax, formulas, and port mappings.
