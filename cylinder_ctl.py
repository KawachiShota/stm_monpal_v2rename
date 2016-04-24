# -*- coding: utf-8 -*-
""" module import """
from pyb import Pin, Timer, UART
import pyb,math,time
import micropython
micropython.alloc_emergency_exception_buf(100)

class Cylinder_controller:
    def __init__(self, number):

        cylinder_list = (1, 2, 3, 4, 5, 6)	#ロッド位置リスト
        number = number - 1
	rod_p = cylinder_list[number]		#位置を選ぶ


        p1 = pyb.Pin(pyb.Pin.board.PE11, mode=pyb.Pin.OUT_PP)
        p2 = pyb.Pin(pyb.Pin.board.PE12, mode=pyb.Pin.OUT_PP)
        p3 = pyb.Pin(pyb.Pin.board.PE13, mode=pyb.Pin.OUT_PP)
        p4 = pyb.Pin(pyb.Pin.board.PE14, mode=pyb.Pin.OUT_PP)
        p5 = pyb.Pin(pyb.Pin.board.PE15, mode=pyb.Pin.OUT_PP)

        if rod_p == 1:
            p1.high()
            p2.low()

        elif rod_p == 2:
            p1.low()
            p2.high()

