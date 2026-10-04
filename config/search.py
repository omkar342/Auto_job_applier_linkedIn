'''
Author:     Omkar Jadhav
LinkedIn:   https://www.linkedin.com/in/omkar-jadhav-7809b7196/
Project:    LinkedIn AI Bot / Auto Job Applier

==============================================================================
LINKEDIN SEARCH PREFERENCES
==============================================================================
This file dynamically loads search terms, location, experience levels,
bad words, and search filters from the active profile defined in
`config/constants.py` ("SIEM_SOAR" or "FULL_STACK").
==============================================================================
'''

from config.constants import JOB_PROFILE

if str(JOB_PROFILE).strip().upper() == "SIEM_SOAR":
    from config.jobs.siem_soar import (
        search_terms,
        search_location,
        switch_number,
        randomize_search_order,
        sort_by,
        date_posted,
        salary,
        easy_apply_only,
        experience_level,
        job_type,
        on_site,
        companies,
        location,
        industry,
        job_function,
        job_titles,
        benefits,
        commitments,
        under_10_applicants,
        in_your_network,
        fair_chance_employer,
        pause_after_filters,
        about_company_bad_words,
        about_company_good_words,
        bad_words,
        security_clearance,
        did_masters,
        current_experience,
    )
else:
    from config.jobs.full_stack import (
        search_terms,
        search_location,
        switch_number,
        randomize_search_order,
        sort_by,
        date_posted,
        salary,
        easy_apply_only,
        experience_level,
        job_type,
        on_site,
        companies,
        location,
        industry,
        job_function,
        job_titles,
        benefits,
        commitments,
        under_10_applicants,
        in_your_network,
        fair_chance_employer,
        pause_after_filters,
        about_company_bad_words,
        about_company_good_words,
        bad_words,
        security_clearance,
        did_masters,
        current_experience,
    )