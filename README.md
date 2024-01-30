Amon-ra server core application
==========================================================

Web dashboard for [ODIN](https://github.com/manti-by/odin) server.


Setup:
----------------------------------------------------------

1. Install python3, pip, virtualenv and sqlite3

    ```shell
    $ sudo apt install -y python3-pip virtualenv
    ```

2. Create and activate virtualenv

    ```shell
    $ virtualenv -p python3 /home/ubuntu/venv
    $ source /home/ubuntu/venv/bin/activate
    ```

3. Clone sources and install pip packages

    ```shell
    $ mkdir /home/ubuntu/app/
    $ git clone https://github.com/manti-by/amon-ra.git app/
    $ pip install -r requirements.txt
    ```

4. Collect static, run migrations and create superuser

    ```bash
    $ cd /home/ubuntu/app/
    $ ./manage.py collectstatic --no-input
    $ ./manage.py createsuperuser
    $ ./manage.py migrate
    ```

5. Run dev server

    ```bash
    $ ./manage.py runserver
    ```
