#!/usr/bin/python

import logging
import time
import smbus
import decimal

logger = logging.getLogger("robotice.sensor.bh1750")

def get_data(sensor):
    """
    Get the luminosity readings.
    """

    name = sensor.get('name')

    bus = smbus.SMBus(1)
    addr = 0x23
    data = bus.read_i2c_block_data(addr,0x11)
    lux2 = str((data[1] + (256 * data[0])) / 1.2)
    lux = decimal.Decimal(lux2).quantize(decimal.Decimal('.01'), rounding=decimal.ROUND_UP)
 
    values = [
        ('%s.lux' % name, lux, ),
    ]
    return values


print outlux