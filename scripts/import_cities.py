#!/usr/bin/env python

import csv
import os
import sys

sys.path.append('..')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

from main.models import State,  City

import django
django.setup()

csv_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "zip_codes_states.csv") 

csv_file = open('zip_codes_states.csv', 'r')


reader = csv.DictReader(csv_file)


for row in reader:  
    #print row

    try:

        state_obj, created = State.objects.get_or_create(abbreviation=row['state'])
       
        new_city, created = City.objects.get_or_create(name=row['city'], state=state_obj)
        new_city.county = row['county']
        new_city.latitude = row['latitude']
        new_city.longitude = row['longitude']
        new_city.zip_code = row['zip_code']
        
    except Exception, e:
        print e
        print row

