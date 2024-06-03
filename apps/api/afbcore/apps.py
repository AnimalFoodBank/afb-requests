from django.apps import AppConfig

# Rich logging handler
#
# Rich is a Python library for rich text and beautiful formatting in the
# terminal. It has a powerful tracebacks feature that can be used to
# display local variables in the stacktrace. This is especially useful for
# debugging purposes.
#
# https://rich.readthedocs.io/en/latest/logging.html
#
# See all config options:
# https://github.com/Textualize/rich/blob/99ed636bea/rich/logging.py#L32
#
# from rich.logging import RichHandler
# from rich.traceback import install
# install(show_locals=False)


class AfbcoreConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "afbcore"

    def ready(self):
        """
        Overriding the ready method to import the signals module.

        Django provides a set of built-in signals that allow certain senders
        to notify a set of receivers when certain actions have taken place.
        We're importing the signals here to ensure that they get registered
        when the application configuration is ready.
        """
        import afbcore.signals  # noqa: F401
