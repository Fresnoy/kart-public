Kart
====

[![Build Status](https://travis-ci.org/Fresnoy/kart-public.svg?branch=main)](https://travis-ci.org/Fresnoy/kart-public)

LeFresnoy's data server.

Kart
====

LeFresnoy's data server.


## Installation
### Requirements

On a Debian-based host - running at least Debian Stretch, you will need the
following packages:
- python3
- virtualenv
- python3-psycopg2 (optional, in case of a PostgreSQL database)

### Quick start

It assumes that you already have the application source code locally - the best
way is by cloning this repository - and that you are in this folder.

1.  Start by creating a new virtual environment under `../venv` and activate it:

        $ virtualenv --system-site-packages ../venv
        $ source ../venv/bin/activate

2.  Install the required Python packages depending on your environment:

        $ pip install -r requirements.txt

3.  Configure the application by setting the proper environment variables
    depending on your environment. You can use the `kart/site_settings.py.dev` which
    give you the main variables with example values.

        $ cp kart/site_settings.py.dev kart/site_settings.py
        $ nano kart/site_settings.py
        $ chmod go-rwx kart/site_settings.py

    Note that this `./kart/site_settings.py` file will be loaded by default when the
    application starts.

4.  Create the database tables - it assumes that you have created the database
    and set the proper configuration to use it:

        $ ./manage.py migrate

That's it! You should now be able to start the Django development server to
check that everything is working fine with:

    $ ./manage.py runserver
