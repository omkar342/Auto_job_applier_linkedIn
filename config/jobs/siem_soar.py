'''
Author:     Omkar Jadhav
LinkedIn:   https://www.linkedin.com/in/omkar-jadhav-7809b7196/
Profile:    SIEM & SOAR / Cybersecurity Integration & Automation Engineer

==============================================================================
SIEM & SOAR CONFIGURATION PROFILE
==============================================================================
All details, skills, search preferences, and AI answer context for
SIEM, SOAR, Security Operations (SOC), and Security Automation roles.
Grounded in hands-on experience at Metron Security and technical mastery
from the SIEM & SOAR Interview Practice Questions.
==============================================================================
'''

profile_name = "SIEM_SOAR"

# ==============================================================================
# SEARCH PREFERENCES & FILTERS
# ==============================================================================

search_terms = [
    "SOC Analyst",
    "SIEM Engineer",
    "SOAR Engineer",
    "Security Automation Engineer",
    "Cybersecurity Integration Engineer",
    "Detection Engineer",
    "Security Operations Engineer",
    "Microsoft Sentinel",
    "Google SecOps",
    "Chronicle SIEM",
    "Cortex XSOAR",
    "Security Engineer",
]

search_location = "India"
switch_number = 10
randomize_search_order = True

sort_by = ""
date_posted = "Past week" # [Past 24 hours,Past 3 days,Past week,Past 2 weeks,Past month,Past 6 months]
salary = ""
easy_apply_only = False

experience_level = ["Entry level", "Associate", "Mid-Senior level"]
job_type = ["Full-time", "Contract"]
on_site = ["On-site", "Remote", "Hybrid"]

companies = []
location = []
industry = []
job_function = []
job_titles = []
benefits = []
commitments = []

under_10_applicants = False
in_your_network = False
fair_chance_employer = False
pause_after_filters = False

about_company_bad_words = ["Crossover"]
about_company_good_words = []
bad_words = ["Security Clearance Required", "Active Secret Clearance", "TS/SCI", "Polygraph", "US Citizen Only"]
security_clearance = False
did_masters = False
current_experience = -1


# ==============================================================================
# APPLICATION & EASY APPLY DETAILS
# ==============================================================================

default_resume_path = "all resumes/default/resume.pdf"
years_of_experience = "3"
recent_employer = "Metron Security"

desired_salary = 1400000       # 12 LPA (in numbers)
current_ctc = 1000000          # 8 LPA (in numbers)
notice_period = 30            # 30 days

linkedin_headline = "Security Integration & Automation Engineer | SIEM & SOAR (Sentinel, Chronicle, XSOAR) | Python & Go | Cloud SecOps"

linkedin_summary = """
Security Integration & Automation Engineer with 3 years of software engineering experience, including 1.5+ years specializing in building cybersecurity integrations and SOAR automation workflows.

Core Strengths & Expertise:
• SIEM Platforms: Microsoft Sentinel (Log Analytics Data Collection API ingestion, custom tables, analytical KQL queries, Sentinel Workbooks/dashboards, incident/alert correlation), Google Security Operations / Chronicle SIEM (Ingestion API, Unified Data Model/UDM schema mapping, YARA-L detection rules), Elastic/Kibana, CrowdStrike Falcon (FDR, FQL, alert workflows), Splunk.
• SOAR & Automation: End-to-end investigation and remediation playbooks in Chronicle SOAR and Cortex XSOAR concepts (automated IOC extraction, threat intel enrichment with VirusTotal/AbuseIPDB/AlienVault OTX, relationship validation via API, finding state verification, automated endpoint isolation & account containment, case management execution logs).
• Identity Threat & Attack Path Analysis: Deep integration experience with BloodHound Enterprise (SpecterOps) to surface Active Directory and Azure AD identity attack paths, automating stale finding closure and active risk escalation.
• Event Processing & Reliability: Built high-throughput ingestion pipelines using Python and Go with enterprise reliability patterns: exponential backoff with jitter, idempotency keys, Dead-Letter Queues (DLQ), rate limiting, and schema normalization.
• Cloud & DevOps: AWS (EC2, SQS, Secrets Manager, Lambda, Route 53, IAM), Azure (Functions, Key Vault, Entra ID, Sentinel, ARM Templates), Docker containerization, CI/CD (GitHub Actions), Git.
• AI in Security: Leveraging LLMs and AI coding agents for integration architecture design, API client generation, and alert triage.
"""

cover_letter = """
Dear Hiring Manager,

I am writing to express my strong interest in the Security Integration & Automation Engineer / SIEM & SOAR position. With 3 years of software engineering experience—including 1.5+ years dedicated to building cybersecurity platform integrations and SOAR automation playbooks at Metron Security—I bring a high-impact blend of software engineering rigor and security operations domain depth.

At Metron Security, I engineered integrations connecting BloodHound Enterprise with major enterprise security platforms, including Microsoft Sentinel, Google Security Operations (Chronicle), Elastic/Kibana, and CrowdStrike Falcon. I developed automated data ingestion pipelines using REST APIs, normalized complex finding structures to platform-specific schemas (such as Chronicle's UDM and custom Sentinel tables), and implemented robust reliability patterns including exponential backoff, idempotency keys, and dead-letter queues. Furthermore, I authored automated SOAR investigation playbooks that query BloodHound APIs to validate whether attack path relationships remain active, auto-closing resolved findings and escalating genuine risks with complete context.

My technical foundation spans Python, Go, Node.js, and cloud ecosystems across Azure and AWS. I design detections using KQL, YARA-L, and FQL, and build SOAR playbooks that accelerate Mean Time to Respond (MTTR). I am eager to contribute this background in security engineering, automation, and API integration to your security operations.

Thank you for your time and consideration.

Sincerely,
Omkar Jadhav
Phone: +91 8329733453
Email: omkarjadhav095@gmail.com
LinkedIn: https://www.linkedin.com/in/omkar-jadhav-7809b7196/
Portfolio: https://omkar-s-modern-portfolio.vercel.app/
"""


# ==============================================================================
# COMPREHENSIVE AI CONTEXT (user_information_all)
# ==============================================================================
# This rich context is supplied to the AI engine (OpenAI / DeepSeek / Gemini)
# to accurately answer any technical, behavioral, or application question during Easy Apply.

user_information_all = """
Candidate Full Profile: Omkar Sameer Jadhav
Location: Pune, Maharashtra, India (Open to Remote, Hybrid, and Relocation to Hyderabad, Bangalore, Mumbai, NCR)
Phone: +91 8329733453
Email: omkarjadhav095@gmail.com
LinkedIn: https://www.linkedin.com/in/omkar-jadhav-7809b7196/
Portfolio: https://omkar-s-modern-portfolio.vercel.app/
Current Employer: Metron Security (March 2025 - Present)
Previous Employer: Civil Guruji (August 2023 - February 2025)
Total Professional Experience: 3 Years (including 1.5+ years in Cybersecurity Integration & Automation Engineering)
Notice Period: 30 Days (Negotiable / Can buy out or serve 30 days)
Current CTC: 8,00,000 INR (8 LPA)
Expected / Desired CTC: 12,00,000 INR (12 LPA)
Visa Status: Indian Citizen, does not require immediate visa sponsorship for India-based roles; Non-citizen seeking work authorization for US/International roles.

--------------------------------------------------------------------------------
1. PRIMARY DOMAIN & SKILLS (SIEM, SOAR, CYBERSECURITY):
--------------------------------------------------------------------------------
- SIEM Platforms:
  * Microsoft Sentinel: Ingesting security findings into custom Log Analytics tables via Azure Data Collection API, writing complex KQL (Kusto Query Language) analytical queries, designing Sentinel Workbooks/dashboards for identity risks and attack path tracking, configuring alert rules and incident creation.
  * Google Security Operations (Chronicle SIEM): Ingesting security findings via Ingestion API, field mapping to Unified Data Model (UDM), writing YARA-L detection rules, parsing and normalizing logs.
  * Elastic / Kibana: Log ingestion via Elasticsearch REST API, index mapping, creating Kibana security dashboards for event visualization.
  * CrowdStrike Falcon: Ingestion and routing of security findings into CrowdStrike workflows, writing Falcon Query Language (FQL) queries, Falcon Data Replicator (FDR) concepts.
  * Splunk: Security telemetry, searching and correlating logs with SPL.
  * BloodHound Enterprise (SpecterOps): Deep expertise in Active Directory and Azure AD identity attack path graphs, REST API querying, finding lifecycle states (open, acknowledged, resolved).

- SOAR & Playbook Engineering:
  * Platforms: Chronicle SOAR (formerly Siemplify) and Cortex XSOAR concepts.
  * Standard Playbook SOP (8-Step Flow):
    1. Collect Alerts from SIEM, EDR, Email Gateways, or Webhooks.
    2. Extract IOCs (IPs, Domains, URLs, File Hashes, Hostnames, Usernames).
    3. Enrich IOCs using Threat Intelligence APIs (VirusTotal, AbuseIPDB, AlienVault OTX, Shodan).
    4. Check reputation and confidence scores against threat thresholds.
    5. Correlate with historical SIEM data to determine blast radius and internal sightings.
    6. Conditional branching based on calculated risk score.
    7. Automated containment via APIs (Host isolation via CrowdStrike/EDR, account disable/token revoke via Active Directory or Entra ID, IP blocking on Firewalls/WAF).
    8. Update case management systems (execution logs, artifact summaries in Chronicle/Jira/ServiceNow) and auto-close stale alerts.
  * Custom Playbooks Built:
    - BloodHound Finding Investigation Playbook: Auto-extracts node identifiers, calls BloodHound REST API to check if node relationship is still active, queries current finding state, auto-closes stale findings, and escalates active attack paths with full context.
    - Phishing Email Investigation & Response Playbook: Header parsing, SPF/DKIM/DMARC analysis, URL unshortening, sandbox detonation, mailbox purging, user notification.
    - Malware & Host Isolation Playbook: File hash validation, process tree analysis, automated endpoint isolation via EDR API.
    - Compromised Account Playbook: Impossible travel detection, revoking active sessions, resetting passwords, forcing MFA re-authentication.

- Data Pipelines & Software Engineering Depth:
  * Programming Languages: Python (primary for scripts, playbooks, API integrations, data transformation), Go (high-throughput concurrent event processing workers with goroutines and channels, low memory footprint), Node.js / TypeScript (REST APIs, webhooks).
  * Enterprise Reliability Patterns:
    - Retries with exponential backoff and jitter for transient API failures (429, 5xx).
    - Idempotency keys (fingerprint hashing of event attributes) preventing duplicate ingestion.
    - Dead-Letter Queues (DLQ) with automated alerting when queue depth breaches threshold.
    - Rate limiting and circuit breakers preventing API overload.
    - Log normalization: Mapping raw schemas into standardized schemas (UDM, ECS, Sentinel custom tables) with type coercion and timestamp UTC standardization.
    - Deduplication and debouncing to suppress flapping alerts.

- Cloud & DevOps:
  * AWS: EC2, Lambda, SQS, Secrets Manager, Route 53, IAM least privilege policies.
  * Azure: Azure Functions (serverless integrations), Azure Key Vault, Microsoft Entra ID (Azure AD), Sentinel workspace management, ARM Templates.
  * Containers & CI/CD: Docker containerization of integration services, GitHub Actions CI/CD pipelines (automated linting, unit testing, SAST scanning, container build and push).

- Core Cybersecurity & Networking Concepts:
  * Network Security: OSI 7 layers, TCP 3-way handshake vs UDP, IP addressing (RFC 1918 private vs public), NAT (SNAT/DNAT), CIDR subnetting, VLANs, Firewalls (stateless/stateful/NGFW), IDS vs IPS, VPNs, Proxies.
  * Cryptography & PKI: AES symmetric vs RSA/ECC asymmetric encryption, SHA-256 hashing, digital signatures, TLS/SSL handshake, Certificate Authorities.
  * Identity & Access Management (IAM): Authentication vs Authorization, MFA, SSO, OAuth 2.0, SAML, Kerberos (TGT, TGS, tickets), Active Directory (Domain Controllers, GPOs, LDAP, Kerberos, NTLM), Entra ID, RBAC vs ABAC, Principle of Least Privilege.
  * Threat Intel & Incident Response: IOCs, MITRE ATT&CK tactics & techniques, Cyber Kill Chain, PICERL incident response lifecycle (Preparation, Identification, Containment, Eradication, Recovery, Lessons Learned).
  * Common Attacks & Mitigations: Phishing, Ransomware, Man-in-the-Middle, DDoS (SYN flood, DNS amplification), SQLi, XSS, CSRF, Pass-the-Hash, Kerberoasting, AS-REP Roasting, DCSync, Golden/Silver Tickets.
  * AI Security & LLMs: Prompt injection, jailbreaking, OWASP Top 10 for LLMs, insecure output handling, sensitive data exposure mitigation, AI-driven alert triage.

--------------------------------------------------------------------------------
2. COMMON EASY APPLY QUESTION REPERTOIRE & ANSWERS:
--------------------------------------------------------------------------------
- Years of Experience with SIEM / SOAR / Python / Security: 3 years total (1.5+ years dedicated cybersecurity integration).
- Authorized to work in India? Yes.
- Require visa sponsorship? No for India roles; Yes for US/International relocations.
- Comfortable with background check / drug test? Yes.
- Notice Period: 30 days.
- Education: Bachelor of Engineering (Computer Science / Engineering background).
- Willing to relocate / hybrid / on-site: Yes, fully flexible.
- Preferred Location: Pune, Hyderabad, Bangalore, or Remote.
"""
