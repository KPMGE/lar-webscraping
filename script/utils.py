from tht import THT
from reservations import Labgrad
import json

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


def save_tht_data():
    tht_service = THT()
    tht_dic = tht_service.get_json()
    with open('./lar-data/tht.json','w',encoding = 'utf-8') as f:
        json.dump(tht_dic, f)
