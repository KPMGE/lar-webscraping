import requests
from bs4 import BeautifulSoup
import json

class CT:
    def __init__(self, temperature, humidity, voltage):
        self.temperature = temperature
        self.humidity = humidity
        self.voltage = voltage

    def get_json(self):
        return {
            "temperature": self.temperature,
            "humidity": self.humidity,
            "voltage": self.voltage
        }

class THT:
    def __init__(self):
        json_tht_string = requests.get("https://lar.inf.ufes.br/tht/getTht").text
        self.json_tht_obj = json.loads(json_tht_string)

    def __get_tht_data(self, ct_name):
        if ct_name != 'ct6' and ct_name!= 'ct7' and ct_name != 'ct9':
            exit("CT value must be 'ct6', 'ct7' or 'ct9'")

        ct_html = self.json_tht_obj['result'][ct_name]
        soup = BeautifulSoup(ct_html, 'lxml')

        tht_string = soup.find('html').text
        tht_data_chunks = tht_string.split(':')

        temperature = float(tht_data_chunks[0])
        humidity = float(tht_data_chunks[1])
        voltage_with_sufix = tht_data_chunks[2]
        voltage_number = voltage_with_sufix.replace('TP_HU_TS', '')

        return float(temperature), float(humidity), float(voltage_number)

    def get_ct(self, ct_name):
        temp, hum, vol = self.__get_tht_data(ct_name)
        ct = CT(temp, hum, vol)
        return ct

    def get_json(self):
        ct6 = self.get_ct('ct6')
        ct7 = self.get_ct('ct7')
        ct9 = self.get_ct('ct9')
        return {
            "ct6": ct6.get_json(),
            "ct7": ct7.get_json(),
            "ct9": ct9.get_json()
        }
