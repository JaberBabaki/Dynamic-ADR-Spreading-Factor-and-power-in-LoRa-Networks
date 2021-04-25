import numpy as np
import os
import statistics as sta

data_dir = os.getcwd()
pathRoot = 'E:\\daneshgah\\arshad\\simulate LoRa\\test\\LoRaSim-ADR-sigma=0,networkSize=480m,adrMethod=pes1,numberOfNodes=100-#0.sca'

g = open(pathRoot)
listOfLines = g.readlines()
#E:\daneshgah\arshad\simulate LoRa\test
a=0;
b=0;
for x in listOfLines:  # insude file
    if x.find('"numReceivedFromNode '+str(b)) != -1:
        print(x);
        #s1 = x.split('"numReceivedFromNode '+str(b)+'"')
        #a=a+int(s1[1]);
        #print(s1[0]);
    b=b+1;
