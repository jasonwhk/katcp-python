
from twisted.internet import reactor
from katcp.txprotocol import TxDeviceServer, ServerFactory, run_server
from katcp import Sensor
from twisted.internet.protocol import Factory
from twisted.python import log
from katcp import Message
from katcp.test.testserver import IntSensor, FloatSensor

PORT = 1235 # or 0

import sys

class DemoServerFactory(ServerFactory):
    protocol = TxDeviceServer
    production = True
    
    def setup_sensors(self):
        self.add_sensor(FloatSensor(Sensor.FLOAT, "float_sensor", "descr",
                                    "milithaum", params=[-1.0, 1.0]))
        self.add_sensor(IntSensor(Sensor.INTEGER, "int_sensor", "descr2",
                               "cows", params=[-100, 100]))

def main():
    factory = run_server(DemoServerFactory, PORT)
    print factory.port.getHost()
    reactor.run()

if __name__ == '__main__':
    main()
