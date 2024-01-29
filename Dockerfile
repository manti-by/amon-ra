FROM python:3.11-slim

# Add directories
RUN mkdir -p /srv/helios/src/ && \
    mkdir -p /var/lib/helios/data/ && \
    mkdir -p /var/lib/helios/static/ && \
    mkdir -p /var/lib/helios/media/ && \
    mkdir -p /var/log/helios/

# Add default user and update permissions
RUN useradd -m -s /bin/bash -d /home/manti manti && \
  chown -R manti:manti /srv/helios/src/ /var/lib/helios/ /var/log/helios/

# Install any needed packages specified in requirements
COPY requirements.txt /tmp/requirements.txt
RUN pip install --trusted-host pypi.org --no-cache-dir --upgrade pip && \
    pip install --trusted-host pypi.org --no-cache-dir -r /tmp/requirements.txt

# Run
USER manti
WORKDIR /srv/helios/src/
CMD python manage.py runserver
