#!/usr/bin/env python

import csv
import os
import sys

sys.path.append('..')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

from main.models import State, StateCapital, City

import django
django.setup()

dir_path = os.path.dirname(os.path.abspath(__file__))

states_csv = os.path.join(dir_path, 'states.csv')

csv_file = open(states_csv, 'r')

csv_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "zip_codes_states.csv")

reader = csv.DictReader(csv_file)


for row in reader:  
    #print row

    new_state, created = State.objects.get_or_create(name=row['state'])
    new_state.abbreviation = row['abbrev']
    new_state.save()


    new_capital, created = StateCapital.objects.get_or_create(name=row['capital'])
    new_capital.state = new_state
    new_capital.latitude = row['latitude']
    new_capital.longitude = row['longitude']
    new_capital.capital_population = row['population']
    

    try:
        new_capital.save()
    except Exception, e:
        print new_capital.name
        print e

    try:
        state_obj = State.objects.get(abbreviation=row['state'])
    except:
        print row['state']

    new_city, created = City.objects.get_or_create(name=row['city'], state=state_obj)
    new_city.county = row['county']
    new_city.latitude = row['latitude']
    new_city.longitude = row['longitude']
    new_city.zip_code = row['zip_code']

    try:
        new_city.save()
    except Exception, e:
        print e
        print new_city.county
        print new_city.latitude
        print new_city.longitude
        print new_city.zip_code
