import speedtest
from colorama import Fore, Style
from tqdm import tqdm
import time
import datetime
import csv


def save_to_csv(data):
    with open('speedtest_results.csv', mode='a', newline='') as file:
        writer = csv.writer(file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(data)

def test(left, right):

    print('{0:>20} {1}'.format(left, right))



# Определение цветов для вывода
def get_color(speed, threshold):
    return Fore.GREEN if speed >= threshold else Fore.RED

def check_speed():
    # Пороговые значения для цветового выделения
    download_threshold = 50  # Мбит/с
    upload_threshold = 10  # Мбит/с
    ping_threshold = 50  # мс

    # Получить текущую дату и время
    current_date_time = datetime.datetime.now()

    # Форматирование даты и времени в нужный формат
    formatted_date_time = current_date_time.strftime("%Y-%m-%d %H:%M:%S")

    # Вывести отформатированную дату и время
    test("[Начало проверки]", formatted_date_time)

    # Создаем объект Speedtest
    st = speedtest.Speedtest(secure=True)

    # Измеряем скорость загрузки, выгрузки и пинг
    download_speed = st.download() / 10**6  # Мбит/с
    upload_speed = st.upload() / 10**6  # Мбит/с
    ping = st.results.ping  # мс

    # Вывод результатов в цвете
    #print(f"[Скорость загрузки] {get_color(download_speed, download_threshold)}{download_speed:.2f} Мбит/с{Style.RESET_ALL}")
    #print(f"[Скорость выгрузки] {get_color(upload_speed, upload_threshold)}{upload_speed:.2f} Мбит/с{Style.RESET_ALL}")
    #print(f"[Пинг] {get_color(ping, ping_threshold)}{ping} мс{Style.RESET_ALL}")

    test("[Скорость загрузки]",f"{get_color(download_speed, download_threshold)}{download_speed:.2f} Мбит/с{Style.RESET_ALL}")
    test("[Скорость выгрузки]",f"{get_color(upload_speed, upload_threshold)}{upload_speed:.2f} Мбит/с{Style.RESET_ALL}")
    test("[Пинг]", f"{get_color(ping, ping_threshold)}{ping} мс{Style.RESET_ALL}")

    # Получить текущую дату и время
    current_date_time = datetime.datetime.now()
    # Форматирование даты и времени в нужный формат
    formatted_date_time2 = current_date_time.strftime("%Y-%m-%d %H:%M:%S")
    # Вывести отформатированную дату и время
    test("[Конец проверки]", formatted_date_time2)
    print("\n")    

    # Save the results to CSV
    save_to_csv([formatted_date_time, formatted_date_time2, f"{download_speed:.2f} Мбит/с", f"{upload_speed:.2f} Мбит/с", f"{ping} мс"])



if __name__ =="__main__":
    while True:
        check_speed()
        time.sleep(600)
        

