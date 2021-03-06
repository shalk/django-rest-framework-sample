#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ConfigParser import ConfigParser
from django.core.management import execute_from_command_line
import os
import sys

ROOT_DIR = os.path.dirname(__file__)

# Get sensitive configuration
config = ConfigParser()
config.read(ROOT_DIR + '/conf/sensitive/configuration.ini')

PROJECT_NAME = config.get('django', 'project_name')

if __name__ == '__main__':

    # Run Celery with root permission
    os.environ.setdefault('C_FORCE_ROOT', 'true')

    # Development mode
    if int(config.get('django', 'development_mode')) == 1:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', PROJECT_NAME + '.settings.dev')
    # Production mode
    else:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', PROJECT_NAME + '.settings.prod')

    execute_from_command_line(sys.argv)
