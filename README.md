# Internal Development Handbook

## Purpose
The primary purpose of this handbook is to act as an essential guide for any development project within our consultancy firm, which operates with more constrained resources compared to a product development house. 

Our focus on promoting best practices and ensuring consistency across our codebase is critical, given our team comprises specialists rather than full-stack developers. 

Each member brings unique strengths to the table, yet faces limitations in their range of capabilities. 

By adhering to a well-defined standard and following our tailored procedures, we mitigate confusion and enable every team member not only to contribute effectively but also to enhance their skills and work more efficiently. 

This approach is pivotal in a consultancy context, where adaptability, precision, and the ability to quickly assimilate and apply shared knowledge can significantly impact the success of client projects. 

Thus, this document is crafted to be a dynamic resource that supports our team's continuous learning and adaptation, fostering a culture of excellence and collaboration that aligns with our consultancy's goals and the diverse needs of our clients.

## Scope
The scope of this handbook is specifically designed to cover the technical and operational guidelines that govern our work in technology projects. 

It is applicable to all members of our team, reflecting our company's flat hierarchy, where collaboration and versatility are highly valued. 

The guidelines detailed within address a range of critical areas, including but not limited to, the use of programming languages, adherence to coding styles, and the implementation of best practices in project setup, testing, documentation, and security. 

This document is pertinent to every project we undertake, ensuring that despite our diverse project requirements and the varied expertise of our team members, there is a cohesive and standardized approach to our development process. 

This alignment is crucial not only for maintaining the quality and consistency of our deliverables but also for facilitating seamless collaboration across our team. 

By clearly defining the boundaries of its application, this handbook aims to streamline our operations and enhance the efficiency and effectiveness of our project execution.
<div>
<h1> Table of Contents</h1>

- [Internal Development Handbook](#internal-development-handbook)
  - [Purpose](#purpose)
  - [Scope](#scope)
- [Code of Conduct](#code-of-conduct)
  - [Expectations](#expectations)
  - [Ethics](#ethics)
- [Programming Languages](#programming-languages)
  - [Python](#python)
    - [CLI](#cli)
    - [APIs](#apis)
    - [Databases](#databases)
    - [Linux/Mac](#linuxmac)
    - [Windows](#windows)
  - [Bash](#bash)
  - [C/C++](#cc)
  - [DotNet C#](#dotnet-c)
- [Coding Styles \& Standards](#coding-styles--standards)
  - [Python Black](#python-black)
  - [Shell Scripting](#shell-scripting)
  - [Code Review Standards](#code-review-standards)
- [Development Tools \& Environments](#development-tools--environments)
  - [IDEs](#ides)
    - [VSCode](#vscode)
  - [Version Control](#version-control)
- [Project Setup \& Configuration](#project-setup--configuration)
  - [Directory Structure](#directory-structure)
  - [Dependency Management](#dependency-management)
- [Testing](#testing)
  - [Testing Frameworks](#testing-frameworks)
  - [Code Coverage](#code-coverage)
- [Continious Integration \& Continious Deployment (CI/CD)](#continious-integration--continious-deployment-cicd)
  - [CI/CD Pipelines](#cicd-pipelines)
  - [Deployment Strategies](#deployment-strategies)
- [Documentation](#documentation)
  - [Code Documentation](#code-documentation)
  - [Project Documentation](#project-documentation)
- [Security Practices](#security-practices)
  - [Secure Coding Guidelines](#secure-coding-guidelines)
  - [Data Protection](#data-protection)
- [Performance Optimisation](#performance-optimisation)
  - [Best Practices](#best-practices)
  - [Scalability Considerations](#scalability-considerations)
- [Accessibility and Internationalisation](#accessibility-and-internationalisation)
  - [Accessibility](#accessibility)
  - [Internationalisation (i18n)](#internationalisation-i18n)
- [Learning and Development](#learning-and-development)
  - [Resources](#resources)
  - [Knowledge Sharing](#knowledge-sharing)
- [Appendencies](#appendencies)
</div>

# Code of Conduct
## Expectations
We establish clear expectations for behavior and professionalism that uphold our company's values of integrity, respect, and collaboration. Our team members are expected to conduct themselves in a manner that fosters a positive and inclusive work environment, free from discrimination, harassment, and any form of unethical behavior. This includes respectful communication, both internally among colleagues and externally with clients and stakeholders, ensuring that all interactions are conducted with courtesy and understanding.

We emphasize the importance of accountability and transparency in our work processes. Team members are encouraged to take ownership of their actions, openly share their ideas and feedback, and constructively address any issues or conflicts that may arise. The goal is to create a culture where everyone feels valued and empowered to contribute to their fullest potential.

Furthermore, we expect all team members to adhere to the highest standards of professionalism when representing our company. This involves maintaining confidentiality, safeguarding sensitive information, and adhering to all legal and contractual obligations. By setting these expectations, we aim to nurture a trustworthy and ethical work environment that not only enhances our team's cohesion and productivity but also strengthens our reputation and relationships with clients and the broader community.

## Ethics
Central to our ethos is the commitment to integrity and fairness, ensuring that all business practices and technological solutions we deliver are conducted in an ethical manner. This commitment extends to respecting the rights and dignity of all individuals, valuing diversity, and fostering an environment where everyone is treated with respect.

We place a high emphasis on responsible decision-making, particularly in areas where our work could have significant societal impacts. This involves considering the ethical implications of our projects, from data privacy and security to the potential consequences of the technologies we develop and deploy. Team members are encouraged to engage in open discussions about ethical dilemmas and to seek guidance when faced with complex decisions, ensuring that our actions align with our moral principles and the best interests of our stakeholders.

Moreover, our ethical framework mandates compliance with all applicable laws, regulations, and professional standards. We are committed to combating corruption in all forms, including bribery and fraud, and to conducting our business in a transparent and accountable manner. By embedding these ethical considerations into our daily operations, we aim to not only uphold our company's integrity but also contribute positively to the broader community and environment in which we operate.


# Programming Languages
We delineate our strategic choice to primarily utilize Python and Bash scripting for our projects. This decision is rooted in the practicality and widespread familiarity of these languages within our team. Given the nature of our consultancy work, it's imperative that all team members can readily understand and contribute to our codebase, regardless of the specific project or tool involved. Python and Bash have been selected not only for their versatility and robust feature sets, which adequately cater to our diverse use cases, but also for their prevalence and strong support within the developer community.

These languages' popularity is a significant advantage, as it ensures an abundance of resources for troubleshooting, learning, and community support online. This accessibility of information and support greatly facilitates problem-solving and innovation within our projects. Additionally, the widespread use of Python and Bash enhances our ability to recruit experienced professionals from the job market, ensuring that our team remains capable and adaptable. By focusing on these languages, we align our resources and efforts towards maximizing efficiency, collaboration, and the quality of our deliverables, ensuring that our team is well-equipped to meet the challenges and opportunities of our consultancy projects.

Generally the following requirements apply to all languages used:

- Code should be self-explanatory; external documentation should be minimal and employed only when absolutely necessary.

- Code readability is paramount; the code must be clear and understandable to other team members.

- Do not re-invent the wheel. Do research first if a solution already exists and can be used to accomplish the goal

- Fail Fast. It is better to write a PoC quickly and see if the approach works, than planning everything out first and then realise that it does not work.

- Done is better than perfect. There is always a way to improve the code, however, there are very few projects that have a long livetivity and often a proof of concept is more than enough. 

- We do not develop products that compete with FANG, we do not have 100+ mio. users. Efficiency in terms of multi processing / threading is often not a requirement, but rather a nice to have. Unfortunately, the bugs faced and time required to make such systems work flawlessly for our use cases is too much and better spend on other tasks.

  - Instead, work with queues and spawn more single threaded workers in docker containers, swarms or k8s - if required

- For any tools that are only run on workstations of our team members environment variables are sufficient enough. 

- Limit yourself to docker compose files, as these can easily be run on every workstation, without configuring docker swarm or k8s/minicube.

- Use a `.gitignore` file from this repo [Github](https://github.com/github/gitignore/tree/main) for your specific project.

## Python

- Every python project should have the `.gitignore` file from [Github](https://github.com/github/gitignore/blob/main/Python.gitignore)

- Every project must utilize its own virtual environment (`virtualenv`) and include a `requirements.txt` file for dependency management.
 
- Adherence to standard PEP conventions is mandatory for all projects to ensure code consistency and readability.
 
- Implementation of [Git Pre-Commit](https://github.com/pre-commit/pre-commit) hooks is required to automate code quality checks before commits.
 
- For larger projects, the development of test cases using [pytest](https://docs.pytest.org/en/8.0.x/) is essential to maintain code quality and reliability.
   
- Avoid using one-liner for loops and similar constructs that compromise the readability of the code.


### CLI
**If you want to write a CLI with certain Quality of Life features check out the following, rather than implementing it yourself:**

- Progress bars via [tqdm](https://github.com/tqdm/tqdm)

- Logging via [loguru](https://github.com/Delgan/loguru)

- Having many arguments and parameters use [Click](https://github.com/pallets/click) instead of `argparse`

- Colors, Tables, Font Styles, Markdown and Syntax Highlighting in console use [Rich](https://github.com/Textualize/rich)

- Columns and "Designs" use [Textual](https://github.com/Textualize/textual)

- Very advanced inputs look into [Promp Toolkit](https://github.com/prompt-toolkit/python-prompt-toolkit) or [cmd2](https://github.com/python-cmd2/cmd2)

- Module based similar to how Metasploit works use [SploitKit](https://github.com/dhondta/python-sploitkit)

### APIs
- Use either [FastAPI](https://fastapi.tiangolo.com/) or [Flask](https://flask.palletsprojects.com/en/3.0.x/)

### Databases
- Do not write SQL queries yourself, as it will most likely require to also manage the table setup etc. Instead use ORMs

- Very quick and dirty project DB can be achieved with [PeeWee](https://docs.peewee-orm.com/en/latest/) it supports SQLite, Postgres and MySQL.

Use the following BaseModel from which all other models should inherit:

```python
class BaseModel(peewee.Model):
    created = peewee.DateTimeField(default=datetime.datetime.now)
    modified = peewee.DateTimeField()

    def save(self, *args, **kwargs):
        self.modified = datetime.datetime.now()
        return super(BaseModel, self).save(*args, **kwargs)

    class Meta:
        database = db
```


- A more complex database ORM solution, that should be used for long living projects is [Django's ORM](https://docs.djangoproject.com/en/5.0/topics/db/queries/) - which can be used without a full django integration, but provides you with automatic migration methods (ALTER table, keys etc).

### Linux/Mac
Use [pyenv](https://github.com/pyenv/pyenv) to easily manage your python installation and have multiple versions installed alongside. It also allows you to specify a different version per project.

### Windows
On linux it is recommended to use `pyenv`, on windows the equivalent is [pyenv-win](https://github.com/pyenv-win/pyenv-win)

## Bash

- Use a tool like [ShellCheck](https://www.shellcheck.net/) to quickly check the quality of code


## C/C++

## DotNet C#

# Coding Styles & Standards
In our commitment to excellence, the "Coding Styles & Standards" section underscores the critical importance of adopting and adhering to rigorous coding standards across all our projects. 

These standards serve as the backbone of our development process, ensuring that our code is not only functional but also clean, consistent, and easily maintainable. 

By establishing a unified set of coding practices, we facilitate smoother collaboration among team members, who may come from diverse coding backgrounds but will work within a common framework. 

This coherence significantly reduces the learning curve for new team members and enhances our collective efficiency in tackling complex projects. 

Furthermore, adherence to established coding conventions, such as those recommended by the Python Enhancement Proposals (PEP) for Python, ensures our codebase aligns with industry best practices, enhancing its readability and reliability. 

Emphasizing coding styles and standards reflects our dedication to quality, scalability, and professionalism, ultimately leading to more robust solutions and satisfied clients. 

It's through these meticulous practices that we not only uphold the integrity of our work but also foster a culture of continuous improvement and excellence within our team.

## Python Black

All python projects must use [black](https://github.com/psf/black). Within VSCode you use the following extension: [Black Formatter](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter)

The pre-commit hooks should then also make use of `https://github.com/psf/black`, as seen in the `.pre-commit-config.yaml.example` file.

## Shell Scripting

## Code Review Standards

# Development Tools & Environments

## IDEs

- each member can use the IDE of their own choice

- whatever IDE you are using, it should support the required items from the handbook

As the majority of people use VSCode the following extensions and configuration options are highlighted. Feel free to add any other editor if you and others are using it.



### VSCode

General:
- https://marketplace.visualstudio.com/items?itemName=codezombiech.gitignore
- https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one

Primarily for python development the following extensions can help with the standards defined in this handbook:

- https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring
- https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter
- https://marketplace.visualstudio.com/items?itemName=ms-python.pylint

## Version Control

# Project Setup & Configuration
## Directory Structure
## Dependency Management

# Testing
## Testing Frameworks
## Code Coverage

# Continious Integration & Continious Deployment (CI/CD)

## CI/CD Pipelines

## Deployment Strategies

# Documentation
## Code Documentation
## Project Documentation

# Security Practices

## Secure Coding Guidelines
## Data Protection

# Performance Optimisation
## Best Practices
## Scalability Considerations

# Accessibility and Internationalisation
## Accessibility
## Internationalisation (i18n)

# Learning and Development
## Resources

## Knowledge Sharing

# Appendencies

