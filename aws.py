import paho.mqtt.client as mqtt
import ssl
import time

# Callback quando il client si connette
def on_connect(client, userdata, flags, rc):
    print("Connesso con codice di risultato: " + str(rc))

# Creazione del client MQTT
client = mqtt.Client()

# Imposta la connessione sicura
client.tls_set(ca_certs="C:\\Users\\andre\\Downloads\\AmazonRootCA1.pem",
               certfile="C:\\Users\\andre\\Downloads\\d9af6cd68bbde4fba27fdc7924ef67ceabad837d023038077e48266da6c1736d-certificate.pem.crt",
               keyfile="C:\\Users\\andre\\Downloads\\d9af6cd68bbde4fba27fdc7924ef67ceabad837d023038077e48266da6c1736d-private.pem.key",
               tls_version=ssl.PROTOCOL_TLSv1_2)

# Imposta le funzioni di callback
client.on_connect = on_connect

# Connessione al broker AWS IoT
client.connect("a1mbwh2u4jtf2v-ats.iot.eu-north-1.amazonaws.com", 8883, 60)

# Loop per mantenere il client attivo
client.loop_start()

try:
    while True:
        client.publish("sensori/dati", "Messaggio da Publisher AWS")
        print("Messaggio pubblicato.")
        time.sleep(5)  # Aspetta 5 secondi tra i messaggi
except KeyboardInterrupt:
    print("Publisher fermato.")
finally:
    client.disconnect()
    client.loop_stop()
