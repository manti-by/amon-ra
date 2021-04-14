FROM python:3.9-slim

# Add directories
RUN mkdir -p /srv/helios/src/ && \
    mkdir -p /var/lib/helios/data/ && \
    mkdir -p /var/lib/helios/static/ && \
    mkdir -p /var/lib/helios/media/ && \
    mkdir -p /var/log/helios/

# Install any needed packages specified in requirements
COPY requirements/base.txt /tmp/base.txt
COPY requirements/prod.txt /tmp/prod.txt
RUN pip install --trusted-host pypi.org --no-cache-dir --upgrade pip && \
    pip install --trusted-host pypi.org --no-cache-dir -r /tmp/prod.txt

# Add default user and update permissions
RUN useradd -m -s /bin/bash -d /home/manti manti && \
  mkdir -p /srv/helios/src/ /var/log/helios/ /var/lib/helios/static/ /var/lib/helios/media/ /var/lib/helios/data/ && \
  chown -R manti:manti /srv/helios/src/ /var/lib/helios/ /var/log/helios/

# Run
USER manti
WORKDIR /srv/helios/src/
CMD python manage.py runserver
