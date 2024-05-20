# Programming Languages
We delineate our strategic choice to primarily utilize Python and Bash scripting for our projects. This decision is rooted in the practicality and widespread familiarity of these languages within our team. Given the nature of our consultancy work, it's imperative that all team members can readily understand and contribute to our codebase, regardless of the specific project or tool involved. Python and Bash have been selected not only for their versatility and robust feature sets, which adequately cater to our diverse use cases, but also for their prevalence and strong support within the developer community.

These languages' popularity is a significant advantage, as it ensures an abundance of resources for troubleshooting, learning, and community support online. This accessibility of information and support greatly facilitates problem-solving and innovation within our projects. Additionally, the widespread use of Python and Bash enhances our ability to recruit experienced professionals from the job market, ensuring that our team remains capable and adaptable. By focusing on these languages, we align our resources and efforts towards maximizing efficiency, collaboration, and the quality of our deliverables, ensuring that our team is well-equipped to meet the challenges and opportunities of our consultancy projects.

## Exceptions
There are engagements, such as deploying custom C2 agents on client systems, in which it makes more sense to implement a native solution or Go version. These must be clearly labeled as an exception. 

The reason behind this is the lack of protection and efficiencies for Python based binaries.

## General requirements

Generally the following requirements apply to all languages used:

- Code should be self-explanatory; external documentation should be minimal and employed only when absolutely necessary.

- Code readability is paramount; the code must be clear and understandable to other team members.

- Do not re-invent the wheel. Do research first if a solution already exists and can be used to accomplish the desired goal

- Fail Fast. It is better to write a PoC quickly and see if the approach works, than planning everything out first, invest a lot of time implementing the perfect solution and then realise that it does not work.

- Done is better than perfect. There is always a way to improve the code, however, there are very few projects that have a long livetivity and often a proof of concept is more than enough. 

- We do not develop products that compete with FAANG, we do not have 100+ mio. users. Efficiency in terms of multi processing / threading is often not a requirement, but rather a nice to have. Unfortunately, the bugs faced and time required to make such systems work flawlessly for our use cases is too much and better spend on other tasks.

  - Instead, explore queues, load balancers and a multi container architecture to distribute load 

- Any tools that are only run on workstations of our team members environment variables are sufficient enough.
  - Key Vaults and similar secret handling MUST be used in deployed services (testing & production)  

- Limit yourself to docker compose files, as these can easily be run on every workstation, without configuring docker swarm or k8s/minicube.
  - When deploying to a cloud like Azure or AWS, kubernetes makes more sense, specifically for flagship projects

- Use a `.gitignore` file from this repo [Github](https://github.com/github/gitignore/tree/main) for your specific project.

- Read and understand the [12 Factor App](https://12factor.net/)

## Python

- Every python project should have the `.gitignore` file from [Github](https://github.com/github/gitignore/blob/main/Python.gitignore)

- Every project must utilise its own virtual environment (`virtualenv`) and include a `requirements.txt` file for dependency management.
  - [Poetry](https://python-poetry.org/) should be preferred
  - Poetry must be used for any publicly available tools that are Python based
 
- Adherence to standard PEP conventions is mandatory for all projects to ensure code consistency and readability.
 
- Implementation of [Git Pre-Commit](https://github.com/pre-commit/pre-commit) hooks is required to automate code quality checks before commits.
 
- For larger projects, the development of test cases using [pytest](https://docs.pytest.org/en/8.0.x/) is essential to maintain code quality and reliability.
   
- Avoid using one-liner for loops and similar constructs that compromise the readability of the code.

- must use Type Hints, use mypy if possible!
  
- must have docstrings with meaningful descriptions that are kept up to date. 

- use F-Strings instead of `.format` or chaining strings

- Django views are written in Class Based Views

- Do not use * imports, specify each import. Do not leave unused imports in the top
  - The order of imports matters: Python Standard, 3rd Party, Project

### pre-commit Setup

To ensure correctly formatted code is pushed to the repositories you can use the following pre-commit configuration:

```yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v2.3.0
    hooks:
      - id: check-yaml
      - id: end-of-file-fixer
      - id: trailing-whitespace
      - id: check-added-large-files
      - id: check-case-conflict
      - id: check-docstring-first
      - id: check-json
      - id: fix-encoding-pragma
      - id: check-merge-conflict
      - id: mixed-line-ending

  - repo: https://github.com/PyCQA/bandit
    rev: 1.7.7
    hooks:
      - id: bandit
        args: ['-c', 'pyproject.toml']
        additional_dependencies: ['bandit[toml]']

  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.3.5
    hooks:
      - id: ruff
        args: [ '--fix' ]
      - id: ruff-format

  - repo: https://github.com/Yelp/detect-secrets
    rev: v1.4.0
    hooks:
    -   id: detect-secrets
        args: ['--baseline', '.secrets.baseline']
        exclude: package.lock.json

  - repo: https://github.com/Lucas-C/pre-commit-hooks-safety
    rev: v1.3.3
    hooks:
    -   id: python-safety-dependencies-check
        files: pyproject.toml
        args: ['--disable-optional-telemetry', "--ignore=51457"]


  - repo: local
    hooks:
      - id: mypy
        name: local mypy
        description: static type checker
        entry: poetry run mypy
        files: ^({PROJECT_NAME}/|tests/)
        language: system
        types: [python]

      - id: coverage
        name: local pytest coverage
        description: runs pytest along with coverage
        entry: poetry run pytest --cov {PROJECT_NAME} tests
        files: ^({PROJECT_NAME}/|tests/)
        language: system
        types: [python]


default_language_version:
  python: python3
```

### Poetry Setup
a typical `pyproject.toml` file should include the following dev dependencies and tool configurations:
```toml
[tool.poetry.group.dev.dependencies]
mypy = "^1.9.0"
nitpick = "^0.35.0"
pre-commit = "^3.7.0"
safety = "^3.1.0"
pytest = "^8.1.1"
wemake-python-styleguide = "^0.19.2"
pytest-cov = "^5.0.0"
detect-secrets = "^1.4.0"
coverage = "^7.4.4"
interrogate = "^1.5.0"
ruff = "^0.3.5"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"

[tool.poetry.scripts]
changeme_app = 'changeme_app.__main__:run'

[tool.mypy]
plugins = [
  "pydantic.mypy"
]

follow_imports = "silent"
warn_redundant_casts = true
warn_unused_ignores = true
disallow_any_generics = true
check_untyped_defs = true
no_implicit_reexport = true

# for strict mypy: (this is the tricky one :-))
disallow_untyped_defs = true

[tool.pydantic-mypy]
init_forbid_extra = true
init_typed = true
warn_required_dynamic_aliases = true

[tool.nitpick]
style = "https://raw.githubusercontent.com/wemake-services/wemake-python-styleguide/master/styles/nitpick-style-wemake.toml"

[tool.interrogate]
ignore-init-method = true
ignore-init-module = true
ignore-magic = true
ignore-semiprivate = false
ignore-private = false
ignore-property-decorators = false
ignore-module = true
ignore-nested-functions = false
ignore-nested-classes = true
ignore-setters = false
fail-under = 95
exclude = ["setup.py", "docs", "build"]
ignore-regex = ["^get$", "^mock_.*", ".*BaseClass.*"]
# possible values: 0 (minimal output), 1 (-v), 2 (-vv)
verbose = 0
quiet = false
whitelist-regex = []
color = true
omit-covered-files = false
generate-badge = "."
badge-format = "svg"

[tool.bandit]
skips = ["B101"]

```

### CLI
**If you want to write a CLI with certain Quality of Life features check out the following, rather than implementing it yourself:**

- Progress bars via [tqdm](https://github.com/tqdm/tqdm)

- Logging via [loguru](https://github.com/Delgan/loguru) or [Structlog](https://www.structlog.org/en/stable/getting-started.html)

- Having many arguments and parameters use [Click](https://github.com/pallets/click) instead of `argparse`

- Colors, Tables, Font Styles, Markdown and Syntax Highlighting in console use [Rich](https://github.com/Textualize/rich)

- Columns and "Designs" use [Textual](https://github.com/Textualize/textual)

- Very advanced inputs look into [Promp Toolkit](https://github.com/prompt-toolkit/python-prompt-toolkit) or [cmd2](https://github.com/python-cmd2/cmd2)

- Module based similar to how Metasploit works use [SploitKit](https://github.com/dhondta/python-sploitkit)

- Emojis via [emoji](https://github.com/carpedm20/emoji)

### APIs
- Use either [FastAPI](https://fastapi.tiangolo.com/) or [Flask](https://flask.palletsprojects.com/en/3.0.x/)
- Stick to REST Apis, in 99.99% of cases a GraphQL API is overkill

### Databases
- Make use of ORMs, writing SQL queries and handling SQL manually is overkill in many projects. Pure SQL requires manual migration setups, connection handling, and allow for possible SQL injections etc. Things ORMs often do out of the box

- Very quick project database can be achieved with [PeeWee](https://docs.peewee-orm.com/en/latest/) it supports SQLite, Postgres and MySQL.

When using peewee make use of the following BaseModel from which all other models should inherit:

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

### Installing python apps
Though, this is not necessarily part of programming; look into pipx to install any python based tools, including our own. pipx will create a managed virtualenvironment for each tool and therefore keep all dependencies separated. 

### Linux/Mac
Use [pyenv](https://github.com/pyenv/pyenv) to easily manage your python installation and have multiple versions installed alongside. It also allows you to specify a different version per project.


### Windows
On linux it is recommended to use `pyenv`, on windows the equivalent is [pyenv-win](https://github.com/pyenv-win/pyenv-win)

## Bash

- Use a tool like [ShellCheck](https://www.shellcheck.net/) to quickly check the quality of code


## Go
- For more scalable solutions, (generally microservices, APIs etc.) you can use Go. It does a lot of the heavy lifting to scale on multiple cores and threads during runtime.

To get started, write `go mod init <project>` where `project` can be the name or path of the project. If 
the project is supposed to be used as a package for other projects, consider naming it a [URL](https://go.dev/ref/mod#module-path). 

For example, if you'd like to include it in another project and the package name is 
```
github.com/username/dirname/path
```

To fetch it you would use:
```go get github.com/username/dirname/path```

Since we're using Azure Devops, it should be URLs that lead to our repositories.

The go.mod file that will be created contains the golang version of your project.

### APIs
[Gorilla Mux](https://github.com/gorilla/mux)

[Chi](https://github.com/go-chi/chi)

[Gin](https://github.com/gin-gonic/gin)

### Some useful packages
[validator](https://github.com/go-playground/validator) for validating structs, useful for sanitizing JSON.

[slices](https://golang.org/x/exp/slices) for many useful slice methods that the std lib refuses to implement.

There's no strict way to build a Go application, but a Makefile can be used if one prefers to make cross-platform compilation easier.

### Naming Conventions
Go uses [camelCase](https://stackoverflow.com/a/22688926) for function names, but beware that for functions or variables (especially struct members!) that should be public from one package to another, the first letter must be uppercase too.


