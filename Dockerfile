FROM ubuntu:focal

ENV LANG C.UTF-8

ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=${USER_UID}
ARG NODE_VERSION=16.17.0

COPY web_django.sh /tmp/library-scripts/

RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get install -y --no-install-recommends \
    sudo \
    build-essential \
    zsh \
    python3.8 \
    python3-pip \
    python3-dev \
    git \
    libmysqlclient-dev \
    libxml2-dev \
    libxslt-dev \
    libcairo2 \
    libpango1.0-0 \
    libxmlsec1-dev \
    pkg-config \
    libxmlsec1-openssl \
    libjpeg8-dev \
    libpangocairo-1.0-0 \
    curl \
    openssh-client \
    && apt-get autoremove -y && apt-get clean -y && rm -rf /var/lib/apt/lists/* \
    && pip3 install pip==21.3.1 && pip install setuptools==57.5.0 wheel pip-tools==6.4.0

# Create the user
RUN groupadd --gid ${USER_GID} ${USERNAME} \
    && useradd --uid ${USER_UID} --gid ${USER_GID} -m ${USERNAME} \
    && echo ${USERNAME} ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/${USERNAME} \
    && chmod 0440 /etc/sudoers.d/${USERNAME}

USER vscode

SHELL [ "/bin/bash", "-l", "-c" ]

RUN bash /tmp/library-scripts/web_django.sh

WORKDIR "/home/vscode/brit_demo_app"

COPY requirements.txt requirements.txt ./

RUN pip install -r requirements.txt

WORKDIR "/home/vscode/brit_demo_app/brit"

CMD [ "/usr/bin/zsh" ]