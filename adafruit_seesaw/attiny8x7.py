# SPDX-FileCopyrightText: 2021 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# 1pylint: disable=missing-docstring,invalid-name,too-many-public-methods,too-few-public-methods

"""
`adafruit_seesaw.attiny8x7` - Pin definition for Adafruit ATtiny817 Breakout with seesaw
==================================================================================
"""

try:
    from micropython import const
except ImportError:

    def const(x):
        return x


__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/adafruit/Adafruit_CircuitPython_seesaw.git"

_ADC_INPUT_0_PIN = const(0)
_ADC_INPUT_1_PIN = const(1)
_ADC_INPUT_2_PIN = const(2)
_ADC_INPUT_3_PIN = const(3)
_ADC_INPUT_4_PIN = const(6)
_ADC_INPUT_5_PIN = const(7)
_ADC_INPUT_6_PIN = const(18)
_ADC_INPUT_7_PIN = const(19)
_ADC_INPUT_8_PIN = const(20)

_PWM_0_PIN = const(0)
_PWM_1_PIN = const(1)
_PWM_2_PIN = const(9)
_PWM_3_PIN = const(12)
_PWM_4_PIN = const(13)


class ATtiny8x7_Pinmap:
    """This class is automatically used by `adafruit_seesaw.seesaw.Seesaw` when
    an ATtiny8x7 Breakout is detected.

    It is also a reference for the capabilities of each pin."""

    #: The pins capable of analog output
    analog_pins = (
        _ADC_INPUT_0_PIN,
        _ADC_INPUT_1_PIN,
        _ADC_INPUT_2_PIN,
        _ADC_INPUT_3_PIN,
        _ADC_INPUT_4_PIN,
        _ADC_INPUT_5_PIN,
        _ADC_INPUT_6_PIN,
        _ADC_INPUT_7_PIN,
        _ADC_INPUT_8_PIN,
    )

    """The effective bit resolution of the PWM pins"""
    pwm_width = 8

    """The pins capable of PWM output"""
    pwm_pins = (_PWM_0_PIN, _PWM_1_PIN, _PWM_2_PIN, _PWM_3_PIN, _PWM_4_PIN)

    """No pins on this board are capable of touch input"""
    touch_pins = ()
