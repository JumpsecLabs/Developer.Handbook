
# Development Tools & Environments

## IDEs

- each member can use the IDE of their own choice, however VSCode is highly preferred

- whatever IDE you are using, it should support the required security and coding practices from the handbook

As the majority of people use VSCode the following extensions and configuration options are highlighted. Feel free to add any other editor if you and others are using it.

Because the primary IDE should be VSCode, it is also advised to use developer containers. That are natively supported by VSCode.
This allows for an equal developer experience and code environment on both Windows and Linux based host systems.


### Developer Containers

[Developer containers](https://code.visualstudio.com/docs/devcontainers/containers) are project specific and should be pushed into the code repository. 

`developercontainer.json`:
```json
{
    "name": "myproject_name-dev-container",
    "build": {
        "dockerfile": "Dockerfile"
    },
    "customizations": {
        "vscode": {
            "extensions": [
                "ms-python.python",
                "njpwerner.autodocstring"
            ]
        }
    }
}
```

`Dockerfile`
```
FROM mcr.microsoft.com/devcontainers/base:jammy
ARG DEBIAN_FRONTEND=noninteractive
ARG USER=vscode

RUN DEBIAN_FRONTEND=noninteractive \
    && apt-get update \
    && apt-get install -y build-essential --no-install-recommends make \
        ca-certificates \
        git \
        libssl-dev \
        zlib1g-dev \
        libbz2-dev \
        libreadline-dev \
        libsqlite3-dev \
        wget \
        curl \
        llvm \
        libncurses5-dev \
        xz-utils \
        tk-dev \
        libxml2-dev \
        libxmlsec1-dev \
        libffi-dev \
        liblzma-dev \
        whois \
        dnsutils \
        pipx

# Python and poetry installation
USER $USER
ARG HOME="/home/$USER"
ARG PYTHON_VERSION=3.12.2

ENV PYENV_ROOT="${HOME}/.pyenv"
ENV PATH="${PYENV_ROOT}/shims:${PYENV_ROOT}/bin:${HOME}/.local/bin:/usr/local/go/bin:${HOME}/go/bin:$PATH"

RUN wget https://go.dev/dl/go1.22.1.linux-amd64.tar.gz -P /home/$USER/ \
    && sudo rm -rf /usr/local/go && sudo tar -C /usr/local -xzf /home/$USER/go1.22.1.linux-amd64.tar.gz

RUN echo "done 0" \
    && curl https://pyenv.run | bash \
    && pyenv install ${PYTHON_VERSION} \
    && pyenv global ${PYTHON_VERSION} \
    && curl -sSL https://install.python-poetry.org | python3 - \
    && poetry config virtualenvs.in-project true
```


### VSCode

General:

- [https://marketplace.visualstudio.com/items?itemName=codezombiech.gitignore](https://marketplace.visualstudio.com/items?itemName=codezombiech.gitignore)

Documentation:

- [https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one)
- [https://marketplace.visualstudio.com/items?itemName=yzane.markdown-pdf](https://marketplace.visualstudio.com/items?itemName=yzane.markdown-pdf)

Primarily for python development the following extensions can help with the standards defined in this handbook:

- [https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring](https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring)
- [https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter)
- [https://marketplace.visualstudio.com/items?itemName=ms-python.pylint](https://marketplace.visualstudio.com/items?itemName=ms-python.pylint)

