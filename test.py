import Home
import time

r1 = Home.Relay("RELAY1")
r2 = Home.Relay("RELAY2")

r1.on()
time.sleep(0.5)
r1.off()
time.sleep(0.5)

r2.on()
time.sleep(0.5)
r2.off()
time.sleep(0.5)
