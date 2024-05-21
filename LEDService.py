from Service import Service
from ServiceStates import ServiceStates
try:
    from micropython import machine
except:
    import machine

class LEDService(Service):

    pin = machine.Pin(2, machine.Pin.OUT)

    def __init__(self, defaultState = ServiceStates.getOffState()):
        if defaultState == ServiceStates.getOnState():
            self.on()
        elif defaultState == ServiceStates.getOffState():
            self.off()
        else:
            self.off()

    def on(self):
        super(LEDService, self).on()
        print("INFO: LEDService.on()")
        self.pin.off()

    def off(self):
        super(LEDService, self).off()
        print("INFO: LEDService.off()")
        self.pin.on()

    def getState(self):
        return self.state
