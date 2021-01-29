# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Add directories
RUN mkdir -p /srv/helios/src/ && \
    mkdir -p /srv/helios/data/ && \
    mkdir -p /srv/helios/static/ && \
    mkdir -p /srv/helios/media/ && \
    mkdir -p /var/log/helios/

# Install any needed packages specified in requirements
COPY requirements/base.txt /tmp/base.txt
COPY requirements/prod.txt /tmp/prod.txt
RUN pip install --trusted-host pypi.org --no-cache-dir --upgrade pip && \
    pip install --trusted-host pypi.org --no-cache-dir -r /tmp/prod.txt

# Run gunicorn
EXPOSE 8000
WORKDIR /srv/helios/src/

# Run
ENV DJANGO_SETTINGS_MODULE=helios.settings.prod
CMD exec gunicorn helios.wsgi:application --bind 0.0.0.0:8101 --workers 2
