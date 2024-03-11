FROM python:3.12-slim

# Add directories
RUN mkdir -p /srv/amon-ra/src/ && \
    mkdir -p /var/lib/amon-ra/data/ && \
    mkdir -p /var/lib/amon-ra/static/ && \
    mkdir -p /var/lib/amon-ra/media/ && \
    mkdir -p /var/log/amon-ra/

# Add default user and update permissions
RUN useradd -m -s /bin/bash -d /home/manti manti && \
  chown -R manti:manti /srv/amon-ra/src/ /var/lib/amon-ra/ /var/log/amon-ra/

# Install any needed packages specified in requirements
COPY ../requirements.txt /tmp/requirements.txt
RUN pip install --trusted-host pypi.org --no-cache-dir --upgrade pip && \
    pip install --trusted-host pypi.org --no-cache-dir -r /tmp/requirements.txt

# Copy source code
COPY build/ /srv/amon-ra/src/

# Run
USER manti
WORKDIR /srv/amon-ra/src/
CMD python manage.py runserver
