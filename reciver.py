import machine
import utime
#car ligth serial 1 coper value 1 turn on value 2 turn off reciver
# Configura o pino GP16 como entrada
rx_pin = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_UP)

# Configura o pino GP2 como saída para controlar a lâmpada
lamp_pin = machine.Pin(2, machine.Pin.OUT)

# Função para receber e decodificar os dados da série
def receive_serial_data():
    data = 0
    for i in range(8):
        # Aguarda o sinal de início de bit
        while rx_pin.value() == 0:
            pass
        utime.sleep_us(300)
        # Lê o valor do bit
        if rx_pin.value() == 1:
            data |= 1 << i
        utime.sleep_us(700)
    return data

while True:
    # Aguarda os dados da série
    value = receive_serial_data()
    # Verifica o valor recebido e controla a lâmpada
    if value == 1:
        lamp_pin.value(1)
    elif value == 2:
        lamp_pin.value(0)

