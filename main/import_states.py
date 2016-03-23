#!/usr/bin/env python
import sys
import csv
import os

sys.path.append('..')
os.environ.setdefault('DJANGO_SETTINGS_MODULE ', 'project.settings')

from main.models import State, City

states = State.objects.all()

for state in states:
	print state.name