Helios Swarm
==========================================================

Web dashboard for [Apollo Swarm](https://github.com/manti-by/apollo/tree/swarm)


Setup:
----------------------------------------------------------

1. Install app requirements

    ```bash
    $ pip install -r requirements.txt
    ```

2. Collect static, run migrations and create superuser

    ```bash
    $ ./manage.py collectstatic --no-input
    $ ./manage.py createsuperuser
    $ ./manage.py migrate
    ```

3. Run dev server

    ```bash
    $ ./manage.py runserver
    ```
