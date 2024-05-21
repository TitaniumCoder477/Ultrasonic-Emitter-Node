# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
try:
    from micropython import machine
except:
    import machine

try:
    from micropython import network
except:
    import network

try:    
    from micropython import uos
except:
    import uos

try:
    from micropython import uselect
except:
    import uselect

try:
    from micropython import usocket
except:
    import usocket

try:
    from micropython import gc
except:
    import gc

import webrepl    
#uos.dupterm(None, 1) # disable REPL on UART(0)

webrepl.start()
gc.collect()

def do_connect():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():

        print("INFO: Loading wifi profile file...")
        try:
            f = open("wifi_profile.txt")
            line = f.read()
            profile = line.split(':')[0].strip()
            password = line.split(':')[1].strip()
        except Exception as e:
            print("ERROR: %s..." % e)
        finally:
            f.close()

        print("INFO: Connecting to wifi...")
        try:
            sta_if.active(True)
            sta_if.connect(profile, password)
            while not sta_if.isconnected():
                pass
            print('network config:', sta_if.ifconfig())
        except Exception as e:
            print("ERROR: %s..." % e)

do_connect()