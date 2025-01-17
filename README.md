# Amon-ra server core application

Web dashboard for [Apollo project](https://github.com/manti-by/apollo).

## About

Amon-ra is a Django based web application that provides a dashboard for the Apollo project.

[![Python 3.12](https://img.shields.io/badge/python-3.12-green.svg)](https://www.python.org/downloads/release/python-3111/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![License](https://img.shields.io/badge/license-BSD-blue.svg)](https://raw.githubusercontent.com/manti-by/db-benchmarks/master/LICENSE)

Author: Alexander Chaika <manti.by@gmail.com>

Source link: [https://github.com/manti-by/amon-ra](https://github.com/manti-by/amon-ra).

Requirements: Python 3.12, PostgreSQL, Docker.

## Setup

1. Install [Python 3.12](https://www.python.org/downloads/release/python-3120/) and
create [a virtual environment](https://docs.python.org/3/library/venv.html) for the project.

2. Clone sources and install pip packages:

    ```shell
    mkdir /home/ubuntu/app/
    git clone https://github.com/manti-by/amon-ra.git app/
    pip install -r requirements.txt
    ```

3. Collect static, run migrations and create superuser:

    ```shell
    python3 manage.py collectstatic --no-input
    python3 manage.py createsuperuser
    python3 manage.py migrate
    ```

4. Run development server and telegram bot:

    ```shell
    python3 manage.py runserver
    python3 -m amon_ra.bot.main
    ```
