# -*- coding: utf-8 -*-
import pyb,time
import monpal_ctl, motor_ctl, cylinder_ctl

received_number = 2		#位置初期値
mon_ctl = monpal_ctl.Monpal_controller(received_number)

while True:

    received_number = mon_ctl.received_position()	#位置情報受取

    monpal_dc = motor_ctl.Motor_controller(received_number)			#モーターデータ送り
    monpal_cylinder = cylinder_ctl.Cylinder_controller(received_number)	#シリンダデータ送り

    
    print(received_number)	#確認用
    time.sleep(1.0)
