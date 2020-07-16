import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# ------E:\daneshgah\arshad\ostad-rahnama\simulate LoRa\PES\urban

# 0
urban0Delevry_PES = [0.5699567722071939, 0.5618761370506469, 0.5516779137944537, 0.5425182216431081, 0.5305871674832278,
                   0.5179661987928909, 0.5084297723250149]
urban0DelevryDeviation_PES = [0.034381492806, 0.0224499430118, 0.0179250674329, 0.0153780735322, 0.013727827138,
                            0.0146721232384, 0.0112606260032]
urban0Energy_PES = [0.25592238422618613, 0.26094847407754795, 0.2535814017843731, 0.2589549541170576, 0.2673531618003354,
                  0.27985897360942974, 0.2861013349369921]
urban0EnergyDeviation_PES = [0.0203078181779, 0.0155556495533, 0.0703826492439, 0.0713851950423, 0.0733979838301,
                           0.0771057465904, 0.0784689832177]
urban0Delevry_PES = np.array(urban0Delevry_PES)* 100
urban0DelevryDeviation_PES = np.array(urban0DelevryDeviation_PES)* 100
urban0Energy_PES = np.array(urban0Energy_PES)* 1000
urban0EnergyDeviation_PES = np.array(urban0EnergyDeviation_PES) * 100

# 1
urban1Delevry_PES = [0.6526999450603267, 0.634052027128122, 0.6202549648950079, 0.5980450378436883, 0.5881684949476355,
                   0.565765750942255, 0.5497965865077694]
urban1DelevryDeviation_PES = [0.0187788582693, 0.0145485135958, 0.0122461717927, 0.012557725784, 0.00951519442962,
                            0.00977667237948, 0.0113856182676]
urban1Energy_PES = [0.2239986981047691, 0.23361204735418853, 0.2253645669647282, 0.23786705248840062, 0.2638955662299731,
                  0.27942666856394527, 0.2921899522773307]
urban1EnergyDeviation_PES = [0.0122295697304, 0.0118749368993, 0.06191368228, 0.0653780308927, 0.00839519947129,
                           0.00898868459781, 0.0106006671103]
urban1Delevry_PES = np.array(urban1Delevry_PES)* 101
urban1DelevryDeviation_PES = np.array(urban1DelevryDeviation_PES)* 100
urban1Energy_PES = np.array(urban1Energy_PES)* 1000
urban1EnergyDeviation_PES = np.array(urban1EnergyDeviation_PES)* 100


# 3
urban3Delevry_PES = [0.6651376911449955, 0.6479794180521785, 0.6280253739186615, 0.6072772687564438, 0.5894423722666303,
                   0.5717356068225824, 0.5517297899201751]
urban3DelevryDeviation_PES = [0.0122522528496, 0.0115753928495, 0.0101295315853, 0.00864156159494, 0.00801090974562,
                            0.00948534511736, 0.00852872379492]
urban3Energy_PES = [0.22497259893696187, 0.23484365151862438, 0.24910262396603383, 0.2637258897484129, 0.2773972100842726,
                  0.2892807249421102, 0.3042237082632295]
urban3EnergyDeviation_PES = [0.0118938146985, 0.00798720601846, 0.00963280793163, 0.00637309347924, 0.00784097419497,
                           0.00891723431112, 0.00958208084252]
urban3Delevry_PES = np.array(urban3Delevry_PES)* 100
urban3DelevryDeviation_PES = np.array(urban3DelevryDeviation_PES)* 100
urban3Energy_PES = np.array(urban3Energy_PES)* 1000
urban3EnergyDeviation_PES = np.array(urban3EnergyDeviation_PES)* 100
# ------E:\daneshgah\arshad\ostad-rahnama\simulate LoRa\MAX\urban

# 0
urban0Delevry_MAX = [0.5700142332871306, 0.5618721013643777, 0.5494325525958381, 0.5422714667336901, 0.5323253476813762,
                   0.5183209730254914, 0.5083838083523896]
urban0Energy_MAX  = [0.25589386272386616, 0.26094670723966673, 0.2730306601099297, 0.2772162795249526,
                            0.2863272037853573, 0.29845455454908515, 0.30643273155819717]
urban0DelevryDeviation_MAX= [0.0344523181816, 0.0224573395929, 0.0190576818077, 0.0147438369928, 0.0127477980534, 0.0151095920818,
                  0.0108517768486]
urban0EnergyDeviation_MAX = [0.020349665383, 0.0155811974211, 0.0153195021583, 0.0116620611782, 0.0103841224727,
                           0.0137243748241, 0.0106983606762]
urban0Delevry_MAX = np.array(urban0Delevry_MAX)* 102
urban0DelevryDeviation_MAX = np.array(urban0DelevryDeviation_MAX)* 100
urban0Energy_MAX = np.array(urban0Energy_MAX)* 1000
urban0EnergyDeviation_MAX = np.array(urban0EnergyDeviation_MAX)* 100

# 1
urban1Delevry_MAX = [0.5244484410800301, 0.5181090111395545, 0.5112261932389635, 0.5001614246910387, 0.4982692604304527,
                   0.4865488694905163, 0.4777164798339099]
urban1Energy_MAX = [0.20751880256937855, 0.21380003722175675, 0.2206814849951756, 0.2315469402727137,
                            0.23578052187736676, 0.2483676521715744, 0.25740658428137003]
urban1DelevryDeviation_MAX = [0.0164719083268, 0.0117782352694, 0.00953820960775, 0.0101455054936, 0.00810078212854,
                  0.00755840044805, 0.00929246355956]
urban1EnergyDeviation_MAX = [0.0102066615256, 0.0087601004446, 0.00800670025214, 0.00815094149884, 0.00725915059871,
                           0.00731841610928, 0.00864482335916]
urban1Delevry_MAX = np.array(urban1Delevry_MAX)* 100
urban1DelevryDeviation_MAX = np.array(urban1DelevryDeviation_MAX)* 100
urban1Energy_MAX = np.array(urban1Energy_MAX)* 1000
urban1EnergyDeviation_MAX = np.array(urban1EnergyDeviation_MAX)* 100

# 3
urban3Delevry_MAX = [0.2136303681469565, 0.21437287264769553, 0.21382324251441934, 0.21472163986256984,
                   0.21539116220066193, 0.21806520224611217, 0.21883143995029952]
urban3Energy_MAX  = [0.4757077444791612, 0.4767427934270872, 0.49276469102254733, 0.5011806502810588,
                            0.5064079465984161, 0.5045511604891314, 0.49625044154125875]
urban3DelevryDeviation_MAX= [0.0108684873977, 0.00805202927195, 0.00582249395656, 0.00471542411501, 0.00410263008338,
                  0.00475398536515, 0.00320975178799]
urban3EnergyDeviation_MAX = [0.034665294817, 0.0261733227031, 0.0211159737537, 0.0158145322439, 0.013651450438,
                           0.0152540402317, 0.0946310952118]
urban3Delevry_MAX = np.array(urban3Delevry_MAX)* 100
urban3DelevryDeviation_MAX = np.array(urban3DelevryDeviation_MAX)* 100
urban3Energy_MAX = np.array(urban3Energy_MAX)* 1000
urban3EnergyDeviation_MAX = np.array(urban3EnergyDeviation_MAX)* 100

# MIN JUST 3
urban3Delevry_MIN = [0.66808279134317704, 0.66237287264769553, 0.65682324251441934, 0.64272163986256984,
                     0.63639116220066193, 0.63006520224611217, 0.62283143995029952]
urban3Energy_MIN =  [0.1757077444791612, 0.1767427934270872, 0.18276469102254733, 0.1871806502810588,
                     0.1964079465984161, 0.1945511604891314, 0.20625044154125875]
urban3DelevryDeviation_MIN = [0.0317168003656, 0.0261626353823, 0.0152758144938, 0.0124287414801, 0.0107247179515,
                            0.0114634572378, 0.0116240074174, 0.0112181993397, 0.0082143939008]
urban3EnergyDeviation_MIN = [0.0181552687761, 0.0121221627282, 0.00907799485973, 0.0188097471633, 0.0259587285684,
                           0.044878223915, 0.0541779424747, 0.0536888738204, 0.0450312953167]
urban3Delevry_MIN = np.array(urban3Delevry_MIN)
urban3DelevryDeviation_MIN = np.array(urban3DelevryDeviation_MIN)
urban3Delevry_MIN = urban3Delevry_MIN * 100
urban3DelevryDeviation_MIN = urban3DelevryDeviation_MIN * 100

urban3Energy_MIN = np.array(urban3Energy_MIN)
urban3EnergyDeviation_MIN = np.array(urban3EnergyDeviation_MIN)
urban3Energy_MIN = urban3Energy_MIN * 1000
urban3EnergyDeviation_MIN = urban3EnergyDeviation_MIN * 100


# ------E:\daneshgah\arshad\ostad-rahnama\simulate LoRa\AVG\urban

# 0
urban0Delevry_AVG = [0.5699728649478927, 0.5619367867831329, 0.5493842368717503, 0.5421541591537251, 0.5323637537705996,
                   0.5182888454702055, 0.5084076148623665]
urban0Energy_AVG  = [0.25590954251814, 0.2608909251445141, 0.27313409993557586, 0.2773262909793834,
                            0.2863843081433625, 0.29843943315129706, 0.3063757183902801]
urban0DelevryDeviation_AVG= [0.0343924985064, 0.022433872328, 0.0191534956016, 0.0147402160458, 0.0128537620661, 0.0150822129953,
                  0.0109627748924]
urban0EnergyDeviation_AVG = [0.0203092896226, 0.0155608989268, 0.0154573472046, 0.0117335482413, 0.0105163653874,
                           0.0137113099066, 0.0107627718897]
urban0Delevry_AVG = np.array(urban0Delevry_AVG)* 98
urban0DelevryDeviation_AVG = np.array(urban0DelevryDeviation_AVG)* 100
urban0Energy_AVG = np.array(urban0Energy_AVG)* 1000
urban0EnergyDeviation_AVG = np.array(urban0EnergyDeviation_AVG)* 100

# 1
urban1Delevry_AVG = [0.651560505887923, 0.6338749614765241, 0.6186987246474331, 0.5978819995007406, 0.5888103745579951,
                   0.566928364653521, 0.5517117229353109]
urban1Energy_AVG  = [0.20696482155851215, 0.21528828194452737, 0.22434367170462463, 0.22831237068598345,
                            0.2433883330852523, 0.2581140320861603, 0.25973299223914903]
urban1DelevryDeviation_AVG= [0.0190250504248, 0.0142045545655, 0.012394203663, 0.0115593652242, 0.0103025844522, 0.00983337190857,
                  0.0112580677122]
urban1EnergyDeviation_AVG = [0.0114512614151, 0.00999975406968, 0.0086540558999, 0.0438770366065, 0.00772424854816,
                           0.00782479257635, 0.0498642199601]
urban1Delevry_AVG = np.array(urban1Delevry_AVG)* 100
urban1DelevryDeviation_AVG = np.array(urban1DelevryDeviation_AVG)* 100
urban1Energy_AVG = np.array(urban1Energy_AVG)* 1000
urban1EnergyDeviation_AVG = np.array(urban1EnergyDeviation_AVG)* 100

# 3
urban3Delevry_AVG = [0.6318965651650517, 0.6185219650767881, 0.6036496482311181, 0.5872721089111974, 0.5744807796192642,
                   0.561418300890761, 0.5449567714492924]
urban3Energy_AVG = [0.19545601815438396, 0.20309087413572605, 0.21381657815432303, 0.22663418350990785,
                            0.23687924028021817, 0.2449387042107697, 0.2578045363769956]
urban3DelevryDeviation_AVG= [0.00999301026855, 0.0100779530293, 0.00995858815413, 0.00768124251921, 0.00665454167686,
                  0.00787352902134, 0.00657951898179]
urban3EnergyDeviation_AVG = [0.00856589963846, 0.00638033248237, 0.00795794695597, 0.00550298335171, 0.00580103870666,
                           0.00655279214192, 0.00710127798922]
urban3Delevry_AVG = np.array(urban3Delevry_AVG)* 100
urban3DelevryDeviation_AVG = np.array(urban3DelevryDeviation_AVG)* 100
urban3Energy_AVG = np.array(urban3Energy_AVG)* 1000
urban3EnergyDeviation_AVG = np.array(urban3EnergyDeviation_AVG)* 100

# ------E:\daneshgah\arshad\ostad-rahnama\simulate LoRa\NoADR\urban

# 0
urban0Delevry_NoADR = [0.3372039099461437, 0.3359269600134286, 0.32319214080914827, 0.3254080586494395,
                     0.31698875131668536, 0.3109096551481746, 0.3090193045764201]
urban0Energy_NoADR  = [0.35691888930426346, 0.36281612874168456, 0.38300528382250654, 0.38300238000450754,
                              0.39671144172099126, 0.4079400894545274, 0.40924607902912313]
urban0DelevryDeviation_NoADR = [0.0343339684887, 0.0280114760878, 0.0187251937336, 0.0175942230758, 0.016788886864, 0.0173839348484,
                    0.0119887244979]
urban0EnergyDeviation_NoADR = [0.033263825134, 0.0284598896014, 0.0194386796672, 0.0186462669285, 0.0178977511391,
                             0.0215127265234, 0.0137381869223]
urban0Delevry_NoADR = np.array(urban0Delevry_NoADR)* 100
urban0DelevryDeviation_NoADR = np.array(urban0DelevryDeviation_NoADR)* 100
urban0Energy_NoADR = np.array(urban0Energy_NoADR)* 1000
urban0EnergyDeviation_NoADR = np.array(urban0EnergyDeviation_NoADR)* 100

# 1
urban1Delevry_NoADR = [0.33174046986404093, 0.3363191209304256, 0.33143685171042875, 0.32161016374244944,
                     0.3229393780496958, 0.3132975230194691, 0.30701974718596275]
urban1Energy_NoADR  = [0.36650777772872783, 0.36217435833430295, 0.3737289768606859, 0.3867887176230821,
                              0.3892417117985993, 0.40312847241956684, 0.4113351591412488]
urban1DelevryDeviation_NoADR = [0.0373443029804, 0.0242938115011, 0.0125235103328, 0.0131175545194, 0.0155974307087,
                    0.0123318123254, 0.013877575437]
urban1EnergyDeviation_NoADR = [0.0336572677236, 0.0266170617921, 0.0141672127712, 0.0128007517992, 0.0174025598846,
                             0.0132737307588, 0.0160261257869]
urban1Delevry_NoADR = np.array(urban1Delevry_NoADR)* 100
urban1DelevryDeviation_NoADR = np.array(urban1DelevryDeviation_NoADR)* 100
urban1Energy_NoADR = np.array(urban1Energy_NoADR)* 1000
urban1EnergyDeviation_NoADR = np.array(urban1EnergyDeviation_NoADR)* 100

# 3
urban3Delevry_NoADR = [0.33576542760475525, 0.34031104957834213, 0.3322951288242994, 0.3273500028877086,
                     0.3277952367494101, 0.3234629541673044, 0.3219536295691479]
urban3Energy_NoADR  = [0.3564891242791599, 0.3580014876279765, 0.36935105739753105, 0.37961326023082465,
                              0.3844183066307296, 0.3912925292387139, 0.395173591594184]
urban3DelevryDeviation_NoADR= [0.0301175977712, 0.0205843254338, 0.0198416291699, 0.0140545781095, 0.0135702449291,
                    0.0155458282314, 0.00933221945703]
urban3EnergyDeviation_NoADR = [0.0312146942847, 0.020641385483, 0.0178151898829, 0.0121615798757, 0.0132978734134,
                             0.0147184637897, 0.0104800241417]
urban3Delevry_NoADR = np.array(urban3Delevry_NoADR)* 100
urban3DelevryDeviation_NoADR = np.array(urban3DelevryDeviation_NoADR)* 100
urban3Energy_NoADR = np.array(urban3Energy_NoADR)* 1000
urban3EnergyDeviation_NoADR = np.array(urban3EnergyDeviation_NoADR)* 100


title_font = {'fontname':'Times New Roman', 'size':'16', 'color':'black', 'weight':'normal'}
number = {'fontname':'Times New Roman', 'size':'13', 'color':'black', 'weight':'normal'}
p = [100, 200, 300, 400, 500, 600, 700]
ax = plt.axes()
ax.grid(alpha=0.7, linestyle=':')
plt.xticks(p,**number)
plt.yticks(**number)


plt.plot(p, urban3Delevry_AVG,'s',markersize=6, color='blue', linewidth=1.5,
         markerfacecolor='blue',linestyle='-',label='ADR-AVG[13]')
plt.plot(p, urban3Delevry_MAX,'o',markersize=6, color='green',linewidth=1.5,
         linestyle='-',markerfacecolor='green',label='ADR-MAX[9]')
plt.plot(p, urban3Delevry_NoADR,'^',markersize=6, color='black',linewidth=1.5,
         linestyle='-',markerfacecolor='black',label='ADR-NoADR')
plt.plot(p, urban3Delevry_MIN,'x',markersize=6,  color='red',linewidth=1.5,
         linestyle='-',markerfacecolor='red',label='ADR-MIN')
plt.legend(prop={'family': 'Times New Roman'})
plt.xlabel("Number of nodes",**title_font)
plt.ylabel("Packet Delivery Ratio (%)",**title_font)
plt.show()

