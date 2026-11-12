# Monitor de Temperatura e Umidade com ESP32

Projeto de IoT em **MicroPython** que lê temperatura e umidade com um sensor DHT11, aciona um relé automaticamente e envia os dados para a nuvem via **ThingSpeak**. Desenvolvido em simulador de ESP32.

## O que o projeto faz

1. Conecta o ESP32 ao Wi-Fi.
2. Lê temperatura e umidade do sensor DHT11 a cada 15 segundos.
3. Liga o relé quando **temperatura > 31 °C** ou **umidade > 70 %**, e desliga nos demais casos.
4. Envia as leituras para o ThingSpeak (campo 1 = temperatura, campo 2 = umidade), onde podem ser vistas em gráficos.

## Componentes (simulados)

| Componente | Pino | Função |
|---|---|---|
| Sensor DHT11 | 9 | Leitura de temperatura e umidade |
| LED | 2 | Representa o relé no simulador |

## Tecnologias

- Python / MicroPython
- ESP32 (simulador)
- Bibliotecas `machine`, `dht`, `network`, `urequests`
- ThingSpeak (API HTTP)

## Como configurar

1. Crie um canal gratuito no [ThingSpeak](https://thingspeak.com) com dois campos (temperatura e umidade).
2. Crie um arquivo `config.py` com a sua chave de escrita:

   ```python
   API_KEY = "SUA_CHAVE_AQUI"
   ```

3. No `main.py`, importe a chave com `from config import API_KEY`.
4. Rode o projeto no simulador de ESP32.

> **Segurança:** o `config.py` não deve ser enviado ao GitHub. Ele está listado no `.gitignore`. O repositório traz apenas o `config_example.py`, com um valor de exemplo.

## O que aprendi

- Ler sensores e tomar decisões com condicionais (`if` com `or`).
- Fazer requisições HTTP a partir de um microcontrolador.
- Respeitar o limite de atualização da API gratuita (intervalo de 15 s entre envios).
- Tratar erros de rede com `try/except` para o programa não parar.
- Não deixar chaves de API expostas no código.

## Ideias de melhoria

- Reconectar automaticamente se o Wi-Fi cair.
- Enviar alertas (e-mail ou Telegram) quando o relé ligar.
- Tornar os limites de 31 °C e 70 % configuráveis.

## Autora

**Bruna Servidone**
