<!-- trunk-ignore(markdownlint/MD014) -->

# AFB Requests -- 2024-01-24


## UI


https://cli.vuejs.org/guide/installation.html

```bash
    <!-- trunk-ignore(markdownlint/MD014) -->
    $ yarn install

    $ npx vite
    $ npx vite --help

    $ npx vite --debug hmr
```


https://tailwindcss.com/docs/installation
https://tailwindcss.com/docs/installation/using-postcss

https://tailwindui.com/documentation#getting-set-up
https://tailwindui.com/documentation#using-vue

Vite is a build tool for Vue.
https://vitejs.dev/guide/#scaffolding-your-first-vite-project

https://vuejs.org/guide/scaling-up/tooling.html#project-scaffolding


We're using Vue 3 with vue-i18n, make sure to install the vue-i18n@next version, which includes support for Vue 3 and TypeScript.

```bash
yarn add vue-i18n@next
```


Remember to configure TypeScript to include the vue-i18n types in your tsconfig.json file:

```json
{
  "compilerOptions": {
    // ...
    "types": ["vue-i18n"]
  }
}
```

This will enable TypeScript to recognize the types from vue-i18n and provide better autocompletion and error checking.


## Commands


### Python Dependencies

```bash

    $ pip-compile --output-file=- requirements.in > requirements.txt
    ...

    $ pip-compile --upgrade --output-file=- requirements.in | tee requirements.txt
    ...

```bash
    curl -v -X POST -H "Content-Type: application/json" -H "X-CSRFToken: $token" -d '{"username":"delbo@solutious.com","password":"1234"}' http://127.0.0.1:8000/auth-token/
```

### DRF


#### Mailpit
https://cookiecutter-django.readthedocs.io/en/latest/developing-locally.html#mailpit
https://github.com/axllent/mailpit

```bash
$ ./mailpit
INFO[2023/11/17 18:22:21] [smtpd] starting on 0.0.0.0:1025
INFO[2023/11/17 18:22:21] [http] starting server on http://localhost:8025/
```
http://localhost:8025



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

    # Rollback to an empty DB
    $  ./manage.py migrate afbcore zero
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


## Links nov 19

https://httptoolkit.com/blog/how-to-debug-cors-errors/


### Email Server (from cookiecutter-django)

In development, it is often nice to be able to see emails that are being sent from your application. If you choose to use [Mailpit](https://github.com/axllent/mailpit) when generating the project a local SMTP server with a web interface will be available.

1. [Download the latest Mailpit release](https://github.com/axllent/mailpit/releases) for your OS.

2. Copy the binary file to the project root.

3. Make it executable:

```bash
        $ chmod +x mailpit
```

4. Spin up another terminal window and start it there:

```bash
    ./mailpit
```

5. Check out http://127.0.0.1:8025/ to see how it goes.
