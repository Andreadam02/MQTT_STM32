import paho.mqtt.client as mqtt
import ssl

# Callback quando il client si connette
def on_connect(client, userdata, flags, rc):
    print("Connesso con codice di risultato: " + str(rc))
    client.subscribe("sensori/dati")  # Sottoscrivi al topic

# Callback quando un messaggio è ricevuto
# Callback quando il client si connette
def on_connect(client, userdata, flags, rc):
    print("Connesso con codice di risultato: " + str(rc))
    client.subscribe("sensori/dati")  # Sottoscrivi
    # al topic

# Callback quando un messaggio è ricevuto
def on_message(client, userdata, msg):
    print(f"Messaggio ricevuto: {msg.topic} {msg.payload.decode()}")

# Creazione del client MQTT
client = mqtt.Client()

# Assicurati che la connessione sicura sia impostata correttamente
client.tls_set(ca_certs="C:\\Users\\andre\\Downloads\\AmazonRootCA1.pem",
               certfile="C:\\Users\\andre\\Downloads\\d9af6cd68bbde4fba27fdc7924ef67ceabad837d023038077e48266da6c1736d-certificate.pem.crt",
               keyfile="C:\\Users\\andre\\Downloads\\d9af6cd68bbde4fba27fdc7924ef67ceabad837d023038077e48266da6c1736d-private.pem.key",
               tls_version=ssl.PROTOCOL_TLSv1_2)

# Imposta le funzioni di callback
client.on_connect = on_connect
client.on_message = on_message


# Connessione al broker AWS IoT
client.connect("a1mbwh2u4jtf2v-ats.iot.eu-north-1.amazonaws.com", 8883, 60)

# Loop per mantenere il client attivo
client.loop_forever()  # Mantiene il client attivo per ricevere messaggi
