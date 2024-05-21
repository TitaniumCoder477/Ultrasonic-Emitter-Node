from Service import Service
from ServiceStates import ServiceStates

class PrintService(Service):

    def __init__(self, defaultState = ServiceStates.getOffState()):
        if defaultState == ServiceStates.getOnState():
            self.on()
        elif defaultState == ServiceStates.getOffState():
            self.off()
        else:
            self.off()

    def on(self):
        super(PrintService, self).on()
        print("On")

    def off(self):
        super(PrintService, self).off()
        print("Off")

    def getState(self):
        return self.state
