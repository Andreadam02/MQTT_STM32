import time
from process.device_handler import send_telemetry
from process.data_processor import connect_and_send_data

if __name__ == "__main__":
    # Connetti al broker MQTT
    client = connect_and_send_data()
    client.loop_start()

    # Invia i dati periodicamente
    while True:
        send_telemetry(client)
        time.sleep(5)  # Invia dati ogni 5 secondi
