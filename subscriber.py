import paho.mqtt.client as mqtt

# Callback quando il client si connette
def on_connect(client, userdata, flags, rc):
    print("Connesso con codice di risultato: " + str(rc))
    client.subscribe("sensori/dati")  # Sottoscrivi al topic

# Callback quando un messaggio è ricevuto
def on_message(client, userdata, msg):
    print(f"Messaggio ricevuto: {msg.topic} {msg.payload.decode()}")

# Creazione del client MQTT
client = mqtt.Client()

# Imposta le funzioni di callback
client.on_connect = on_connect
client.on_message = on_message

# Connessione al broker
try:
    client.connect("localhost", 1883, 60)
except Exception as e:
    print(f"Errore di connessione: {e}")
    exit(1)

# Loop per mantenere il client attivo
client.loop_forever()
