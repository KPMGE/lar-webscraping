import requests
import time
from bs4 import BeautifulSoup
import json
from datetime import date

labgrad_id = 1
current_date = '2022-04-19'

class Reservation: 
    def __init__(self, professor_name, discipline_name, date, hour):
        self.professor_name = professor_name
        self.discipline_name = discipline_name
        self.date = date
        self.hour = hour

    def get_json(self):
        return {
            'professorName': self.professor_name,
            'disciplineName': self.discipline_name,
            'date': self.date,
            'hour': self.hour
        }
    

class Labgrad:
    def __init__(self, id):
        self.id = id

    def __get_labgrad_reservations(self):
        current_date = date.today()
        response = requests.get(f'https://lar.inf.ufes.br/aula/getHorarioReservas?labgrad_id={self.id}&data_atual={current_date}').text
        dic = json.loads(response)
        reservations_dic = dic['dados']

        reservations = []
        for reservation in reservations_dic: 
            professor_name = reservation['nome']
            discipline_name = reservation['disciplina']
            dis_date = reservation['data']
            hour = reservation['hora']
            reservation_obj = Reservation(professor_name, discipline_name, dis_date, hour)
            reservations.append(reservation_obj)

        return reservations

    def get_reservations_as_json(self): 
        reservations_arr = self.__get_labgrad_reservations()

        json_reservations = []
        for reservation in reservations_arr: 
            json_reservation = reservation.get_json()
            json_reservations.append(json_reservation)
        
        return json_reservations


def save_all_reservations(): 
    labgrad1 = Labgrad(1)
    labgrad2 = Labgrad(2)
    labgrad3 = Labgrad(3)

    json_reservations_lab1 = labgrad1.get_reservations_as_json()
    json_reservations_lab2 = labgrad2.get_reservations_as_json()
    json_reservations_lab3 = labgrad3.get_reservations_as_json()

    reservations_json = {
        'labgrad1': json_reservations_lab1,
        'labgrad2': json_reservations_lab2,
        'labgrad3': json_reservations_lab3
    }

    with open('./lar-data/reservations.json','w',encoding = 'utf-8') as f:
        json.dump(reservations_json, f)


class CT:
    def __init__(self, temperature, humidity, voltage):
        self.temperature = temperature
        self.humidity = humidity
        self.voltage = voltage

    def get_dictionary(self):
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

    def get_dictionary(self):
        ct6 = self.get_ct('ct6')
        ct7 = self.get_ct('ct7')
        ct9 = self.get_ct('ct9')
        return {
            "ct6": ct6.get_dictionary(),
            "ct7": ct7.get_dictionary(),
            "ct9": ct9.get_dictionary()
        }


def save_lar_info():
    tht_service = THT()
    tht_dic = tht_service.get_dictionary()
    with open('./lar-data/tht.json','w',encoding = 'utf-8') as f:
        json.dump(tht_dic, f)

if __name__ == "__main__":
    while True:
        save_lar_info()
        save_all_reservations()
        ten_minutes = 10 * 60
        time.sleep(ten_minutes)
