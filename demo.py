# python==3.10.11
# pyserial==3.5
import serial
import TOFSense
import time

# 根据实际情况设置串口号和波特率
serial_port = "COM19"
baud_rate = 921600

try:
    ser = serial.Serial(serial_port, baud_rate)
except Exception as e:
    print(e)
    exit()

# TOFSense P/PS/F/FP 型号
t = TOFSense.TOFSense_P_F(ser)


# 主动输出模式
while True:
    data = t.get_data()
    if data != {0}:
        print(data)

"""
# 查询输出模式
# 0.02 = 1 / 50HZ
# 50HZ : 模块帧率 不同型号/模式有所不同，请自行更改
waiting_time = 0.02
while True:
    time.sleep(waiting_time)
    data = t.get_data_inquire(3)
    if data != {0}:
        print(data)
"""
