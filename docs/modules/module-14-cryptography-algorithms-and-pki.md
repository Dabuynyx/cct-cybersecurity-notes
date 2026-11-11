# Module 14: Cryptography Algorithms & PKI

> **Source Material:** Authentic CCT Study Notes & Slide Deconstructions (Pages 537 – 577)  
> **Author:** [@Dabuynyx](https://github.com/Dabuynyx)  
> **Related Hands-on Lab:** [lab-08-openssl-cryptography-pki.md](../../labs/lab-08-openssl-cryptography-pki.md)  
> **Quick Reference:** [cct-exam-quick-reference.md](../../cheatsheets/cct-exam-quick-reference.md)

---

## 🧭 My Complete Study Notes & Slide Walkthroughs

### Slide / Page 537

Cryptography 
Chapter 14 
14.1- Overview of Cryptographic Security Technique 
 
- Cryptography is the conversion of encrypted data. 
 
- Cryptography is used to protect confidential data. 
 
Objectives: 
 
è Confidentiality 
 
è Authentication 
 
è Integrity  
 
è Nonrepudiation 
 
Encryption: 
Protection of information using an encrypted algorithm, which uses a key to perform transformation.


### Slide / Page 538

Types:  
Symmetric Encryption:  
 
- Uses a single key for encrypting and decrypting the data 
 
- Used to encrypt large amounts of data 
 
Asymmetric Encryption: 
 
à Uses two separate keys to encrypt and decrypt; One key is called the public key used to encrypt 
messages. Second key is private key used to decrypt messages 
 
à Used to encrypt small amounts of data 
 
 
Government Access to keys (GAK) 
 
è Software companies will give copies of keys to the government


### Slide / Page 539

Various Cryptographic Algorithms 
14.2 
 
Ciphers: Used to encrypt or decrypt the data 
 
Types of Ciphers 
 
à Classical Cipher: 
 
Substitution Cipher: plaintext is replaced with cipher text 
 
Transposition Cipher: Letters of the plaintext are shifted to form a cryptogram 
 
à Modern Cipher 
 
Based on the type of key-  
 
Public key: two different types are used to encrypt and decrypt  
 
Private key: Same key is used for encryption and decryption


### Slide / Page 540

è Block Cipher: Encrypts blocks of fixed data 
 
è Stream Cipher: Encrypts continuous flow of data 
 
 
 
14.2 Understanding Various Cryptographic Algorithms 
Data Encryption Standard (DES) 
 
è Symmetric-key block cipher that encrypts data in 64-bit blocks using 56-bit key.  
 
è Archetypal block cipher- it takes a fixed-length string of plaintext bits and transforms it into a 
ciphertext bit string of the same length 
 
è Insecure to brute-force attacks.


### Slide / Page 541

RC4, RC5, RC6 Algorithms 
 
RC4: Symmetric key stream cipher based in random permutation. Encrypts data one byte at a time by 
combining plain text to a pseudorandom key stream generated from a secret key. 
 
 
RC5: Parameterized algorithm with a variable block size, variable key size, and variable number of rounds. 
128 Bits that determines the size of the data block or key used for operations. 
 
à 2-bit registers 
 
RC6: Symmetric key block cipher that comes from the RC5. 
 
à Integer multiplication 
 
à 4-bit working registers 
 
Data Signature Algorithm (DSA) & Rivest Shamir Adleman (RSA 
 
è DSA: FIPS 168-2 specific the DSA.  
 
è Can be used in the generation and verification of digital signatures for sensitive unclassified 
applications


### Slide / Page 542

RSA: 
è Internet encryption and authentication system with the algorithm made by RSA 
 
è Commonly used and is one of the de-facto encryption standards 
 
De-facto encryption standards: widely used encryption methods accepted for securing communication 
 
Elliptic Curve Cryptography: 
 
è Morden public-key to avoid a larger crypto-key usage 
 
è Depends on number theory and mathematical elliptic curves 
 
è Replacement of RSA to reduce key size 
 
Quantum Cryptography: 
 
è Based on quantum mechanics. 
 
è Encrypted by a sequence of photons 
 
è Attackers can conduct a passive attack without manipulation because the photons are transferred 
through arbitrary filters


### Slide / Page 543

Homomorphic Encryption: 
 
è Allows users to secure and leave their data in an encrypted format even if it is being processed or 
manipulated 
 
è Encryption and decryption have the same key holder 
 
è Enables encryption of the confidential data and output source to the enterprise via cloud service to 
process the given data 
 
Post-Quantum Cryptography 
 
è Protects security system from conventual and quantum computers 
 
è Secures wide0range communication 
 
Lightweight Cryptography 
 
è Low-complexity application 
 
è Less power and less resources


### Slide / Page 544

Cipher Modes of Operation 
 
è Encrypts a fixed block of plain text using secret key and initialization vector 
è Provides data with confidentiality and authenticity


### Slide / Page 545

Key Stretching 
Process of key strengthening 
 
Types: 
Password-Based Key Derivation Function (PKDF) 2: Applies some function such as Hash or HMAC


### Slide / Page 546

Bcrypt: used with passwords from a derivation of blowfish algorithm, converted to a hashing algorithm to 
hash a password and add Salt to it 
 
Blowfish algorithm: A fast block cipher that adapts it to secure a password by adding a unique value 
(salt) and using key stretching to make the hash process more tense.


### Slide / Page 547

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - L Common Use Cases of Cryptography
> - Low-power Devices
> - Low-power devices are typically integrated with cryptographic algorithms
> - such as elliptic-curve cryptography (ECC) that have low power
> - consumption for asymmetric encryption or use small symmetric keys
> - Low Latency
> - © Applications that require low latency must use symmetric cryptography
> - with small keys to keep the process efficient
> - 6 Confidentiality
> - iy Cryptography is used to perform file-level, disc-level, and email-based
> - &. encryption to achieve confidentiality
> - Integrity and Resiliency
> - = The source and destination must use encrypted cryptographic hash functions,
> - which are compared at both sides to validate the data and confirm that the data
> - have not been tampered with in transit
> - = Alongside providing packet-level integrity, highly resilient control systems ca’
> - also be developed using crvPmage phic methods
> - Copyright © by E&-Commell. All Rights Rese production bs Strict _
> - >))


### Slide / Page 548

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Common Use Cases of Crypto Stography (c Cont’d)
> - Obfuscation
> - = Cryptography helps in hiding the contents of data using obfuscation
> - techniques
> - 1¢ Authentication
> - Cryptography is also used for authentication by storing passwords in the
> - form of hashes and validating the hashes later when the user attempts to
> - login or access resources
> - Non-repudiation
> - It is a technique used to guarantee that the sender of a message cannot later
> - deny having sent the message; it also guarantees that the recipient cannot
> - deny having received the message
> - f
> - fe
> - Individuals and organizations use digital signatures to ensure non-repudiatio


### Slide / Page 549

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Other Encryption Techniques and Technologies (Cont’d)
> - teem nen "
> - Hardware-
> - Based
> - Encryption
> - Hardware-based encryption uses computer hardware for assisting or replacing the software
> - when the data encryption process is underway
> - These devices are also capable of storing encryption keys and other sensitive information in
> - secured areas of RAM or other nonvolatile storage devices
> - Types of hardware encryption devices
> - TPM © Trusted platform module (TPM) is a crypto-processor or chip that is present on the motherboard that can
> - securely store the encryption keys, and it can perform many cryptographic operations
> - HSM © Hardware security module (HSM) is an additional external security device that is usediin a system for crypto-
> - processing and can be used for managing, generating, and securely storing cryptographic keys
> - alte © USB encryption is an additional feature for USB storage devices that offers onboard en tion services
> - Encryption ve . i 96 Sty
> - Hard Drive >) Hard drive encryption is a technology where the data stored in the hardware can be encrypted using a wide
> - Encryption range of encryption options
> - Copyright © by EC-Camnell, All Rights Reserved. Reproduct Strictly Prohi


### Slide / Page 550

Understanding Various Hash Functions and Cryptography Tools 
14.3 
 
 
Message Digest Algorithm 
 
MD5- Arbitrary Length as an input and a 128-bit fingerprint digest of the input 
 
Latest algorithms such as MD6, SHA-2 and SHA-3 is recommended 
 
MID6- Allows immense parallel computation of hashes for very long inputs; Resistant to differential 
cryptanalysis attacks 
 
 
Arbitrary Length: Ability of a hash functuion to process inputs of any size or length and generate a fixed-
length hash value 
 
parallel computation: simultaneous execution of multiple tasks to solve a problem more effieciently by 
making it into smaller subtasks 
 
MD5 and MD6 are deployed for digital signature applications, file integrity checking, and storing 
passwords


### Slide / Page 551

Secure Hashing Algorithm (SHA) 
Secures a one-way hash; published by the NIST as a US FIPS 
 
SHA-1: 160-bit digest from a message with a maximum length of (264-1) bits, and it resembles MD5A 
 
SHA-2:  
SHA-256 that uses a 32-bit word 
 
SHA-512 that uses a 64-bit word 
 
SHA-3: 
Sponge construction where the message blocks are absorbed by mixing it into the state then squeezes out 
the hash through a series of transformations. 
 
Hash Messaging Authentication Code (HMAC) 
 
è Uses cryptographic key with cryptographic hash function 
 
è Includes SHA-1 and MD5 
 
è Depends on the embed hash function, key size and size of hash output. 
 
è  HMAC protects data from various large extension attacks


### Slide / Page 552

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - WIDS and MD6 Hash Calculators
> - 41S NC AI Rubee ale heer.
> - MDS Calculator
> - wrery MD6 Hash Generator
> - : Attps://veww.browserling.com
> - H
> - i All Hash Generator
> - MD6 Hash Generator
> - 3 https://convert-tool.com
> - ‘brtgresdorwwr beatings nen 5
> - as sai anatretreeteaiaese SPSMM AICHE “a
> - 4 TAMRON LACHES UdT ne ea Shed MERA AN Te TPS 1B md5 hash generator
> - H : aT<eccttlets 193 Me BISIROISMST Wess EST SES RSA eee. https://onlinehashtools.com
> - HashMy A cd TINITASTMRGLAITEEAN ED Hc PENTA OOH ETNET EE ote
> - Fil H ADULTE TITRE, es RODS A ratte,
> - es i Meebo tecleleibaemteTSKeTT.. TAMIL Get ie s TATA,
> - | Pebantseoymastcend sisevsnshoplaqeopincanieeaa PM cte ATTRA SATE ‘
> - 5 RAISED eC RBC TOP, HashCatc’
> - fttps://www.siavesoft.com


### Slide / Page 553

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Cryptography Tools
> - BCTextEncoder
> - AxCrypt
> - Q  Encrypts confidential text in your message hetps://axcrypt.net
> - — Q Uses strong symmetric and public-key algorithms for data encryption
> - } (ie Gedicdcuamcenaa mun a x | Microsoft Cryptography Tools
> - https://docs.microsoft.com
> - © 0 6 © @
> - a. |
> - Strictly Pras


### Slide / Page 554

Overview of PKI and Certificate Management Concepts 
14.4 
 
Digital Signature 
 
è Digital signatures use asymmetric key algorithms for data integrity, employing a private key to sign 
and a public key to verify. They rely on hashing for efficiency, using the hash code with the sender's 
private key to create the signature, which is validated with the sender's public key. 
 
 
Key Exchange through Digital Envelopes 
- Prevents digital data being exposed to external entities 
- Digital Envelope encapsulates both secret keys and data within 
 
Perfect Forward Secrecy (PFS) 
- Cryptographic technique that protects encrypted session data against unauthorized attacks even if the 
private key is compromised 
 
- DH key exchange to generate a unique session key (ephemeral key) between client and server; Key is 
only used for specific sessions


### Slide / Page 555

Digital certificates 
Securely binds public keys to their owners via a trusted intermediary. The sender signs a message with 
their private key and includes the certificate, while the receiver uses the certificate to verify the signature 
with the public key. 
 
 
Public Key Infrastructure (PKI) 
A network and regulations required for creating, managing, distributing, using, storing, and revoking digital 
certificates 
 
Components of a PKI 
 
è Certificate Authority that verifies digital certificates 
 
è Registration Authority that acts as the verifier 
 
è A Certificate management system for generation, distribution, storage, and verification of 
certificates 
 
è One or more directories where the certificates (with public keys) are stored


### Slide / Page 556

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - 000000
> - Digital Certificate Attributes
> - Serial number: Represents the unique certificate
> - identity
> - Subject: Represents the owner of the certificate
> - which may be a person or an organization
> - Signature algorithm: States the name of the
> - algorithm used for creating the signature
> - Key-usage: Specifies the purpose of the public key,
> - whether it should be used for encryption,
> - signature verification, or both
> - Public key: Used for encrypting a message or
> - verifying the signature of the owner
> - Issuer: Provides the identity of the
> - intermediary who issued the certificate
> - ©
> - >)
> - ©
> - c)
> - oO
> - Valid from: Denotes the date from which the
> - certificate is valid
> - Valid to: Denotes the date till which the
> - certificate is valid
> - Thumbprint algorithm: Specifies the hashing
> - algorithm used for digital signatures
> - Thumbprint: Specifies the hash value for the
> - certificate, which is used for verifying the certificate’s
> - integrity
> - Subject Alternative Name (SAN): Secures multiple
> - domains/subdomains or hostnames with a single
> - certificate


### Slide / Page 557

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Digital Certificate Standard: x.509
> - Serial Number
> - OQ X.509 is the most widely used digital et in GAN See
> - certificate standard hl
> - Q Inthe X.509 system, a certification
> - authority issues a certificate binding a
> - public key to a particular distinguished
> - name. A distinguished name is a unique -
> - name such as an email address or a
> - domain name Es
> - Q Adistinguished name contains information
> - about the certificate holder and signature —
> - of the entity that issued the certificate
> - PEPER TAN e nn ea teeet eee De
> - Version1
> - pyeeteaduastccenseatenesd
> - Version 3
> - ven eeerien


### Slide / Page 558

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Digital Certificate Formats
> - stinguished Encoding DER is a binary encoding for both certificates and private keys, and the encoded files
> - Rules (DER) have the extensions .der and .cer
> - Privacy Enhanced -A PEM file consists of Base64-encoded ASCII data with the extensions .crt, .pem, .cer,
> - Mail (PEM) and .key
> - Personal Information PFX, also referred to as PKCS#12, is a binary format to store a main host certificate and
> - Exchange (PFX) derived intermediate certificate with an associated private key in an encrypted file
> - CER => CER files are security files issued by a third-party CA to check website authenticity
> - ae The P7B or PKCS#7 format employs Base64 ASCII encoding and uses the file extensions
> - -p7b and .p7c
> - see The PKCS#8 format consists of private hays and securely encrypted private key data
> - with the extension .p&


### Slide / Page 559

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - In secure PKI, root and
> - intermediate CAs are created,
> - and root CAs can be taken
> - offline, leaving the certificate
> - issuing tasks to the
> - intermediate CAs (which
> - serve as the active CAs) ‘a : ‘ : So ctesetees :
> - @ When the validity of an
> - intermediate CA expires, the
> - root CA is brought online to
> - perform renewal tasks | Client Certificates


### Slide / Page 560

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - PKI Trust Models |
> - A trust model is a set of rules or constraints that instruct a client application on how to verify the authenticity of
> - digital certificates
> - Peer-to-Peer trust model
> - Clients depend on their local CAs, which serve as a
> - starting point
> - It is useful for small organizations
> - >
> - User User


### Slide / Page 561

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - PKI Trust Models (Cont’d)
> - Hierarchical Trust Model
> - It is an inverted tree—like structure in which one master
> - CA, called a root, is the initial point of trust
> - ¥
> - : z Subordinate 2 Subordinate
> - 1 fey CAL wes, CA2
> - The root CA sends all the information to its descendant
> - known as intermediate orsubordinate CAs fff stag rrrnnet Rgernnenncene 3
> - y¥
> - ordinate EP Subordinate lg
> - All nodes in this model trust the master CA and hold t! = can Se
> - public key certificate of the master CA = ‘
> - ¥
> - Any problem in the root CA can impact the overall trust
> - in the PKI infrastructure 1 t ae eee aa iy
> - i
> - Ea Fa kel


### Slide / Page 562

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - PKI Trust Models (Cont’a)
> - Hybrid Trust Model
> - O itis. acombination of peer-to-peer and hierarchical trust
> - models
> - O The root CAs perform peer-to-peer tasks by sharing public
> - keys
> - O The intermediate CAs trust only their respective root CAs
> - and other intermediate CAs within the hybrid environment
> - Root CA Root CA
> - Imermediate cA | Sy Intermediate CA 3 7
> - asa!
> - Bridge Trust Model
> - Ott reduces the number of cross-certificates needed to be
> - associated with PKis
> - O Ina bridge CA, one'CA serves as a central hub for connecting
> - all other CAs and acts asa communication medium for them
> - «A «A
> - gf Be:
> - Ef iy
> - BS
> - sce s.
> - : a Bridge CA a tt
> - El :8
> - cA CA


### Slide / Page 563

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Helin tt a
> - } fuer}


### Slide / Page 564

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Types of Digital Certificates
> - A wildcard certificate can be configured to a domain and all its
> - subdomains to minimize the complexity and cost
> - sane A SAN certificate is used to protect multiple websites with a
> - Hiteinative single SSL certificate aS :
> - Name (SAN) .
> - _ Itis a certificate that consists of a digital signature and is used to
> - _ sign executables or scripts used in code to prove the identity of
> - the developer or publisher |
> - A self-signed certificate is signed by the person or company that
> - Self-signed created it, instead of a trusted certificate authority
> - A machine certificate, also known as a computer certificate, is
> - generated at the time of activation of a computer
> - Computer


### Slide / Page 565

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Types of Digital Certificates (Cont’d)
> - * Email certificates are employed to sign and encrypt iorsalls. and protect the, integrity
> - Email '
> - 1 of email data using secure pratacol suc ch as PGP and: Senne i il
> - User ; = Auser certificate is mapped to a user account on ane oe is controlled
> - Root : * Itis self-signed certificate that belongs t € issuing CA. A ieee certificate is the
> - sia I topmost certificate in the hierarchy and is used to sign other ‘certificates alia
> - ‘s | i
> - See = Aserver certificate is used to validate a server's aces to the client and
> - I
> - ensures that the information provided by the user is safe and secure
> - Domainand | = A domain certificate is issued to a user after they prove a degree of Rees over a domain
> - Extended ! . Extended validation certificates are issued by CAs and are the highest class.of SSL
> - validation certificates


### Slide / Page 566

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Internet Key Exchange (IKE)
> - = ©) IPsec relies on IKE for secure key exchange and authentication
> - O IKE establishes security associations (SAs) to share security parameters such as digital certificates,
> - pre-shared keys, cipher algorithms, and key sizes
> - (a4 The negotiation of the IKE SA is performed in the following two phases
> - Phase I = Phase 2
> - The IKE establishes a secure channel between two The hosts use the previously created secure
> - hosts using the Diffie-Hellman key-exchange channel to negotiate SA security parameters to
> - algorithm for the hosts to authenticate each other by be used with IPsec
> - sharing the private secret key and to encrypt the
> - communication 2


### Slide / Page 567

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Key Escrow and Certificate Chaining
> - = Itis the process of keeping secret keys with a
> - certified third-party that serves as a backup for
> - cryptographic keys
> - = It ensures that critical keys are safe in case of
> - disasters
> - Sends copses of the private hey to
> - the trusted third party
> - Also referred to as the chain of trust, certificate
> - chaining is established by a set of certificates
> - starting from the server certificates and ending
> - with the root certificates
> - Organization's
> - certificate


### Slide / Page 568

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Certificate 7 eer
> - OQ Certificate pinning allows a client application to verity the corresponding setver’s certificate using a pre-
> - installed certificate ‘
> - O The client application follows the basic validation nprocedure using thes server oS public key and verifies whether
> - the server's certificate matches its pinned cont cate
> - O HTTP Public Key Pinning (HPKP) allows a web client to associate a specific Public ey certificate with a particular
> - server to minimize the risk of MITM attacks
> - TAS Session Establishment
> - Doe 2 prereeirscrcerecr eee oa
> - hrnnin
> - Ce sees >. enseaver
> - ‘XK towalid Public key


### Slide / Page 569

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - certificate Revocation List (CRL) and Online Certificate
> - Status Protocol (OCSP)
> - Certificate Revocation List (CRL)
> - : is the list of all revoked certificates used for checking the
> - ertificate status
> - As maintain the CRL database, which stores all the suspended
> - md revoked certificates
> - ve client
> - Ahan e: :@ Me client downloads the CRL
> - =® certificate
> - Client
> - Online Certificate Status Protocol (OCSP)
> - © OSCP, also known as online revocation check, is an alternative
> - to CRL for checking the status of certificate revocation
> - &) The OCSP responder at the CA checks the certificate’s unique
> - serial number to determine the certificate status
> - me
> - The cient e =os ° The CA checks the certiticate’s serial
> - contacts the CA 2 number and responds to the client
> - oO The client attempts to
> - access a website
> - e The server responds with a
> - Gient digital certificate


### Slide / Page 570

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - OpenssL
> - QO OpenSSL is a cryptographic toolkit for applications that can protect communications across
> - a network from sniffing/snooping
> - OpenSSL Usage
> - a a openssl rsa -in XYZ.key -pubout -
> - be our ees teeaecneens ee ee 02 ‘out X¥Z_public.key (Extracts the public
> - (Creates a key pair) keyvi io
> - epenssl x509 -in X¥Z.csr —out
> - openssl req -new -key X¥Z.key -out 04 XYZ.crt -req -signkey XY¥Z.key -days
> - xY¥Z.csr (Creates a CSR} 4200 (Creates a self-signed certificate using
> - given CSR values) é
> - ee


### Slide / Page 571

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - O  certmermsc is a part
> - of the Microsoft
> - management console
> - available in Windows.
> - It assists in viewing
> - information related to
> - the certificates in the
> - certificate store
> - Windows Certificates: certmgr.msc
> - Gh cers - Cetticatss - Camere ter ames foot Conti men acorns Conticenss
> - Fie Acton
> - View Hele
> - xS3'a-
> - lees <
> - WOAM Cottcate Sewer:
> - we itets Autor ter Foot CA
> - 2, atm net Commerce
> - Cp Beaton Porsanat C4 Into.
> - Shetee
> - we letans Tasted Meteors C3
> - SSGinss 3 Pubic Primary Cocticet Giant 1 Public Prema Leticwe ESOS
> - Stepper teens D hace Ct
> - Ce Tghet Geew Feet
> - Witipten GotatBoce St
> - Gta Get Bet
> - me Oigtet Magn Amarance EV Re ShgCet high Aasarance fY finet
> - SOs Ree a8 D5T Rost CA
> - ww Ertret Poet Cortticsten Seth fetrat Finct Cothc ster tattherty
> - : frees fect Cotticames tuthen
> - Ertnact Font Cottecaton Bathom
> - Fetes eat Cee Ba anne Batten


### Slide / Page 572

Understanding Other Applications of Cryptography 
14.5


### Slide / Page 573

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Authentication Protocols: Password Authentication Protocol (PAP)
> - @ e @€) It is the most basic form of authentication
> - Username and password are transmitted over a network and the server evaluates them against the
> - credentials stored in its local database table
> - @ i Passwords stored in the table are encrypted, however the transmission of the passwords are in clear text
> - and unencrypted. This is the main weakness with PAP.
> - @ ° © The Basic Authentication feature built into the HTTP protocol uses PAP
> - e Username and password is sent in clear text
> - If the username and password are
> - valid, client is authenticated
> - Remote PC Server


### Slide / Page 574

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Authentication Protocols: Shiva Password Authenticati
> - Protocol (S-PAP)
> - Proprietary version of PAP
> - (02) Most experts consider SPAP somewhat more secure than PAP because both username
> - and password are encrypted before being transmitting over the network
> - nies Username and password are sent encrypted
> - ferxé 1+ if the username and password are valid, client is
> - authenticated
> - Remote PC Server


### Slide / Page 575

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Challenge-Handshake Authentication Protocol
> - (CHAP) Pa Met
> - After Link Establishment phase, the authenticator ane a challenge’
> - The peer responds with a value calculated using a “one:
> - The authenticator checks the response against its own calculation of
> - © If the values match, the authentication is acknowledged
> - © Ifnot, the connection should be terminated
> - expected hash value
> - At random intervals, the authenticator sends a new challenge to the peer, and repeats steps 1 to 3


### Slide / Page 576

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Blockchain
> - Process of Creating a Blockchain Types of | Blockchain
> - a A block is created and ne
> - participant be 2 : @ Public Blockchain
> - . > :
> - Oo Private Blockchain
> - Federated Blockchain
> - Hybrid Blockchain
> - Camel. Ax Rights Reserved. Reproduction & Strictly Prt
> - oo
> - (S) = A copy of the shared
> - s} iene is generated and
> - ade available to all
> - members


### Slide / Page 577

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Steganography
> - Steganography is a technique of hiding a secret message within an ordinary message and extracting
> - it at the destination to maintain confidentiality of data
> - ey ® Utilizing a graphic image as a cover is the most popular method to conceal the data in files
> - '
> - 5 Secies osntnertar : £C-Council “Hackers
> - are here, Where are ferseeceeees : Si Object  «—_—___ tet n eee > are here, Where are
> - pies ieostigniaten tego Object Extracted you?”
> - ‘ message



---

## 🛠️ Connecting Theory to Practice
- **Execute the Lab:** Open [`labs/lab-08-openssl-cryptography-pki.md`](../../labs/lab-08-openssl-cryptography-pki.md) to work through the practical workshop reinforcing this module.
- **Reference Card:** Check [`cheatsheets/cct-exam-quick-reference.md`](../../cheatsheets/cct-exam-quick-reference.md) for rapid command syntax, formulas, and port mappings.
