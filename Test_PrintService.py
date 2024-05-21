from PrintService import PrintService
from ServiceStates import ServiceStates

class TestFailed(Exception):
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

def on_whenSuccessful():
    testName = "on_whenSuccessful"
    print("Test:", testName)
    desiredValue = ServiceStates.getOnState()
    service = PrintService(ServiceStates.getOffState())
    service.on()
    state = service.getState()
    if state != desiredValue:
        raise TestFailed(testName, "We expected the state to be on.")

def off_whenSuccessful():
    testName = "off_whenSuccessful"
    print("Test:", testName)
    desiredValue = ServiceStates.getOffState()
    service = PrintService(ServiceStates.getOnState())
    service.off()
    state = service.getState()
    if state != desiredValue:
        raise TestFailed(testName, "We expected the state to be on.")

def main():

    try:
        on_whenSuccessful()
        off_whenSuccessful()
    except TestFailed as err:
        print("Test failed: ", err)

main()
