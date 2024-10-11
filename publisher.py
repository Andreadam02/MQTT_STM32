import paho.mqtt.client as mqtt
import time

# Callback quando il client si connette
def on_connect(client, userdata, flags, rc):
    print("Connesso con codice di risultato: " + str(rc))

# Creazione del client MQTT
client = mqtt.Client()

# Imposta la funzione di callback per la connessione
client.on_connect = on_connect

# Connessione al broker
client.connect("localhost", 1883, 60)

# Pubblica messaggi in un loop
try:
    while True:
        message = "Ciao dal publisher!"
        client.publish("sensori/dati", message)
        print(f"Messaggio pubblicato: {message}")
        time.sleep(2)  # Pubblica ogni 2 secondi
except KeyboardInterrupt:
    print("Pubblicazione interrotta.")

# Disconnessione dal broker
client.disconnect()
