#!/srv/robotice/bin/python

import sys
from oslo.config import cfg
from oslo.config import types

try:
    import sensor
except Exception, e:
    raise e

common_opts = [
    cfg.Opt('name',
            short='n',
            default="bh1750",
            help='Sensor name'),
    cfg.Opt('bus',
            short='b',
            default="1",
            help='I2C bus'),
]

CONF = cfg.CONF
CONF.register_cli_opts(common_opts)
CONF(sys.argv[1:])

print(sensor.get_data(CONF))
