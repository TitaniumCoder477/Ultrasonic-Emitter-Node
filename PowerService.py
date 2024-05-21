from Service import Service
from ServiceStates import ServiceStates

try:
    from micropython import machine
except:
    import machine
    
import time

class PowerService(Service):

    unsetPin = machine.Pin(15, machine.Pin.OUT)
    setPin = machine.Pin(16, machine.Pin.OUT)

    def __init__(self, defaultState = ServiceStates.getOffState()):
        if defaultState == ServiceStates.getOnState():
            self.on()
        elif defaultState == ServiceStates.getOffState():
            self.off()
        else:
            self.off()

    def on(self):
        super(PowerService, self).on()
        self.setPin.off()
        self.unsetPin.on()
        time.sleep_ms(10)
        self.unsetPin.off()

    def off(self):
        super(PowerService, self).off()
        self.unsetPin.off()
        self.setPin.on()
        time.sleep_ms(10)
        self.setPin.off()

    def getState(self):
        return self.state
