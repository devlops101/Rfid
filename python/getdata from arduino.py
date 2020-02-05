import serial.tools.list_ports
import serial
se=serial.Serial("/dev/ttyACM1",9600)
b=''
b=str(se.readline())
b=b[2:len(b)-5]
print(b)
