#comunicazione sensori e lettura dei dati

import smbus2 # Per comunicazione I2C
import time

class SensorHandler:
    def __init__(self, bus_number=1):
        self.bus = smbus2.SMBus(bus_number)
        self.address = 0x68  # Indirizzo I2C del MPU-9250
        self.setup_sensor()

    def setup_sensor(self):
        # Configurazione del sensore (esempio per MPU-9250)
        self.bus.write_byte_data(self.address, 0x6B, 0)  # Wake up il sensore

    def read_accelerometer(self):
        # Lettura accelerometro (esempio, modificare in base al datasheet)
        acc_x = self.bus.read_word_data(self.address, 0x3B)
        acc_y = self.bus.read_word_data(self.address, 0x3D)
        acc_z = self.bus.read_word_data(self.address, 0x3F)
        return acc_x, acc_y, acc_z

    def read_gyroscope(self):
        # Lettura giroscopio (esempio, modificare in base al datasheet)
        gyro_x = self.bus.read_word_data(self.address, 0x43)
        gyro_y = self.bus.read_word_data(self.address, 0x45)
        gyro_z = self.bus.read_word_data(self.address, 0x47)
        return gyro_x, gyro_y, gyro_z

    def read_magnetometer(self):
        # Lettura magnetometro (esempio, potrebbe essere su un altro indirizzo)
        # Assumendo che tu abbia un magnetometro separato, ad esempio l'HMC5883L
        mag_address = 0x1E  # Indirizzo I2C dell'HMC5883L
        mag_x = self.bus.read_word_data(mag_address, 0x03)
        mag_y = self.bus.read_word_data(mag_address, 0x07)
        mag_z = self.bus.read_word_data(mag_address, 0x05)
        return mag_x, mag_y, mag_z
