# CANbusMonitor
# read signal setting from signal.cfg
# while 1:[check buff file && sleep]
#     if buff:Read buff csv && display
#     else:do nothing
# by:TakanashiKoucha

import matplotlib.pyplot as plt

x_time = []
y_data = []

plt.ion()

while True:
    try:
        x_time.append(float(input("x_time:")))
        y_data.append(int(input("y_data:")))
        plt.clf()
        plt.plot(x_time, y_data)
    except:
        plt.ioff()
        print("Warning!!!")
