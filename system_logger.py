import psutil
import os
import datetime
import platform
import socket

# Sprawdź, czy folder "sessions" istnieje, jeśli nie, to go utwórz
if not os.path.exists("sessions"):
    os.mkdir("sessions")

# Pobierz nazwę komputera
computer_name = platform.node()

folder_path = "sessions"

numer = 0
txt_file_count = 0
ip = socket.gethostbyname(socket.gethostname())

for filename in os.listdir(folder_path):
    if filename.endswith(".log"):
        txt_file_count += 1

# Pobierz aktualny czas i utwórz nazwę pliku dziennika
current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
log_filename = f"sessions/{current_time}_{computer_name}.log"

# Otwórz plik dziennika w trybie do zapisu
with open(log_filename, "w") as log_file:
    log_file.write(f"Plik zawiera dane monitorowania sesji dla komputera {computer_name}, {ip}\n")
    log_file.write(f"Dotychczasowa łączna ilość sesji utworzonych dla {computer_name}: {txt_file_count}\n")

    # Pobierz listę procesów działających na komputerze
    for process in psutil.process_iter(attrs=['pid', 'name']):
        try:
            process_name = process.info['name']
            process_pid = process.info['pid']

            # Zapisz informację o otwartym procesie do pliku dziennika
            numer += 1
            log_file.write(f"{datetime.datetime.now()} - Otwarcie: {process_name} (PID: {process_pid}) (akcja {numer})\n")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

# Monitorowanie działania programu
while True:
    for process in psutil.process_iter(attrs=['pid', 'name']):
        try:
            process_name = process.info['name']
            process_pid = process.info['pid']

            # Zapisz informację o zamkniętym procesie do pliku dziennika
            if not psutil.pid_exists(process_pid):
                with open(log_filename, "a") as log_file:
                    log_file.write(f"{datetime.datetime.now()} - Zamknięcie: {process_name} (PID: {process_pid})\n")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
