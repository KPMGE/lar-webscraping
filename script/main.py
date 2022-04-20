import time
from utils import save_tht_data
from utils import save_all_reservations

if __name__ == "__main__":
    while True:
        save_tht_data()
        save_all_reservations()
        ten_minutes = 10 * 60
        time.sleep(ten_minutes)
