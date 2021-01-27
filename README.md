Helios
==========================================================

Web dashboard for [Apollo IoT module](https://github.com/manti-by/apollo)


Setup:
----------------------------------------------------------

1. Install app requirements

        $ pip install -r requirements/dev.txt
        
2. Collect static, run migrations and create super user

        $ ./manage.py collectstatic --no-input
        $ ./manage.py migrate
    
3. Run dev server

        $ ./manage.py runserver