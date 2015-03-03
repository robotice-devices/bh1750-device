#!/usr/bin/python

import logging
import time
import smbus

logger = logging.getLogger("robotice.sensor.bh1750")

def get_data(sensor):
    """
    Get the luminosity readings.
    """

    name = sensor.get('name')
    bus = sensor.get('bus')

    bus = smbus.SMBus(int(bus))
    addr = 0x23
    data = bus.read_i2c_block_data(addr,0x11)
    lux = str((data[1] + (256 * data[0])) / 1.2)
 
    values = [
        ('%s.luminosity' % name, lux, ),
    ]
    return values
