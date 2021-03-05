import serial
import time
from numpy import cos, sin
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
#----------------------------------------------------#
arduinoData = serial.Serial('com3', 9600)
#----------------------------------------------------#
# Inceputul Programului
print("Scrieti (Start) pentru a incepe programul")
if input() == 'Start':
    arduinoData.write(b's')
#----------------------------------------------------#
theta1 = 0  # unghiul senzorului 1
theta2 = 15  # unghiul senzorului 2
theta3 = 30  # unchiul senzorului 3
theta4 = 45  # unghiul senzorului 4
theta5 = 60  # unghiul senzorului 5
theta6 = 75  # unchiul senzorului 6
theta1_list = [theta1]
theta2_list = [theta2]
theta3_list = [theta3]
theta4_list = [theta4]
theta5_list = [theta5]
theta6_list = [theta6]
#----------------------------------------------------#
# Lista in care se stocheaza toate datele de la senzori
distanceDataList = []
# Lista datelor de la Senzorul1
distance_Senzor1 = []
# Lista datelor de la Senzorul2
distance_Senzor2 = []
# Lista datelor de la Senzorul3
distance_Senzor3 = []
# Lista datelor de la Senzorul1
distance_Senzor4 = []
# Lista datelor de la Senzorul2
distance_Senzor5 = []
# Lista datelor de la Senzorul3
distance_Senzor6 = []
#----------------------------------------------------#
# x,y Senzor1
x1 = []
y1 = []
# x,y Senzor2
x2 = []
y2 = []
# x,y Senzor3
x3 = []
y3 = []
# x,y Senzor4
x4 = []
y4 = []
# x,y Senzor5
x5 = []
y5 = []
# x,y Senzor6
x6 = []
y6 = []
#----------------------------------------------------#
for i in range(300):
    time.sleep(0.1)
    print('Pas[{}]'.format(i))
    distanceData = arduinoData.readline().strip()
    distanceDataList.append(str(distanceData).strip('b'))
    theta1 += 1.8
    theta2 += 1.8
    theta3 += 1.8
    theta4 += 1.8
    theta5 += 1.8
    theta6 += 1.8
    theta1_list.append(theta1)
    theta2_list.append(theta2)
    theta3_list.append(theta3)
    theta4_list.append(theta4)
    theta5_list.append(theta5)
    theta6_list.append(theta6)
#----------------------------------------------------#
# print(distanceDataList)
# print(len(distanceDataList))
#----------------------------------------------------#
for x in range(0, len(distanceDataList), 6):  # 3 inainte
    distance_Senzor1.append(
        float(distanceDataList[x].split(' ')[2].strip("'")))
    distance_Senzor2.append(
        float(distanceDataList[x+1].split(' ')[2].strip("'")))
    distance_Senzor3.append(
        float(distanceDataList[x+2].split(' ')[2].strip("'")))
    distance_Senzor4.append(
        float(distanceDataList[x+3].split(' ')[2].strip("'")))
    distance_Senzor5.append(
        float(distanceDataList[x+4].split(' ')[2].strip("'")))
    distance_Senzor6.append(
        float(distanceDataList[x+5].split(' ')[2].strip("'")))
#----------------------------------------------------#
# Vizualizare date senzori
print('Senzor1={}'.format(distance_Senzor1))
print('Senzor2={}'.format(distance_Senzor2))
print('Senzor3={}'.format(distance_Senzor3))
print('Senzor4={}'.format(distance_Senzor4))
print('Senzor5={}'.format(distance_Senzor5))
print('Senzor6={}'.format(distance_Senzor6))
#--------------Vizualizare Date in csv---------------#
"""
d = {'Senzor1': distance_Senzor1, 'Senzor2': distance_Senzor2, 'Senzor3': distance_Senzor3, 'Senzor4': distance_Senzor4, 'Senzor5': distance_Senzor5, 'Senzor6': distance_Senzor6}
df = pd.DataFrame(data=d)
df.to_csv('date.csv', sep='\t')"""
#------------Aflarea Coordonatelor x,y---------------#
for i in range(len(distance_Senzor1)):
    # x si y pentru Senzorul 1
    x1.append(distance_Senzor1[i]*cos(theta1_list[i]))
    y1.append(distance_Senzor1[i]*sin(theta1_list[i]))
    # x si y pentru Senzorul 2
    x2.append(distance_Senzor2[i]*cos(theta2_list[i]))
    y2.append(distance_Senzor2[i]*sin(theta2_list[i]))
    # x si y pentru Senzorul 3
    x3.append(distance_Senzor3[i]*cos(theta3_list[i]))
    y3.append(distance_Senzor3[i]*sin(theta3_list[i]))
    # x si y pentru Senzorul 4
    x4.append(distance_Senzor4[i]*cos(theta4_list[i]))
    y4.append(distance_Senzor4[i]*sin(theta4_list[i]))
    # x si y pentru Senzorul 5
    x5.append(distance_Senzor5[i]*cos(theta5_list[i]))
    y5.append(distance_Senzor5[i]*sin(theta5_list[i]))
    # x si y pentru Senzorul 6
    x6.append(distance_Senzor6[i]*cos(theta6_list[i]))
    y6.append(distance_Senzor6[i]*sin(theta6_list[i]))
#----------Vizualizare coordonate puncte-------------#
print('x1={}'.format(x1), '\n', 'y1={}'.format(y1))
print('x2={}'.format(x2), '\n', 'y2={}'.format(y2))
print('x3={}'.format(x3), '\n', 'y3={}'.format(y3))
print('x4={}'.format(x4), '\n', 'y1={}'.format(y4))
print('x5={}'.format(x5), '\n', 'y2={}'.format(y5))
print('x6={}'.format(x6), '\n', 'y3={}'.format(y6))
#----------------------Grafice-----------------------#
fig = plt.figure()
ax = Axes3D(fig)

ax.scatter(x1, y1, zs=1, zdir='z', s=len(x1), c='r', depthshade=True)
ax.scatter(x2, y2, zs=1.005, zdir='z', s=len(x2), c='b', depthshade=True)
ax.scatter(x3, y3, zs=1.01, zdir='z', s=len(x3), c='g', depthshade=True)
ax.scatter(x4, y4, zs=1.015, zdir='z', s=len(x4), c='c', depthshade=True)
ax.scatter(x5, y5, zs=1.02, zdir='z', s=len(x5), c='m', depthshade=True)
ax.scatter(x6, y6, zs=1.025, zdir='z', s=len(x6), c='y', depthshade=True)
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
ax.set_title('Plot')
"""
ax.plot(x1,y1,10)
ax.plot(x2,y2,12.5)
ax.plot(x3,y3,15)
ax.plot(x4,y4,17.5)
ax.plot(x5,y5,20)
ax.plot(x6,y6,22.5)
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
ax.set_title(' Plot')"""
plt.show()
