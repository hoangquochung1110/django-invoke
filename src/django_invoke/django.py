import datetime as dt
import os

import invoke
from invoke.exceptions import Failure
from invoke.watchers import FailingResponder, Responder

from . import _config, printer, python


@invoke.task
def manage(context, command):
    """Run ``manage.py`` command.

    This command also handle starting of required services and waiting DB to
    be ready.

    Args:
        context: Invoke context
        command: Manage command
        watchers: Automated responders to command

    """
    config = _config.Config.from_context(context)
    env = {
        "DJANGO_SETTINGS_MODULE": config.django.settings_path,
    }

    return python.run(
        context,
        " ".join([
            config.django.manage_file_path,
            command
        ]),
        env=env,
    )


@invoke.task
def run(context):
    """Run development web-server."""
    config = _config.Config.from_context(context)
    printer.success("Running web app")
    manage(context, config.django.runserver_command)
