# Module 18: Security Logging and Auditing

> **Source Material:** Authentic CCT Study Notes & Slide Deconstructions (Pages 679 – 701)  
> **Author:** [@Dabuynyx](https://github.com/Dabuynyx)  
> **Related Hands-on Lab:** [lab-04-snort-nids-rule-crafting.md](../../labs/lab-04-snort-nids-rule-crafting.md)  
> **Quick Reference:** [cct-exam-quick-reference.md](../../cheatsheets/cct-exam-quick-reference.md)

---

## 🧭 My Complete Study Notes & Slide Walkthroughs

### Slide / Page 679

Chapter 18 
Overview of Logging Concepts  
18.1:


### Slide / Page 680

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Q Log is a collection of information/
> - data on events generated in the form
> - of audit trail by the various
> - components of information system
> - such as network, applications, OS,
> - service, etc.
> - Q Logging is the process of recording
> - and storing logs of the events that
> - occur in the network
> - QO itis an 'mportant source that helps
> - detect flaws or problems as well as
> - network attacks, frauds, and
> - inappropriate uses of data
> - Ey Example of Log:
> - > Trail of Login Failure events
> - followed by Login Successful
> - event
> - >» 212/622
> - 12
> - (y)
> - Wirele > 2
> - Access Logs
> - Executive
> - Linux, Unix,
> - Windo\
> - $ OS Lo;
> - VPN Logs
> - IPS/IDS Logs
> - NAS Access
> - Logs
> - Yin :
> - VA Web
> - Scan. Server
> - Logs Activity
> - Control Log
> - and mz
> - Financial
> - ~ Switch Logs
> - Web
> - Cache and
> - Proxy Logs


### Slide / Page 681

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - ry security incidents
> - Or policy violations
> - fy fraudulent activity
> - tify operational and long-term
> - problems
> - dlish baselines
> - ensure compliance witt laws, rules and regulations
> - > 2:55 76:29


### Slide / Page 682

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Need of Logs
> - To identify security incidents '
> - To monitor policy violations
> - To identify fraudulent activity
> - To identify operational and long-term problems
> - To establish baselines
> - To ensure compliance with laws, rules, and regulations
> - (iii
> - Copyright


### Slide / Page 683

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - QO Before enabling
> - should know:
> - Y What to log
> - v Where to store the
> - Y Methods for logging
> - Y Tools required for logging
> - Y Log format
> - > 3:10/6:22
> - You should be able to:
> - v
> - Perform regular tuning and review of logs
> - Y Synchroni
> - tamps of all the so:
> - correlation
> - urces to perform
> - Prevent unauthorized access and manipulation to the lo,
> - the data sources to identify
> - Analyze the securit
> - Correlate any malicious activity
> - that are to be stored in the


### Slide / Page 684

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Q Log file contains
> - Q
> - Typical log includes
> - following types of
> - information:
> - > 4157622
> - various types of information that helps provide valuable and actionable j
> - ormation from the , Proper log analysis and monitoring is
> - User identification information
> - Date and time
> - Type of event
> - Success or failure indication
> - Event origination point
> - nforr


### Slide / Page 685

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - > 4:49 / 6:22
> - esc
> - 4ser credentia'
> - dates, creation,
> - holds or crossing dangerous
> - disk space, memory, or pro
> - F3
> - QO Centralized logging involves
> - by the network devices on a
> - QO) Examples of Instances when network devi
> - logs in a central server:
> - » Addition/deletion of network device
> - Changes implemented in network
> - Changes to the user access to the network
> - Successful/failed user access to the network initiated
> - to/from the compute
> - Network crashes
> - Applications installed/uni
> - Changes to the firewall p
> - Additions,
> - accounts
> - F4 F5 Oe


### Slide / Page 686

Understanding Log Monitoring and Analysis on Windows System 
18.2


### Slide / Page 687

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - centralized wa
> - or applic
> - 2 and hardware
> - vents
> - Q Windows Event log audit configuratio
> - recorded based on the egistry key
> - HKEY LOCAL MACHINE \sYsTEM\ CurrentControlSet \Services \Even
> - tLog\<Event Log>
> - i.e., log retention, log
> - Ba
> - Gt
> - OU ke
> - 6
> - faye] =]
> - 0:13 / 6:05
> - ee


### Slide / Page 688

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - ES EISTS AT SPaT TIES SUES EEALGEELEDT SRLS RMSE AT a
> - Event Viewer p
> - occurred
> - Ce
> - a quick
> - en, where, and how an event
> - ck Windows Event Log for various ty
> - System logs: Windo ogs
> - Security logs /failed events
> - Setup logs: Config:
> - Application logs: Events >gorized
> - Forwarded event lo; another computer in a network
> - Typical log entrie
> - wing types of information about the
> - events:
> - “> Level: It defines the severity of the event; various types of severity lev.
> - Error, Warnin dit, and Failure Audit
> - Keywords: It d
> - arious type
> - AuditFailure, F
> - nse T
> - ie date of events ocx
> - source of the event
> - Event ID: A unique event IL
> - Task Category: It defines task cat
> - > 1:15/6:05
> - a


### Slide / Page 689

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Warning
> - Information
> - Success
> - Audit
> - Failure Audit
> - Event Types
> - Description
> - An event indicates a significant problem such as loss of data or
> - loss of functionality. For example, if a service fails to load during
> - startup, an Error event is logged
> - An event that is not necessarily significant but May indicate a
> - Possible future problem. For example, when disk space is low, a
> - Warning event is logged. If an application can recover from an
> - €vent without loss of functionality Or data, it can generally classify
> - the event as a Warning event
> - An event that describes successful Operation of an
> - driver, or service. For example, when a network driver loads
> - successfully, it may be appropriate to log an Information event.
> - ly inappropriate for @ desktop application to
> - log an event each time it starts
> - application,
> - event that records an audited security access attempt th
> - atis
> - Successful. For example, a user
> - ssful attempt to log on to
> - the system is logged as a Success Audit event
> - An event that records an audited security access attempt that
> - fails. For example, if a user tries to access a network drive and
> - fails, the attempt is logged asa Failure Audit event
> - Copyright © by E


### Slide / Page 690

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - tayed in tt
> - 2:39 / 6:05
> - ie a


### Slide / Page 691

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - > 4:43 /6:05
> - »
> - Sebi |


### Slide / Page 692

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - System Log Entries
> - The system log contains events logged OQ) The application log contains events
> - by Windows system components
> - logged by applications or programs
> - System log includes:
> - Changes to the OS 2 Q) Application log includes:
> - Changes to the hardware configuration
> - > Installation and removal of a Particular
> - Device driver insta P software package
> - Confirmation/refutation of virus
> - installations
> - infection
> - Starting and stopping of services
> - System shutdown/restart Startup and shutdown of firewall
> - Log-on failu
> - Detection of hacking attempts
> - Alteration of machine information
> - Printing jobs
> - SD}
> - > 4:58/6:05
> - a ee
> - ak


### Slide / Page 693

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - eal
> - Mon ih
> - Security Log
> - Entries
> - > 5:27/6:05
> - oa
> - ia)
> - Q
> - G


### Slide / Page 694

Understanding Log Monitoring and Analysis on Linux 
18.3 
 
Linux Logs: Record of any activity or event in the linux OS 
 
è Located at /var/log directory in a plain ASCII text method 
 
è System log daemon (syslogd) produces logs for the system and different programs in linux OS


### Slide / Page 695

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - > /var/log/messages
> - »” Gener
> - /var/log/auth.log > /var/log/lighttpd/
> - ?” Authentication lo fe
> - FP Lighttpd ac nd error logs directory
> - /Nar/log/kern.log /var/log/boot.log
> - 7” Kernel logs >
> - ” System boot log
> - /var/log/cron.log /var/log/mysqld.log
> - ” Crond logs (cron job) >
> - ” MySQL database serv
> - /var/log/maillog > /var/log/secure or /var/log/auth.log
> - » Mail server logs ” Authentication log
> - /var/log/qmail/
> - * Qmail log directory (more files inside this dire
> - > /var/log/utmp or /var/log/wtmp
> - > Login records file
> - ZS /var/log/yum.log
> - =>
> - > Yum command log file
> - Copyright © by EC-Coumeil. All Rights Reserved. Reproduction is Strictly Prohibit +
> - > 0:52 /2:34
> - pilin


### Slide / Page 696

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Type of Log Severity of Log
> - I
> - ma
> - All severity log mail are written to
> - (var/log/maillog
> - > 1:07 / 2:34
> - eit
> - PD)


### Slide / Page 697

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - severity Leve
> - of Linux Logs
> - Emerge! y
> - Alert
> - Critical
> - Error
> - Warning
> - Notice
> - Info
> - Debug
> - g.conf Extension
> - -alert
> - -crit
> - err
> - -Warning
> - notice
> - -info
> - debug
> - Meanir
> - System is unusable
> - Action must be taken
> - immediately
> - Critical conditions
> - Error Conditions
> - Warning conditions
> - Normal but s!gnificant
> - condition
> - Informational messages
> - Debug-level


### Slide / Page 698

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Commands Used to Monitor and Analyze Linux Lo
> - cat command
> - ontents of a
> - number of lines
> - grep command
> - grep comr
> - s »
> - ault Ad
> - head [-n] [filename]
> - > 1:40 / 2:34


### Slide / Page 699

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Kiwi Syslog Server Provide
> - simplified log message m.
> - network devices and servi
> - S$ centralized and
> - anagement across
> - ers Splunk Light
> - Attps://www.splunk.com
> - WhatsUp Gold
> - http: pgold.com
> - g
> - Fastvue Syslo,
> - https.
> - 3 / 2:34
> - BD)
> - Mime eb


### Slide / Page 700

Understanding Various Log Management Tools 
18.4


### Slide / Page 701

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - > 0:59 / 1:32 oD)



---

## 🛠️ Connecting Theory to Practice
- **Execute the Lab:** Open [`labs/lab-04-snort-nids-rule-crafting.md`](../../labs/lab-04-snort-nids-rule-crafting.md) to work through the practical workshop reinforcing this module.
- **Reference Card:** Check [`cheatsheets/cct-exam-quick-reference.md`](../../cheatsheets/cct-exam-quick-reference.md) for rapid command syntax, formulas, and port mappings.
