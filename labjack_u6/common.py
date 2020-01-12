"""
Classfile for LabJack U6: Common Functions
"""

import LabJackPython
import threading


class ei1050:

    def getHandle(self):
        self.handle

    # configure the data, clock, and power ports
    # returns True on success, False on failure
    def configure(self, power_port, data_port, clock_port):
        try:
            # u6_device = LabJackPython.openLabJack(LabJackPython.LJ_dtU6, LabJackPython.LJ_ctUSB, handleOnly=True)
            LabJackPython.ePut(self.handle, LabJackPython.LJ_ioPUT_DIGITAL_BIT, power_port, 1, 0)
            LabJackPython.ePut(self.handle, LabJackPython.LJ_ioPUT_CONFIG, LabJackPython.LJ_chSHT_DATA_CHANNEL,
                               data_port, 0)
            LabJackPython.ePut(self.handle, LabJackPython.LJ_ioPUT_CONFIG, LabJackPython.LJ_chSHT_CLOCK_CHANNEL,
                               clock_port, 0)
            LabJackPython.GoOne(self.handle)
            return True
        except Exception as ex:
            print(ex)
            return False

    def getTemperature_kelvin(self):
        LabJackPython.AddRequest(self.handle, LabJackPython.LJ_ioSHT_GET_READING, LabJackPython.LJ_chSHT_TEMP, 0,
                                 0, 0)
        LabJackPython.GoOne(self.handle)
        return LabJackPython.GetResult(self.handle, LabJackPython.LJ_ioSHT_GET_READING,
                                       LabJackPython.LJ_chSHT_TEMP)

    def getTemperature_celsius(self):
        LabJackPython.AddRequest(self.handle, LabJackPython.LJ_ioSHT_GET_READING, LabJackPython.LJ_chSHT_TEMP, 0,
                                 0, 0)
        LabJackPython.GoOne(self.handle)
        return (LabJackPython.GetResult(self.handle, LabJackPython.LJ_ioSHT_GET_READING,
                                        LabJackPython.LJ_chSHT_TEMP) - 273.15)

    def getTemperature_fahrenheit(self):
        LabJackPython.AddRequest(self.handle, LabJackPython.LJ_ioSHT_GET_READING, LabJackPython.LJ_chSHT_TEMP, 0,
                                 0, 0)
        LabJackPython.GoOne(self.handle)
        k = LabJackPython.GetResult(self.handle, LabJackPython.LJ_ioSHT_GET_READING,
                                    LabJackPython.LJ_chSHT_TEMP)
        return 9 / 5 * (k - 273) + 32

    def getRelativeHumitidy(self):
        return LabJackPython.AddRequest(self.handle, LabJackPython.LJ_ioSHT_GET_READING,
                                        LabJackPython.LJ_chSHT_RH, 0, 0, 0)


"""
    def record_Temperature_kelvin_ToCSV(self, sample_interval, duration):
        threading.Timer(sample_interval, record_Temperature_kelvin_ToCSV).start()
        print("TEST")

        return "test"
"""
