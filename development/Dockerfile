ARG python_ver=3.7
FROM python:${python_ver}

ARG nautobot_ver=main
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /opt

RUN pip install --upgrade pip\
  && pip install poetry

# -------------------------------------------------------------------------------------
# Install Nautobot
# -------------------------------------------------------------------------------------
RUN git clone --single-branch --branch ${nautobot_ver} https://github.com/nautobot/nautobot.git /opt/nautobot/ && \
    cd /opt/nautobot/ && \
    poetry config virtualenvs.create false && poetry install

# -------------------------------------------------------------------------------------
# Install Nautobot Plugin
# -------------------------------------------------------------------------------------
WORKDIR /source
COPY . /source
RUN mkdir -p /root/.nautobot && \
    cat ./development/base_configuration.py >> /root/.nautobot/nautobot_config.py && \
    cat ./development/nautobot_${nautobot_ver}/configuration.py >> /root/.nautobot/nautobot_config.py
RUN poetry install --no-interaction --no-ansi

WORKDIR /opt/nautobot/
