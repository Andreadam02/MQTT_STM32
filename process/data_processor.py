#SUBSCRIBER

import paho.mqtt.client as mqtt
from conf.mqtt_conf_param import MqttConfigurationParameters


# Callback per la connessione
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connesso al broker MQTT!")
        client.subscribe(MqttConfigurationParameters.MQTT_TOPIC_SUBSCRIBE)  # Iscrizione ai comandi se necessario
    else:
        print(f"Errore nella connessione: {rc}")


# Callback per la ricezione di messaggi
def on_message(client, userdata, msg):
    print(f"Messaggio ricevuto: {msg.payload.decode()} su topic {msg.topic}")
    # Qui puoi aggiungere la logica per gestire i comandi ricevuti


def connect_and_send_data():
    client = mqtt.Client()

    # Configura le callback
    client.on_connect = on_connect
    client.on_message = on_message

    # Se necessario, imposta il username e la password per la connessione al broker
    if MqttConfigurationParameters.MQTT_USERNAME and MqttConfigurationParameters.MQTT_PASSWORD:
        client.username_pw_set(MqttConfigurationParameters.MQTT_USERNAME, MqttConfigurationParameters.MQTT_PASSWORD)

    # Connessione al broker
    try:
        client.connect(MqttConfigurationParameters.MQTT_BROKER_ADDRESS, MqttConfigurationParameters.MQTT_BROKER_PORT,
                       60)
        print("Tentativo di connessione al broker...")
    except Exception as e:
        print(f"Errore durante la connessione: {e}")

    return client


def publish_data(client, topic, payload):
    try:
        result = client.publish(topic, payload)
        status = result.rc
        if status == 0:
            print(f"Messaggio inviato a {topic}: {payload}")
        else:
            print(f"Errore nell'invio del messaggio a {topic}")
    except Exception as e:
        print(f"Errore durante la pubblicazione: {e}")


def loop(client):
    try:
        client.loop_start()  # Avvia il loop del client MQTT
        print("Loop MQTT avviato")
    except Exception as e:
        print(f"Errore nel loop MQTT: {e}")
