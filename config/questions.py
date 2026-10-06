'''
Author:     Omkar Jadhav
LinkedIn:   https://www.linkedin.com/in/omkar-jadhav-7809b7196/
Project:    LinkedIn AI Bot / Auto Job Applier

==============================================================================
CONSOLIDATED APPLICATION & PERSONAL QUESTIONS (SINGLE FILE)
==============================================================================
This single file contains ALL questions answered by the bot during Easy Apply:
  1. Personal Information Questions (Name, Contact, Location, EEO/Demographics)
  2. General Application Questions (Visa, Links, Citizenship, Confidence, Pause)
  3. Role-Specific Content (Headline, Summary, Cover Letter, Skills, Experience,
     Resume Path, CTC, Salary) dynamically loaded from the active job profile
     defined in `config/constants.py` ("SIEM_SOAR" or "FULL_STACK").
==============================================================================
'''

from config.constants import JOB_PROFILE

# Dynamically import role-specific details and skills based on the constant selector
if str(JOB_PROFILE).strip().upper() == "SIEM_SOAR":
    from config.jobs.siem_soar import (
        default_resume_path,
        years_of_experience,
        recent_employer,
        desired_salary,
        current_ctc,
        notice_period,
        linkedin_headline,
        linkedin_summary,
        cover_letter,
        user_information_all,
    )
else:
    from config.jobs.full_stack import (
        default_resume_path,
        years_of_experience,
        recent_employer,
        desired_salary,
        current_ctc,
        notice_period,
        linkedin_headline,
        linkedin_summary,
        cover_letter,
        user_information_all,
    )


# ==============================================================================
# 1. PERSONAL INFORMATION QUESTIONS & INPUTS
# ==============================================================================

# Legal Name
first_name = "Omkar"
middle_name = "Sameer"
last_name = "Jadhav"
full_name = f"{first_name} {middle_name} {last_name}".replace("  ", " ").strip()

# Phone number (10 digits)
phone_number = "8329733453"

# Current City
current_city = "Pune"

# Full Address (required by some applications)
street = "169, Budhavar Peth"
state = "Maharashtra"
zipcode = "411002"
country = "India"

# Equal Opportunity / Demographics questions
ethnicity = "Decline"          # "Decline", "Asian", "White", etc.
gender = "Male"                # "Male", "Female", "Other", "Decline"
disability_status = "No"       # "Yes", "No", "Decline"
veteran_status = "No"          # "Yes", "No", "Decline"


# ==============================================================================
# 2. GENERAL EASY APPLY APPLICATION QUESTIONS
# ==============================================================================

# Do you need visa sponsorship now or in the future?
require_visa = "No"            # "Yes" or "No"

# Portfolio Website URL
website = "https://omkar-s-modern-portfolio.vercel.app/"

# LinkedIn Profile URL
linkedIn = "https://www.linkedin.com/in/omkar-jadhav-7809b7196/"

# Citizenship Status
# Valid options: "U.S. Citizen/Permanent Resident", "Non-citizen allowed to work for any employer",
# "Non-citizen allowed to work for current employer", "Non-citizen seeking work authorization",
# "Canadian Citizen/Permanent Resident", "Other"
us_citizenship = "Non-citizen seeking work authorization"

# Confidence level (scale 1-10)
confidence_level = "8"


# ==============================================================================
# 3. INTERACTION & PAUSE SETTINGS
# ==============================================================================

# Pause before submitting each Easy Apply application to let you verify
pause_before_submit = False

# Pause if the bot needs manual assistance with a failed/unmatched question
pause_at_failed_question = False

# Overwrite previously saved answers on LinkedIn
overwrite_previous_answers = False