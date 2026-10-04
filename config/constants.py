'''
Author:     Omkar Jadhav
LinkedIn:   https://www.linkedin.com/in/omkar-jadhav-7809b7196/
Project:    LinkedIn AI Bot / Auto Job Applier

==============================================================================
JOB APPLICATION PROFILE SELECTOR (CONSTANT CONFIG)
==============================================================================
Decide here which jobs to apply for: Full Stack or SIEM/SOAR.
Simply set `JOB_PROFILE` to either "SIEM_SOAR" or "FULL_STACK".
The bot will automatically apply with the corresponding resume, search terms,
headline, summary, cover letter, skills, and AI answer details!

Options:
  - "SIEM_SOAR"  : Security Integration & Automation Engineer, SIEM/SOAR, Sentinel, Chronicle, XSOAR, SOC Analyst, Detection Engineer
  - "FULL_STACK" : Full Stack Developer, Software Engineer, Backend/Frontend, React.js, Node.js, TypeScript, Cloud
==============================================================================
'''

# Change this single constant to switch between job profiles:
JOB_PROFILE = "SIEM_SOAR"  # "SIEM_SOAR" or "FULL_STACK"
