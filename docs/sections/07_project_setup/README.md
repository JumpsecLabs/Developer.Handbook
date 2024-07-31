# Project Setup & Configuration

## Planning
- Ask yourself what you are developing and why, what does already exist and is available to use?
- Who will maintain the code? How realistic is it for us to maintain the code (Time, Budget & People) ?
- For bigger projects that go on for a long period of time make use of the [Secure Development Lifecycle](https://www.microsoft.com/en-us/securityengineering/sdl/practices) as much as possible
- You use [OWASP Checklist](https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/stable-en/02-checklist/05-checklist) as a checklist to help review your code
- Pay specific attention to `Input Validation`, `Output encoding`, `Access Control`, `Session Management` and `Data Protection`
- Look into Secure Software Development Lifecycle (SSDL)
- Threat Modelling can make use of [Threat Dragon](https://github.com/OWASP/threat-dragon)
  
## (Secure) Software Development Lifecycle

### Phase 1: Requirements
In this early phase, requirements for new features are collected from various stakeholders. It’s important to identify any security considerations for functional requirements being gathered for the new release.

- Sample functional requirement: user needs the ability to verify their contact information before they are able to renew their membership.

- Sample security consideration: users should be able to see only their own contact information and no one else’s.

### Phase 2: Design
This phase translates in-scope requirements into a plan of what this should look like in the actual application. Here, functional requirements typically describe what should happen, while security requirements usually focus on what shouldn’t.

- Sample functional design: page should retrieve the user’s name, email, phone, and address from CUSTOMER_INFO table in the database and display it on screen.

- Sample security concern: we must verify that the user has a valid session token before retrieving information from the database. If absent, the user should be redirected to the login page.

### Phase 3: Development
When it’s time to actually implement the design and make it a reality, concerns usually shift to making sure the code well-written from the security perspective. There are usually established secure coding guidelines as well as code reviews that double-check that these guidelines have been followed correctly. These code reviews can be either manual or automated using technologies such as static application security testing (SAST).

That said, modern application developers can’t be concerned only with the code they write, because the vast majority of modern applications aren’t written from scratch. Instead, developers rely on existing functionality, usually provided by free open source components to deliver new features and therefore value to the organization as quickly as possible. In fact, 90%+ of modern deployed applications are made of these open-source components. These open-source components are usually checked using Software Composition Analysis (SCA) tools.

Secure coding guidelines, in this case, may include:
- Using parameterized, read-only SQL queries to read data from the database and minimize chances that anyone can ever commandeer these queries for nefarious purposes

- Validating user inputs before processing data contained in them

- Sanitizing any data that’s being sent back out to the user from the database

- Checking open source libraries for vulnerabilities before using them

### Phase 4: Verification
The Verification phase is where applications go through a thorough testing cycle to ensure they meet the original design & requirements. This is also a great place to introduce automated security testing using various technologies. The application is not deployed unless these tests pass. This phase often includes automated tools like CI/CD pipelines to control verification and release.

Verification at this phase may include:
- Automated tests that express the critical paths of your application

- Automated execution of application unit tests that verify the correctness of the underlying application

- Automated deployment tools that dynamically swap in application secrets to be used in a production environment

### Phase 5: Maintenance and Evolution
The story doesn’t end once the application is released. In fact, vulnerabilities that slipped through the cracks may be found in the application long after it’s been released. These vulnerabilities may be in the code developers wrote, but are increasingly found in the underlying open-source components that comprise an application. This leads to an increase in the number of “zero-days”—previously unknown vulnerabilities that are discovered in production by the application’s maintainers.

These vulnerabilities then need to be patched by the development team, a process that may in some cases require significant rewrites of application functionality. Vulnerabilities at this stage may also come from other sources, such as external penetration tests conducted by ethical hackers or submissions from the public through what’s known as “bug bounty” programs. Addressing these types of production issues must be planned for and accommodated in future releases.


## Directory Structure Examples

A simple python PoC:

```
poc.py
requirements.txt
README.md
```

A more complex Python example:
```
src/
README.md
pyproject.toml
.pre-commit-config.yaml
.gitignore
CHANGELOG.md
.secrets.baseline
```


## Dependency Management
### Python
- Preferrably use `poetry` for more than just scripts.
- Use `pip` and `pip freeze > requirements.txt` to store all requirements
- make sure that this comes from a virtual environment and not the global python interpreter