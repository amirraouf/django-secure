# Django-secure

This project is an example of the do's and don'ts of code cleaning and security vulnerabilities for simple API endpoints.
This project is simple implementation of additional security topics mentioned at django project official documentation, so you have to read: https://docs.djangoproject.com/en/dev/topics/security/

There are two apps in this repository:

One that is not secure, to show the common pitfalls when writing a Django app and the other tries to show a better way of doing things.
 
The insecure app shows some vulnerabilities (Listed below along with the OWASP V4 code designation):

 1. Business Logic Data Validation (OTG-BUSLOGIC-001)
 2. Unexpected uploaded file types (OTG-BUSLOGIC-008)
 3. Media Access vulnerability (OTG-CLIENT-012)
 4. URL Phishing Detection & Mitigation
 
As we use Django, we don't have to care about much in terms of security since a lot of the work is done on the framework level. A Django developer is usually concerned with readability of the code and the scalability of the solution they're working on.
 
We'll show how django handles something like SQL Injection or password hashing but doesn't help with downloading user media.
 
We'll show also some tips on how to solve django double sided issues like user creation and how can password may be saved as plaintext if you don't know what you're doing.
 
The following is out of scope for this project: 

 1. security headers or production things (SSL, webserver hardening, ..), these are handled using www.securityheaders.com or `python manage.py check --deploy`
 2. Authentication or permissions (Builtin django authentication).
 3. Handling sensitive data like `secret_key` and system environment or how to protect them using environ from any code leakage or from any unauthorized access to a device containing the source code.
 5. Settings should be broken down into environments: (e.g. local, testing, staging, production).

Each app has its own dependencies and settings file.

Protip: You can use django-cookiecutter to start a new project with the latest best practices and save time

To run this project, just run `docker-compose up`

If you have other scenarios in mind don't hesitate to contribute.
Thanks for contributers: Mahmoud Hossam https://github.com/mahmoudhossam 
