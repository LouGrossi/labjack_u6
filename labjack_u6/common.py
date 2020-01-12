"""
Classfile for LabJack U6: Common Functions
"""

import LabJackPython
import time, threading, signal
from datetime import timedelta
import multiprocessing
import csv

u6_device = LabJackPython.openLabJack(LabJackPython.LJ_dtU6, LabJackPython.LJ_ctUSB, handleOnly=True)


class ei1050:

    def getHandle(self):
        return self.handle

    def configure(self, power_port, data_port, clock_port):
        try:
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

    class humidity:
        def relative_humidity(self):
            try:
                LabJackPython.AddRequest(self.handle, LabJackPython.LJ_ioSHT_GET_READING,
                                         LabJackPython.LJ_chSHT_RH, 0, 0, 0)
                LabJackPython.GoOne(self.handle)
                return LabJackPython.GetResult(self.handle, LabJackPython.LJ_ioSHT_GET_READING,
                                               LabJackPython.LJ_chSHT_RH)
            except Exception as ex:
                print(ex)
                return False

    class temperature:

        def kelvin(self):
            LabJackPython.AddRequest(self.handle, LabJackPython.LJ_ioSHT_GET_READING, LabJackPython.LJ_chSHT_TEMP, 0,
                                     0, 0)
            LabJackPython.GoOne(self.handle)
            return LabJackPython.GetResult(self.handle, LabJackPython.LJ_ioSHT_GET_READING,
                                           LabJackPython.LJ_chSHT_TEMP)

        def celsius(self):
            LabJackPython.AddRequest(self.handle, LabJackPython.LJ_ioSHT_GET_READING, LabJackPython.LJ_chSHT_TEMP, 0,
                                     0, 0)
            LabJackPython.GoOne(self.handle)
            return (LabJackPython.GetResult(self.handle, LabJackPython.LJ_ioSHT_GET_READING,
                                            LabJackPython.LJ_chSHT_TEMP) - 273.15)

        def fahrenheit(self):
            LabJackPython.AddRequest(self.handle, LabJackPython.LJ_ioSHT_GET_READING, LabJackPython.LJ_chSHT_TEMP, 0,
                                     0, 0)
            LabJackPython.GoOne(self.handle)
            k = LabJackPython.GetResult(self.handle, LabJackPython.LJ_ioSHT_GET_READING,
                                        LabJackPython.LJ_chSHT_TEMP)
            return 9 / 5 * (k - 273) + 32
