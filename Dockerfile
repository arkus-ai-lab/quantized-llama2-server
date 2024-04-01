FROM python:3.9-slim
LABEL maintainer="Kwaai - Arkusnexus AI Labs"

ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y \
    git \
    build-essential \
    python3-dev \
    python3-pip

RUN git clone --recurse-submodules https://github.com/abetlen/llama-cpp-python.git /app

COPY ./requirements.txt /tmp/requirements.txt

COPY ./app /app
WORKDIR /app
COPY ./scripts /scripts
EXPOSE 8001

RUN pip install -e .

RUN python3 -c "import llama_cpp; print(llama_cpp.__version__)"

ARG DEV=false

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    python3-dev \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --no-cache-dir -r /tmp/requirements.txt \
    && apt-get purge -y --auto-remove gcc python3-dev libpq-dev \
    && chmod +x /scripts/*

ENV PATH="/scripts:/py/bin:$PATH"

CMD ["run.sh"]