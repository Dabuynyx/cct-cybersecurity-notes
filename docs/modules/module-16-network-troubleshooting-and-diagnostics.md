# Module 16: Network Troubleshooting & Diagnostics

> **Source Material:** Authentic CCT Study Notes & Slide Deconstructions (Pages 627 – 661)  
> **Author:** [@Dabuynyx](https://github.com/Dabuynyx)  
> **Related Hands-on Lab:** [lab-03-tcp-wireshark-deep-dive.md](../../labs/lab-03-tcp-wireshark-deep-dive.md)  
> **Quick Reference:** [nmap-and-wireshark-commands.md](../../cheatsheets/nmap-and-wireshark-commands.md)

---

## 🧭 My Complete Study Notes & Slide Walkthroughs

### Slide / Page 627

Chapter 16: Network Troubleshooting- 
Overview of Network Trouble Shooting 
16.1 
 
Troubleshooting: Process of finding issues in a computer network and diagnosing them.


### Slide / Page 628

Basic Network Issues: 
 
è Unreachable Networks: ICMP destination is unreachable if host or port is unreachable or the 
network is unreachable 
 
Destination Unreachable Message: 
 
è ICMP returns with a unreachable message when it cannot be forwarded to its destination 
 
à Fragmentation packet is required to transfer a packet 
 
è May be that the FTP or web services are unavailable


### Slide / Page 629

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - > Network Issues: Time Exceeded Message
> - ICMP Time Exceeded
> - Type =11
> - IP Header
> - Type (8 bits) Code (8 bits) Checksum (16 bits)
> - Parameters
> - Data.
> - O) ATTL value is defined in each datagram (IP packet)
> - Q) As each router processes the datagram, it decreases
> - the TTL value by one
> - When the TTL of the datagram value reaches zero, the
> - packet is discarded
> - ICMP uses a time exceeded message to notify the
> - source device that the TTL of the datagram has been
> - exceeded


### Slide / Page 630

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - ‘rk Issues: IP
> - .eter Problem
> - _ forward a datagram owing to some type of error in
> - the header
> - Q This error does not relate to the state of the
> - destination host or network but still prevents the
> - datagram from being processed and delivered
> - Q AnICMP type-12 parameter problem message is sent
> - to the source of the datagram i)
> - ICMP Parameter Problem _ Type (3) Code (0-12) Checksum
> - Type = 12 Unused (must be zero)
> - Internet Header + First 64 Bits of Datagram


### Slide / Page 631

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - are not the result of lost packets or error conditions that
> - of conditions such as the follow


### Slide / Page 632

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Basic Network Issues: ICMP Redirects
> - ICMP Redirects Type Code
> - Type = 5, Code = 0to3 (8 bits) (8 bits) a
> - Parameters
> - The default gateway sends the ICMP redirect/change
> - request messages only if the following conditions are met: Data..........
> - The interface on which the packet enters the router is the
> - same as that on which the packet is routed out
> - The router is configured to send redirects
> - The subnet/network of the source IP address is the
> - A ke same as that of the next-hop IP address of the routed
> - packet
> - The route for the redirect is not another ICMP
> - redirect or a default route


### Slide / Page 633

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Troubleshooting Network
> - Issues: IP Problems
> - Using tools, locate the devices that raised the issue in
> - the path of communication
> - Check the physical connections between the source and
> - the destination
> - LAN connectivity faults can raise network connectivity
> - issues
> - At each intermediate hop, check whether the router is
> - working
> - © Ensure the proper configuration settings of the devices


### Slide / Page 634

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Tr
> - ‘ing Network Issues: Network Cable is
> - Unplugged
> - The network issue called “network cable is unplugged”
> - indicates that the computer is not detecting an Ethernet Everts Resources Power Management
> - connection correctly |
> - network adapter. Click
> - left. and then select ts value
> - latel(R) Ethernet Connection (7) 1219-V Properties 4
> - Theo £ a aaa
> - ihe followi 1c
> - Value
> - [Pato Negotaton =]
> - Restart the computer
> - Check the Ethernet network cable
> - Change the Ethernet Adapter’s Duplex Settings
> - Disable the Ethernet Network Adapter
> - Update the Network Adapter Driver


### Slide / Page 635

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - roubleshooting Network Issues: Network
> - Path Cannot Be Found
> - CQ) The issue of “network Path was not found”
> - may arise for the following reasons:
> - » The network connection does not exist
> - >» The network security settings do not allow sharing
> - » The name of the computer with which the connection is to be established is too long
> - ‘
> - » The connection of system is blocked by firewall or the antivirus software
> - Network Error exe (¢ ? Troubleshooting
> - Windows Cannot access \\test v Verify the shared drive
> - Check the spelling of the name. Ctherwise, there might be a problem weh your network. To v Ping the IP address of the ta
> - try to sdentrfy ard recolve network problems, chick Diagnose
> - ¥ Modify the network security
> - (A) Hide detois
> - Y Reinstall the network adapt
> - Y Enable NetBIOS over TCP/IP
> - ¥ Rename the computer
> - Y Disable the firewall
> - Cugnose Cancel
> - Enror code: Ox20070035
> - The network psth was not found.


### Slide / Page 636

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Troubleshooting Network Issues: Physical
> - Connectivity Issues
> - Steps to Troubleshoot Physical Connectivity Issues
> - Check for aC
> - » Check that suitable cables are used for connections between devices
> - » Loose connections are to be avoided
> - » \f there are no loose connections, check for old cables and replace them with new ones
> - and then try to connect the device
> - > If the problem persists, then it may be faulty port issue
> - Check for
> - » Check the ports where the link is established and confirm that the indicator lights are
> - on
> - Check for tr
> - ® Crosscheck the capacity of the devices in the network and the traffic flowing through it
> - > Exceeding the specified limit could lead to the interruption of communication between
> - the source and destination aa
> - _—
> - 7 =
> - Copyright © by EC-Coumeil. all Rights Reserved. Reproduction is Strictly Prohibitl/
> - ,


### Slide / Page 637

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - #teps to lroubleshoot #hysical Routing Issues
> - Use the traceroute utility to locate the hop/router responsible for the
> - problem
> - If the issue persists, investigate each hop/router to find where the
> - problem has occurred
> - When the problematic hop/router is detected, login to it using
> - Telnet and ping the destination and source
> - If the ping is unsuccessful, configure the routes between the source and
> - destination with a subnet mask if they are not defined
> - Check for a routing loop by pinging again. If it exists, rectify it by tracing
> - and reconfiguring the routing
> - <q) Check the routing protocol if the problem persists, and change it
> - ’ according to the network
> - .ooting Network Issues: Routing Problems
> - ?
> - 1
> - '
> - '
> - '
> - '
> - '
> - '
> - '
> - '
> - '
> - '
> - '
> - '
> - '
> - i
> - '
> - '
> - '
> - '
> - '
> - '
> - '
> - '
> - '
> - '
> - '
> - '
> - '
> - '
> - '
> - '
> - 1
> - '
> - t
> - 1
> - '
> - '
> - '
> - é
> - Copyright © by E6-Coumell. All Rights Reservec
> - = fl
> - TS -


### Slide / Page 638

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Trouble:
> - Firewall blocking the flow of incoming and
> - outgoing traffic
> - «
> - Server or service down
> - |
> - yy j Authentication Process issue resulting in the
> - * | inability to access a service between the host
> - ’ A and server
> - | Issues with software compatibility of the
> - | devices, version mismatches, etc.
> - ting Network Issues: Upper-layer Faults
> - til
> - Move the host in the network such that it
> - bypasses the firewall blocking the traffic.
> - Replace the server that is down with a
> - temporary server to continue the services.
> - Use software to deploy checks for
> - authentication-related issues.
> - Upgrade the devices such that they are
> - compatible and have the same version.


### Slide / Page 639

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - ing Network Issues: Wireless Network
> - Connection Issues
> - .. whether Wi-Fi is enabled in the devices: i
> - » Go to Settings > Network & Internet > Wi-Fi
> - ‘
> - ; OQ Ifthe problem persists,
> - > Check and change the service set identifier
> - (SSID) and access points to allocate the
> - requesting device an IP address
> - QO) Use the Windows Network Diagnostics tool to
> - troubleshoot the network-related issue:
> - » Windows Network Diagnostics will troubleshoot
> - and detect the problem by downloading and
> - installing available patches
> - CQ) Restore the router to its factory settings and
> - restart it
> - Copyright © by EC-Coumell. All Rights Reserved


### Slide / Page 640

Learn Troubleshooting Basic Network Issues Using Utilities and Tools 
16.2


### Slide / Page 641

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Network Troubleshooting Utilities and Tools: Ping
> - E The ping utility is used to test whether an IP address or a website is accessible by the host
> - 6 A reply from the pinged IP address indicates that the packets are transferring between the system and given IP
> - me (Ct Launch command prompt and execute ping x.x.x.x orping example.com tocheck the availability of the
> - = host to the computer
> - iS The message “Request timed out” indicates that there is no connection between the system and host or that the system is
> - unable to connect to the host
> - SB CAWindows\
> - system32\cmd.exe = Oo x }
> - “eiping & -§
> - Cz \Users\
> - pinging 8.8.8.8 with 32 bytes of data:
> - bytes=32
> - bytes-32
> - bytes-32
> - | bytes-32
> - Ping statistics for 8.0.8.8:
> - Packets: Sent - 4, Received - 4,
> - pproximate round trip times
> - Minimum - 5S5as, Maximum = 183ms, Average = 111s
> - time
> - SSms TTL-128
> - time-183es
> - time-162m=>
> - TTt-128
> - TTtL-128
> - time-G67ms TTL-128
> - Lost
> - in milli-seconds:
> - - © (0% loss),
> - >ping 8.8.8.8
> - with 32 bytes of data:
> - timed out.
> - timed out.
> - timed out.
> - tined out.
> - Ping statistics for 8.8.8.8:
> - Packets: Sent = 4, Received = 8, Lost = 4 (100% loss),


### Slide / Page 642

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Network Tr
> - QO) The traceroute utility is used to trace
> - packets across a network and to
> - understand connections to a server
> - \It sends an ICMP echo request message
> - to the specified destination
> - If the destination is active, it sends
> - ICMP echo reply messages as a
> - response, which confirms that the
> - connection is active
> - If not, the destination may not be
> - active, or it could be a connectivity
> - issue of the source
> - ibleshooting Utilities ©
> - and Tools: traceroute/tracert
> - NUse eotracert Seevegeua.con
> - racing route to &
> - Bpver a maxinun of 38 ho}
> - ns
> - ns
> - ns
> - ood
> - ns
> - 3m
> - (288 .43.115.82)
> - 192.168.1.254
> - 18. -
> - 34
> - 14.134
> - Request tined out.
> - 7S.184.217.183
> - tei-S.bbrOi .vb81.seaBi .netuorklayer.com (206.81.
> - ac8.bbré@i.cs81.denBi.networklayer.con (173.192.1)
> - ac?. bbr62.cs@1.den@1 .nctworklayer.con (173.192.1
> - ac8.bbr@2.eq81.chi8i .nctworklayer.con (173.192.1
> - ac8. bbrd2.cq@l .wic82.netuorklayer.con
> - act .dar@i.sr@i.udcBl .netuorklayer.con
> - pot. fcr@i.sr@i.uicOi.netuorklayer.con (2609.43.11
> - cmmmeguati.con (289.43.115.82)


### Slide / Page 643

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - S& aN OQ) ipconfig is a command-line utility used to display all current TCP/IP network configuration
> - <y values along with the IP address, subnet mask, and default gateway for all adapters
> - Q ifconfig is a similar utility but for Linux-based machines
> - soe
> - Fie Eat View Search Termrol
> - >\Users\ ipconfig 8.
> - indows IP Configuration
> - inet 10.10.10.13 netmask 255.255.255.0 broadcast 10.10.10.255
> - Ethernet adapter Etherneto: inet6 fe80::8064:a0e6:facb:283 prefixten 66 scopeid Ox20<lLinio
> - ; ether 00:0¢ eb:cd:af txquevelen 1000 (Ethernet)
> - RK packets 621 bytes 865066 (844.7 KiB)
> - Link-local IPv6 Address #e80: :aS$1f:1¢29:8fa1:2182X6 } RX errors 0 dropped O overruns O {frase 0
> - IPva Addross. . . . . - 10.10.10.10 TX packets 102 bytes 7793 (7.6 Ki8)
> - Subnet Mask . . 1. 2 + « 2$S.25S.25$.0 TX errors @ dropped 0 overruns © carrier 0 collisions 0
> - Default Gateway . . . : 10.10.10.2
> - Connection-specific ONS
> - 0: flags=73<UP,LOOPEACK,PUNNING> stu 65536
> - inet 127.0.0.2 netmask 255.0.0.0
> - inet6 ::2 prefixlen 128 scopeid 6xl0<host>
> - £080: :7099:753F :b7¢8:b27b%X7, Loop tuguevelen 1009 (Local Loopback)
> - PS bi RK packets 82 bytes 6826 (6.6 Kis)
> - Connection-specific ONS Suffix
> - Link-local IPv6 Address ... .-
> - Autoconfiguration IPv4 Address. 169.254.178.123
> - Subnet Mask . . . 05 ? 255.255.0.0 FX errors @ dropped © overruns © frame 0
> - Default Gateway . . o- TX packets 82 bytes 6826 (6.6 Ki8)
> - TX errors © dropped © owerruns O carrier @ collisions O


### Slide / Page 644

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - S ‘ "4 ‘* 7 i } (ZA WI .
> - Swi, ANIL ett CS) | DADANSZZIBZ Wy BSS |II(( SN ff
> - The nslookup utility is used to lookup a specific \P address or multiple IP addresses associated with a domain name(s)
> - at atime
> - ADVE i
> - °
> - nslookup is used when a user can access a resource by specifying its IP address but not by specifying its domain name
> - The nslookup utility is used to resolve DNS address resolution issues
> - The nslookup command is executed in the command prompt to lookup the IP address for a domain name
> - G2Nu wnslookup www.google.com
> - CiServer: dns.googie
> - Address: 8.8.8.8
> - sfNon-authoritative answer:
> - Name: www.google.com
> - Addresses: 2404 :6800: 40607 : 866: : 2004
> - 142.250.196.68


### Slide / Page 645

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - etwork Troubleshooting Utilities and Tools: netstat
> - CL» netstat is a command-line utility used to display both the incoming and outgoing TCP/IP traffic
> - [4° The current state of the active hosts on the network can be determined using netstat
> - [» netstat is also used to identify the services associated with user-defined ports
> - r > Execute the netstat command without any parameters in the terminal to show the list of active connections
> - > Use thenetstat —e command to show the statistics of various protocols h
> - ormmand Prompt
> - netst
> - ace Statistic
> - Received Sent
> - 3850711362 49360888
> - tT packets 5477744 607283
> - picast packets
> - cs
> - °
> - °
> - °
> - m protocols
> - >


### Slide / Page 646

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Utilities and Tools: PuTTY
> - PuTTY is an FTP or
> - SSH FTP (SFTP)
> - client for
> - transferring files. It
> - generates hashes
> - for passwords
> - PulTY Configuration
> - Caregory: Basic options for your PuTTY sesn0r
> - Logging Host Name (or 1P address) Bort
> - = Terral 22
> - Keydows Connecbon type:
> - Bex OR OFeinet Rog gH \sepeat
> - Features Load, save oF Gciete 3 stored sesn0n
> - ~ Wiexdow _ Saeed Seaton
> - Appaw ance
> - Defaut Setungs bed
> - ' Onty on Gean cat
> - A A eRe ee


### Slide / Page 647

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Utilities and Tools:
> - IP Subnet Calculator
> - | Subnet Oy ee Ee |
> - about IPv4 and IPv6 subnets and for
> - the division of classes of subnets -
> - |
> - I addres aad Netoiayk |
> - } Radom IP I
> - ©
> - IP Address:
> - Subnet is used to find information
> - \
> - |
> - |
> - |
> - i
> - Netmask:
> - The IP subnet calculator is used to define
> - Wildcard Mask:
> - possible IP addresses, along with classes | Gn Notation:
> - of IP Network Address: 100.00
> - @
> - Usable Host Range: 10,0.0,2-10,.0.285.254
> - Broadcast Address: 10.0,255.355,
> - Binary Netmask: 1111121.11133221.00000000,00000000,
> - Broadcast ranges, network, and host
> - ranges are calculated using the IP
> - |
> - calculator { Larcta Ultdouoiluse abebesinee f
> - :
> - Total number of hosts:
> - Number of usable hosts:
> - ©
> - Move to adjacent network Bacenre | Formed


### Slide / Page 648

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Learn Troubleshooti work Issues using Utilities and Tools
> - ~ ; :
> - QO) speedtest.net is a website used to determine the available bandwidth
> - for a host at a point of time
> - Q The bandwidth values assigned by the service provider may differ from
> - the actual bandwidth values
> - ett.
> - @ PINGms © DOWNLOAD Mbps @ UPLOAD Mbps
> - 3 17.41 542.19
> - s es (<0 ) oo Fibernet
> - bss 2 9 @
> - Change Server
> - ght © by £6-Commell Ai nj


### Slide / Page 649

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Network Troubleshooting Utilities and
> - Tools: pathping
> - The pathping utility is used to provide detailed information about the path
> - characteristics from a specific host to a specific destination in a single picture
> - In the first step, pathping traces the route to the destination. Next, it runs a 25-s
> - test on this route and collects the rate at which data is lost at each router
> - Use the pathping —n command to show numeric IP numbers instead of DNS
> - host names h
> - eo
> - google (8.8.8.8)
> - ver 2 maximum of 30 hops:
> - Windows10 [(10.10.10.10}
> - 10.10.20.2
> - 2192.168.2.2
> - 100.64.63.254
> - 192.168.34.201
> - 192.168.48.6
> - 192.168.48.2
> - 192.168.48.49
> - nsg-corporate-229.104.185.122.airtel.in (122.185.104.229
> - 182.79.198.6
> - 72.14.208.234
> - 208.170.234.3
> - 142.251.55.227
> - Gns.google (8.8.8.8)
> - °
> - 2
> - 2
> - 3
> - a
> - 6
> - 7
> - 8
> - 9
> - Computing statistics for 325 seconds...


### Slide / Page 650

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Network Troubleshooting Utilities
> - Sra
> - and Tools: route
> - Q The route utility is used to show the
> - ongoing status of the routing table on
> - the host
> - sIntel(R) 825741 G: Dit Network Connection
> - sa scoreitecpbackrintertace) s
> - OQ Netmasks, network destinations, and Se TaletonertChISATASAgapter
> - = = O09 00 00 ©0 Teredo Tunneling Paeudo-Interface
> - gateways are displayed in the active C0 00 00 e0 Microsoft ISATAP Adapter 22
> - routes section of the route utility
> - =: oes
> - Network Destination Netmask Gateway
> - 0.0.0.0 0.0.00
> - QO route [-p] command dest 10.10.1010 __285.268.268.0 : iecaes
> - = 10.10.10.10 255.255.255.255 10.20.10.10
> - [mask subnet] gateway [-if thee : 50.20, 50.39
> - interface] is the command for 35s: : :
> - 3 " z - 0. = - 169. ates 278. 223
> - adding, deleting, or changing a route } e378: ae see a eara7e7s23
> - 0.0. - 27.0.0.
> - entry 0. 0. seo 38404
> - 2. 240.0.0. On-link a
> - 255.255.255.255 355°: 3850 258-258 127.0.0.3
> - 255.255.255.255 255.255.255.25 5 269.254.278.123
> - 255.255.255.255 255.255.255. 20.20.10.10
> - metric
> - Default
> - IPv6 Route Table
> - Active Routes
> - twork Destination
> - 13/0


### Slide / Page 651

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Network Troubleshooting Utilities and Tools: Nmap
> - 2 Nmap ("Network Mapper") is a security Service Discovery
> - scanner for network exploration
> - oe Terman - o Pad
> - Scan Toot Profie tielp
> - It allows the discovery of hosts, ports, and D | tergee | 10.10.1016 <) Protite =] . [scan
> - GS services on a computer network, thus creating commana:
> - a “map” of the network (litem) services Nenap Output Ports /Mowts Topology Most Deta Scans
> - OS ¢ Most 7 nenep -6T ow 10.10.1016 a | °. %
> - Host Discovery aa coon Sommer ps
> - — o~
> - ‘ ” — open
> - Lenenep - a =< eren
> - conn
> - ran loot Protie ticip open
> - oom
> - eget | 10:10.100-13 T] Preteen 7] ee pense
> - =
> - se oer
> - Saas] Eericas] . hemap- Craps ‘Pens stem, Vepelogy Sine Octnts” Scone onen
> - Satan = fomepan 08 1O0RIODS =] =
> - a Seacstad: ase? ae ( Mttpe //nmap.ore ) ot 2O2E-Co-28 12:97 paseo
> - ~ torowr Se elgren -
> - > rerorow = =
> - 2 Cr\evegres Pites (x06)\uene
> - > 4 2 IP address (1 host wm) scanned in 226.66
> - Pater Mout gear


### Slide / Page 652

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Service and Version Discovery
> - Commend
> - remap -a¥ TDID. 1009
> - Sterting tmeo
> - wicrosott TTS meted
> - Is/tew
> - 18 ee
> - petpion aie
> - 445/teR CoN wleroRet toes
> - 10 aicroxort €s (worepresp) MDREGEOUP)
> - D289/LED OMA -SEL/e WOR Server?
> - SHIP Seen BITS Ricrosett mttRast
> - tts 2.0 (9S0P ure)
> - PAC ADICEND, OOOC D9. TR AD (Weare)
> - SAOVACe_infe; Most: MINDONSIO; C5: wincows, CPE) cowry
> - Lervice Getectlon pertormns. Please report any
> - Incorrect results st Mttps!//neap.org/subelt/ .
> - Mmea_gene: 2 IP ecsress (2 hoat vo) scanned in 67.35
> - seconds
> - Network Troubleshooting Utilities and Tools: Nmap (Cont’d)
> - OS Discovery
> - nema > sseept amber dncavery mee AOMAND.10
> - Starting map 7.80 ( pttpsi//neap.oce )
> - 13:99 GT Stansera Tine
> - Meas scen report for 10.10.10.10
> - St ds wD (O,008 Latency)
> - Sat. anowns |993 closes ports
> - STATE stavice
> - Dree we
> - mMortee meee
> - Ine -_re
> - Ae eew AetBies—van
> - microsoft a.
> - ma Ot werver
> - OS: Windows 10 Enterprise 10%n6 (Windows 10
> - Enterorise 6.3)
> - OF CPL) Cpe i/o microsort iminsows
> - Computer nese: Wingows10
> - NetBIOS Komouter name: WINOOWSIO\xO0
> - MorKEroup! MORKGROUP\ «00
> - System time: 2022-06-207T23) 39156005130
> - Neew_dune: 2 IF avaress (1 Host up) scanned in 1,56
> - Aecongs
> - © by (€-Coumcll Al Rights c Reproduction is Strictly Prohi


### Slide / Page 653

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Network Troubleshooting Utilities and Tools: Wireshark
> - Qa ‘Wireshark enables capturing and interactively browsing the traffic in a computer network
> - Ott captures live network traffic from Ethernet, IEEE 802.11, PPP/HDLC, ATM, Bluetooth, hig Token Ring, Frame Relay, and
> - "Fob! networks.
> - -~ eee renner eee teeeeemeeereneeee
> - il rf eener®
> - Loe Kiem Go Captune  Anatyze  Stemntice ( Teck  tteip
> - Skeshcahle deettarts: teal
> - Ter || nase 80 2 2790 [Pe
> - tee (| base Bo = E730 fe
> - ree 341700 = we (ACK.
> - PEI +60.915710
> - *S2 SHO.929124
> - a To. 2434 we = 1790 [Pe
> - ‘SS S8O.930779 Bred 2334 BO = 3750 (Ace.
> - 06 460.93077) 237.20.292.200— rer A424 GO = 2720 (acm
> - G7 660.990779 237.36.292.200 To? 2954 co = 2730 (Pom
> - SE L50.9305179 10.10.10.30 oo; 34 1700 + be [ACK
> - OP >00,9)6208 - - tc. 2o24 GO = 2730 [acm
> - SO 380. 992508 30.20.10.20 ree 2324 Bo = 3730 [ACK
> - O2 380.936506 20.20.2020 TCR 2934 ce + 2790 [Pa
> - YI 280.9724 10.1 327-18.222,200 Tor 34 n73@ = wo [ACK
> - OP 4eO.950015 337. 19.30, 38-10\ (rer) GAS 60 = 3770, Liguaa -j} noe
> - 63 bytes Captured (370 Bite) on Interface
> - fevicdiaf>. Ont: Veeere fer2eioi (00:40:%
> - Internet Protocol Version 4, Src) 19,10,30.13, Ost: S.9.8.6
> - User Oatagras Protocol, “re Ports 30379, Oxt Ports 8
> - Krein ewe System (query)
> - POOGN, IATA bytes on wire (11692 tee IAS bytes aKa ease Glen pits
> - weet IL, Set Wieere_fer2G1 G2 (OOrTO1SEIFer2E: GL), Ost: Vreere_af i 7914d (OO1Oc! Ai}?
> - ~et Protocol Version 4, Srct 137.308.752.200, Ost: 10.10.10,10 ie
> - aAcks 3
> - mission Control wrotecol, Se Port! BO, Ost Mort: 1720, Seah 274037773.
> - ELLER LA ELF LS TEER OE EET EET ORS HEE SRP MA POM ER RES BOE EE F


### Slide / Page 654

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Network Troubleshooting Utilities and Tools: Hping2/Hping3
> - ] Hping2/Hping3 is command line networt i fting tool for the TCP/IP protocol
> - It can be used for network security iting, fir | ing, manual path MTU discovery, advanced traceroute,
> - remote OS fingerprinting, remote uptime guessing, TCP/IP stacks auditing, etc.
> - ACK Scanning on port 80
> - To oe
> - Fle €
> - View Search Termirei Help
> - b
> - set, 28 headers + 8 data bytes
> - O rtt=4.9 as
> - al rtt=4.2 as
> - Seq=2 rtt=3.3 a5
> - 46780 icmp seq=3 rtt«3.1 as
> - 46781 icmp _seq=4 rtt=2.2 as
> - 46782 icep_seqeS rtt=9.1 as
> - 6783 icmp_seq=6 rtt«=8.1 ms seqe6 winsd
> - P_seq=7 rtt=8.0 as $eq=7 wind
> - Pp. “8 rtt=4.] as seqeS wine
> - 10.10
> - transmitted, 9 packets re
> - in/avg/@ax = 2.2/5.2/9.2
> - itted, 9 packets received. O% packet loss
> - g/max = 2.0/5.1/8.4 as
> - ed, O% packet loss


### Slide / Page 655

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Network Troubleshooting Utilities and Tools: Hping2/Hping3
> - QO T- Hping2/Hping3 is command line network scanning and packet crafting tool for the TCP/IP protocol
> - 02 - Itcan be used for network security auditing, firewall testing, manual path MTU discovery, advanced traceroute,
> - é Temote OS fingerprinting, remote uptin.e guessing, TCP/IP stacks auditing, etc.
> - ICIVIP Scanning ACK Scanning on port 80
> - — ap
> - 46790 s a)
> - F id=46791 a
> - ttle128 OF id=46792 sport=80
> - ttl=123 OF id=46793 sport=80
> - Ltlel28 OF id=s6795 sportssd
> - 6-trip min/avg
> - e@parrot


### Slide / Page 656

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Network Troubleshooting Utilities and Tools: netcat
> - QO netcat is a network utility used for rane network connections on both Windows- and
> - Linux-based systems
> - O It provides various commands to perform the thorough monitoring of traffic flow
> - across a network
> - QO) It provides features such as port scanning, OS fingerprinting, file transferring, DNS
> - checking, and source routing
> - Q Test the connectivity with a remote host using the following coh: manc|
> - ne -w3 -4 -v <target host> <port number>
> - 0
> - Perform port scanning on a given IP address or host name using the following
> - command:
> - nce -v -n <IP address> <port number/range>
> - fa i ubuntu@ubuntu: ~
> - ~$ nc -w3 www.google.com 80
> - n 10.10.16.16 21
> - wrn.google.com 86 port [tcp/http) succeeded!
> - |
> - Connection to 1 © 21 port [tcp/*] succeeded
> - 226 Microsoft FTP Service


### Slide / Page 657

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Network Troubleshooting Utilities and Tools: dig
> - | The dig command can be used on Linux-based systems to query DNS servers and retrieve information about
> - target host addresses, name servers, and mail exchanges
> - Retrieve a specific DNS record Test whether the target DNS allows zone transfers
> - ubuntu@ubuntu: = 2 fi ubuntu@ubuntu: ~
> - S[dig as certifiedhacker.con| Atus : s[ato @ns2-bluchost.conm certtftedhacker.con axfr
> - <<>> O1G 9.11.5-Pi-lubuntu2.6-Ubunty <<>> ns certifledhacker.con
> - global options: +cnd
> - Gt answer:
> - =>>HEADER<<- opcode: QUERY, status: NOERROR, id:
> - flags: qr rd raz QUERY: 2, ANSWER: 2, AUTHORITY:
> - OPT PSEUDOSECTION:
> - EONS: version: 0, flegs:; udp: 6sa94
> - QUESTION SECTION:
> - ttf ledhacker.con. IN
> - 33 ANSWER SECTION:
> - icerttftedhacker..con. fs1.bluehost.con.
> - icertiftedhacker .con. ns2.bluehost.con.
> - Query tine: 129 nsec
> - SERVER: 127.0.0.53853(227.0.0.53)
> - WHEN: Mon Jun 28 05:17:34 POT 2022
> - MSG SIZE revd: 93


### Slide / Page 658

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Network Troubleshooting Utilities and Tools: arp and tcpdump
> - A command-line tool
> - used to troubleshoot
> - th ARP cact ab].
> - the ARP cache table nterface: 10.10.10.10 --- ©x6
> - in network devices Internet Address Physical Address
> - é 10.10.10.2 @0-SO-S6-fc-26-81
> - "UL such as routers, -10.10.255 ff-ff-ff-ff-£F-FF
> - oe 4 i -0.0.22 ©1-00-Se-00-00-16
> - Wy pools ate y switches, and other 10.0.252 01-00-Se-00-00- fc
> - wi baree® ji ‘ 224.0.0.253 01-00-Se-00-00-fd
> - Le routing devices See as.
> - Dovel sll
> - root@ubuntu:fhome/ubuntuy fF) =
> - | ootgubuntu: /hone/ubuntus] tepdunp =A any =< 3]
> - cpdump: verbose output suppress: use or -vv for full pro
> - ‘ocol decode ehh ca seen A network packet
> - A{stening on any, nk-type LINUX_SLL (Linux » capture :
> - ize peared bytes capturing tool used
> - 15:49:36.601995 ARP, Request who-has _gateway (Broadcast) tell for analyzing
> - 10.10.10.10, length 46 SAS
> - D5:49:36.809197 IP Llocalhost.$4838 > localhost.donatn: 7288+ [ network traffic and
> - au) PTR? 2.10.10.10.in-addr.arpa. (52) :
> - bS:49:36.809413 IP ubuntu.60436 > _gatexay.donatn: 59922+ [1au troubleshooting
> - PIR? 2.10.10.10.{n-addr.arpa. (52) | network issues
> - pack tured)
> - R9 packets recetved by filter
> - 9 packets dropped by kernel
> - fF oot@ubuntu: /hone/ubuntus ff
> - Copyright © ‘AM Rights Reserved. Reproduction bs Strictly Pro!


### Slide / Page 659

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Network Troubleshooting Utilities and Tools:
> - tcpreplay and dnsenum
> - tcpreplay dnsenum
> - A GPLv3 licensed utility that supports Unix-like operating
> - A Perl script that enumerates the DNS information of a we
> - systems for modifying and replaying previously sniffed domain to discover noncontiguous IP blocks
> - traffic from tools such as Wireshark and tcpdump
> - Parrot Terminally
> - Fie EG View Search Terminal, Help,
> - s [43]
> - g (errno
> - 42 pac sent in 12.48 seconds
> - Successful packets:



---

## 🛠️ Connecting Theory to Practice
- **Execute the Lab:** Open [`labs/lab-03-tcp-wireshark-deep-dive.md`](../../labs/lab-03-tcp-wireshark-deep-dive.md) to work through the practical workshop reinforcing this module.
- **Reference Card:** Check [`cheatsheets/nmap-and-wireshark-commands.md`](../../cheatsheets/nmap-and-wireshark-commands.md) for rapid command syntax, formulas, and port mappings.
