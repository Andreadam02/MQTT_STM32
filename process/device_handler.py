import json
from telemetry.telemetry import  TelemetryData
from process.data_processor import publish_data
from process.sensor_handler import SensorHandler


def send_telemetry(client):
    sensor_handler = SensorHandler()

    # Leggi i dati dai sensori
    acc_x, acc_y, acc_z = sensor_handler.read_accelerometer()
    gyro_x, gyro_y, gyro_z = sensor_handler.read_gyroscope()
    mag_x, mag_y, mag_z = sensor_handler.read_magnetometer()

    # Crea un dizionario per i dati di telemetria
    data = {
        "accelerometer": {
            "x": acc_x,
            "y": acc_y,
            "z": acc_z
        },
        "gyroscope": {
            "x": gyro_x,
            "y": gyro_y,
            "z": gyro_z
        },
        "magnetometer": {
            "x": mag_x,
            "y": mag_y,
            "z": mag_z
        }
    }

    # Converti in JSON
    payload = json.dumps(data)
    publish_data(client, "sensori/dati", payload)
