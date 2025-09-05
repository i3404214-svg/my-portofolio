# Simple production-ready image for Django + Gunicorn
FROM python:3.13-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

# System deps
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
  && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

# Collect static at build time
RUN python manage.py collectstatic --noinput

ENV PORT=8000 \
    DJANGO_SETTINGS_MODULE=portfolio_site.settings \
    DEBUG=False

EXPOSE 8000

CMD gunicorn portfolio_site.wsgi:application --bind 0.0.0.0:${PORT} --workers 3 --timeout 60 --log-level info --access-logfile - --error-logfile -

