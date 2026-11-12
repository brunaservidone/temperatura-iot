# Nome:Bruna Servidone
from machine import Pin
import dht
import time
import network
import urequests
# ThingSpeak
# A chave fica em um arquivo separado (config.py), que NAO vai para o GitHub.
# Se o arquivo nao existir, usa um valor de exemplo.
try:
    from config import API_KEY
except ImportError:
    API_KEY = "SUA_CHAVE_AQUI"
# Sensor DHT11
sensor = dht.DHT11(Pin(9))
# LED representa o relé no simulador
rele = Pin(2, Pin.OUT)
# Wi-Fi
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect("espide-simulator", "")
print("Conectando ao Wi-Fi...")
time.sleep(3)
print("Wi-Fi conectado:", wifi.isconnected())
print("ESP32 iniciado.")
print("Sensor DHT11 pronto.")
while True:
    try:
        # Leitura do sensor
        sensor.measure()
        temperatura = sensor.temperature()
        umidade = sensor.humidity()
        print("Temperatura:", temperatura, "°C")
        print("Umidade:", umidade, "%")
        # Controle do relé
        if temperatura > 31 or umidade > 70:
            rele.value(1)
            print("Relé: LIGADO")
        else:
            rele.value(0)
            print("Relé: DESLIGADO")
        # Envio para o ThingSpeak
        url = "https://api.thingspeak.com/update?api_key=" + API_KEY + "&field1=" + str(temperatura) + "&field2=" + str(umidade)
        resposta = urequests.get(url)
        print("ThingSpeak:", resposta.text)
        resposta.close()
        print("----------------")
    except OSError as e:
        print("Erro:", e)
    # ThingSpeak gratuito exige intervalo entre atualizações
    time.sleep(15)
