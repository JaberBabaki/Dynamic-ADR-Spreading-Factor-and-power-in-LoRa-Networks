import numpy as np
import os
import statistics as sta

data_dir = os.getcwd()
pathRoot = 'E:\\daneshgah\\arshad\\ostad-rahnama\\simulate LoRa'
dir0 = os.listdir(pathRoot)
pathRoot2 = pathRoot + '\\' + str(dir0[1])
dir1 = os.listdir(pathRoot2)
pathRoot3 = pathRoot2 + '\\' + str(dir1[(1)])
dir2 = os.listdir(pathRoot3)
print("------" + pathRoot3)
for j in range(len(dir2)):  # 0 or 3  or 5
    pathRoot4 = pathRoot3 + '\\' + str(dir2[(j)])
    dir3 = os.listdir(pathRoot4)
    print("------\n")
    print("------\n")
    print("------\n")
    avDelivery0 = []
    avEnergy0 = []
    for f in range(len(dir3)):  # 100  or  200  or  300 ....
        pathRoot5 = pathRoot4 + '\\' + str(dir3[(f)])
        dir4 = os.listdir(pathRoot5)
        sx = 0
        avDelivery = []
        avEnergy = []
        for h in dir4:  # inside folder 30 ta
            # print(pathRoot5)
            # print(h)
            g = open(pathRoot5 + '\\' + h)
            listOfLines = g.readlines()
            v = str(h).split('#')
            v2 = v[1].split('.')
            sx += 1
            totalEnergyAllNode = 0
            for x in listOfLines:  # insude file
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
        print('                                             -->  ' + dir2[j] + '    ' + dir3[f] + '    ' + str(
            np.mean(avDelivery)))
        print('                                             -->  ' + dir2[j] + '    ' + dir3[f] + '    ' + str(
            np.mean(avEnergy)))
        print('                                             -->  ' + dir2[j] + '    ' + dir3[f] + '    ' + str(
            sta.stdev(avDelivery)))
        print('                                             -->  ' + dir2[j] + '    ' + dir3[f] + '    ' + str(
            sta.stdev(avEnergy)))
