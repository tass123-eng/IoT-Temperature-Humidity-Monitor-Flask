import grovepi
import time 
dht_sensor = 4 
dht_type = 0 
while True: 
    temp, hum = grovepi.dht(dht_sensor, dht_type) 
    print("Temperature:", temp) 
    print("Humidity:", hum) 
    print("--------------------")
    time.sleep(2)
