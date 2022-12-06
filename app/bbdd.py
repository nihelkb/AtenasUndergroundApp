from parada import *

#LINEA 1

p101 = parada(101, "Piraeus", 37.94811629457029, 23.643279368625524, (645,749), (-386.0, -300.0), "#a0fb0e")
p102 = parada(102, "Faliro", 37.94499013986155, 23.66522449702415, (734, 747), (-294.0, -299.0) , "#a0fb0e")   # Draw distinto
p103 = parada(103, "Moschato", 37.95505354378356, 23.67966282816376,(777,712), (-253.0, -261.0) , "#a0fb0e")
p104 = parada(104, "Kallithea", 37.96052673513547, 23.697283817961743, (802,687), (-228.0, -236.0) , "#a0fb0e")
p105 = parada(105, "Tavros", 37.96246593225603, 23.703389866787433, (828,659), (-202.0, -209.0) , "#a0fb0e")
p106 = parada(106, "Petralona", 37.968633169183285, 23.70920623701997, (854,632), (-176.0, -181.0) , "#a0fb0e") # Draw distinto
p107 = parada(107, "Thissio", 37.97665872985702, 23.720696914650578, (866,605), (-163.0, -153.0) , "#a0fb0e")
p108v = parada(108, "Monastiraki", 37.976156586157984, 23.725543666342997, (866,562), (-165.0, -110.0) , "#a0fb0e")       # Linea 1 verde
p109v = parada(109, "Omonia", 37.98418411389954, 23.72869392276704, (866,521), (-165.0, -71.0) , "#a0fb0e")              # Linea 1 verde
p110 = parada(110, "Victoria", 37.99306307638207, 23.73033216026106, (864, 469), (-165.0, -20.0) , "#a0fb0e") # Draw distinto
p111v = parada(111, "Attiki", 37.99944575382092, 23.722576292324174, (823,429), (-206.0, 22.0), "#a0fb0e")             # Linea 1 verde
p112 = parada(112, "Aghios Nikolaos", 38.006918475588094, 23.727666328798236, (844,407), (-187.0, 43.0) , "#a0fb0e")
p113 = parada(113, "Kato Patissia", 38.0115784651099, 23.72859031245151, (869,383),(-162.0, 67.0) , "#a0fb0e")
p114 = parada(114, "Aghios Eleftherios", 38.02011686985624, 23.73178976895845, (893,358),(-138.0, 94.0) , "#a0fb0e")
p115 = parada(115, "Ano Patissia", 38.02378986594461, 23.73596583622907, (917, 335),(-114.0, 117.0) , "#a0fb0e")
p116 = parada(116, "Perissos", 38.032730102525214, 23.744634963161342, (938,312),(-93.0, 138.0) , "#a0fb0e")
p117 = parada(117, "Pefkakia", 38.03713926864271, 23.750174140044294, (962,290),(-68.0, 161.0) , "#a0fb0e")
p118 = parada(118, "Nea Ionia", 38.04156868847245, 23.755212096558044, (980,269),(-48.0, 182.0) , "#a0fb0e")
p119 = parada(119, "Iraklio", 38.04622859864819, 23.766090657553583, (1013, 238),(-17.0, 212.0) , "#a0fb0e") # Draw distinto
p120 = parada(120, "Irini", 38.043721814731654, 23.782689281341607, (1086,237),(55.0, 213.0) , "#a0fb0e")
p121 = parada(121, "Neratziotissa", 38.044852574447894, 23.79266810507687, (1119,235),(89.0, 216.0) , "#a0fb0e")
p122 = parada(122, "Maroussi", 38.056293481328524, 23.805074572845157, (1162,192),(132.0, 259.0) , "#a0fb0e")
p123 = parada(123, "KAT", 38.06591417038175, 23.80406937901929, (1202,154),(169.0, 298.0) , "#a0fb0e")
p124 = parada(124, "Kifissia", 38.07357538178982, 23.808140002595298, (1238, 116),(207.0, 333.0) , "#a0fb0e")

p101.añadirConexion(p102, 2)
p102.añadirConexion(p101, 2)

p102.añadirConexion(p103, 2)
p103.añadirConexion(p102, 2)

p103.añadirConexion(p104, 1.6)
p104.añadirConexion(p103, 1.6)

p104.añadirConexion(p105, 0.570)
p105.añadirConexion(p104, 0.570)

p105.añadirConexion(p106, 0.810)
p106.añadirConexion(p105, 0.810)

p106.añadirConexion(p107, 1.6)
p107.añadirConexion(p106, 1.6)

p107.añadirConexion(p108v, 0.530)
p108v.añadirConexion(p107, 0.530)

p108v.añadirConexion(p109v, 0.860)
p109v.añadirConexion(p108v, 0.860)

p109v.añadirConexion(p110, 1.1)
p110.añadirConexion(p109v, 1.1)

p110.añadirConexion(p111v, 1.1)
p111v.añadirConexion(p110, 1.1)

p111v.añadirConexion(p112, 1)
p112.añadirConexion(p111v, 1)

p112.añadirConexion(p113, 0.580)
p113.añadirConexion(p112, 0.580)

p113.añadirConexion(p114, 0.980)
p114.añadirConexion(p113, 0.980)

p114.añadirConexion(p115, 0.520)
p115.añadirConexion(p114, 0.520)

p115.añadirConexion(p116, 1.3)
p116.añadirConexion(p115, 1.3)

p116.añadirConexion(p117, 0.680)
p117.añadirConexion(p116, 0.680)

p117.añadirConexion(p118, 0.680)
p118.añadirConexion(p117, 0.680)

p118.añadirConexion(p119, 1.3)
p119.añadirConexion(p118, 1.3)

p119.añadirConexion(p120, 1.5)
p120.añadirConexion(p119, 1.5)

p120.añadirConexion(p121, 1)
p121.añadirConexion(p120, 1)

p121.añadirConexion(p122, 1.7)
p122.añadirConexion(p121, 1.7)

p122.añadirConexion(p123, 1.1)
p123.añadirConexion(p122, 1.1)

p123.añadirConexion(p124, 1.1)
p124.añadirConexion(p123, 1.1)

#LINEA 2
p201 = parada(201, "Aghios Antonios", 38.00668553570866, 23.699447869096325, (750, 354),(-280.0, 96.0), "#960018")
p202 = parada(202, "Sepolia", 38.002710778495135, 23.713655086379916, (787, 392), (-243.0, 60.0), "#960018")
p111r = parada(111, "Attiki", 37.99944575382092, 23.722576292324174, (823,429), (-206.0, 22.0), "#960018") # Transbordo
p203 = parada(203, "Larissa Station", 37.992066064654296, 23.721366342246696, (824, 468),(-206.0, -17.0), "#960018")
p204 = parada(204, "Metaxourghio", 37.986325663935574, 23.721481322354894, (827, 517),(-206.0, -66.0), "#960018")
p109r = parada(109, "Omonia", 37.98418411389954, 23.72869392276704, (866,521),(-166.0, -70.0), "#960018") # Transbordo
p205 = parada(205, "Panepistimio", 37.98054432519301, 23.73351102722727, (889, 542), (-143.0, -89.0), "#960018")
p206r = parada(206, "Syntagma", 37.97465889945412, 23.735569579603855, (909, 563),(-122.0, -111.0), "#960018") 
p207 = parada(207, "Akropoli", 37.96879775311836, 23.72978243649906, (912, 607),(-118.0, -155.0), "#960018")
p208 = parada(208, "Sygrou - Fix", 37.96437760465376, 23.727030685384282, (913, 642),(-118.0, -192.0), "#960018")
p209 = parada(209, "Neos Kosmos", 37.957681856044836, 23.729044062616964, (912, 676),(-118.0, -225.0), "#960018")
p210 = parada(210, "Aghios loannis", 37.95674487994592, 23.735144747060275, (912, 709),(-118.0, -260.0), "#960018")
p211 = parada(211, "Dafni", 37.94928445289386, 23.73752144052115, (913, 743),(-118.0, -293.0), "#960018")
p212 = parada(212, "Aghios Dimitrios", 37.94068513862538, 23.741652915121485, (911, 778),(-118.0, -326.0), "#960018")

p201.añadirConexion(p202, 1.3)
p202.añadirConexion(p201, 1.3)

p202.añadirConexion(p111r, 1.1)
p111r.añadirConexion(p202, 1.1)

p111r.añadirConexion(p203, 0.760)
p203.añadirConexion(p111r, 0.760)

p203.añadirConexion(p204, 0.760)
p204.añadirConexion(p203, 0.760)

p204.añadirConexion(p109r, 0.660)
p109r.añadirConexion(p204, 0.660)

p109r.añadirConexion(p205, 0.640)
p205.añadirConexion(p109r, 0.640)

p205.añadirConexion(p206r, 0.660)
p206r.añadirConexion(p205, 0.660)

p206r.añadirConexion(p207, 1.1)
p207.añadirConexion(p206r, 1.1)

p207.añadirConexion(p208, 0.530)
p208.añadirConexion(p207, 0.530)

p208.añadirConexion(p209, 1.2)
p209.añadirConexion(p208, 1.2)

p209.añadirConexion(p210, 0.580)
p210.añadirConexion(p209, 0.580)

p210.añadirConexion(p211, 0.830)
p211.añadirConexion(p210, 0.830)

p211.añadirConexion(p212, 0.970)
p212.añadirConexion(p211, 0.970)

#LINEA 3
p301 = parada(301, "Egaleo", 37.99197713841019, 23.68180804242772,(682, 464), (-349.0, -13.0), "#00ffff")
p302 = parada(302, "Eleonas", 37.98796794969659, 23.694188303915244,(731, 513), (-300.0, -62.0), "#00ffff")
p303 = parada(303, "Kerameikos", 37.97862997972868, 23.711495597009225,(781, 559), (-251.0, -109.0), "#00ffff")
p108a = parada(108, "Monastiraki", 37.976156586157984, 23.725543666342997,(866, 561), (-165.0, -111.0), "#00ffff") # Transbordo
p206a = parada(206, "Syntagma", 37.97465889945412, 23.735569579603855, (909, 563), (-121.0, -110.0), "#00ffff") 
p304 = parada(304, "Evangelismos", 37.97603509413124, 23.746616168172817,(984, 561), (-46.0, -111.0), "#00ffff")
p305 = parada(305, "Megaro Moussikis", 37.979320807022255, 23.752912297009242,(1032, 558), (2.0, -108.0), "#00ffff")
p306 = parada(306, "Ambelokipi", 37.98699580348293, 23.76223686817322,(1070, 528), (37.0, -77.0), "#00ffff")
p307 = parada(307, "Panormou", 37.99318406631609, 23.76341384726534,(1088, 508), (57.0, -57.0), "#00ffff")
p308 = parada(308, "Katehaki", 37.993169700334064, 23.77615186074951,(1107, 486), (77.0, -36.0), "#00ffff")
p309 = parada(309, "Ethniki Amyna", 38.00005237698352, 23.785750665254792,(1128, 465), (97.0, -16.0), "#00ffff")
p310 = parada(310, "Holargos", 38.00451268334984, 23.7947224746732,(1148, 445), (117.0, 4.0), "#00ffff")
p311 = parada(311, "Nomismatokopio", 38.00927268201013, 23.80566601294359,(1169, 425), (139.0, 25.0), "#00ffff")
p312 = parada(312, "Aghia Paraskevi", 38.017223333622894, 23.812289216575675,(1189, 405), (159.0, 46.0), "#00ffff")
p313 = parada(313, "Halandri", 38.021661421954065, 23.82119265468349,(1209, 386), (178.0, 66.0), "#00ffff")
p314 = parada(314, "Doukissis Plakentias", 38.023885044934055, 23.833603320795778,(212.0, 99.0), (213.0, 97.0), "#00ffff")
p315 = parada(315, "Pallini", 38.00571411424471, 23.869641490662428,(1294, 355), (263.0, 96.0), "#00ffff")
p316 = parada(316, "Paiania-Kantza", 37.98373452959684, 23.869882025072506,(1300, 429), (268.0, 23.0), "#00ffff")
p317 = parada(317, "Koropi", 37.91299760993833, 23.895798820031143,(1305, 575), (272.0, -125.0), "#00ffff")
p318 = parada(318, "Airport", 37.93664288305453, 23.94455920732838,(1372, 582), (342.0, -129.0), "#00ffff")

p301.añadirConexion(p302, 1.1)
p302.añadirConexion(p301, 1.1)

p302.añadirConexion(p303, 1.9)
p303.añadirConexion(p302, 1.9)

p303.añadirConexion(p108a, 1.3)
p108a.añadirConexion(p303, 1.3)

p108a.añadirConexion(p206a, 0.920)
p206a.añadirConexion(p108a, 0.920)

p304.añadirConexion(p206a, 0.92)
p206a.añadirConexion(p304, 0.92)

p304.añadirConexion(p305, 0.63)
p305.añadirConexion(p304, 0.63)

p305.añadirConexion(p306, 0.1)
p306.añadirConexion(p305, 0.1)

p306.añadirConexion(p307, 0.89)
p307.añadirConexion(p306, 0.89)

p307.añadirConexion(p308, 1.2)
p308.añadirConexion(p307, 1.2)

p308.añadirConexion(p309, 1.2)
p309.añadirConexion(p308, 1.2)

p309.añadirConexion(p310, 0.94)
p310.añadirConexion(p309, 0.94)

p310.añadirConexion(p311, 1.12)
p311.añadirConexion(p310, 1.12)

p311.añadirConexion(p312, 1.06)
p312.añadirConexion(p311, 1.06)

p312.añadirConexion(p313, 0.920)
p313.añadirConexion(p312, 0.920)

p313.añadirConexion(p314, 1.1)
p314.añadirConexion(p313, 1.1)

p314.añadirConexion(p315, 4.4)
p315.añadirConexion(p314, 4.4)

p315.añadirConexion(p316, 2.5)
p316.añadirConexion(p315, 2.5)

p316.añadirConexion(p317, 8.4)
p317.añadirConexion(p316, 8.4)

p317.añadirConexion(p318, 5.84)
p318.añadirConexion(p317, 5.84)

#TRANSBORDOS

# Attiki
p111v.añadirConexion(p111r, 0.2)
p111r.añadirConexion(p111v, 0.2)
# Omonia
p109v.añadirConexion(p109r, 0.2)
p109r.añadirConexion(p109v, 0.2)
# Monastiraki
p108v.añadirConexion(p108a, 0.2)
p108a.añadirConexion(p108v, 0.2)
# Sintagma
p206r.añadirConexion(p206a, 0.2)
p206a.añadirConexion(p206r, 0.2)

import paradas

#Encontrar la parada dadas unas coordenadas
def which_stop(x,y):
    for parada in paradas.listaParadas:
        ret = parada.is_in_circle(x,y)
        if ret is None or False:
            continue
        elif ret is parada:
            return ret