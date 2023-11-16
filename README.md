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

    # With django-extensions installed, you can run the
    # development server with Werkzeug's debugger.
    # https://werkzeug.palletsprojects.com/en/3.0.x/
    $ ./manage.py runserver_plus
```



### Django Unfold Admin

https://github.com/unfoldadmin/django-unfold#installation


## Visual Studio Code

`launch.json` configurations for running, debugging and testing Django applications.

```json
{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [

        {
            "name": "Django Runserver",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/manage.py",
            "args": [
                "runserver"
            ],
            "django": true,
            "justMyCode": true,


        },
        {
            "name": "Django Test (Current file)",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/apps/api/manage.py",
            "args": [
                "test",
                "--keepdb",
                "${fileDirname}",
                "--pattern",
                "${fileBasename}"
            ],
            "django": true,
            "justMyCode": true,
        }
        {
            "name": "Django Test (all)",
            "type": "python",
            "request": "launch",
            "cwd": "${workspaceFolder}/apps/api",
            "program": "./manage.py",
            "args": [
                "test",
                "afbcore/tests"
            ],
            "django": true,
            "justMyCode": true,
        }
    ]
}
```
