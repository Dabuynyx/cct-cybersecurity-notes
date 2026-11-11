# Module 09: Application Security Fundamentals

> **Source Material:** Authentic CCT Study Notes & Slide Deconstructions (Pages 424 – 458)  
> **Author:** [@Dabuynyx](https://github.com/Dabuynyx)  
> **Related Hands-on Lab:** [lab-06-owasp-web-vulnerabilities.md](../../labs/lab-06-owasp-web-vulnerabilities.md)  
> **Quick Reference:** [cct-exam-quick-reference.md](../../cheatsheets/cct-exam-quick-reference.md)

---

## 🧭 My Complete Study Notes & Slide Walkthroughs

### Slide / Page 424

- In the next module, we will discuss application security in detail. 
https://docs.skillable.com/docs/skillable-studio 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Module 09


### Slide / Page 425

Application Security 
 
What is a secure Application: 
- An app that ensures confidentiality, integrity, and availability of instructed resources 
 
- A restricted source is any object, data, feature, or function designed to be accessed only 
by authorized users  
 
User => Sends their identify and key => Authentication of key <= => Authorization to a set of 
resource that is granted of trust to the user 
 
 
Need for Application Security: 
Firewalls and IDS systems are not effective to defend API, because port 80 and 443 are 
generally opened on perimeter devices traffic for legitimate web traffic, which attackers 
can use to exploit the App level vulnerabilities


### Slide / Page 426

Application Security Administration: 
 
- App security admin contains a set of actions for governing the security of the apps 
installed on an organization’s infrastructure of networks 
 
Responsibilities: 
 
- Protecting users from contributing to harmful applications 
 
- Preventing apps from creating and modifying executable files 
 
- Preventing apps from accessing and editing Os resources unnecessarily 
 
- Preventing apps from loading into various processes 
 
- Regularly updating apps with the latest patches and versions for security 
 
- Securely configuring apps to protect against security risks arising from security 
misconfigurations


### Slide / Page 427

Application Security Administration Practices: 
 
01. Application whitelisting/blacklisting 
 
02. Application sandboxing: limiting the environment 
 
03. Application patch management: Process of testing, acquiring and installing patches 
(code changes) on computer systems to repair and identify vulnerabilities 
 
04. Application-level firewall (WAF) Deployments


### Slide / Page 428

3W’s in Application security: 
 
Why should we care about App Security? 
è  Apps are becoming popular targets for attackers to compromise an organization’s 
security 
 
What do we need for App Sec 
urity? 
è  Careful observation during development  
 
    Who is responsible for App Security? 
è Managers, architects, developers, testers, and administrators are responsible for App 
Security


### Slide / Page 429

Secure Application Design and Architecture 
 
è Negligence at design and architecture phrase lead to vulnerabilities that are difficult 
to detect and expensive to fix 
 
è Security vigilance at design phrase enables to detect security flaws at the early 
development phrase of the software 
 
è Security designed is based on the security requirements identified in the previous 
phrase of the Software Development Life Cycle (SDLC) 
 
è Security Design is a challenging process as it requires security controls that might 
obstruct the business functionality requirements 
 
Goals of Secure Design Process: 
 
01: Identifying the threats to understand and code to reduce risks


### Slide / Page 430

02: Designing the architecture that reduces threats 
 
03: Enforcing a secure design principle that force developers to consider security 
Secure Design Actions 
 
- Security Requirement Specification at Requirement Phrase 
 
- Secure Design Principles at Development Phrase 
 
- Threat Modelling 
 
- Secure Application Architecture 
 
Security Requirements Specifications 
 
- Software security requirements are non-functional meaning it depends on how the 
program should perform to maintain CIA


### Slide / Page 431

- Stakeholders may overlook the inception (initial) phrase of software development this 
results in the application to have a possibility of being vulnerable to attacks 
 
- Gathering security requirements should be part of the strategic application 
development process  
 
Secure Design Principles: 
 
-  Protocols that should be enforced in the developers to follow during the development 
phrase 
 
- Secures the architectural security decisions  
 
- Elamites design and architecture flaws and mitigates common security vulnerabilities 
within the application


### Slide / Page 432

Threat Modelling: 
 
01: Process of Identifying, analyzing, and mitigating the threats to the application 
 
02: Structured approach that allows the developer to rate the threats based on the 
architecture and implementation of the application 
 
è 03- Performed at the Design Phrase.


### Slide / Page 433

04: Iterative process that starts from the design phrase of the application throughout 
the life and generates a sequence of outcomes for threats 
 
05: Output of threat modelling shows all the possible threats and vulnerabilities on the 
application


### Slide / Page 434

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - Identify
> - the Assets
> - i)
> - Outline
> - Rate Severity Architecture
> - of Threats
> - Break Down 3
> - . the Application
> - Classify &
> - Structure Identif
> - Threats lentify
> - 5 Threats 4


### Slide / Page 435

Secure Application Architecture: 
 
S Three tier: Web, Application, and Data base at a typical web architecture 
 
01. One security isn’t enough since an attacker can breach the security of another tier 
to compromise the application 
 
02. Defence-in-depth principle provides security at each tier of web application 
 
03. Multi-tied include input validation, database layer, abstraction, server 
configuration, proxies, web application firewalls, data encryption, OS hardening, … 
etc…  
Multiple layer security in AI makes the application more robust and secure 
 
Tier 1 → Web Server: Input validation, users’ authorization, secure exception, and 
configurations 
 
Tier 2 → Application Server: Authenticating and authorizing upstream identities, secure 
auditing and logging, and transactions


### Slide / Page 436

Tier 3 → Database serve: Encrypt and hash stored in data base  
Securing Code Practices: Input Validation 
 
- Input validation is the process of verifying and testing user inputs that come from an 
untrusted data source 
 
- Simplest defensive technique for an injection web attack 
 
- Eliminates vulnerabilities in web applications 
 
Checks for input validation: 
• Data type (string, integer, real, etc.) 
• Allowed character set 
• Minimum and maximum length 
• Whether null is allowed 
• Numeric range 
• Whether duplicates are allowed 
• Whether the parameter is required or not 
• Specific legal values (enumeration) 
• Specific patterns (regular expressions)


### Slide / Page 437

Secure Coding Practices 
 
- Parameterized Queries: 
→  SQL with each query supplied dynamically without parameter embedding; This 
technique helps in distinguishing between code and data for user input 
 
→ Parameterized queries do not allow attacks to change the input of the query 
 
- Parameterized Stored Procedures:  
 
è  Allows the developer to write SQL code first and pass parameters to it 
 
è  Non-parameterized stored procedures are at the database with values supplied to 
them then called by the application 
- Unicode Normalization: Process of normalizing strings and determining whether two 
Unicode strings are equal 
 
→ Normalization is needed since UniCode strings can be different


### Slide / Page 438

→ Web Apps accept unknown input strings that use input filters and validation process 
→  Input validation is applied after normalization to prevent vulnerabilities such as XXS 
 
- Output Encoding 
è  Secure coding technique to convert special characters into a different format that is 
not vulnerable to the target interpreter 
 
è Converts input characters into their equivalent encoded values then sent to web 
pages 
 
è Renders harmful characters and allows them to be safe 
 
è Prevents attacks such XXS


### Slide / Page 439

- Error/Exception Handling 
 
→ Exceptions are the unusual errors that arise during the execution of a program or an 
application 
 
→ Exception handling is a mechanism that anticipates, detects, and resolves programming 
errors during execution of the application 
 
→ Improper error or exception handling may crash the whole system or may fail in the 
middle of important operations 
 
→ It may affect confidentiality, integrity, and availability of sensitive data in an application 
 
→ The error handling mechanism needs to be secure so that it can prevent the application 
from entering the unknown state


### Slide / Page 440

- Secure Session Cookies 
 
è Browsers use cookies to maintain a session state 
 
è They also contain sensitive, session-specific data e.g. user IDs, passwords, account 
numbers, links to shopping cart contents, supplied private information, and session 
IDs) 
 
è Use proper session token generation mechanisms to issue random session IDs 
 
è Do not store plaintext or weakly encrypted passwords in cookies 
 
è implement cookie timeout 
 
è Cookies authentication credentials should be associated with an IP address


### Slide / Page 441

è Employ cookie randomization to change the website or a service cookie whomever 
the user makes a request


### Slide / Page 442

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - i i ‘ he
> - Secure Response Headers :
> - Secure ap ite Practices:
> - (J A secure response header ciiatces the security of aweb page or pplication i in the alcbal network
> - Li Setting security headers | or policy settings hardens hes auplication against security, threats and
> - prevents browsers from delivering vulnerable r resources | i
> - ‘
> - ' ’
> - ' Content Security Policy (CSP) | Cache Control
> - Security (HSTS) ' '
> - “ HSTS heips web servers force “ itis a type of secure HTTP header \ ¥ This type of HTTP header is svt to
> - web browsers to interact with response that can be used by ‘ determing wheter the bravser
> - them using HTTPS modern web browsers to improve needs to cache the requests or
> - the security of a web poze \ responses
> - ~ With the HSTS header option, ail '
> - insecure RTTP connections are ¥ |l protects brovesers from XSS, H ~
> - ftaperates based on the dineetives
> - ‘ or rules
> - automatically converted to
> - code injection, clickjacking. and
> - HTTPS connections
> - wmmontod tar caching
> - other types of attacks


### Slide / Page 444

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - eee nt yee
> - ‘Secure Coding Practices: Obfuscation/ Camouflage
> - Obfuscation/camouflage is a technique isle es Spplicats on developers 01
> - to secure thelr code fram reverse engineering by attackers |
> - Itis performed by modifying the application executable to safeguard
> - the code from illicit access, dats tempering, license cracking, and QZ
> - | iaheltastin property th eft
> - Using this technique, ind ilies can alter the me
> - structure of the program and remove the spaces O39
> - between lines, erent vitdsais orinsert dummy code
> - i f
> - This process can be performed either manually or by using }
> - automated obfuscation techniques without changing the O44
> - application functionality or program throughput
> - | ! i ¥


### Slide / Page 445

> **Visual & Diagram Breakdown (from Lecture Slide):**
> - O Code siening is used by softwere
> - publishers/Gevelopers to digitally
> - sign software, product updates, or
> - executables
> - O This signature ensures the ihteprity
> - and authenticity of an application
> - or software upon installstion and
> - execution on a system
> - O Code signing involves the usage of
> - the PRI mechanism based on a
> - public and private key to sign and
> - verify the certificate containing the
> - developer and publisher
> - information
> - secure Coding
> - Practices: Code
> - Signing


### Slide / Page 446

9.2- Understanding Software Security Standard, Models, and Frameworks 
 
 Open Web Application Security Project (OWASP): 
 
- Organization that focuses on improving the security of software 
 
- Makes software security visible so that networks (people and organization) could make 
informed decisions  
 
Software Security Framework: 
 
è Software Assurance Maturity Model (SAMM): 
- Open framework that helps organizations to formulate and implement strategies for 
software security  
 
SAMM tasks: 
→ Evaluates software security practices → Builds a balanced security assurance iteration 
program → Demonstrates improvements → defines and measures security-related 
activities


### Slide / Page 447

è Building Security In Maturity Model: 
- Enables an organization to analyze and implement the security features  
- A framework for 113 activities  
- 12 practices into four domains 
Governance: 
→ Strategy and Metrics 
→ Compliance and Policy 
→ Training 
 
Intelligence: 
→ Attack Models 
→ Security Features and Design 
→ Standard and requirements 
 
SSDL Touchpoints: 
→ Architecture Analysis 
→ Code Review 
→ Security Testing 
Deployment:


### Slide / Page 448

→ Penetration Testing → Software Environment → Configuration Management and 
Vulnerability Management 
9.3- Understanding Secure Application Development, Deployment and Automation 
 
Secure Application Development Environment: 
 
è A protected environment from the design to deployment of an application and 
maintenance are implemented 
Development:  
- Guarantees that application or software runs smoothly   
 
- Developers define change and version controls to keep track 
 
Testing:  
- Monitors if software is accomplishing tasks without 
complications 
 
- Staging: - Ensures stability 
- Production: - Deploys to a real-time environment 
- Quality Assurance (QA): - Testers preform quality checks to find any issues for end-users


### Slide / Page 449

Resiliency and Automation Strategies 
 
è Systems can be restored to their operating conditions after an outrage 
 
è Resiliency of a system can be improved by adopting a proper configuration such as 
snapshots, strengthen the ability to return to normal state, and an appropriate fault 
tolerance, and redundancy methods 
 
è Automation can be used to make systems, application, or networks resilient through 
continuous automated operations.


### Slide / Page 450

9.4- Overview of Application Security Testing Techniques and Tools 
Static Application Security Testing (SAST): 
 
01. SAST aka secure code review identifies security-related weakness in the code 
 
02.  Detailed systematic inspection of source code to detect vulnerabilities and design 
flaws


### Slide / Page 451

03. Performed toward the end of the source code development when the application 
code is stable or nearly completed 
 
04. Tools such as Covertly Static Application Security Testing, Appknox, Attackflow, 
etc… are used to preform SAST 
 
Types Of SAST 
 
- Automated Source Code Analysis (SCA): Scans the code and reports potential flaws 
- Manual Source Code Review: Manually inspects source code to detect any defects and 
security-related flaws 
Dynamic Application Security Testing (DAST) 
 
è Simulates attacks against the application and analyzes application behaviour 
 
è Dynamically tested form the outside when the application is running 
 
è DAST is generally performed by pen-testers or security practitioners on a working 
system


### Slide / Page 452

è Netsparker, Acuentix, Vulnerability Scanner, HCL AppScan, etc. are used to preform 
DAST 
 
è Scanners believes in fuzzing the application inputs with attack payloads to detect 
security weaknesses 
 
Types of DAST 
- Automated Application Vulnerability Scan: Classic application security scanners for 
vulnerabilities 
 
- Manual Application Vulnerability Testing: Uses proxy-based security testing tools to 
craft and send requests manually to analyze the responses from the application 
Web Application Fuzz Testing: 
 
è Black-box testing method. It is a quality checking and assurance technique to identify 
coding errors and security loopholes in web applications 
 
è Random data called ‘Fuzz’ are generated by fuzz testing tools (Fuzzers) against the 
target web to discover vulnerabilities that can be exploited by various attacks


### Slide / Page 453

è Fuzz testing technique tests the robustness and immunity of the developed web 
application against attacks such as buffer overflow, DoS, XSS, and SQL Injection 
 
Application Whitelisting:  
 
è Security practice to control access by allowing only a list of approved application, 
software, emails, domains, etc… and denies the rest that aren’t in the whitelisting 
 
This helps with: Protection from malware attacks → Mitigates Zero-day attacks →Increases 
visibility and reduces attack surface greatly → Security independent of constant application 
updates → Reduces bring-your-own-devices (BYOD) risks 
 
 
Application Blacklisting: 
 
è Prepares a list of undesirable applications and prevents their execution 
 
è Automatically allow all other blacklisted applications 
 
è Implemented by antivirus programs, IDS/IPS, and spam filters


### Slide / Page 454

è Knowledge of threats with programs is required to prepare an application blacklist 
 
Application Sandboxing: 
 
è Runs apps in a sealed container so they can’t access critical system resources 
 
è Executes untrusted or untested programs from third parties 
 
è Provides an extra layer of security and protects the network from malicious apps 
 
è Able to test tasks without affecting the system 
 
Patch Management: A process used to fix known vulnerabilities by ensuring that 
appropriate patches are installed on a system 
 
Process: 
è Detect 
è Assess 
è Acquire


### Slide / Page 455

è Test 
è Deploy  
è Maintain 
 
Web Application Firewall (WAF) 
→ Security layer that protects the web server from malicious traffic 
 
→ A conventional firewall is not effective against layer 7 at the OSI model so it is not 
effective against SQL injection or XXS.


### Slide / Page 456

Placement of WAF and Its Working: WAF sits between the internet and the web server, 
intercepting traffic before it reaches the main server


### Slide / Page 457

Scope of Protection in Different Security Products: 
 
IDS/IPS: Intercepts DoS attacks and network vulnerability but do not handle web 
application vulnerability attacks 
 
WAF is effective against web application vulnerability for its specialized role in protecting 
against threats that target the application layer 
 
Bug Bounty Programs (Rewardable based on the Severity Level): 
 
- Challenge hosted by networks to participate and break into their security to report the 
latest bugs and vulnerabilities 
 
- Focuses on identifying the latest security flaws in software or any web application that 
most security fail to detect 
 
- Strengthens cyber security by patching ignored vulnerabilities


### Slide / Page 458

Web Application Scanners: N-Stalker web app security checks for vulnerabilities such as 
SQL injection, XSS, and other known attacks 
 
 
 
Proxy-based Security Testing Tools 
- Burp Suite: Various tools that support the entire testing process from initial mapping 
and analysis of an application’s attack surface to finding and exploiting security 
vulnerabilities 
 
- OWASP Zed Attack Proxy (ZAP) Finds vulnerabilities in web applications



---

## 🛠️ Connecting Theory to Practice
- **Execute the Lab:** Open [`labs/lab-06-owasp-web-vulnerabilities.md`](../../labs/lab-06-owasp-web-vulnerabilities.md) to work through the practical workshop reinforcing this module.
- **Reference Card:** Check [`cheatsheets/cct-exam-quick-reference.md`](../../cheatsheets/cct-exam-quick-reference.md) for rapid command syntax, formulas, and port mappings.
