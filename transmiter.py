import machine
import utime
#car ligth transmit serial 1 coper 9600bps
# Configuração do pino de saída
pin_led = machine.Pin(25, machine.Pin.OUT)

# Configuração do pino de transmissão
pin_tx = machine.Pin(0, machine.Pin.OUT)

# Loop infinito de transmissão
while True:
    # Envia o valor binário 1 para ligar a lâmpada
    pin_tx.value(1)
    pin_led.value(1)
    utime.sleep(3)

    # Envia o valor binário 2 para desligar a lâmpada
    pin_tx.value(2)
    pin_led.value(0)
    utime.sleep(3)
