import time
import Adafruit_ADS1x15
adc = Adafruit_ADS1x15.ADS1115()

GAIN = int(input("What will be your gain? (Pick 1, 2, 4, 8, or 16):\n")) # Asks user for the gain.
rate = int(input("What is the sampling rate that you are using to use? (Pick 8, 16, 32, 64, 128, 250, 475, 860 samples per second):\n")) # Asks user for the sampling rate, in samples per second.
duration = int(input("For how long are you sampling?\n"))

adc.start_adc(0, GAIN, rate) # Starts continuous read on channel 0, with a gain inputted, and data rate as inputted.

initial = time.time()

while (time.time() - initial) <= duration:
    value = adc.get_last_result()
    statement = str(time.time()) + " " + str(value)
    print(statement)

adc.stop_adc() # Stops ADC
