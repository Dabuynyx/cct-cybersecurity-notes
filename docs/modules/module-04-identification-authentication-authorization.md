# Module 04: Identification, Authentication & Authorization (IAM)

> **Source Material:** Authentic CCT Study Notes & Slide Deconstructions (Pages 169 – 197)  
> **Author:** [@Dabuynyx](https://github.com/Dabuynyx)  
> **Related Hands-on Lab:** [lab-08-openssl-cryptography-pki.md](../../labs/lab-08-openssl-cryptography-pki.md)  
> **Quick Reference:** [cct-exam-quick-reference.md](../../cheatsheets/cct-exam-quick-reference.md)

---

## 🧭 My Complete Study Notes & Slide Walkthroughs

### Slide / Page 169

MODULE 04: IDENTIFCATION, AUTHORIZATION, AND Authorization. 
 
Access Control: Authorization of the user to access the information. 
 
The access control mechanism uses user identification, authentication, and authorization to 
restrict/ allow access to a specific asset/ resource 
 
Access control Terminologies: à 
 
Subject (user or process of accessing) à Object (specific resource wanted by the user) 
 
 à Reference Monitor (authorization of the access control rule) àOperation (action of 
control that includes abilities and its permissions) 
 
Access Control Principles: 
→  
Separation of Duties (SoD): the separation of an entity’s ability to reduce one’s power. 
 
Need-to-know: providing information that is only required for that specific task


### Slide / Page 170

Principle of Least Privilege (POLP): keeps the system stabled from malicious behaviour


### Slide / Page 171

Logical Implementation of DAC (Discretionary Access Control), MAC (Mandatory Access 
Control, and RBAC (Role – Based Access Control) 
 
Logical implementation of access control is preformed by ACLIs, group policies, passwords, 
and account restriction 
 
 
DAC based on the identity of the users and the discretion of owners who could modify 
Access Control List (ACL) 
 
MAC based on fixed policies that govern access based on labels, typically determined by the 
system without user intervention. 
 
RBAC based on roles assigned to users with specific permission.


### Slide / Page 173

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Sb teehee) VE POCA PU PA beet EP Peet TST Vin se ms -_~
> - Identity and Access Management (IAM)
> - |
> - | IAM is responsible for providing the right individual with right access at the right time
> - |
> - Access Management
> - ¥
> - Authentication Authorization
> - Identity Management Identity Repository
> - Identity Vianagement
> - Copyright © by EG-Gemmecil. All Rights Reserved. Reproduction is St


### Slide / Page 174

Identity is the set of elements linked to an entity that can be stored and authenticated 
digitally


### Slide / Page 175

User Identiy management (IDM) is to ensure the user holds a valid identity such as 
username and account number. IDM involves managing user elements in their repository 
(storage of users’ identities)  
 
 
User Access Management (AM) is the process of managing users’ access to a system and 
includes all the protocols


### Slide / Page 176

Types of Authentication: 
 
Passwords: A combination of a username and a password to authenticate users through 
the database to gain access to the system. Password authentication can be vulnerable to 
password cracking attacks susch as brute force and dictrionary attacks.


### Slide / Page 177

Two-Factor Authentication: uses more than one factor to authenticate the user’s identity 
such as Face ID or a fingerprint. “Something you know, you have, you are.” 
 
Tokens: Hardware token such as a USB with an in-built token code used to access 
restricted resources or even a software token with a single-use login PIN or dynamically 
generated token. 
 
 
 
 
 
 
 
Two-factor Authentication Technique: OATH (open authentication)- 
 
An open strong authentication technology for various of networks. Its main goal is to 
provide a secure online transaction based on TFA. 
 
It has introduced three algorithims: HOTP, OCRA, TOTP for implementing OTP 
authentication


### Slide / Page 178

HTOP (HMAC-Based One-Time Password): HMAC uses a cryptographic authnentication 
technique that uses a hash function and secret key as a one-time password. 
 
OCRA (OATH Challenge-Response Algorithm): Challenge-Response mechanism that 
generates a secret password as a challenge to its user. 
 
TOTP (Time-based One-Time Password): Generates a OTP based on current time. 
 
Security Key à Variable à Algorithm à OTP


### Slide / Page 179

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - User Access Management (AM): User Authentication (Cont'd)
> - Factors Attributes
> - ¥Y Something you know: Also known as ¥ Somewhere you are: Also known as location-based
> - knowledge factor. Something that user knows authentication. Refers to authentication based on
> - like username or password user’s physical location
> - Y Something you have: Also known as owner ¥ Something you do: Also known as behavioral
> - characteristics. Refers to authentication based on
> - factor or hard tokens. Something that users
> - user’s actions such as gesture or touch inputs
> - retain with them such as a hardware token,
> - employee ID cards, etc.
> - ¥ Something you exhibit: Also known as behavioral-
> - based authentication and authorization. Refers to
> - Y Something you are: Also known as biometric
> - BY authentication exhibiting some device or thing
> - factor. Something that is inherent in users,
> - such as biometrics, voice recognition, retina
> - ¥Y Someone you know: Relies on web of trust model.
> - Sean, €tc.
> - Refers to authentication through peer-level
> - certification and reputation networks


### Slide / Page 180

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Types of
> - Authentication: OQ Biometrics refers to the i
> - Biometric | “i i based on their physical eherectencice
> - Authentication
> - Fingerprint Scanning
> - Analyzes dhe i ayer of blood vessels
> - at the back of their eyes to identify
> - a person
> - Compares two fingerprints for
> - verification and identification on the
> - basis of the patterns on the finger
> - Vein Structure Recognition
> - = Py. ae CORRE
> - lris Scanning
> - Analyzes the colored part of the eye oe ; Analyzes thickness and location of
> - suspended behind the cornea = veins to identify a person
> - Copyright © by! (6-Gomreil. AU Rights Reserved. Reproduction ts Strictly Prohibit


### Slide / Page 181

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Types of Authentication: Biometric Authentication (Cont’d)
> - Biometric Identification Techniques
> - 2 @
> - Sty
> - ee
> - on a\ | 2
> - ( 4 Hace | Veise 8 Gait analysis
> - W Recognition | Recognition
> - . ‘wy ) Uses facial | Uses voice Uses patterns of
> - C cn features to patterns to locomotion
> - | y , | identify or verify identify or verify exhibited by
> - ; a person a person moving limbs while
> - | walking or running
> - are different
> - among different
> - individuals


### Slide / Page 182

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Types of Authentication: Biometric
> - Authentication (Cont’d)
> - Depends on technical components, devices used to capture samples, algorithms used to
> - compare with references, and the environment in which the biometric sensor operates
> - Efficacy Rates
> - Percentage of identification occurrences in which an unauthorized user gains access to the
> - j False Acceptance Rate (FAR) ecards
> - Percentage of identification occurrences in which an authorized user is denied access to the
> - False Rejection Rate (FRR) en
> - The value of the false rejection rate and false acceptance rate when sensitivity is configured
> - Crossover ErrorRate (CER) 4+ that FRA and FAR are equal
> - Receiver Operating
> - sett, Visual characterization plot of the trade-off between FAR and FRR
> - Characteristic
> - Matching Speed Time taken to authenticate an individual
> - Ratio of the number of times the system does not capture the samples presented to it to the
> - total number of samples presented
> - i Failure to Enroll (FTE) Ratio of the number of users that are not enrolled in the system to the total number of users
> - presented to the system ‘
> - |
> - |
> - | Throughput Total time taken to enroll the biometric of a user and authenticate the user
> - 1
> - 3 Failure To Capture (FTC)
> - Copyrient © by Et: Eouneil) All Rights Reserved, Reproduction esiricly Pronk


### Slide / Page 183

Types of Authentication: Smart Cards- small computer chip device that holds personal 
information for authentication. Cryptography-based authentication.


### Slide / Page 184

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - ee ee ree
> - Types of Authentication: Single Sign-on (SSO) Authentication
> - A QO) It allows a user to authenticate themselves to multiple servers on a network with a single password
> - WV) without re-entering it every time
> - Advantages
> - No need to remember passwords of multiple applications or systems
> - 02.) Reduces the time for entering a username and password
> - 03] _ Reduces the network traffic to the centralized server
> - Users need to enter credentials only once for multiple applications
> - APPLICATION SERVER
> - EMAIL SERVER
> - | : fe
> - — a hicsitiaisiniaiice cn aie > DATABASE SERVER
> - User Single Sign-on (SSO) Authentication |


### Slide / Page 185

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - User Access Management (AM):. Ruthorization
> - ¢ Authorization involves See the access of information for an individual (E. g.: A user can only read a file,
> - but not write in it or delete it)
> - Application
> - Server | ee
> - i “*. Read only fi
> - TEM Se I Ml MM A I | a onakehereccce steeeenenskhasesecuseasaaee >
> - a4 Read- write
> - 48 vial evar ee ocou ea
> - | ‘ eee >
> - Access Control
> - Application r
> - Server one Authorization
> - Application
> - Server


### Slide / Page 186

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - User Access Management (AM): Authorization (Cont’d)
> - Types of Authorization Systems
> - Centralized Authorization me id
> - ¥ Authorization for network access is done using a single
> - centralized authorization unit
> - vit maintains a single database for authorizing all the
> - network resources or applications
> - Implicit Authorization
> - ¥ Users. can access the requested resource on
> - behalf of others
> - ¥ The access request goes through a primary
> - resource to access the requested resource
> - v itis an easy and inexpensive authorization approach
> - i o
> - Explicit Authorization
> - Decentralized Authorization AH ©
> - Y Each network resource maintains its
> - authorization unit and performs authorization =
> - locally
> - ¥ Unlike implicit authorization, explicit
> - authorization requires separate authorizatio
> - for each requested resource
> - ¥Y |t maintains its own database for authorization
> - ¥ |t explicitly maintains authorization for each
> - requested object
> - Copyright © by EG-Gaunell_ al Rights Reserved. Reproduction is Strictly Prohibit


### Slide / Page 187

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - User Access Management (AM): Accounting
> - Q Accounting is a method of keeping track of user actions on the network, It keeps track of who, when,
> - <=) and how the users access the network
> - ; ly
> - Q It helps in identifying authorized and unauthorized actions
> - Q The account data can be used for trend analysis, data breach detection, forensics investigations, etc.
> - Authorization
> - i (What rights
> - do you have?) |
> - il All Rights Reserved. Reproduction is Strictly


### Slide / Page 188

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - —— ee —— oo re no em en
> - User Accounts Guest Accounts Service Accounts
> - = Default accounts of operating systems = Least privileged accounts without = | Domain or local accounts
> - ae ee sh passwords, created to share’ that allow applications or
> - ee Sas eemenes et system resources services to communicate
> - permissions such as running with the operating system
> - applications/programs and creating = Do not have any privileges to and run programs
> - and manipulating files modify system files, directories, ee
> - or settings = Has administrative
> - privileges based on the
> - application requirement
> - Administrator/Root Accou
> - # Privileged accounts that can perform ~ | @ \'Hayve administrative control over one or several
> - various system-level functions such systems
> - as install and uninstall applications :
> - i : =» | Permitted to access any resoul in th
> - or system software and modify ie fi yp
> - system, configure drivers, add/discard
> - system-level settings
> - applications from service, etc,


### Slide / Page 189

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Account Types (Cont’d)
> - Shared/Generic Accounts
> - = Credentials are shared
> - = Typically used when the network is divided and needs individual centralized uni
> - for network management
> - Application Accounts
> - = Used by applications to i and
> - = Have wide access to the data stored in the organ
> - Group-based Account
> - = Created to simplify the process of
> - e user
> - all the participat
> - Third-party 2
> - = Ss p with a cryptographic
> - ph APIs o:


### Slide / Page 190

MODULE 04: LAB WORK 
 
THE MOST SERIOUS RISK IS UNAUTHOIRZIUED ACCESSS 
 
Identification: Confirming the identity of the subject accessing the network 
 
Authentication: Verifying the credentials provided by a user for specific resources within 
the network 
 
Authorizing: Providing the permission to resources in the network 
 
EXERCISE 01: Implementing access control in windows machine 
 
AC is a method to limit access to resources for users. 
 
AC uses IDAA to maintain integrity, confidentiality, and availability of the information. 
 
PowerShell is used to automate the management of systems.


### Slide / Page 191

Exercise 03: Role-Based Access Control in Windows Admin Center 
 
WAC provides a web console to perform admin tasks and manage sytems within a network 
 
WAC allows the management of system activity such as starting various services, adding 
and removing resources, and controlling applications.


### Slide / Page 192

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - ee ee ree
> - Types of Authentication: Single Sign-on (SSO) Authentication
> - A QO) It allows a user to authenticate themselves to multiple servers on a network with a single password
> - WV) without re-entering it every time
> - Advantages
> - No need to remember passwords of multiple applications or systems
> - 02.) Reduces the time for entering a username and password
> - 03] _ Reduces the network traffic to the centralized server
> - Users need to enter credentials only once for multiple applications
> - APPLICATION SERVER
> - EMAIL SERVER
> - | : fe
> - — a hicsitiaisiniaiice cn aie > DATABASE SERVER
> - User Single Sign-on (SSO) Authentication |


### Slide / Page 193

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - User Access Management (AM):. Ruthorization
> - ¢ Authorization involves See the access of information for an individual (E. g.: A user can only read a file,
> - but not write in it or delete it)
> - Application
> - Server | ee
> - i “*. Read only fi
> - TEM Se I Ml MM A I | a onakehereccce steeeenenskhasesecuseasaaee >
> - a4 Read- write
> - 48 vial evar ee ocou ea
> - | ‘ eee >
> - Access Control
> - Application r
> - Server one Authorization
> - Application
> - Server


### Slide / Page 194

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - User Access Management (AM): Authorization (Cont’d)
> - Types of Authorization Systems
> - Centralized Authorization me id
> - ¥ Authorization for network access is done using a single
> - centralized authorization unit
> - vit maintains a single database for authorizing all the
> - network resources or applications
> - Implicit Authorization
> - ¥ Users. can access the requested resource on
> - behalf of others
> - ¥ The access request goes through a primary
> - resource to access the requested resource
> - v itis an easy and inexpensive authorization approach
> - i o
> - Explicit Authorization
> - Decentralized Authorization AH ©
> - Y Each network resource maintains its
> - authorization unit and performs authorization =
> - locally
> - ¥ Unlike implicit authorization, explicit
> - authorization requires separate authorizatio
> - for each requested resource
> - ¥Y |t maintains its own database for authorization
> - ¥ |t explicitly maintains authorization for each
> - requested object
> - Copyright © by EG-Gaunell_ al Rights Reserved. Reproduction is Strictly Prohibit


### Slide / Page 195

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - User Access Management (AM): Accounting
> - Q Accounting is a method of keeping track of user actions on the network, It keeps track of who, when,
> - <=) and how the users access the network
> - ; ly
> - Q It helps in identifying authorized and unauthorized actions
> - Q The account data can be used for trend analysis, data breach detection, forensics investigations, etc.
> - Authorization
> - i (What rights
> - do you have?) |
> - il All Rights Reserved. Reproduction is Strictly


### Slide / Page 196

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - —— ee —— oo re no em en
> - User Accounts Guest Accounts Service Accounts
> - = Default accounts of operating systems = Least privileged accounts without = | Domain or local accounts
> - ae ee sh passwords, created to share’ that allow applications or
> - ee Sas eemenes et system resources services to communicate
> - permissions such as running with the operating system
> - applications/programs and creating = Do not have any privileges to and run programs
> - and manipulating files modify system files, directories, ee
> - or settings = Has administrative
> - privileges based on the
> - application requirement
> - Administrator/Root Accou
> - # Privileged accounts that can perform ~ | @ \'Hayve administrative control over one or several
> - various system-level functions such systems
> - as install and uninstall applications :
> - i : =» | Permitted to access any resoul in th
> - or system software and modify ie fi yp
> - system, configure drivers, add/discard
> - system-level settings
> - applications from service, etc,


### Slide / Page 197

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Account Types (Cont’d)
> - Shared/Generic Accounts
> - = Credentials are shared
> - = Typically used when the network is divided and needs individual centralized uni
> - for network management
> - Application Accounts
> - = Used by applications to i and
> - = Have wide access to the data stored in the organ
> - Group-based Account
> - = Created to simplify the process of
> - e user
> - all the participat
> - Third-party 2
> - = Ss p with a cryptographic
> - ph APIs o:



---

## 🛠️ Connecting Theory to Practice
- **Execute the Lab:** Open [`labs/lab-08-openssl-cryptography-pki.md`](../../labs/lab-08-openssl-cryptography-pki.md) to work through the practical workshop reinforcing this module.
- **Reference Card:** Check [`cheatsheets/cct-exam-quick-reference.md`](../../cheatsheets/cct-exam-quick-reference.md) for rapid command syntax, formulas, and port mappings.
