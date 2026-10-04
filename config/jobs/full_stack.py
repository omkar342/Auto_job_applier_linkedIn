'''
Author:     Omkar Jadhav
LinkedIn:   https://www.linkedin.com/in/omkar-jadhav-7809b7196/
Profile:    Full Stack Developer / Software Engineer

==============================================================================
FULL STACK CONFIGURATION PROFILE
==============================================================================
All details, skills, search preferences, and AI answer context for
Full Stack Developer, Backend Developer, Frontend Developer, and
Software Engineering roles.
Grounded in production web development at Civil Guruji, Metron Security,
and 400+ solved algorithmic problems.
==============================================================================
'''

profile_name = "FULL_STACK"

# ==============================================================================
# SEARCH PREFERENCES & FILTERS
# ==============================================================================

search_terms = [
    "Full Stack Developer",
    "Software Engineer",
    "Backend Developer",
    "Nodejs Developer",
    "React Developer",
    "Software Developer",
    "JavaScript Developer",
    "TypeScript Developer",
    "Frontend Developer",
    "Web Developer",
    "Python Developer",
]

search_location = "India"
switch_number = 10
randomize_search_order = False

sort_by = ""
date_posted = "Past month" # [Past 24 hours,Past 3 days,Past week,Past 2 weeks,Past month,Past 6 months]
salary = ""
easy_apply_only = True

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
current_ctc = 1200000          # 8 LPA (in numbers)
notice_period = 30            # 30 days

linkedin_headline = "Full Stack Developer | React.js, Next.js, Node.js, TypeScript | AWS, Docker & Scalable REST APIs"

linkedin_summary = """
Full Stack Developer with 3 years of software engineering experience designing, developing, and deploying scalable web applications, RESTful APIs, and event-driven architectures. Proven track record of enhancing system performance by 30% and building reliable systems serving 200,000+ users.

Core Strengths & Expertise:
• Frontend: React.js, Next.js, TypeScript, JavaScript, Redux Toolkit, HTML5, CSS3, Tailwind CSS, Material UI, Chakra UI, responsive UI design, performance optimization, client-side caching.
• Backend: Node.js, Express.js, Socket.IO, RESTful APIs, Webhook processing, asynchronous message queues, microservices, Python.
• Databases & Caching: MongoDB, PostgreSQL, MySQL, Redis, Firebase, database indexing, complex aggregation pipelines.
• Cloud & DevOps: AWS (EC2, S3, Route 53, NGINX configuration, SQS), Microsoft Azure, Docker containerization, CI/CD automation with GitHub Actions, Git.
• Algorithmic Problem Solving: 400+ Data Structures & Algorithms (DSA) problems solved on LeetCode; strong grasp of system design, design patterns, and clean architecture.
"""

cover_letter = """
Dear Hiring Manager,

I am writing to express my strong interest in the Full Stack Developer / Software Engineer position. With 3 years of software engineering experience building scalable, high-performance web applications and backend systems, I bring a demonstrated ability to deliver end-to-end features with high quality and speed.

During my tenure at Civil Guruji, I designed and developed an event-driven notification platform serving over 200,000 users, implementing asynchronous worker queues (FCM, SendGrid, Twilio), idempotency, and retries with backoff to handle traffic bursts without dropping requests. I optimized REST APIs, boosting overall website response times by 30%, and provisioned AWS EC2 infrastructure configured with NGINX and Route 53. At Metron Security, I further engineered backend services and event-driven pipelines handling real-time data ingestion and processing, while modernizing user interfaces with React and TypeScript.

Beyond software development, I have a disciplined problem-solving background with over 400 algorithmic problems solved on LeetCode. I write clean, modular, and maintainable code across React, Next.js, Node.js, Express, TypeScript, and Python.

I would love the opportunity to contribute to your engineering team's mission. Thank you for your time and consideration.

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
Total Professional Experience: 3 Years
Notice Period: 30 Days (Negotiable / Can buy out or serve 30 days)
Current CTC: 8,00,000 INR (8 LPA)
Expected / Desired CTC: 12,00,000 INR (12 LPA)
Visa Status: Indian Citizen, does not require visa sponsorship for India-based roles; Non-citizen seeking work authorization for US/International roles.

--------------------------------------------------------------------------------
1. PRIMARY FULL STACK & SOFTWARE ENGINEERING SKILLS:
--------------------------------------------------------------------------------
- Frontend Engineering:
  * Frameworks & Libraries: React.js, Next.js, Redux / Redux Toolkit, Context API, React Hooks.
  * Languages: TypeScript, JavaScript (ES6+), HTML5, CSS3.
  * Styling & UI Components: Tailwind CSS, Material UI (MUI), Chakra UI, Bootstrap, CSS Modules, Responsive Web Design.
  * Optimization: Code splitting, lazy loading, debouncing, throttling, memoization (useMemo, useCallback), Core Web Vitals optimization.

- Backend Engineering:
  * Runtimes & Frameworks: Node.js, Express.js, Python, RESTful API design and implementation.
  * Real-Time & Event-Driven Systems: Socket.IO (WebSockets), Webhook receivers with signature verification (HMAC), message queues.
  * System Reliability: Retries with exponential backoff and jitter, rate limiting, circuit breakers, idempotency keys, Dead-Letter Queues (DLQ).
  * Architecture: Microservices, MVC architecture, clean layered architecture, API gateway concepts.

- Databases & Caching:
  * NoSQL: MongoDB (Mongoose ORM, aggregation pipelines, schema validation, compound indexes), Firebase Firestore.
  * Relational SQL: PostgreSQL, MySQL (tables, normalization, relations, transactions).
  * In-Memory & Caching: Redis (session storage, caching layers, pub/sub).

- Cloud & DevOps:
  * AWS: EC2 instance provisioning and configuration, Amazon Route 53 (DNS and custom domain routing), NGINX reverse proxy setup with SSL/TLS, AWS S3, AWS SQS, AWS IAM.
  * Microsoft Azure: Azure Functions (serverless), Azure Key Vault, ARM Templates, Microsoft Azure Portal.
  * Containers & CI/CD: Docker (containerizing applications, multi-stage Dockerfiles), GitHub Actions CI/CD (automated testing, linting, build and deployment), Git version control.

- Algorithmic Problem Solving & System Design:
  * DSA: 400+ problems solved across LeetCode and competitive programming platforms (Arrays, Trees, Graphs, Dynamic Programming, Two Pointers, Sliding Window, Greedy, Binary Search).
  * System Design: Load balancing, caching strategies, horizontal vs vertical scaling, database sharding, asynchronous processing.

--------------------------------------------------------------------------------
2. WORK EXPERIENCE HIGHLIGHTS:
--------------------------------------------------------------------------------
- Metron Security (Mar 2025 - Present) — Full Stack Developer:
  * Built and maintained backend services and integrations handling high-volume data ingestion, processing, and inter-service communication; reduced processing delays by up to 25%.
  * Designed event-driven pipelines using webhooks/streams enabling real-time handling of alerts and updates, cutting processing latency from minutes to seconds.
  * Optimized the SaaS platform user interface using React and TypeScript to visualize complex system vulnerabilities, significantly improving user experience.

- Civil Guruji (Aug 2023 - Feb 2025) — Full Stack Developer:
  * Engineered an event-driven notification platform delivering push, email, and SMS notifications to 200,000+ users with background queue workers (FCM, SendGrid, Twilio), retries, and deduplication.
  * Enhanced website and API performance by 30% through query optimization, payload reduction, and caching.
  * Provisioned AWS EC2 instances, configured NGINX reverse proxy, automated SSL/TLS certificates, and mapped custom domains via Amazon Route 53.
  * Implemented GitHub Actions CI/CD pipelines reducing deployment times significantly.

- Cerence Inc. (Jan 2023 - Jul 2023) — Software Engineer Intern:
  * Enhanced dialog flow system and intent recognition by 26% using JavaScript, Node.js, and TypeScript.

- Shopout India & Vebsigns Technologies — Full Stack Developer Internships:
  * Built MERN stack web applications with authentication, responsive UIs, and dynamic database schemas.

--------------------------------------------------------------------------------
3. COMMON EASY APPLY QUESTION REPERTOIRE & ANSWERS:
--------------------------------------------------------------------------------
- Years of Experience with React / Node.js / Full Stack / TypeScript / Python: 3 years.
- Authorized to work in India? Yes.
- Require visa sponsorship? No for India roles; Yes for US/International relocations.
- Comfortable with background check / drug test? Yes.
- Notice Period: 30 days.
- Education: Bachelor of Engineering (Computer Science / Engineering background).
- Willing to relocate / hybrid / on-site: Yes, fully flexible.
- Preferred Location: Pune, Hyderabad, Bangalore, or Remote.
"""
