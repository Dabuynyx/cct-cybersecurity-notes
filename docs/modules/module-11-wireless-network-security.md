# Module 11: Wireless Network Security

> **Source Material:** Authentic CCT Study Notes & Slide Deconstructions (Pages 476 – 495)  
> **Author:** [@Dabuynyx](https://github.com/Dabuynyx)  
> **Related Hands-on Lab:** [lab-03-tcp-wireshark-deep-dive.md](../../labs/lab-03-tcp-wireshark-deep-dive.md)  
> **Quick Reference:** [cct-exam-quick-reference.md](../../cheatsheets/cct-exam-quick-reference.md)

---

## 🧭 My Complete Study Notes & Slide Walkthroughs

### Slide / Page 476

Module 11- Wireless Network Security 
11.1- Overview of Wireless Network Fundamentals: 
 
Wireless Terminologies 
 
Global System for Mobile communications (GSM): Universal system for mobile transportation for wireless 
networks worldwide 
 
Bandwidth: Amount of information broadcasted over a connection 
 
Basic Service Set (BSSID): MAC Address of an access point 
 
ISM band: Set of frequencies for international, industrial, scientific, and medical communications. 
 
Access Point: Used to connect wireless devices to a network 
 
Hotspot: A place where a wireless network is available for public use  
 
Association: Process of connecting a wireless device to an AP


### Slide / Page 477

Service Set Identifier (SSID): Unique Digit of 32 alphanumeric given to WLAN 
 
Orthogonal Frequency-division Multiplexing (OFDM): Method of encoding digital data on multiple carrier 
frequencies 
 
Multiple input, multiple output Orthogonal Frequency-division Multiplexing (MMO-OFDM): An Air 
interface for 4G and 5G broadband wireless communications 
 
Direct-sequence Spread Spectrum (DSSS): Spreads data over a wide frequency to reduce interference and 
boost security. Used in Wi-Fi (802.11b). 
 
Frequency-hopping Spread Spectrum (FHSS): Quickly jumps between frequencies to avoid interference 
and improve security. Used in Bluetooth. 
 
 
Wireless Networks 
 
WN uses radio frequency (RF) signals to connect wireless-enabled devices in a network. 
 
Institute of Electrical and Electronics Engineers (IEEE) standard of 802.11 and uses radio waves for  
communications.  
 
PROS:


### Slide / Page 478

- Easy installation and eliminates wiring 
 
- Access to the network is anywhere within the range of an AP 
 
- Public places can offer a constant internet connection using WLAN 
 
 
CONS 
Interference: RF signals can be disrupted by other devices or physical barriers. 
Security risks: Wireless networks are more vulnerable to hacking without proper encryption. 
Limited range: Signal strength decreases with distance from the access point. 
 
 
Wireless Technologies: Data transmissions by electromagnetic waves that carry signals over the 
communication path 
 
Types of Wireless Technologies: 
 
- Wi-Fi: uses radio waves or microwaves to allow electronic devices to exchange information on the 
network 
 
- Bluetooth: Data is transmitted across devices over a short distance


### Slide / Page 479

- RFID: Radio frequency uses EM waves to transfer data for automatic identification and for tracking tags 
attached to objects 
 
- WiMAX: Long distance wireless network with high-speed internet from the IEEE 802.16 for network 
standards


### Slide / Page 480

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Wireless Standards
> - Protocol Frequency (GHz)
> - 802.11 (Wi-Fi) 2.4 22
> - 802.11a 5 yA0)
> - 3.7
> - 802.11b 2.4 22
> - 802.11d
> - It is an enhanced
> - version of 802.11a and
> - 802.11b that enables
> - global portability by
> - allowing variation in
> - frequencies, power
> - levels, and bandwidth
> - 802.11e
> - It provides guidance
> - for prioritization of
> - data, voice, and video
> - transmissions by
> - enabling quality of
> - service (QoS)
> - 802.119 2.4 20
> - Bandwidth (MHz)
> - Stream data rate
> - (Mbit/s)
> - 1,2
> - 6, 9, 12, 18, 24, 36, 48,
> - 54
> - 1, 2, 5.5, 11
> - 6, 9, 12, 18, 24, 36, 48,
> - 54
> - Modulation
> - DSSS, FHSS
> - OFDM
> - DSss
> - OFDM
> - Range (m)
> - Indoor
> - 20
> - 35
> - 35


### Slide / Page 481

Wireless Network Topologies: Devices can exchange information without AP by configuring the wireless 
adapter for all devices; then, set all devices to have the same channel name and SSID to activate the 
connections. 
WPAN,…


### Slide / Page 482

Components of a Wireless Network: 
 
- AP: Hardware device that allows wireless communications via wireless standards such as Bluetooth, 
Wi-Fi 
 
- Wireless Cards: Requires a network interface cards (NIC) to establish a ethernet connection 
 
- Wireless Modem 
 
- Wireless Bridge: Connects multiple LANS at the medium access control layer. Increases wireless 
network coverage 
 
- Wireless Repeater: Retransmits signal from an AP to create a new network 
 
- Wireless Router 
 
- Wireless Gateways: Routes data packets and functions as a wireless AP.  
 
- Wireless USB Adapter


### Slide / Page 483

Types of Antenna: Converts electrical impulses into radio waves and vice versa 
 
è Directional Antenna:  Single direction for both obtaining radio waves and broadcasting 
 
è Parabolic Grid Antenna: Based on a sat dish and can pick up Wi-Fi over 16 km or more 
 
è Dipole Antenna: Used for supporting client connections 
 
è Omnidirectional Antenna: 360° hor. Radiation pattern. Used in wireless base stations. 
 
è Yargi Antenna: Focuses on one direction. From 10MHz to very high freq and ultra high freq 
 
è Reflector Antennas: Concentrates EM energy that is radiated or received at its focal point


### Slide / Page 484

11.2: Overview of Wireless Network Encryption Mechanisms 
 
   Types of Wireless Encryption: 
 
 
à 802.11i: IEEE amendment for 802.11 wireless networks 
 
à Wired Equivalent Privacy (WEP): IEEE  
 
à Extensible Authentication Protocol (EAP): Multi-Authentication methods such as token cards,  
Kerberos, and certificates 
 
à Lightweight Extensible Authentication Protocol (LEAP): A authentication method developed by Cisco 
Systems allows users to authenticate multiple times via RADIUS 
 
à Temporal Key Integrity Protocol (TKIP): Uses more encryption than WEP for LANs


### Slide / Page 485

àWi-Fi Protected Access (WPA): Advanced wireless encryption protocol using TKIP and Message Integrity 
Code (MIC) to provide stronger encryption and authentication as a replacement for WEP 
 
 
 
 
 
à WPA2: AES + CCMP 
 
è Advanced Encryption Standard (AES):  a symmetric encryption algorithm widely used across the 
globe to secure data. It is used to encrypt the data being transmitted over the wireless network. 
Remains unreadable without proper decryption key.  
 
è Computer Mode with Cipher Chaining Message Authentication Protocol (CCMP): Ensures data 
integrity and authentication alongside encryption 
 
 
à WPA2 Enterprise: Unites Extensible Authentication Protocol (EAP) to provide more secure and flexible 
authentication mechanisms. 
 
àRemote Authentication Dial-In User Service (RADIUS): Centralized Authentication + Authorization 
management system


### Slide / Page 486

à  Protected Extensible Authentication Protocol (PEAP): Encapsulates EAP withing a authenticated 
transport layer security (TLS) tunnel 
 
à WPA3: Third-Generation Wi-Fi security protocol that uses GCMP-256 for encryption and HMSAC-SHA-
384 for authentication 
  
 
 
 
Wi-Fi Authentication Methods: Open System Authenticatio n 
 
è Any device can be authenticated with the AP; This allows devices to transmit only when its WEP key 
matches with the AP 
 
Wired Equivalent Privacy (WEP): 
WEP: A security protocol defined by 802.11b standard.  
 
è Provides a WLAN with security and privacy 
 
WEP uses a 24-bit initialization vector (IV) to form stream cipher RC4 for confidentiality and the CRC-32 
checksum for integrity of wireless transmissions 
 
WEP is highly unsecured.


### Slide / Page 487

WPA2 Encryption: 
è Includes cipher block chaining message authentication code protocol (CCMP) and an AES-based 
encryption mode with strong security  
 
Modes of operation: 
WPA2-Personal: 
 
à Uses set-up password (pre-shared key, PSK) to protect unauthorized network access. 
 
à PSK mode encrypts each network device with network traffic using a 128-bit key which is derived from 
of 8 to 63 ASCII Characters.


### Slide / Page 488

WPA2- Enterprise: 
 
à Includes EAP or RADIUS for centralized client authentication.  
 
à Uses multiple authentication methods such as token cards and Kerberos 
 
à Users are assigned login credentials by a centralized server to connect. 
 
 
 
 
 
 
WPA3 Encryption: 
 
è Advanced implementation of WPA2 providing with new protocols and uses the AES-GCMP 256 
encryption algorithm  
 
WPA3- Personal: 
 
à Mainly used to deliver password-based authentication using SAE protocol aka Dragonfly Key Exchange 
 
à Authentication encryption via GCMP-256


### Slide / Page 489

à HMAC-SHA-384 to generate cryptographic keys 
 
à ECDSA-384 for exchanging keys 
 
WPA3- Enterpirse: 
 
à Protects sensitive data using multiple cryptographic algorithms 
 
à Authentication encryption via GCMP-256 
 
à HMAC-SHA-384 to generate cryptographic keys 
 
à ECDSA-384 for exchanging keys 
11.3- Understanding Different Types of Wireless Network Authentication Methods: 
 
Shared Key Authentication: AP with the same WEP key should be enabled and configured manually on the 
AP and the client for authentication. 
 
Using a Centralized Authentication Server via a RADIUS sever on a 802.1X network NACP. 
 
11.4- Understanding Different Types of Wireless Network Security Measures:


### Slide / Page 490

Creating an Inventory of Wireless Devices: 
 
è Identity and document all client devices according to the applications, encryption firmware, wireless 
channel, etc…  
 
 
è Helps network defenders to manage and monitor the wireless devices in the network


### Slide / Page 491

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Placement of a Wireless AP
> - + Guidelines for AP mounting:
> - Place APs in central locations.
> - Install an AP on the ceiling.
> - Avoid placing APs too high on ceilings.
> - Avoid mounting an AP on a wall as it may restrict its 360° coverage.
> - Avoid installing APs in corridors.
> - Avoid installing APs above suspended ceilings.
> - Use locks and a plastic or steel enclosure to secure the AP from theft.
> - Avoid enclosing the AP in a metal cage.
> - Keep the AP away from metal objects.


### Slide / Page 492

Disable SSID Broadcasting: it shows its presence and names when it is on, this discourages. If users know 
the SSID they can still connect with the password. 
 
Selecting a strong wireless encryption mode-


### Slide / Page 493

Detecting Rogue Access Points: 
 
Wireless Scanning- 
 
- Detects Wireless APs  
 
- If the AP is not listed, then it is a rouge AP 
 
- Wireless Discover tools such as insider, Netsuveyor, NetStumbler, Vistumbler, Kismet, etc… to detect 
wireless networks 
 
Wired Network Scanning- 
 
è Network scanners such as Nmap to identify Aps on the network; helps locate rouge wired devices 
 
Simple Network Management Protocol (SNMAP) Polling- 
 
- SNMP identifies the IP devices attached to wired network 
 
- SNMP utilities such SolarWinds, SNMP Scanner, Lansweeper SNMP Scanner, etc… identifies SNMAP-
enabled devices on the network  
 
To use SNMAP polling, the SNMP service on all IP devices should be enabled


### Slide / Page 494

Wireless Security Tools: 
 
- Cisco Adaptive Wireless IPS 
 
Provides wireless-network threat detection and mitigation against malicious attacks and security 
vulnerabilities


### Slide / Page 495

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - AirMagnet WiFi Analyzer PRO
> - RFProtect
> - https://www.arubanetworks.com
> - HH
> - Fern Wifi Cracker



---

## 🛠️ Connecting Theory to Practice
- **Execute the Lab:** Open [`labs/lab-03-tcp-wireshark-deep-dive.md`](../../labs/lab-03-tcp-wireshark-deep-dive.md) to work through the practical workshop reinforcing this module.
- **Reference Card:** Check [`cheatsheets/cct-exam-quick-reference.md`](../../cheatsheets/cct-exam-quick-reference.md) for rapid command syntax, formulas, and port mappings.
