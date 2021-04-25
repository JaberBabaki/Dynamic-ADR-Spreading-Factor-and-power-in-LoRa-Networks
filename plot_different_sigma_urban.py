import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# ------E:\daneshgah\arshad\ostad-rahnama\simulate LoRa\all\0\0.8\1.7\2.6\3.5\

# AVG
sub0Delevry_AVG = [0.5699728649478927, 0.6090540804126415, 0.6381131615334461, 0.6545289514345903, 0.6318965651650517]
sub0Energy_AVG = [0.25590954251814, 0.2050509459270121, 0.2110938107525512, 0.19670995476998196, 0.19545601815438396]
sub0DelevryDeviation_AVG = [0.0343924985064, 0.0205468116773, 0.0269331231959, 0.0153846691709, 0.00999301026855]
sub0EnergyDeviation_AVG = [0.0203092896226, 0.0167294071109, 0.0137958809938, 0.00821090229377, 0.00856589963846]
sub0Delevry_AVG = np.array(sub0Delevry_AVG)
sub0DelevryDeviation_AVG = np.array(sub0DelevryDeviation_AVG)
sub0Delevry_AVG = sub0Delevry_AVG * 100
sub0DelevryDeviation_AVG = sub0DelevryDeviation_AVG * 100

sub0Energy_AVG = np.array(sub0Energy_AVG)
sub0EnergyDeviation_AVG = np.array(sub0EnergyDeviation_AVG)
sub0Energy_AVG = sub0Energy_AVG * 1000
sub0EnergyDeviation_AVG = sub0EnergyDeviation_AVG * 100

# MAX
sub0Delevry_MAX = [0.5700142332871306, 0.6218137868677238, 0.5197155220948917, 0.3271350613890414, 0.2136303681469565]
sub0Energy_MAX = [0.25589386272386616, 0.20182707228610378, 0.21002781067567053, 0.321494310714993,
                  0.4757077444791612]
sub0DelevryDeviation_MAX = [0.0344523181816, 0.0274701721526, 0.0160028802716, 0.0120421030874, 0.0108684873977]
sub0EnergyDeviation_MAX = [0.020349665383, 0.0144521268851, 0.0123743092214, 0.0203125024311, 0.034665294817]
sub0Delevry_MAX = np.array(sub0Delevry_MAX)
sub0DelevryDeviation_MAX = np.array(sub0DelevryDeviation_MAX)
sub0Delevry_MAX = sub0Delevry_MAX * 100
sub0DelevryDeviation_MAX = sub0DelevryDeviation_MAX * 100

sub0Energy_MAX = np.array(sub0Energy_MAX)
sub0EnergyDeviation_MAX = np.array(sub0EnergyDeviation_MAX)
sub0Energy_MAX = sub0Energy_MAX * 1000
sub0EnergyDeviation_MAX = sub0EnergyDeviation_MAX * 100

# MIN
sub0Delevry_MIN = [0.2776926754179688, 0.51024126326329, 0.6451412789578549, 0.6636309453666956, 0.66808279134317704,
                   ]
sub0Energy_MIN = [0.4857077444791612,0.291494310714993,0.20002781067567053,0.18670995476998196, 0.17545601815438396]
sub0DelevryDeviation_MIN = [0.0317168003656, 0.0261626353823, 0.0152758144938, 0.0124287414801, 0.0107247179515,
                            0.0114634572378, 0.0116240074174, 0.0112181993397, 0.0082143939008]
sub0EnergyDeviation_MIN = [0.0181552687761, 0.0121221627282, 0.00907799485973, 0.0188097471633, 0.0259587285684,
                           0.044878223915, 0.0541779424747, 0.0536888738204, 0.0450312953167]
sub0Delevry_MIN = np.array(sub0Delevry_MIN)
sub0DelevryDeviation_MIN = np.array(sub0DelevryDeviation_MIN)
sub0Delevry_MIN = sub0Delevry_MIN * 100
sub0DelevryDeviation_MIN = sub0DelevryDeviation_MIN * 100

sub0Energy_MIN = np.array(sub0Energy_MIN)
sub0EnergyDeviation_MIN = np.array(sub0EnergyDeviation_MIN)
sub0Energy_MIN = sub0Energy_MIN * 1000
sub0EnergyDeviation_MIN = sub0EnergyDeviation_MIN * 100



# NoADR
sub0Delevry_NoADR = [0.3372039099461437, 0.33575237361228005, 0.33675244139228816, 0.3302741197328445,
                     0.33576542760475525]
sub0Energy_NoADR = [0.35691888930426346, 0.35829248148811915, 0.3587166622104879, 0.3678188657356181,
                    0.3564891242791599]
sub0DelevryDeviation_NoADR = [0.0343339684887, 0.0334292638709, 0.0358889719239, 0.036396821299, 0.0301175977712]
sub0EnergyDeviation_NoADR = [0.033263825134, 0.0310966444856, 0.0307901879948, 0.0373484067779, 0.0312146942847]
sub0Delevry_NoADR = np.array(sub0Delevry_NoADR)
sub0DelevryDeviation_NoADR = np.array(sub0DelevryDeviation_NoADR)
sub0Delevry_NoADR = sub0Delevry_NoADR * 100
sub0DelevryDeviation_NoADR = sub0DelevryDeviation_NoADR * 100

sub0Energy_NoADR = np.array(sub0Energy_NoADR)
sub0EnergyDeviation_NoADR = np.array(sub0EnergyDeviation_NoADR)
sub0Energy_NoADR = sub0Energy_NoADR * 1000
sub0EnergyDeviation_NoADR = sub0EnergyDeviation_NoADR * 100

# PES
sub0Delevry_PES = [0.5699567722071939, 0.6124041149606863, 0.643155090774879, 0.6644042057888477, 0.6651376911449955]
sub0Energy_PES = [0.25592238422618613, 0.23672843698191542, 0.22890679042298037, 0.22577895163884654, 0.22497259893696187]
sub0DelevryDeviation_PES = [0.034381492806,0.0308727392729, 0.0250491567616, 0.0179071418749, 0.0122522528496]
sub0EnergyDeviation_PES = [0.0203078181779, 0.0203097067466, 0.0170161106121, 0.0128810747725, 0.0118938146985]
sub0Delevry_PES = np.array(sub0Delevry_PES)
sub0DelevryDeviation_PES = np.array(sub0DelevryDeviation_PES)
sub0Delevry_PES = sub0Delevry_PES * 100
sub0DelevryDeviation_PES = sub0DelevryDeviation_PES * 100

sub0Energy_PES = np.array(sub0Energy_PES)
sub0EnergyDeviation_PES = np.array(sub0EnergyDeviation_PES)
sub0Energy_PES = sub0Energy_PES * 1000
sub0EnergyDeviation_PES = sub0EnergyDeviation_PES * 100



p = [0.00,0.89, 1.78, 2.67, 3.56]
title_font = {'fontname':'Times New Roman', 'size':'16', 'color':'black', 'weight':'normal'}
number = {'fontname':'Times New Roman', 'size':'13', 'color':'black', 'weight':'normal'}
ax = plt.axes()
ax.grid(alpha=0.7, linestyle=':')
plt.xticks(p,**number)
plt.yticks(**number)

"""
plt.plot(p, sub0Energy_AVG,'s',markersize=6, color='blue', linewidth=1.5,
         markerfacecolor='blue',linestyle='-',label='ADR-AVG[17]')
plt.plot(p, sub0Energy_MAX,'o',markersize=6, color='green',linewidth=1.5,
         linestyle='-',markerfacecolor='green',label='ADR-MAX[8]')
plt.plot(p, sub0Energy_NoADR,'^',markersize=6, color='black',linewidth=1.5,
         linestyle='-',markerfacecolor='black',label='ADR-NoADR')
plt.plot(p, sub0Energy_PES,'x',markersize=6,  color='red',linewidth=1.5,
         linestyle='-',markerfacecolor='red',label='ADR-OWA')
plt.plot(p, sub0Energy_MIN,'P',markersize=6,  color='orange',linewidth=1.5,
         linestyle='-',markerfacecolor='orange',label='ADR-MIN')
plt.legend(prop={'family': 'Times New Roman'})
plt.xlabel(r"$\sigma$",**title_font)
plt.ylabel("Energy Consumption (mJ)",**title_font)
plt.show()
"""


plt.plot(p, sub0Delevry_AVG,'s',markersize=6, color='blue', linewidth=1.5,
         markerfacecolor='blue',linestyle='-',label='ADR-AVG[17]')
plt.plot(p, sub0Delevry_MAX,'o',markersize=6, color='green',linewidth=1.5,
         linestyle='-',markerfacecolor='green',label='ADR-MAX[8]')
plt.plot(p, sub0Delevry_NoADR,'^',markersize=6, color='black',linewidth=1.5,
         linestyle='-',markerfacecolor='black',label='ADR-NoADR')
plt.plot(p, sub0Delevry_PES,'x',markersize=6,  color='red',linewidth=1.5,
         linestyle='-',markerfacecolor='red',label='ADR-OWA')
plt.plot(p, sub0Delevry_MIN,'P',markersize=6,  color='orange',linewidth=1.5,
         linestyle='-',markerfacecolor='orange',label='ADR-MIN')
plt.legend(prop={'family': 'Times New Roman'})
plt.xlabel(r"$\sigma$",**title_font)
plt.ylabel("Packet Delivery Ratio(%)",**title_font)
plt.show()

