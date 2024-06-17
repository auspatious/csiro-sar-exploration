FROM ghcr.io/osgeo/gdal:ubuntu-small-3.8.5

# Install apt dependencies
RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-dev \
    git \
    libpq-dev \
    rustc \
    cargo \
    ca-certificates \
    build-essential \
    && apt-get autoclean \
    && apt-get autoremove \
    && rm -rf /var/lib/{apt,dpkg,cache,log}

RUN pip3 install --upgrade pip setuptools wheel
ADD requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt

ADD . /code
WORKDIR /code
RUN pip3 install .
