# Security Practices

Overall the developer handbook has described many security aspects that need to be followed when it comes to 
best practices in programming. However, this section also includes previously observed issues and acts as a general reminder of core problems.

## Secure Coding Guidelines

The most important topics to consider when developing:

- Just like it is important to install the latest security patches for any OS, updating the 3rd party dependencies is important
- Sanitise any user input, Encode any output
- Validate any data that is being worked on
- ensure Authentication and Authorisation is properly implemented, if needed
- follow a least privilege principle
- keep the code base as minimal as possible - every extra line of code needs to be maintained and secured
- enabled structured logging
- make use of [Threat Dragon](https://github.com/OWASP/threat-dragon)

### Python

- use f-Strings

- use an ORM instead of hand written SQL queries

- use [validators](https://github.com/python-validators/validators)

- run [trivy](https://github.com/aquasecurity/trivy) locally

- use [pydantic](https://docs.pydantic.dev/latest/)

```
trivy.exe fs <folder_name>
```


## Data Protection

- don't commit secrets to git, use .env file locally, use a key vault in deployment

You can check this also with [detect-secrets](https://github.com/Yelp/detect-secrets)