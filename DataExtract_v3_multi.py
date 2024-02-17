import sys
import csv
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import pandas as pd
import time
import os

def deviceColor(value):
    if value == 1:
        return 'red'
    elif value == 2:
        return 'blue'
    elif value == 3:
        return 'green'
    elif value == 4:
        return 'black'

def deviceLabel(value):
    if value == 1:
        return 'Device 1'
    elif value == 2:
        return 'Device 2'
    elif value == 3:
        return 'Device 3'
    elif value == 4:
        return 'Device 4'

current_dir = os.getcwd()
file_data = "Static.txt"

#filename = r"D:\PhD\00Program\LMC_Multiple_Extract\DataLMC15.txt"
#filename = r"D:\PhD\00Program\LMC_Multiple_Extract\Static.txt"
filename = os.path.join(current_dir, file_data)

dataFile = pd.read_csv(filename,index_col=False,sep=r',|\t', engine='python')
dataFile = dataFile.replace('\t','', regex=True)

datas=dataFile
iter=0

# You probably won't need this if you're embedding things in a tkinter plot...
plt.ion()

fig = plt.figure(figsize=(12, 7.5))
ax = fig.add_subplot(111, projection='3d')

ax.view_init(0, 90, 180)
ax.set_xlim(-300,300)
ax.set_ylim(0,200)
ax.set_zlim(-300,300)
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')

X_init = []
Y_init = []
Z_init = []
ScatterData1 = ax.scatter(X_init, Y_init, Z_init, c='red')
LineData1 = ax.plot(X_init, Y_init, Z_init, c='red')  
ScatterData2 = ax.scatter(X_init, Y_init, Z_init, c='blue')
LineData2 = ax.plot(X_init, Y_init, Z_init, c='blue') 
ScatterData3 = ax.scatter(X_init, Y_init, Z_init, c='green')
LineData3 = ax.plot(X_init, Y_init, Z_init, c='green') 
ScatterData4 = ax.scatter(X_init, Y_init, Z_init, c='black')
LineData4 = ax.plot(X_init, Y_init, Z_init, c='black')
    
data_dev1 = pd.DataFrame()
data_dev2 = pd.DataFrame()
data_dev3 = pd.DataFrame()
data_dev4 = pd.DataFrame()

while(iter<=datas.index.max()):
#while(iter<=100):

    datas_=pd.DataFrame([datas.loc[iter]]) #Data used start from Arm Proximal

    datas_X = pd.DataFrame()    
    for i in range(13, datas_.shape[1], 3):
        datas_X = pd.concat([datas_X, datas_.iloc[:, i]], axis=1)   
    datas_X = datas_X.T.reset_index(drop=True)
    datas_X = datas_X.rename(columns={0:'X'})

    datas_Y = pd.DataFrame()
    for i in range(14, datas_.shape[1], 3):
        datas_Y = pd.concat([datas_Y, datas_.iloc[:, i]], axis=1)   
    datas_Y = datas_Y.T.reset_index(drop=True)
    datas_Y = datas_Y.rename(columns={0:'Y'})

    datas_Z = pd.DataFrame()
    for i in range(15, datas_.shape[1], 3):
        datas_Z = pd.concat([datas_Z, datas_.iloc[:, i]], axis=1)   
    datas_Z = datas_Z.T.reset_index(drop=True)
    datas_Z = datas_Z.rename(columns={0:'Z'})

    datas_Coord = pd.concat([datas_X, datas_Y,datas_Z], axis=1)
    
    plot_order = [0, 1, 2, 3, 4, 5, 6, 5, 4, 8, 9, 10, 11, 10, 9, 8, 13, 14, 15, 16, 15, 14 ,13, 18, 19, 20, 21, 20, 19, 18, 23, 24, 25, 26, 25, 24, 23,
              22, 17, 12, 7, 2, 1, 22]
    datas_CoordPlot = datas_Coord.iloc[plot_order]
    datas_CoordPlot.reset_index(drop=True, inplace=True)

    datas_Coord = datas_Coord.to_numpy(dtype='f')
    datas_CoordPlot = datas_CoordPlot.to_numpy(dtype='f')

    if datas.iloc[iter,0]==1 :        
        data_dev1 =  pd.concat([data_dev1,datas.loc[iter].to_frame().T], axis = 0, ignore_index=True)
        X1, Y1, Z1 = datas_CoordPlot[:,0], datas_CoordPlot[:,1], datas_CoordPlot[:,2]
        ScatterData1.remove()
        LineData1[0].remove()       
        ScatterData1 = ax.scatter(X1, Y1, Z1, c=deviceColor(datas.iloc[iter,0]))
        LineData1 = ax.plot(X1, Y1, Z1, c=deviceColor(datas.iloc[iter,0]), label=deviceLabel(datas.iloc[iter,0]))        
    if datas.iloc[iter,0]==2 :        
        data_dev2 =  pd.concat([data_dev2,datas.loc[iter].to_frame().T], axis = 0, ignore_index=True)
        X2, Y2, Z2 = datas_CoordPlot[:,0], datas_CoordPlot[:,1], datas_CoordPlot[:,2]        
        ScatterData2.remove()
        LineData2[0].remove()
        ScatterData2 = ax.scatter(X2, Y2, Z2, c=deviceColor(datas.iloc[iter,0]))
        LineData2 = ax.plot(X2, Y2, Z2, c=deviceColor(datas.iloc[iter,0]), label=deviceLabel(datas.iloc[iter,0]))
    if datas.iloc[iter,0]==3 :
        data_dev3 =  pd.concat([data_dev3,datas.loc[iter].to_frame().T], axis = 0, ignore_index=True)
        X3, Y3, Z3 = datas_CoordPlot[:,0], datas_CoordPlot[:,1], datas_CoordPlot[:,2]
        ScatterData3.remove()
        LineData3[0].remove()
        ScatterData3 = ax.scatter(X3, Y3, Z3, c=deviceColor(datas.iloc[iter,0]))
        LineData3 = ax.plot(X3, Y3, Z3, c=deviceColor(datas.iloc[iter,0]), label=deviceLabel(datas.iloc[iter,0]))
    if datas.iloc[iter,0]==4 :
        data_dev4 =  pd.concat([data_dev4,datas.loc[iter].to_frame().T], axis = 0, ignore_index=True)
        X4, Y4, Z4 = datas_CoordPlot[:,0], datas_CoordPlot[:,1], datas_CoordPlot[:,2]
        ScatterData4.remove()
        LineData4[0].remove()
        ScatterData4 = ax.scatter(X4, Y4, Z4, c=deviceColor(datas.iloc[iter,0]))
        LineData4 = ax.plot(X4, Y4, Z4, c=deviceColor(datas.iloc[iter,0]), label=deviceLabel(datas.iloc[iter,0]))        

    ax.legend()
    
    plt.draw()
    plt.pause(0.00001)        

    iter = iter+1    

plt.ioff()

# Display the final plot
plt.show()
