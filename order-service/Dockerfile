
# =====================================================
# Build Arguments
# =====================================================

ARG PYTHON_VERSION=3.11
ARG APP_NAME=booktrack-order
ARG APP_VERSION=1.0.0
ARG APP_PORT=8003

# =====================================================
# Base Image
# =====================================================

FROM python:${PYTHON_VERSION}-slim-bookworm

ARG APP_NAME
ARG APP_VERSION
ARG APP_PORT

# =====================================================
# Application Environment
# =====================================================

ENV APP_NAME=${APP_NAME} \
    APP_VERSION=${APP_VERSION} \
    APP_PORT=${APP_PORT} \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

LABEL application="${APP_NAME}" \
      version="${APP_VERSION}"

# =====================================================
# Working Directory
# =====================================================

WORKDIR /app

# =====================================================
# Install Dependencies
# =====================================================

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# =====================================================
# Create Non-Root User
# Disable Login Shell
# =====================================================

RUN groupadd --gid 65532 app \
    && useradd \
       --uid 65532 \
       --gid 65532 \
       --no-create-home \
       --shell /usr/sbin/nologin \
       app \
    && mkdir -p /app/uploads \
    && chown -R 65532:65532 /app

# =====================================================
# Copy Application
# =====================================================

COPY --chown=65532:65532 . .

# =====================================================
# Runtime Security
# =====================================================

USER 65532:65532

# =====================================================
# Application Port
# =====================================================

EXPOSE ${APP_PORT}

# =====================================================
# Health Check
# =====================================================

HEALTHCHECK --interval=30s \
    --timeout=5s \
    --start-period=20s \
    --retries=3 \
    CMD ["python", "-c", "import os,urllib.request; urllib.request.urlopen('http://127.0.0.1:'+os.getenv('APP_PORT','8003')+'/health', timeout=3)"]

# =====================================================
# Start Application Without Shell
# =====================================================

CMD ["python", "-c", "import os,uvicorn; uvicorn.run('main:app', host='0.0.0.0', port=int(os.getenv('APP_PORT','8003')))"]
