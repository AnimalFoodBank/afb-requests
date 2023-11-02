<!-- trunk-ignore(markdownlint/MD014) -->

# afb-requests -- 2023-09-21


## UI


https://cli.vuejs.org/guide/installation.html

```bash

    # TODO: Update for Vite
    $ npm install -g @vue/cli

```


https://tailwindcss.com/docs/installation
https://tailwindcss.com/docs/installation/using-postcss

https://tailwindui.com/documentation#getting-set-up
https://tailwindui.com/documentation#using-vue

Vite is a build tool for Vue.
https://vitejs.dev/guide/#scaffolding-your-first-vite-project

https://vuejs.org/guide/scaling-up/tooling.html#project-scaffolding



## Commands


### Python Dependencies

```bash

    $ pip-compile --output-file=- requirements.in > requirements.txt
    ...

    $ pip-compile --upgrade --output-file=- requirements.in | tee requirements.txt
    ...

```



### Django Management

```bash

    # create a superuser
    $ ./manage.py createsuperuser

    # create a new app
    $ ./manage.py startapp <app_name>

    # create a new migration
    $ ./manage.py makemigrations

    # run migrations
    $ ./manage.py migrate

    # run the development server
    $ ./manage.py runserver

    # run the development server with a specific port
    $ ./manage.py runserver 8080

    # run the development server with a specific host
    $ ./manage.py runserver
```


### Django-Tailwind

https://django-tailwind.readthedocs.io/en/latest/usage.html

```bash
    # start a long-running process that watches files for changes
    $ ./manage.py tailwind start

    # create a production build of your theme
    $ ./manage.py tailwind build

```

### Django Unfold Admin

https://github.com/unfoldadmin/django-unfold#installation
