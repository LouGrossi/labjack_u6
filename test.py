import labjack_u6.common as common
import LabJackPython
"""
    Editable pinout variables 
"""
EI1050_GROUND_PORT = 0
EI1050_POWER_PORT = 1
EI1050_DATA_PORT = 2
EI1050_CLOCK_PORT = 3

"""
    Objects you need
"""
u6_device = LabJackPython.openLabJack(LabJackPython.LJ_dtU6, LabJackPython.LJ_ctUSB, handleOnly=True)

"""
    Test code below
"""
# configure u6 for temp/humidity probe
common.ei1050.configure(u6_device, 1, 2, 3)

# print the temp in fahrenheit
print(common.ei1050.getTemperature_fahrenheit(u6_device))