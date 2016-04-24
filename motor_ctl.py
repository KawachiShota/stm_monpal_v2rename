# -*- coding: utf-8 -*-
""" module import """
from pyb import Pin, Timer, UART
import pyb,math,time
import micropython
micropython.alloc_emergency_exception_buf(100)

class Motor_controller:
    def __init__(self, number):


        dc_list = (1, 0, 1, 1, 1, 1)	#モーターON/OFFリスト
        number = number - 1
        self.dc_data = dc_list [number]		#位置に対応したデータを選ぶ


        p1 = pyb.Pin(pyb.Pin.board.PE9, mode=pyb.Pin.OUT_PP)

        if self.dc_data == 1:
        	p1.high()

        else:
        	p1.low()



