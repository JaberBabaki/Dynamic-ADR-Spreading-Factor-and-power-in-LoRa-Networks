import numpy as np
import os
import statistics as sta

data_dir = os.getcwd()
pathRoot = 'E:\\daneshgah\\arshad\\ostad-rahnama\\simulate LoRa'
dir0 = os.listdir(pathRoot)
pathRoot2 = pathRoot + '\\' + str(dir0[0])
dir1 = os.listdir(pathRoot2)
pathRoot3 = pathRoot2 + '\\' + str(dir1[(1)])
dirU = os.listdir(pathRoot3)
pathRoot4 = pathRoot3 + '\\' + str(dirU[(0)])
dir2 = os.listdir(pathRoot4)
print("------"+pathRoot4 )
avDelivery0 = []
avEnergy0 = []
for j in range(len(dir2)):
    pathRoot5 = pathRoot4 + '\\' + str(dir2[(j)])
    dir3 = os.listdir(pathRoot5)
    print("------\n")
    print("------\n")
    print("------\n")
    avDelivery = []
    avEnergy = []
    for f in dir3:  # inside folder 30simulates
        g = open(pathRoot5 + '\\' + f)
        listOfLines = g.readlines()
        v = str(f).split('#')
        v2 = v[1].split('.')
        totalEnergyAllNode = 0
        for x in listOfLines:  # inside file
            if x.find("transmission count") != -1:
                s1 = x.split('count"')
                TP = s1[1]
            if x.find("totalReceivedPackets") != -1:
                s1 = x.split("totalReceivedPackets")
                RP = s1[1]
            if x.find("totalEnergyConsumed") != -1:
                s1 = x.split("totalEnergyConsumed")
                TE = s1[1]
                totalEnergyAllNode = totalEnergyAllNode + float(TE)
        avDelivery.append(float(RP) / float(TP))
        avEnergy.append(float(totalEnergyAllNode) / float(RP))
    avDelivery0.append(np.mean(avDelivery))
    avEnergy0.append(np.mean(avEnergy))
    print(
        '                                             --------------------------------------------------------------')
    print('                                             -->  ' + dir2[j] + '    ' + str(
        np.mean(avDelivery)))
    print('                                             -->  ' + dir2[j] + '    ' + str(
        np.mean(avEnergy)))
    print('                                             -->  ' + dir2[j] + '    ' + str(
        sta.stdev(avDelivery)))
    print('                                             -->  ' + dir2[j] + '    ' + str(
        sta.stdev(avEnergy)))
