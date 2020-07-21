import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# ------E:\daneshgah\arshad\ostad-rahnama\simulate LoRa\all\0\0.8\1.7\2.6\3.5\4.4\5.3\6.2\7.9

# AVG
sub0Delevry_AVG = [0.6021796313431198, 0.6463738287150689, 0.6688375215117578, 0.6772030314439319, 0.6450440201561758,
                   0.5954790800461313, 0.5278405090253518, 0.4615638865879994, 0.35740263571677655]
sub0Energy_AVG = [0.23042317267391693, 0.2050509459270121, 0.18902222445773173, 0.1782234476703362, 0.18132300989610856,
                  0.18751540131225086, 0.20656633449502854, 0.22528468299880344, 0.27333948912213213]
sub0DelevryDeviation_AVG = [0.0333004394297, 0.0205468116773, 0.0173327511955, 0.0171977655572, 0.012977106342,
                            0.00679654601966, 0.00669800730158, 0.00617752136739, 0.0072538237746]
sub0EnergyDeviation_AVG = [0.0180818153071, 0.0113464244069, 0.00984679616258, 0.00956605721669, 0.00877472953543,
                           0.00592463276346, 0.00870613253348, 0.00669718546599, 0.0118759016224]
sub0Delevry_AVG = np.array(sub0Delevry_AVG)
sub0DelevryDeviation_AVG = np.array(sub0DelevryDeviation_AVG)
sub0Delevry_AVG = sub0Delevry_AVG * 100
sub0DelevryDeviation_AVG = sub0DelevryDeviation_AVG * 100

sub0Energy_AVG = np.array(sub0Energy_AVG)
sub0EnergyDeviation_AVG = np.array(sub0EnergyDeviation_AVG)
sub0Energy_AVG = sub0Energy_AVG * 1000
sub0EnergyDeviation_AVG = sub0EnergyDeviation_AVG * 100

# MAX
sub0Delevry_MAX = [0.6076926754179688, 0.65024126326329, 0.5391412789578549, 0.3336309453666956, 0.21808279134317704,
                   0.16606465872800644, 0.14355245003850559, 0.12968619510850488, 0.12491215694986889]
sub0Energy_MAX = [0.22781528129188977, 0.18213065091802483, 0.18955104190009708, 0.29739592069161047,
                  0.44260536617791674, 0.5542366189786251, 0.6038780343509885, 0.6443084856321939, 0.6444185465736384]
sub0DelevryDeviation_MAX = [0.0317168003656, 0.0261626353823, 0.0152758144938, 0.0124287414801, 0.0107247179515,
                            0.0114634572378, 0.0116240074174, 0.0112181993397, 0.0082143939008]
sub0EnergyDeviation_MAX = [0.0181552687761, 0.0121221627282, 0.00907799485973, 0.0188097471633, 0.0259587285684,
                           0.044878223915, 0.0541779424747, 0.0536888738204, 0.0450312953167]
sub0Delevry_MAX = np.array(sub0Delevry_MAX)
sub0DelevryDeviation_MAX = np.array(sub0DelevryDeviation_MAX)
sub0Delevry_MAX = sub0Delevry_MAX * 100
sub0DelevryDeviation_MAX = sub0DelevryDeviation_MAX * 100

sub0Energy_MAX = np.array(sub0Energy_MAX)
sub0EnergyDeviation_MAX = np.array(sub0EnergyDeviation_MAX)
sub0Energy_MAX = sub0Energy_MAX * 1000
sub0EnergyDeviation_MAX = sub0EnergyDeviation_MAX * 100

# MIN
sub0Delevry_MIN = [0.2776926754179688, 0.45024126326329, 0.5891412789578549, 0.6336309453666956, 0.66808279134317704,
                   0.68606465872800644, 0.69355245003850559, 0.70168619510850488, 0.71091215694986889]
sub0Energy_MIN = [0.6444185465736384,0.5443084856321939,0.4038780343509885,0.3042366189786251,
                  0.25260536617791674, 0.20739592069161047 , 0.18955104190009708 ,0.19213065091802483 ,0.22781528129188977 ]
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
sub0Delevry_NoADR = [0.3733257211995366, 0.37345993470674965, 0.363524044731205, 0.37976274941359106,
                     0.37436474846412315, 0.3802145588650098, 0.3734111876300881, 0.3824006138305301,
                     0.39063034039433936]
sub0Energy_NoADR = [0.3226683566235749, 0.32342316050232256, 0.3336440779046755, 0.32006352389470166,
                    0.3251448623125777, 0.31855749758621965, 0.31795125217362435, 0.316167643058894, 0.3090387777700097]
sub0DelevryDeviation_NoADR = [0.0395491908448, 0.0382094441243, 0.0362127044626, 0.0284433875579, 0.0346399498169,
                              0.0390397521533, 0.024788558389, 0.0283341427474, 0.0190256221455]
sub0EnergyDeviation_NoADR = [0.0299769808548, 0.0275849993249, 0.032735788927, 0.0186376920453, 0.0281258236703,
                             0.027671522733, 0.0199235482021, 0.0203156929275, 0.0140395611298]
sub0Delevry_NoADR = np.array(sub0Delevry_NoADR)
sub0DelevryDeviation_NoADR = np.array(sub0DelevryDeviation_NoADR)
sub0Delevry_NoADR = sub0Delevry_NoADR * 100
sub0DelevryDeviation_NoADR = sub0DelevryDeviation_NoADR * 100

sub0Energy_NoADR = np.array(sub0Energy_NoADR)
sub0EnergyDeviation_NoADR = np.array(sub0EnergyDeviation_NoADR)
sub0Energy_NoADR = sub0Energy_NoADR * 1000
sub0EnergyDeviation_NoADR = sub0EnergyDeviation_NoADR * 100

# PES
sub0Delevry_PES = [0.6034135854781947, 0.6497624815622896, 0.6769873521948477, 0.6904818406323129, 0.6856446027900268,
                   0.6706850224728, 0.6586590435763136, 0.6416327967528266, 0.6088097179709769]
sub0Energy_PES = [0.23102145115006698, 0.21011907750484615, 0.2028283764794982, 0.20494555887082536, 0.2074130844760642,
                  0.21437607593237404, 0.21959537197846238, 0.22650847853151837, 0.24450965017998896]
sub0DelevryDeviation_PES = [0.0357071284569, 0.0272397199981, 0.0182036002905, 0.0172385531115, 0.0100443663801,
                            0.0103940307316, 0.0139351949772, 0.00934644465033, 0.0101580080545]
sub0EnergyDeviation_PES = [0.0227678447103, 0.0150557926521, 0.0105932472859, 0.0136529011359, 0.0107557554972,
                           0.00883672215104, 0.0093229324261, 0.0105049071828, 0.0135627471178]
sub0Delevry_PES = np.array(sub0Delevry_PES)
sub0DelevryDeviation_PES = np.array(sub0DelevryDeviation_PES)
sub0Delevry_PES = sub0Delevry_PES * 100
sub0DelevryDeviation_PES = sub0DelevryDeviation_PES * 100

sub0Energy_PES = np.array(sub0Energy_PES)
sub0EnergyDeviation_PES = np.array(sub0EnergyDeviation_PES)
sub0Energy_PES = sub0Energy_PES * 1000
sub0EnergyDeviation_PES = sub0EnergyDeviation_PES * 100

p = [0.00,0.89, 1.78, 2.67, 3.56, 4.46, 5.35,6.24,7.13]
title_font = {'fontname':'Times New Roman', 'size':'16', 'color':'black', 'weight':'normal'}
number = {'fontname':'Times New Roman', 'size':'13', 'color':'black', 'weight':'normal'}
ax = plt.axes()
ax.grid(alpha=0.7, linestyle=':')
plt.xticks(p,**number)
plt.yticks(**number)


plt.plot(p, sub0Delevry_AVG,'s',markersize=6, color='blue', linewidth=1.5,
         markerfacecolor='blue',linestyle='-',label='ADR-AVG[13]')
plt.plot(p, sub0Delevry_MAX,'o',markersize=6, color='green',linewidth=1.5,
         linestyle='-',markerfacecolor='green',label='ADR-MAX[9]')
plt.plot(p, sub0Delevry_NoADR,'^',markersize=6, color='black',linewidth=1.5,
         linestyle='-',markerfacecolor='black',label='ADR-NoADR')
plt.plot(p, sub0Delevry_PES,'x',markersize=6,  color='red',linewidth=1.5,
         linestyle='-',markerfacecolor='red',label='ADR-OWA')
plt.legend(prop={'family': 'Times New Roman'})
plt.xlabel(r"$\sigma$",**title_font)
plt.ylabel("Packet Delivery Ratio(%)",**title_font)
plt.show()




