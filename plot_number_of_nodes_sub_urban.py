import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# ------ E:\daneshgah\arshad\ostad-rahnama\simulate LoRa\PES\sub-urban

# 0
sub0Delevry_PES = [0.6021875639913224, 0.5974919251472112, 0.5833417007658959, 0.5755964797313513, 0.565929600918642,
                   0.5531268308769751, 0.5425365435676928]
sub0DelevryDeviation_PES = [0.0333071696536, 0.0189531893303, 0.0167846965006, 0.0134242274087, 0.0121355751537,
                            0.0143161163154, 0.0116345523418]
sub0Energy_PES = [0.230434987050303, 0.23292349826794204, 0.2439448449669439, 0.24768312975675205, 0.2555891974241784,
                  0.264749724522885, 0.27238664917937255]
sub0EnergyDeviation_PES = [0.0180827982286, 0.011892722314, 0.013188433061, 0.00991341067823, 0.00901274864705,
                           0.0117310226957, 0.0100496735337]
sub0Delevry_PES = np.array(sub0Delevry_PES)* 100
sub0DelevryDeviation_PES = np.array(sub0DelevryDeviation_PES)* 100
sub0Energy_PES = np.array(sub0Energy_PES)* 1000
sub0EnergyDeviation_PES = np.array(sub0EnergyDeviation_PES) * 100


# 3
sub3Delevry_PES = [0.6831513129456683, 0.6663690242605893, 0.6515038883863414, 0.6332918376715259, 0.6210900829815399,
                   0.5981448156435387, 0.5817618417753962]
sub3DelevryDeviation_PES = [0.0109031638267, 0.00758575391513, 0.0088876906691, 0.00703809709208, 0.00614001196364,
                     0.00768193408085, 0.00936646538135]
sub3Energy_PES = [0.21116658714799014, 0.21956484252995834, 0.2288011474994685, 0.2324971732955858, 0.24952627202393635,
                  0.266043706659513, 0.2769775579335892]
sub3EnergyDeviation_PES = [0.0108892645399, 0.00976011207514, 0.00861817979717, 0.0445097331357, 0.00604960594383,
                           0.00703211311195, 0.00876864864479]
sub3Delevry_PES = np.array(sub3Delevry_PES)* 100
sub3DelevryDeviation_PES = np.array(sub3DelevryDeviation_PES)* 100
sub3Energy_PES = np.array(sub3Energy_PES)* 1020
sub3EnergyDeviation_PES = np.array(sub3EnergyDeviation_PES)* 100

# 7
sub7Delevry_PES = [0.6116527809375375, 0.6022191123818441, 0.5907800840891096, 0.5750684971357852, 0.5604445211101383,
                    0.5450623269648653, 0.5263585078713717]
sub7DelevryDeviation_PES = [0.00643311521492, 0.00826376747, 0.00695801787075, 0.00601287537893, 0.00648137238964,
                             0.00732955560088, 0.00673750422503]
sub7Energy_PES = [0.24017061477086593, 0.2511708074674191, 0.2655528060224902, 0.28284791169093787, 0.29994475106684554,
                  0.3129692496343647, 0.33154834141321593]
sub7EnergyDeviation_PES = [0.0136372798501, 0.00748483593091, 0.00914710587021, 0.00772623691832, 0.00848513609507,
                           0.00990827809841, 0.00941028148552]
sub7Delevry_PES = np.array(sub7Delevry_PES)* 100
sub7DelevryDeviation_PES = np.array(sub7DelevryDeviation_PES)* 100
sub7Energy_PES = np.array(sub7Energy_PES)* 1000
sub7EnergyDeviation_PES = np.array(sub7EnergyDeviation_PES)* 100

# ------E:\daneshgah\arshad\ostad-rahnama\simulate LoRa\MAX\sub-urban

# 0
sub0Delevry_MAX = [0.6021853384678446, 0.5975814624621542, 0.5832415011219939, 0.5756410172989904, 0.5662183430841551,
                   0.5524685526901238, 0.5425752118989354]
sub0Energy_MAX  = [0.23041970436548737, 0.23286945767168413, 0.24398548174973098, 0.2476715412311038,
                            0.255275605152106, 0.2652650303477112, 0.2722848884716277]
sub0DelevryDeviation_MAX= [0.0333033277758, 0.0190079544505, 0.0167208859265, 0.0134251478681, 0.0120133805999, 0.0142267852483,
                  0.0114956105174]
sub0EnergyDeviation_MAX = [0.0180844060235, 0.011858971163, 0.0130995197924, 0.00992979270853, 0.0089545420697,
                           0.0115347125229, 0.00997113440336]

sub0Delevry_MAX = np.array(sub0Delevry_MAX)* 102
sub0DelevryDeviation_MAX = np.array(sub0DelevryDeviation_MAX)* 100
sub0Energy_MAX = np.array(sub0Energy_MAX)* 1000
sub0EnergyDeviation_MAX = np.array(sub0EnergyDeviation_MAX)* 100


# 3
sub3Delevry_MAX = [0.1894900625682999, 0.19592658787078315, 0.1963976319764172, 0.1984755529873867, 0.20069998808743306,
                   0.20234928205697303, 0.2048936458109655]
sub3Energy_MAX= [0.49936143842776143, 0.4912755899616133, 0.4954725240353494, 0.5015044661886989,
                            0.4995766707874381, 0.5085290070716242, 0.5094227535699108]
sub3DelevryDeviation_MAX  = [0.0102098320507, 0.0079750836517, 0.0053834245716, 0.00445126651524, 0.00386829682407,
                  0.00402303550984, 0.00438656584191]
sub3EnergyDeviation_MAX = [0.0331449450382, 0.0251633343321, 0.0173681198919, 0.0139761387239, 0.0135521009662,
                           0.0145298650193, 0.015333207196]
sub3Delevry_MAX = np.array(sub3Delevry_MAX)* 100
sub3DelevryDeviation_MAX = np.array(sub3DelevryDeviation_MAX)* 100
sub3Energy_MAX = np.array(sub3Energy_MAX)* 1000
sub3EnergyDeviation_MAX = np.array(sub3EnergyDeviation_MAX)* 100

# 7
sub7Delevry_MAX = [0.12928114095067814, 0.12932162274245693, 0.1298621501714176, 0.1312160035520545,
                   0.13225321191608877, 0.13593435946827834, 0.1375763824949446]
sub7Energy_MAX= [0.6217278240236085, 0.6265042638018163, 0.6308945775767316, 0.6324806179599628,
                            0.6349745375150203, 0.6264886458903466, 0.6281674491564322]
sub7DelevryDeviation_MAX  = [0.00939177924193, 0.00876724348664, 0.00531323115818, 0.00434213829964, 0.00431504239118,
                  0.00475588670519, 0.00331120616408]
sub7EnergyDeviation_MAX = [0.0486404711861, 0.0451901230895, 0.0299646168073, 0.0219086390021, 0.023135038602,
                           0.0245166198712, 0.0174811899153]
sub7Delevry_MAX = np.array(sub7Delevry_MAX)* 100
sub7DelevryDeviation_MAX = np.array(sub7DelevryDeviation_MAX)* 100
sub7Energy_MAX = np.array(sub7Energy_MAX)* 1000
sub7EnergyDeviation_MAX = np.array(sub7EnergyDeviation_MAX)* 100


# MIN just 7
sub7Delevry_MIN = [0.71091215694986889, 0.70591215694986889, 0.6991412789578549, 0.6836309453666956, 0.67808279134317704,
                   0.66606465872800644, 0.65355245003850559]
sub7Energy_MIN = [0.2344185465736384,0.2393084856321939,0.2458780343509885,0.25542366189786251,
                  0.26160536617791674, 0.26939592069161047 , 0.27355104190009708]
sub7DelevryDeviation_MIN = [0.0317168003656, 0.0261626353823, 0.0152758144938, 0.0124287414801, 0.0107247179515,
                            0.0114634572378, 0.0116240074174, 0.0112181993397, 0.0082143939008]
sub7EnergyDeviation_MIN = [0.0181552687761, 0.0121221627282, 0.00907799485973, 0.0188097471633, 0.0259587285684,
                           0.044878223915, 0.0541779424747, 0.0536888738204, 0.0450312953167]
sub7Delevry_MIN = np.array(sub7Delevry_MIN)
sub7DelevryDeviation_MIN = np.array(sub7DelevryDeviation_MIN)
sub7Delevry_MIN = sub7Delevry_MIN * 100
sub7DelevryDeviation_MIN = sub7DelevryDeviation_MIN * 100

sub7Energy_MIN = np.array(sub7Energy_MIN)
sub7EnergyDeviation_MIN = np.array(sub7EnergyDeviation_MIN)
sub7Energy_MIN = sub7Energy_MIN * 1000
sub0EnergyDeviation_MIN = sub7EnergyDeviation_MIN * 100

# ------E:\daneshgah\arshad\ostad-rahnama\simulate LoRa\AVG\sub-urban

# 0
sub0Delevry_AVG = [0.6021782823596078, 0.5976542177870048, 0.583399598857316, 0.5755277283794717, 0.5655633829763632,
                   0.5523159378830766, 0.5424951102654092]
sub0Energy_AVG = [0.23043529195284862, 0.23285928589843008, 0.24382191253370372, 0.24773928009087026,
                            0.24712268115916572, 0.2653829753663827, 0.27233608005512017]
sub0DelevryDeviation_AVG  = [0.0333035716861, 0.0189780208701, 0.0167078938939, 0.013444030384, 0.0118166641923, 0.0141017155559,
                  0.0117139087323]
sub0EnergyDeviation_AVG = [0.0180824494392, 0.0119018749141, 0.0130169929418, 0.00996843303558, 0.0474937940911,
                           0.0115153548361, 0.0101009724621]
sub0Delevry_AVG = np.array(sub0Delevry_AVG)* 98
sub0DelevryDeviation_AVG = np.array(sub0DelevryDeviation_AVG)* 100
sub0Energy_AVG = np.array(sub0Energy_AVG)* 970
sub0EnergyDeviation_AVG = np.array(sub0EnergyDeviation_AVG)* 100

# 3
sub3Delevry_AVG = [0.62905665893431, 0.6191559209979346, 0.6089992810192542, 0.5949807312949656, 0.5878730027253831,
                   0.5708456590451855, 0.5578936745651563]
sub3Energy_AVG = [0.18237547437076218, 0.1888303625359364, 0.19632511896109855, 0.20578282220166944,
                            0.2117016177413091, 0.22473795940649588, 0.23435512298025046]
sub3DelevryDeviation_AVG  = [0.00903058894451, 0.00596969297455, 0.00658344146617, 0.00554776185871, 0.00517295157536,
                  0.00663234846349, 0.00706536851009]
sub3EnergyDeviation_AVG = [0.00681135700403, 0.00515878156734, 0.00592527323837, 0.00525485230807, 0.00492239972371,
                           0.00565655997545, 0.00644242670738]
sub3Delevry_AVG = np.array(sub3Delevry_AVG)* 100
sub3DelevryDeviation_AVG = np.array(sub3DelevryDeviation_AVG)* 100
sub3Energy_AVG = np.array(sub3Energy_AVG)* 1000
sub3EnergyDeviation_AVG = np.array(sub3EnergyDeviation_AVG)* 100

# 7
sub7Delevry_AVG = [0.36493680618603574, 0.3627910853961495, 0.3615862017437202, 0.3601532389217598, 0.35909197810005405,
                   0.35788445094455573, 0.35634167262538924]
sub7Energy_AVG = [0.26970832188265415, 0.2748126847620433, 0.2846003974573183, 0.29370897866528783,
                            0.300906300989471, 0.3065998902287148, 0.31579665450714955]
sub7DelevryDeviation_AVG  = [0.00824422352846, 0.00545080608919, 0.00426435356793, 0.00343574468124, 0.00393501791967,
                  0.00357854117145, 0.00246645341042]
sub7EnergyDeviation_AVG = [0.0114253663767, 0.00755235313295, 0.00623057010109, 0.00573202589063, 0.00663528915042,
                           0.00635871276276, 0.00571882964934]
sub7Delevry_AVG = np.array(sub7Delevry_AVG)* 100
sub7DelevryDeviation_AVG = np.array(sub7DelevryDeviation_AVG)* 100

sub7Energy_AVG = np.array(sub7Energy_AVG)* 1000
sub7EnergyDeviation_AVG = np.array(sub7EnergyDeviation_AVG)* 100
# ------E:\daneshgah\arshad\ostad-rahnama\simulate LoRa\NoADR\sub-urban


# 0
sub0Delevry_NoADR = [0.3733257211995366, 0.37173306479385637, 0.3610484944043886, 0.3621098640244838,
                     0.3536983480586016, 0.3502402228071165, 0.3449969385634565]
sub0Energy_NoADR = [0.3226683566235749, 0.3275540909320138, 0.3431420357262853, 0.3440167857611814,
                              0.35546850966009974, 0.36176209143475935, 0.36667355820788805]
sub0DelevryDeviation_NoADR  = [0.0395491908448, 0.0291423952452, 0.0220272037455, 0.0170625626973, 0.0181834049634,
                    0.0169073028998, 0.0127690992864]
sub0EnergyDeviation_NoADR = [0.0299769808548, 0.0220926596175, 0.020792999811, 0.0133976782364, 0.0151400946731,
                             0.0163356921024, 0.0129893083437]
sub0Delevry_NoADR = np.array(sub0Delevry_NoADR)* 100
sub0DelevryDeviation_NoADR = np.array(sub0DelevryDeviation_NoADR)* 100
sub0Energy_NoADR = np.array(sub0Energy_NoADR)* 1000
sub0EnergyDeviation_NoADR = np.array(sub0EnergyDeviation_NoADR)* 100

# 3
sub3Delevry_NoADR = [0.37616380235909147, 0.37819735368744906, 0.37448078279890823, 0.3641055447850453,
                     0.3664955464893336, 0.3559099696639621, 0.3502415733350159]
sub3Energy_NoADR = [0.32211128928423854, 0.32155784424193357, 0.3304779611395271, 0.34148172404614446,
                              0.3426754461166622, 0.3548704777309123, 0.36024273977595833]
sub3DelevryDeviation_NoADR  = [0.0342992171271, 0.0214242007783, 0.011073820335, 0.0130510460553, 0.0129574568821, 0.0116495744418,
                    0.0129548849059]
sub3EnergyDeviation_NoADR = [0.0245782408908, 0.0189124498104, 0.0103373526141, 0.00956711972224, 0.0118798614369,
                             0.010670270773, 0.0115534936469]
sub3Delevry_NoADR = np.array(sub3Delevry_NoADR)* 100
sub3DelevryDeviation_NoADR = np.array(sub3DelevryDeviation_NoADR)* 100
sub3Energy_NoADR = np.array(sub3Energy_NoADR)* 1000
sub3EnergyDeviation_NoADR = np.array(sub3EnergyDeviation_NoADR)* 100

# 7
sub7Delevry_NoADR = [0.38625962556506294, 0.3882345413068965, 0.3811087248503382, 0.3764368510097259,
                     0.37572792242934017, 0.3732813674218506, 0.37108518997339235]
sub7Energy_NoADR= [0.3085467943348148, 0.313191380477793, 0.32154640017440234, 0.3299834949119797,
                              0.3352781627151601, 0.3394240159814206, 0.3424396246821247]
sub7DelevryDeviation_NoADR  = [0.0218573206671, 0.0166448739374, 0.0158432367311, 0.0107627071098, 0.0100782781475,
                    0.0109641892932, 0.00744680780483]
sub7EnergyDeviation_NoADR = [0.0178425323499, 0.0132905237395, 0.0113761414318, 0.00746600870163, 0.00889071766908,
                             0.00856377965519, 0.007201012658]
sub7Delevry_NoADR = np.array(sub7Delevry_NoADR)* 100
sub7DelevryDeviation_NoADR = np.array(sub7DelevryDeviation_NoADR)* 100
sub7Energy_NoADR = np.array(sub7Energy_NoADR)* 1000
sub7EnergyDeviation_NoADR = np.array(sub7EnergyDeviation_NoADR)* 100


title_font = {'fontname':'Times New Roman', 'size':'16', 'color':'black', 'weight':'normal'}
number = {'fontname':'Times New Roman', 'size':'13', 'color':'black', 'weight':'normal'}
p = [100, 200, 300, 400, 500, 600, 700]
ax = plt.axes()
ax.grid(alpha=0.7, linestyle=':')
plt.xticks(p,**number)
plt.yticks(**number)

"""
plt.plot(p, sub7Energy_AVG,'s',markersize=6, color='blue', linewidth=1.5,
         markerfacecolor='blue',linestyle='-',label='ADR-AVG[17]')
plt.plot(p, sub7Energy_MAX,'o',markersize=6, color='green',linewidth=1.5,
         linestyle='-',markerfacecolor='green',label='ADR-MAX[8]')
plt.plot(p, sub7Energy_NoADR,'^',markersize=6, color='black',linewidth=1.5,
         linestyle='-',markerfacecolor='black',label='ADR-NoADR')
plt.plot(p, sub7Energy_PES,'x',markersize=6,  color='red',linewidth=1.5,
         linestyle='-',markerfacecolor='red',label='ADR-OWA')
plt.plot(p, sub7Energy_MIN,'P',markersize=6,  color='orange',linewidth=1.5,
         linestyle='-',markerfacecolor='orange',label='ADR-MIN')

plt.legend(prop={'family': 'Times New Roman'})
plt.xlabel("Number of nodes",**title_font)
plt.ylabel("Energy Consumption (mJ)",**title_font)
plt.show()
"""


plt.plot(p, sub7Delevry_AVG,'s',markersize=6, color='blue', linewidth=1.5,
         markerfacecolor='blue',linestyle='-',label='ADR-AVG[17]')
plt.plot(p, sub7Delevry_MAX,'o',markersize=6, color='green',linewidth=1.5,
         linestyle='-',markerfacecolor='green',label='ADR-MAX[8]')
plt.plot(p, sub7Delevry_NoADR,'^',markersize=6, color='black',linewidth=1.5,
         linestyle='-',markerfacecolor='black',label='ADR-NoADR')
plt.plot(p, sub7Delevry_PES,'x',markersize=6,  color='red',linewidth=1.5,
         linestyle='-',markerfacecolor='red',label='ADR-OWA')
plt.plot(p, sub7Delevry_MIN,'P',markersize=6,  color='orange',linewidth=1.5,
         linestyle='-',markerfacecolor='orange',label='ADR-MIN')

plt.legend(prop={'family': 'Times New Roman'})
plt.xlabel("Number of nodes",**title_font)
plt.ylabel("Packet Delivery Ratio(%)",**title_font)
plt.show()
