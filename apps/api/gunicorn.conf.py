# Description: Gunicorn configuration file for the Django API
#
#
#
# Usage:
#
#     $ gunicorn --config apps/api/gunicorn.conf.py afb.wsgi:application
#
# About Workers:
#
# Worker class determines the type of workers to use. The
# default synchronous workers assume that your application
# is resource-bound in terms of I/O operations.
#
# worker_class = "sync"  # The default class. It can handle
# applications that are I/O-bound but not suitable for
# long-polling or other long-held socket connections.
#
# "gthread" - A threaded worker. It uses threads to handle
# requests. Good for I/O-bound applications and also can be
# used for long-polling. It's a good alternative to 'sync'
# with better concurrency for I/O-bound workloads.
# worker_class = "gthread"
#
# "gevent" - A worker class for handling a large number of
# connections. It uses greenlets to provide high-performance,
# network-based concurrency. Suitable for applications that
# require long-polling, WebSockets, or other long-lived
# connections.
#

import os
import sys

# Add the current directory to the beginning of the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

# Set the Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "afb.settings")

# Server socket
bind = "0.0.0.0:8000"
backlog = 2048


# Worker processes: 2-4 per core is a good start
workers = 4

# Choose one worker class by uncommenting:
# 1. Sync: Default, for fast responses, CPU-bound apps
# worker_class = "sync"
#
# 2. gthread: Threaded, good for mixed I/O and CPU workloads
worker_class = "gthread"
threads = 4  # Adjust based on your needs
#
# 3. gevent: For many concurrent connections, long-polling
# worker_class = "gevent"
# worker_connections = 1000

# Common settings
max_requests = 1000
max_requests_jitter = 50
timeout = 30
keepalive = 2

# Security
limit_request_line = 4096
limit_request_fields = 100
limit_request_field_size = 8190

# Logging
accesslog = os.getenv("GUNICORN_ACCESS_LOG", "-")
errorlog = os.getenv("GUNICORN_ERROR_LOG", "-")
loglevel = os.getenv("GUNICORN_LOG_LEVEL", "info")

# Process naming
proc_name = "gunicorn_myapp"

# Server mechanics
daemon = False
pidfile = None
umask = 0
user = None
group = None
tmp_upload_dir = None

# SSL
# keyfile = '/path/to/key.pem'
# certfile = '/path/to/cert.pem'


# Hook functions
def on_starting(server):
    print("Starting Gunicorn server...")


def on_reload(server):
    print("Reloading Gunicorn server...")


def on_exit(server):
    print("Shutting down Gunicorn server...")


# Server hooks
post_fork = lambda server, worker: server.log.info(
    f"Worker spawned (pid: {worker.pid})"
)
pre_fork = lambda server, worker: server.log.info("Forking worker...")
pre_exec = lambda server: server.log.info("Forked child, re-executing...")


# Customize this based on your app's needs
def when_ready(server):
    server.log.info("Server is ready. Spawning workers...")


# Error handling
def worker_abort(worker):
    worker.log.info(f"worker {worker.pid} aborted")
