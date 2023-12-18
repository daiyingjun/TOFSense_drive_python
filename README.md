# python-TOFSense

---

## 简介

python driver for TOFSense

- TOFSense.py  驱动主要实现 支持TOFSense全系列
- demo.py   TOFSense-P/PS/F/FP 型号的demo
- demo_M.py  TOFSense-M/MS 型号的demo
  
PS：TOFSense-M4*4模式需要手动将self.datalen更新为TOFSENSE_DATA_LEN_M_44

## 使用

使用时提前实例化串口对象，并将串口对象传入实例化函数。
>*PS:串口号与波特率需要提前确认并更改*
>*串口号确认方法：*
>*我的电脑--设备管理器--端口(COM & LPT)--COMxx*
>*波特率确认方法：*
>*我的电脑--设备管理器--端口(COM & LPT)--COMxx--属性--波特率*
```
# 根据实际情况设置串口号和波特率
serial_port = "COM19"
baud_rate = 921600
ser = serial.Serial(serial_port, baud_rate)
```
实例化对象
```
# TOFSense P/PS/F/FP 型号
t = TOFSense.TOFSense_P_F(ser)

# TOFSense M/MS 型号
t = TOFSense.TOFSense_M(ser)
```
主动输出模式读取数据
```
t.get_data()
```
查询输出模式读取数据

```
id = 0
t.get_data_inquire(id)
```