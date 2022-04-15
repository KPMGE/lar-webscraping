import requests
from bs4 import BeautifulSoup
import json

class THT: 
    def __init__(self):
        json_tht_string = requests.get("https://lar.inf.ufes.br/tht/getTht").text
        self.json_tht_obj = json.loads(json_tht_string)

    def get_tht_data(self, ct):
        if ct != 'ct6' and ct != 'ct7' and ct != 'ct9':
            exit("CT value must be 'ct6', 'ct7' or 'ct9'")

        ct_html = self.json_tht_obj['result']['ct6']
        soup = BeautifulSoup(ct_html, 'lxml')

        tht_string = soup.find('html').text
        tht_data_chunks = tht_string.split(':')

        temperature = float(tht_data_chunks[0])
        humidity = float(tht_data_chunks[1])
        voltage_with_sufix = tht_data_chunks[2]
        voltage_number = voltage_with_sufix.replace('TP_HU_TS', '')

        return temperature, humidity, voltage_number


tht_service = THT()
temperature_ct6, humidity_ct6, voltage_ct6 = tht_service.get_tht_data('ct6')
temperature_ct7, humidity_ct7, voltage_ct7 = tht_service.get_tht_data('ct7')
temperature_ct9, humidity_ct9, voltage_ct9 = tht_service.get_tht_data('ct9')

print("CT6:")
print(f"temperature: {temperature_ct6}, humidity: {humidity_ct6}, voltage: {voltage_ct6}\n")

print("CT7:")
print(f"temperature: {temperature_ct7}, humidity: {humidity_ct7}, voltage: {voltage_ct7}\n")

print("CT9:")
print(f"temperature: {temperature_ct9}, humidity: {humidity_ct9}, voltage: {voltage_ct9}\n")
