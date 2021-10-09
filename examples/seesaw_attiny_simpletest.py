# SPDX-FileCopyrightText: 2021 Kattni Rembor for Adafruit Industries
# SPDX-License-Identifier: MIT
import time
import board
import digitalio
from adafruit_seesaw import seesaw, neopixel, pwmout
from adafruit_seesaw.digitalio import DigitalIO

seesaw = seesaw.Seesaw(board.I2C())

seesaw.pin_mode(5, seesaw.OUTPUT)

# pixels = neopixel.NeoPixel(seesaw, 19, 12)
# pixels.brightness = 0.2

switch = DigitalIO(seesaw, 0)
switch.direction = digitalio.Direction.INPUT
switch.pull = digitalio.Pull.UP

pwm = pwmout.PWMOut(seesaw, 12)

while True:
    print(switch.value)
    seesaw.digital_write(5, switch.value)  # turn the LED on (True is the voltage level)
    # for i in range(100):
    #     # PWM LED up and down
    #     if i < 50:
    #         pwm.duty_cycle = int(i * 2 * 65535 / 100)  # Up
    #     else:
    #         pwm.duty_cycle = 65535 - int((i - 50) * 2 * 65535 / 100)  # Down
    # pwm.duty_cycle = 1000
    time.sleep(0.2)
    # pixels.fill((255, 0, 0))
    # pixels.fill(0)
    # time.sleep(1)
