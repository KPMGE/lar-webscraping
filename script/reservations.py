import requests
from bs4 import BeautifulSoup
import json
from datetime import date

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
