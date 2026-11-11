# Module 17: Network Traffic Monitoring & Analysis

> **Source Material:** Authentic CCT Study Notes & Slide Deconstructions (Pages 662 – 678)  
> **Author:** [@Dabuynyx](https://github.com/Dabuynyx)  
> **Related Hands-on Lab:** [lab-03-tcp-wireshark-deep-dive.md](../../labs/lab-03-tcp-wireshark-deep-dive.md)  
> **Quick Reference:** [nmap-and-wireshark-commands.md](../../cheatsheets/nmap-and-wireshark-commands.md)

---

## 🧭 My Complete Study Notes & Slide Walkthroughs

### Slide / Page 662

Chapter 17 
Understanding the Need and Advantage of Network Traffic Monitoring 
 
Network Traffic Monitoring 
è Retrospective security approach that monitors the network for issues 
 
è Integral part of network security and is demanded within the network security operations of 
organizations 
 
è Continuous network traffic monitoring and analysis for effective threat detection


### Slide / Page 663

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - GD PrmesPovee State Sow [CC Tv Mente
> - I r Network
> - onitoring
> - Even when security tools are in place, attackers can
> - find ways to bypass such security mechanisms to
> - enter the network
> - ai
> - ?
> - 1
> - 1
> - 1
> - 1
> - i
> - ?
> - J
> - - Ca 4
> - - Security tools generally use signature-ba sed detection
> - techniques. Hence, they are often unable to identify
> - 0 continuously changing attack signatures/patterns
> - 1 |
> - I
> - 1
> - 1
> - I
> - 1
> - 1
> - -
> - |
> - 1
> - 1
> - Security tools are generally not designed to identify
> - behavioral anomalies and are unable to detect
> - activities of attackers that are initiated before and
> - during an attack
> - Copyright © by EG-Coumell. All Rights Reserved. Rey


### Slide / Page 664

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Advantages of Network
> - Monitoring
> - --> Understanding how data flows in a network
> - healt > Optimizing network performance
> - -> Avoiding bandwidth bottlenecks
> - Monitoring network
> - traffic helps in
> - pixies > Detecting signs of malicious activity
> - -> Finding unnecessary and vulnerable application:
> - Investigating security breaches
> - EC-Coumeil. All Rights Reserved


### Slide / Page 665

Understanding Baseline Traffic Signatures for Normal and Suspicious Network Traffic 
17.2


### Slide / Page 666

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - etwork Traffic Signatures
> - QA Signe set of traffic characteristics such asa source/destination IP address, ports,
> - Transmission Control Protocol (TCP) flags, packet length, time to live (TTL), and protocols (www)
> - Q Signatures are used to define the type of activity on a network a
> - Normal Traffic Signature q
> - ,
> - Attack Signatures
> - 7 Acceptable traffic patterns
> - » Suspicious traffic patterns not
> - allowed to enter the network
> - allowed to enter the network


### Slide / Page 667

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Baselining Normal Traffic Signatures
> - QC) Anetwork baseline is the accepted behavior for normal network traffic.
> - It is a benchmark to differentiate between normal and suspicious traffic
> - Q) Network traffic baselines differ between organizations and change over
> - time according to the operating environment and prevailing threat
> - scenario
> - some considerations to create a baseline for normal traffic:
> - TCP/IP communication involves a three-way handshake for normal
> - traffic
> - " ASYN flag appears at the beginning and a FIN flag at the end of a
> - connection
> - * All conversations originating inside the demilitarized zone (DMZ) are
> - trusted traffic items
> - Any traffic violating the network policies is malicious traffic; e.g., the
> - existence of File Transfer Protocol (FTP) traffic when this type is
> - restricted indicates a potential issue


### Slide / Page 668

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - s of Suspicious Traffic Signatures
> - AnioOYImationa
> - Reconnaissance
> - Traffic containing certain signatures
> - that may appear suspicious but
> - might not be malicious
> - Traffic containing certain signatures
> - that indicate an attempt to gain
> - information
> - Unauthorized Access Denial of Service
> - Traffic containing certain signatures
> - that indicate an attempt to gain
> - unauthorized access
> - Traffic containing certain signatures
> - that indicate a DoS attempt that
> - floods a server with a large number
> - of requests
> - Copyright © by EG-Coumell. all Rights R


### Slide / Page 669

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - ignature Analysis Techniques
> - Content 2d signature analysis
> - -- |
> - C) Attack signatures are contained in packet payloads
> - HEADER @ PAYLOAD *
> - O Check for specific strings occurring in the suspicious
> - payload
> - "
> - Atomic-signature-based analysis
> - C) Single-packet analysis is sufficient to detect attack
> - signatures
> - HEADER PAYLOAD
> - Context-based signature analysis
> - Q) Attack signatures are contained in packet headers
> - @ HEADER | PAYLOAD
> - Q) Inspect packets for unusual/suspicious header
> - information such as the following:
> - » Source and destination IP addresses
> - » IP options, protocols, and checksums
> - * Source and destination port numbers
> - » \P fragmentation flags, offset, or identification
> - Composite-signature-based analysis
> - QC) Multiple-packet analysis is required to detect attack
> - signatures
> - HEADER | PAYLOAD HEADER | PAYLOAD
> - Copyright © by EG-Couneil. All Rights Reserved. Reprod


### Slide / Page 670

TCP STREAM

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Packet Detats Pan
> - Packet Bytes Pane


### Slide / Page 671

Perform Network Monitoring for Suspicious Traffic 
17.3


### Slide / Page 672

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Follow TCP Stream in Wireshark
> - Mf Wiwechark - Follow TCP Stream (tep.stresm €q 25) » Ethernet - o os
> - , ee
> - Fae da View Go Coptore Ante Sutimics dephony Wieder Teoh. Hap
> - Cc@NSete tests aaan
> - THENOL8" Lost / HtTP/32.2 |
> - Host: wm.moviescope.com
> - | User-Agent: Mozilla/$.0 (Windows NT 10.0; Winé4; x64; ¢v:71.0) Gecko/2019036).
> - Firefox/72.0
> - Accept: text/html ,epplication/xhtwlenl,epplication/xl;9q-0.9,°/*5q°0.8 '
> - Accept+Language: en-US,en3q0.5 |
> - Accept-Encoding: gzip, deflate
> - Content-Type: application/x-mm-forn-urlencoded
> - Content-Length: 322
> - Origin: http://wew.moviescope.com
> - Key: _VIEMSTATIGONERATOR
> - Value: C2ttoes
> - ~ Form item: ~_EVENTVALIOATIONT = “/wiGaaSRour2EROInhO1CP IHEQEETE tr Rsl i Gak BONG ID OGG FOOL AND are Gv J2F If 36
> - Key! _SVENTVALIDATION |
> - Value: /widsrsdoue 2080 LeMMOLP INEGI trl I Gaf SOB EID MOC PCORANVANREGVD III LinSKugatirs GX? Rf qqtNSéass
> - ~ Form iter: “txtusername” = "san"
> - Key! txtusernane f Connection: keep-alive
> - Value: som Referer: http://mwu.eoviescope.com/ ,
> - ~ Form iter: Ttetmed” = Thest@i27 Upgrade-Insecure-Requests: 1 if
> - Key: txtemed
> - VIEWS TATE ©K2 Fh POWELL TEWDCSMSQ2OTSKTAGOVIAL ff mvthS2vPCOcOcPVU]T IduRfeSAKINPLIOGR__
> - VIEMSTATEGENERATOR@CIEEQAESS_EVENTVALIDATION=S2FwEGAASRpurZEROLNhHOIePIHEQUMeRUTE
> - DaE SOO RIDCNOGGCPOONLAKIaxReGVIQI2FF, jC PELWAZFEYEXTQ Pye}
> - SeGNUKTHs faql RIOR tx fusernancesonatatprdatestasoissgbtnlogineLogin \
> - Valuer testgizs
> - SEP EL TE cmOGeCFO CULAGax
> - “@3 Oe At 47 47 6) WAT Af 32 4c ad
> - S265 96 76 44-51 Go 32 46 33 6 33 41:77:59 4d ReewrQJZ PIF SaWSK
> - 75 G7 G2 4b 45.61.39. 72 SO 37 7052. 7271-74 wgetdadg ITzAf gat
> - 4e 35 36 G2 73 62 49 62 06 6) 70 A Ge 77 IS: 32— NGanaTd EcpslatD riuslecriuvdaecemte
> - 46 42 99 74 55 Se TL S879 77 43 Ge US OF AT Ge PEYEKIGE yu SScmn
> - de Ad S448 73. M4 TL Ae Ge 40 25 93 44 26 TE CTH HAg LrPeRIORE
> - ©2208 78 24 7S 73 GS 72 Ge Gl Od 65 96 26 74 xtuserna eeofEEht
> - 7h 7 7077 GL 34 14.65 73 74 2S 34-0 DL 3293 xtpedete sthe0229 Password revealed
> - 26 62 74 ter be OF 67 be Be de OF 67 0 Kotnlogi metogin
> - ina TCP Stream
> - DOF eae Creo torn ake), DO Packets: L222 * Depiayet: 45 (2.7%) * Oreeoet:


### Slide / Page 673

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Additional Wireshark Filters
> - tep.flags.reset==1
> - Displays all TCP resets
> - udp contains 33:27:58
> - Sets a filter for the HEX values of 0x33 0x27 0x58 at
> - any offset
> - http.request
> - Displays all HTTP GET requests
> - tep.analysis. Retransmission
> - Displays all retransmissions in the trace
> - tcp contains traffic
> - Displays all TCP packets that contain the word
> - “traffic”
> - !(arp or icmp or dns)
> - Masks out arp, icmp, dns, or other protocols and
> - allows you to view traffic of your interest
> - tep.port == 4000
> - Sets a filter for any TCP packet with 4000 as a
> - - source or destination port
> - tcp.port eq 25 or icmp
> - Displays only SMTP (port 25) and ICMP traffic
> - ip.srce==192.168.0.0/16 and
> - ip.dst==192.168.0.0/16
> - Displays only traffic in the LAN (192.168.x.x),
> - between workstations and servers — no Internet
> - sre VS KK. MAK. ARK. AA EE
> - ip.dst != xxx.xxx.xxx.xxx && sip
> - Filter bya protocol (e.g., SIP ) and filter out
> - ‘ unwanted IPs
> - ictly Pr 0
> - Copyright © by & cl All Rights Reserved. Reproductio


### Slide / Page 674

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - transfer files over
> - Tcp, and its default
> - port is 21 Ps
> - J
> - FTP sends data ina
> - cleartext format
> - Use the ftp filter to
> - check whether any
> - unauthorized FTP
> - sessions have been
> - established in the
> - network
> - a ae |
> - =21 Win=2108160 Len=0 ISv
> - =
> - 89 Response: "334 Password required
> - 66 aia d
> - 1 =
> - Sequence number: (relative sequence number)
> - oe soe Lo 21 (relative Raa ee )
> - k=51 Win=64256 Len=0 TSval
> - k=37 Win=2108160 Len=0 TSv
> - header Length: 32 bytes (8)
> - 39°47 00-45 Sd53°39 71 08 00 45 10 ]S9G-- ]59q =
> - df 62 Ga 32 0a 0a =-H2:0-@. “b-
> - 68 4e UNSEEN 90 18 : Y. oleat-
> - 08 0a 48 02 cb Ge 01 3e --
> - S78 72 -.USER A dalniste
> - ator


### Slide / Page 675

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Monitoring and Analyzing Telnet Traffic
> - Telnet can provide access to remote hosts including most network
> - equipment and operating systems
> - Telnet is not encrypted; the password and all other data are transmitted
> - as cleartext
> - Ideally, it should be disabled; enabling it poses huge security risks
> - to the network
> - It is essential to check whether any Telnet session is
> - established within the network
> - Copyright © by Ef


### Slide / Page 676

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - for established Telnet sessions:
> - =
> - & Goto the Statistics Menu and
> - click on Conversations
> - ¥
> - > Goto the TCP tab and select
> - the appropriate Telnet
> - communication indicated by
> - port 23 and click Follow
> - Stream...
> - > The Telnet traffic and the
> - credentials will be viewable
> - in cleartext
> - Qo Perform the following to check
> - Monitoring and Analyzing Telnet Traffic (Cont’d)
> - '
> - ar
> - epee
> - 2°
> - f
> - > Differentiated Services Field: 0x10 (DSC
> - Total Length: 79
> - Nov 27 20:21:42 en ttyp2 froe bam. 2:09.079
> - peros tickets issued.
> - D.G-eta (OOF) 4: Tu Oct 42 20:42:22 COT 1799
> - fags: Ox me Frageent Meleone te Opens: The preactively secure Unie-Line operating sy
> - Please ure the seadbug{t) UUILLy to report bugs In the system
> - ato 00 4f 46 Je 40 00 40 Zi 73 07 co a8 00 Betore reporting a bug. pleave try to reproduce it with the late,
> - veraion of the cose, With buy feports, please tty to ensure t
> - Crough inforsation to reprosuce the preblea is enclosed, and 2
> - trow {1x for At casts, incluge that as well
> - 3 /421n/ping ma, vadeo.com
> - hts Reserved.


### Slide / Page 677

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Monitoring and Analyzing HTTP Traffic
> - Capturing from etho
> - “File 6 View Go Capture Analyze Statistics Telephony Woeless Tools Help i
> - ZREAZOPDRVOR ee Stele
> - Q The HTTP sends information in plain
> - text
> - Q Monitor and analyze HTTP traffic for
> - the following purposes:
> - ® Check whether any sensitive
> - information is sent using HTTP
> - = Detect malicious traffic
> - = Check the traffic against a policy
> - violation
> - = Detect applications using Encoded: applicatien/x-mmw-fora-urlenc
> - . . ARSE!
> - unnecessary/restricted services
> - Q Use the http filter to check the
> - specific HTTP traffic


### Slide / Page 678

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Network Sniffers for Network |
> - tcpdump is a command-line network analyzer or a
> - =) tcpdump packet sniffer that helps in capturing and analyzing
> - network traffic
> - Riverbed Packet Analyzer P
> - https://wraw.riverbed.com
> - root@ubuntu:/home/ubuntu)
> - fe)) OmniPeek
> - root@ubuntu: /hone/ubuntus | tcpdunp-tiany) ; t i
> - tcpdunp: verbose output suppress: usen-v or -vv for full protocol decode. ; oC, Attps://vvaw.liveaction.com
> - listening on any, Link-type LINUX_SLL (Linux cooked), capture size 262144) bytes
> - 00:11:47.680445 IP locathost.mdnsi> 224.0.0-251-mdns: © (2q]| PTR (QH)?) pps.
> - mocals PTR (QM)? _tpps._' sche local. (45)
> - 224. a pesddevarpat (os) i : fA» Observer Analyzer
> - 60:11:47.106763 IP ubuntu.43582 > _gateway.domain: 54303+ [1au] PTR? 251.6.0: 224) : we ¢ pemeney mienees ‘spill
> - //wviw.viavisolations.com
> - -in-addr.arpa. (53)
> - 7.109566 IP _gateway.domain > ubuntu.43582: $4303 NXDomain 0/1/1 (110)
> - 7.111851 IP ubuntu.43582 > _gateway.donain: $4303+ PTR? 251.0.0.224:1i -3d)
> - 7.117485 IP _gateway.domain > ubuntu.43582: $4303 NXOomatn 0/1/0 (99), "5 a
> - 7.119111 IP localhost.35287 > localhost.domatn: 61525+ (1au] PTR?) 53-0. Ces SolarWinds Deep Packet
> - a i Inspection and Analysis
> - 247.909735 IP6 ubuntu.mdns > ff62::fb.mdns: 6 [2q) PTR (QU)? —tpps._tcp., Attps://wwew.solarwinds.com
> - lL. PTR (QH)? _tpp._tcp.local. (45)
> - 47.910452 IP localhost.42133 > localhost.donatn: 27298+ [1au) PTR? b.f.
> - 0.0.0.0.0.0.0.0.0.0.0.0.0.6.0.0.0.0.0.0.0.0.0.0.2.0.f.f-1p6.arpa. (101) i
> - 47.911456 IP ubuntu.36331 > _gateway.domain: 20696+ [1a] PTR? b.f.0.0 i
> - -0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.2.0.f.f.1p6.arpa. (101) i 3 ‘ Xplico
> - 47.914304 IP _gateway.domain > ubuntu. 36331: 20696 NXOomatn 0/1/1 (365) H a hetps://veww.xplico.org
> - 47.915164 IP ubuntu.36331 > ae gongs 20696¢+ PTR? G0. 10.0. Os OF ; f
> - ic iaselarnghe



---

## 🛠️ Connecting Theory to Practice
- **Execute the Lab:** Open [`labs/lab-03-tcp-wireshark-deep-dive.md`](../../labs/lab-03-tcp-wireshark-deep-dive.md) to work through the practical workshop reinforcing this module.
- **Reference Card:** Check [`cheatsheets/nmap-and-wireshark-commands.md`](../../cheatsheets/nmap-and-wireshark-commands.md) for rapid command syntax, formulas, and port mappings.
