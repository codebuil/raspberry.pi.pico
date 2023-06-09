import machine
import time
# raspberry pi pico piano
# Configurar os pinos dos sensores como entrada
sensor_pins = [0, 1, 2, 3, 4, 5, 6, 7]
sensors = [machine.Pin(pin, machine.Pin.IN) for pin in sensor_pins]

# Configurar o pino da saída do som
buzzer_pin = machine.Pin(8, machine.Pin.OUT)

# Função para reproduzir uma nota no buzzer
def beep(frequency, duration):
    period_us = int(1000000 / frequency)
    cycles = int(frequency * duration / 1000)
    for i in range(cycles):
        buzzer_pin.on()
        time.sleep_us(period_us // 2)
        buzzer_pin.off()
        time.sleep_us(period_us // 2)

# Loop principal do programa
while True:
    # Ler o estado dos sensores
    sensor_values = [sensor.value() for sensor in sensors]

    # Reproduzir uma nota para cada sensor ativo
    for i, value in enumerate(sensor_values):
        if value == 1:
            frequency = 440 * 2**(i / 12) # calcular a frequência da nota com base na posição do sensor
            beep(frequency, 100) # reproduzir a nota por 100ms

