Helios Swarm
==========================================================

Web dashboard for [Apollo Swarm](https://github.com/manti-by/apollo/tree/swarm)


Setup:
----------------------------------------------------------

1. Install python3, pip, virtualenv and sqlite3

    ```shell
    $ sudo apt install -y python3-pip virtualenv sqlite3
    ```
   
2. Create and activate virtualenv

    ```shell
    $ virtualenv -p python3 --prompt=helios- /home/manti/venv
    $ source /home/manti/venv/bin/activate
    ```
   
3. Clone sources and install pip packages

    ```shell
    $ mkdir /home/manti/app/
    $ git clone -b swarm https://github.com/manti-by/helios.git app/
    $ pip install -r app/requirements.txt
    ```

4. Collect static, run migrations and create superuser

    ```bash
    $ cd /home/manti/app/
    $ ./manage.py collectstatic --no-input
    $ ./manage.py createsuperuser
    $ ./manage.py migrate
    ```

5. Run dev server

    ```bash
    $ ./manage.py runserver
    ```
