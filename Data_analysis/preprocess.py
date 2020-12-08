import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('simulations/singleSide/results/singleSide_data_density_144.csv', header=None)

dataset.to_csv('C:/fyp/simulations/singleSide/results/singleSide_data_density_144.csv', header=['PacketID',
                'PacketSize', 'SenderSSID', 'ReceiverSSID', 'RSSI', 'ArrivalTime', 'EndToEndDelay', 
                'SenderXPos', 'SenderYPos', 'SenderSpeed', 'ReceiverXPos', 'ReceiverYPos', 'ReceiverSpeed', 
                'Contention', 'Collisions', 'AccessClass'], index=False)
                
dataset = pd.read_csv('simulations/singleSide/results/singleSide_data_density_144.csv')

###### split data based on access class ######
ac0_data = dataset.loc[dataset['AccessClass'] == 0]
ac1_data = dataset.loc[dataset['AccessClass'] == 1]
ac2_data = dataset.loc[dataset['AccessClass'] == 2]
ac3_data = dataset.loc[dataset['AccessClass'] == 3]

numOfNodes = 140 #Number of vehicles
ac_frames = [ac0_data, ac1_data, ac2_data, ac3_data]
ACs = ['AC0', 'AC1', 'AC2', 'AC3']
i = 0

for ac_frame in ac_frames:
    for receiver in range(numOfNodes):
        if (receiver < 10):
            toData = ac_frame.loc[ac_frame['ReceiverSSID'] == 'node_0'+str(receiver)]
        else:
            toData = ac_frame.loc[ac_frame['ReceiverSSID'] == 'node_'+str(receiver)]

        for sender in range(numOfNodes):
            if (sender < 10):
                fromToData = toData.loc[toData['SenderSSID'] == 'node_0'+str(sender)] 
            else:
                fromToData = toData.loc[toData['SenderSSID'] == 'node_'+str(sender)]
                
            fromToData['PIR'] = fromToData['ArrivalTime'].diff() #Add PIR column

            var = ACs[i]+'_density_144_from_'+str(sender)+'_to_'+str(receiver)+'.pkl'
            newPath = os.path.join('./pickle_files/density_144/', var)
            pd.to_pickle(fromToData, newPath) #Convert to pickle format
    i += 1
