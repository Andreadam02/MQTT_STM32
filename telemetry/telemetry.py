class TelemetryData:
    def __init__(self, accelerometer, gyroscope, magnetometer):
        self.accelerometer= accelerometer;
        self.gyroscope= gyroscope;


    def to_dict(self):
        return {
            "accelerometer": self.accelerometer,
            "gyroscope": self.gyroscope
        }