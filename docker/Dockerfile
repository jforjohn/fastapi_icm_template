FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /usr/src/app

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential libssl-dev libffi-dev libpq-dev && \
    rm -rf /var/lib/apt/lists/*

# Copy and install Python dependencies
COPY ../requirements.txt /usr/src/app/
RUN pip install --upgrade pip setuptools wheel && \
    pip install --no-cache-dir -r requirements.txt && \
    rm -rf /root/.cache/pip

# Copy project files
COPY .. /usr/src/app/

RUN pip install -e . --no-cache-dir --no-deps

ENTRYPOINT ["icm/service/run.sh"]
