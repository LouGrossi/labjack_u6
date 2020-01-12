import labjack_u6.common as common
import LabJackPython
"""
    Editable pinout variables 
"""
EI1050_GROUND_PORT = "GND"  # black
EI1050_POWER_PORT = 0   # red
EI1050_DATA_PORT = 1    # green
EI1050_CLOCK_PORT = 2   # white

"""
    Objects you need
"""
u6_device = LabJackPython.openLabJack(LabJackPython.LJ_dtU6, LabJackPython.LJ_ctUSB, handleOnly=True)

"""
    Test code below
"""
# configure u6 for temp/humidity probe
print(common.ei1050.configure(u6_device, EI1050_POWER_PORT, EI1050_DATA_PORT, EI1050_CLOCK_PORT))
print(common.ei1050.humidity.relative_humidity(u6_device))
#print(common.ei1050.temperature.kelvin(u6_device))
#print(common.ei1050.temperature.celsius(u6_device))
#print(common.ei1050.temperature.fahrenheit(u6_device))
# print the temp in fahrenheit

#common.ei1050.temperature.