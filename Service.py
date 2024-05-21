from ServiceStates import ServiceStates

class Service(object):  

    def __init__(self, defaultState = ServiceStates.getOffState()):
        if defaultState == ServiceStates.getOnState():
            self.on()
        elif defaultState == ServiceStates.getOffState():
            self.off()
        else:
            self.off()

    def on(self):
        self.state = ServiceStates.getOnState()

    def off(self):
        self.state = ServiceStates.getOffState()

    def getState(self):
        return self.state
