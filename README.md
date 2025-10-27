<!-- trunk-ignore(markdownlint/MD014) -->

# AFB Requests -- 2024


## UI



### Nuxt.js 3 (Vue 3)

https://nuxtjs.org/docs/3.x/get-started/installation

Nuxt.js is a framework for building server-side rendered (SSR) applications with Vue.js. It is a powerful tool for building SEO-friendly, fast, and scalable web applications. Nuxt.js 3 is the latest version of the framework and it is built on top of Vue 3.


### Vueform


https://vueform.com/docs/getting-started


## API

### Django Rest Framework (DRF)

[Django 5.1](https://docs.djangoproject.com/en/5.1/)

https://www.django-rest-framework.org/


### PostgreSQL 15

[PostgreSQL 15](https://www.postgresql.org/docs/15/index.html)


## Deployment


### Gunicorn


[Gunicorn Deployment docs](https://docs.gunicorn.org/en/latest/deploy.html)



### Caddy Server

https://caddyserver.com/docs/getting-started

Caddy is a powerful, enterprise-ready, open source web server with automatic HTTPS written in Go. It is a production-ready server that is easy to use, configure, and extend.

We use Caddy as a reverse proxy to serve the Django application and the Vue.js frontend. It also handles the automatic HTTPS certificate generation and renewal. Configuration is simple and straightforward. Here is an example of a Caddyfile:

```caddy
    example.com {
        reverse_proxy
        {
            to localhost:8000
        }
    }
```

This configuration will automatically generate an HTTPS certificate for example.com and proxy all requests to the Django application running on port 8000.



## Dev tools


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


#### Mailpit

Send emails from your Django application in development without sending them to real email addresses. Mailpit is a local SMTP server with a web interface that allows you to view emails sent from your application.


https://cookiecutter-django.readthedocs.io/en/latest/developing-locally.html#mailpit
https://github.com/axllent/mailpit

```bash
$ ./mailpit
INFO[2023/11/17 18:22:21] [smtpd] starting on 0.0.0.0:1025
INFO[2023/11/17 18:22:21] [http] starting server on http://localhost:8025/
```
http://localhost:8025


### SMTP Service (Amazon SES)

#### Testing SMTP credentials

After you have created your SMTP credentials and updating the .env file, you can test the email sending functionality from the Django shell.

```bash
    $ ./manage.py shell_plus
```



```python
from django.core.mail import send_mail

# Define the email parameters
subject = 'Test Email'
message = 'This is a test email sent from the Django shell.'
from_email = 'support@afb.pet'
to_email = ['shep@afb.pet']

# Send the email
send_mail(
    subject=subject,
    from_email=from_email,
    message=message,
    recipient_list=to_email,
    fail_silently=False,
)

```

#### To create your SMTP credentials

1. Sign in to the AWS Management Console and open the Amazon SES console at https://console.aws.amazon.com/ses/.
2. Choose SMTP settings in the left navigation pane - this will open the Simple Mail Transfer Protocol (SMTP) settings page.
3. Choose Create SMTP Credentials in the upper-right corner - the IAM console will open.
4. (Optional) If you need to view, edit, or delete SMTP users you’ve already created, choose Manage my existing SMTP credentials in the lower-right corner - the IAM console will open. Details for managing SMTP credentials is given following these procedures.
5. For Create User for SMTP, type a name for your SMTP user in the User Name field. Alternatively, you can use the default value that is provided in this field. When you finish, choose Create user in the bottom-right corner.
6. Select Show under SMTP password - your SMTP credentials are shown on the screen.
7. Download these credentials by choosing Download .csv file or copy them and store them in a safe place, because you can't view or save your credentials after you close this dialog box.
8. Choose Return to SES console.


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




### Django Unfold Admin

https://

The Django Unfold Admin is a modern Django admin theme that uses the latest technologies. It is a drop-in replacement for Django's built-in admin interface.
