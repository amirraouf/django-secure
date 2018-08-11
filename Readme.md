## Django Sample app
This project is sample yet concerning more about code cleaning, securing vulnerabilities for simple entry points

There're two apps one is not secure, the other is solving it in secure and non secure way
 
 It contains some vulnerabilities (According to OWASP V4)
 1. Business Logic Data Validation (OTG-BUSLOGIC-001)
 2. Unexpected uploaded file types (OTG-BUSLOGIC-008)
 3. Media Access vulnerability (OTG-CLIENT-012)
 4. Url Phishing Detection & Mitigation
 
 As I'm using django as the framework, we shouldn't care about many security aspects but who are working on django as long as caring about security, they should care about accessability, scalability and leaving us to do our homework and ivest time in the task not the technology itself.
 
 I'll show how django care about something like SQL Injection or password hashing but doesn't care about easy access to download media files (Documents, photos, .. etc)
 
 I'll show also some tricks to solve django double sided issues like User creation and how can password may be saved as plain text if you don't know django hands well
 
 At This project, I'll not care here about: 
 1. security headers or production things (SSL, webserver hardening, ..) however you can check using @www.securityheaders.com or `python manage.py check --deploy`
 2. Authentication or privilege / Permissions (Builtin django authentication system)
 3. I'll not care about sensitive data like `secret_key` and system environment or how to protect them using environ from any code leakage or from any developers machine breakthrough.
 4. Not caring about seamless user experience (Frontend).
 5. Settings must be divided for each environment local, testing, staging, production
Each have Secret key and dependencies related to it with base setting file to inherit from

You can use django-cookiecutter for starting new project in its best practice and cut off some time

run `docker-compose build` and `docker-compose up`