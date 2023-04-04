import serial

# Configuração da porta serial
ser = serial.Serial('/dev/ttyUSB0', 9600)  # Altere '/dev/ttyUSB0' para a porta USB correta e 9600 para a velocidade correta

# Configuração dos pinos de entrada/saída
from machine import Pin
led = Pin(25, Pin.OUT)

# Loop principal
while True:
    # Espera receber dados na porta serial
    if ser.in_waiting > 0:
        # Lê os dados recebidos
        dados = ser.readline().decode().strip()

        # Verifica o comando recebido
        if dados == 'ligar':
            # Liga o LED
            led.on()
        elif dados == 'desligar':
            # Desliga o LED
            led.off()

