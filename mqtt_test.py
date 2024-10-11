import paho.mqtt.client as mqtt
import time

# Parametri di configurazione
MQTT_BROKER_ADDRESS = "192.168.1.100"  # Sostituisci con l'indirizzo IP del tuo broker
MQTT_BROKER_PORT = 1883
MQTT_TOPIC_PUBLISH = "sensori/dati"
MQTT_TOPIC_SUBSCRIBE = "sensori/comandi"

# Callback per la connessione
def on_connect(client, userdata, flags, rc):
    print("Connesso al broker MQTT!")
    client.subscribe(MQTT_TOPIC_SUBSCRIBE)  # Iscrizione al topic di comandi

# Callback per la ricezione di messaggi
def on_message(client, userdata, msg):
    print(f"Messaggio ricevuto: {msg.payload.decode()} su topic {msg.topic}")

# Crea un client MQTT
client = mqtt.Client()

# Imposta le callback
client.on_connect = on_connect
client.on_message = on_message

# Connessione al broker
client.connect(MQTT_BROKER_ADDRESS, MQTT_BROKER_PORT, 60)

# Avvia il loop per gestire le callback
client.loop_start()

# Pubblica un messaggio
try:
    while True:
        message = "Hello from MQTT test!"
        client.publish(MQTT_TOPIC_PUBLISH, message)
        print(f"Inviato messaggio: {message} al topic {MQTT_TOPIC_PUBLISH}")
        time.sleep(5)  # Invia un messaggio ogni 5 secondi
except KeyboardInterrupt:
    print("Interrotto, chiusura del client.")
finally:
    client.loop_stop()  # Ferma il loop
    client.disconnect()  # Disconnetti dal broker
