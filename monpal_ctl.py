# -*- coding: utf-8 -*-
import pyb, time

usb = pyb.USB_VCP()		#jetsonに接続

class Monpal_controller:

    def __init__(self, number):
        self.number = number
#        print(self.number)

    def received_position(self):	#位置受取
        number = usb.read()

        if number == None:		#位置入力がなしなら停止
            number = 2

        self.number = int(number)

        if self.number > 6:		#位置入力が異常なら停止
            self.number = 2
        
        return self.number





