import os.path
import numpy as np
import pandas as pd
from statistics import mean

packetsSent = pd.read_pickle('simulations/singleSide/results/singleSide_msgSent_density_144.pkl')

#Find performance metrics for each receiver
def findMetrics(sender, distance, ac):
    
    min_EndToEndDelay = []
    avg_EndToEndDelay = []
    max_EndToEndDelay = []
    min_PIR = []
    avg_PIR = []
    max_PIR = []
    PDR = []
    avg_RSSI = []
    avg_Contention = []
    avg_Collisions = []
    
    if (sender < 10):
        numSent = packetsSent.loc[packetsSent['Node'] == 'node_0'+str(sender), 'SentPackets'].iloc[0]
    else:
        numSent = packetsSent.loc[packetsSent['Node'] == 'node_'+str(sender), 'SentPackets'].iloc[0]
    
    start = sender - distance
    end = sender + distance
    for receiver in range(start, end+1): #Loop through receivers
        var = ac+'_density_144_from_'+str(sender)+'_to_'+str(receiver)+'.pkl'
        path = os.path.join('./pickle_files/density_144/', var)
        senderToReceiverData = pd.read_pickle(path)
        
        min_EndToEndDelay.append(senderToReceiverData['EndToEndDelay'].min())
        avg_EndToEndDelay.append(senderToReceiverData['EndToEndDelay'].mean())
        max_EndToEndDelay.append(senderToReceiverData['EndToEndDelay'].max())
        
        min_PIR.append(senderToReceiverData['PIR'].min())
        avg_PIR.append(senderToReceiverData['PIR'].mean())
        max_PIR.append(senderToReceiverData['PIR'].max())
        
        numReceived = senderToReceiverData.shape[0]
        #if(receiver < sender):
        PDR.append(float(numReceived)/(numSent))
        #else:
        #    PDR.append(float(numReceived)/(numSent-5*(receiver-sender)))
            
        avg_RSSI.append(senderToReceiverData['RSSI'].mean())
        avg_Contention.append(senderToReceiverData['Contention'].mean())
        avg_Collisions.append(senderToReceiverData['Collisions'].mean())

    return min_EndToEndDelay, avg_EndToEndDelay, max_EndToEndDelay, min_PIR, avg_PIR, max_PIR, PDR, avg_RSSI, avg_Contention, avg_Collisions

#sender = 30 #Sender node
distance = 65 #Range

ACs = ['AC0', 'AC1', 'AC2', 'AC3']
for ac in ACs:
    for sender in range(65, 75):
        minDelay, avgDelay, maxDelay, minPIR, avgPIR, maxPIR, PDR, avgRSSI, avgContention, avgCollisions = findMetrics(sender, distance, ac)

        nodes = [*range(sender-distance, sender+distance+1)]
        #nodes = [*range(sender-distance, sender)]
        result = pd.DataFrame({'Receiver Node':nodes, 'Minimum Delay':minDelay, 
                               'Average Delay':avgDelay, 'Maximum Delay':maxDelay, 'Minimum PIR':minPIR, 'Average PIR':avgPIR, 
                               'Maximum PIR':maxPIR, 'PDR':PDR, 'RSSI':avgRSSI, 'Contention':avgContention, 'Collision':avgCollisions})

        va = ac+'_denstiy_144_sender_'+str(sender)+'.pkl' 
        path = os.path.join('./pickle_files/density_144/', va) 
        pd.to_pickle(result, path)
