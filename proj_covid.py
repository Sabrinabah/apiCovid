#!/usr/bin/env python
# coding: utf-8
import requests
import datetime as dt
import csv

url = 'https://api.covid19api.com/dayone/country/brazil'
resp = requests.get(url)
resp.status_code


raw_data = resp.json()
raw_data[0]

final_data = []
for obs in raw_data:
    final_data.append([obs['Confirmed'],obs['Deaths'], obs['Recovered'], obs['Active'], obs['Date']])

final_data.insert(0, ['confirmados', 'obitos', 'recuperados', 'ativos','data'])
final_data

CONFIRMADOS = 0
OBITOS = 1
RECUPERADOS = 2
ATIVOS = 3
DATA = 4

for i in range(1, len(final_data)):
    final_data[i][DATA] = final_data[i][DATA][:10]

final_data

with open('brasil_covid.csv','w') as file:
    writer = csv.writer(file)
    writer.writerows(final_data)

for i in range(1, len(final_data)):
        final_data[i][DATA] = dt.datetime.strptime(final_data[i][DATA],'%Y-%m-%d')

final_data

def get_datasets (y, labels):
    if type(y[0]) == list:
        datasets = []
        for i in range(len(y)):
            datasets.append({
                'label': labels[i],
                'data': y[i]
            })
        return datasets
    else:
        return [
            {
                'label': labels[0],
                'data': y  
            }
        ]
def set_title(title=''):
    if title != '':
        display = 'true'
        #true em minusculo por orientação da API
    else:
        display = 'false'

def create_chart(x,y, labels, kind='bar', title=''):
    datasets = get_datasets(y, labels)
    options = set_title(title)
    
    chart = {
        'type': Kind,
        'data': {
            'labels': x,
            'datasets': datasets
        },
        'options': options
    }
    return chart

