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
