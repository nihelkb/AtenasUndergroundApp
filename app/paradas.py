import bbdd as bd

listaParadas = []

# LINEA 1: Añadir las paradas de la línea 1 a la lista de paradas

listaParadas.append(bd.p101)
listaParadas.append(bd.p102)
listaParadas.append(bd.p103)
listaParadas.append(bd.p104)
listaParadas.append(bd.p105)
listaParadas.append(bd.p106)
listaParadas.append(bd.p107)
listaParadas.append(bd.p108v)
listaParadas.append(bd.p109v)
listaParadas.append(bd.p110)
listaParadas.append(bd.p111v)
listaParadas.append(bd.p112)
listaParadas.append(bd.p113)
listaParadas.append(bd.p114)
listaParadas.append(bd.p115)
listaParadas.append(bd.p116)
listaParadas.append(bd.p117)
listaParadas.append(bd.p118)
listaParadas.append(bd.p119)
listaParadas.append(bd.p120)
listaParadas.append(bd.p121)
listaParadas.append(bd.p122)
listaParadas.append(bd.p123)
listaParadas.append(bd.p124)

# LINEA 2: Añadir las paradas de la línea 2 a la lista de paradas

listaParadas.append(bd.p201)
listaParadas.append(bd.p202)
listaParadas.append(bd.p111r)
listaParadas.append(bd.p203)
listaParadas.append(bd.p204)
listaParadas.append(bd.p109r)
listaParadas.append(bd.p205)
listaParadas.append(bd.p206)
listaParadas.append(bd.p207)
listaParadas.append(bd.p208)
listaParadas.append(bd.p209)
listaParadas.append(bd.p210)
listaParadas.append(bd.p113)
listaParadas.append(bd.p211)
listaParadas.append(bd.p212)

# LINEA 3: Añadir las paradas de la línea 3 a la lista de paradas

listaParadas.append(bd.p301)
listaParadas.append(bd.p302)
listaParadas.append(bd.p303)
listaParadas.append(bd.p304)
listaParadas.append(bd.p305)
listaParadas.append(bd.p306)
listaParadas.append(bd.p307)
listaParadas.append(bd.p308)
listaParadas.append(bd.p309)
listaParadas.append(bd.p310)
listaParadas.append(bd.p311)
listaParadas.append(bd.p312)
listaParadas.append(bd.p313)
listaParadas.append(bd.p314)
listaParadas.append(bd.p315)
listaParadas.append(bd.p316)
listaParadas.append(bd.p317)
listaParadas.append(bd.p318)
listaParadas.append(bd.p108a)
listaParadas.append(bd.p206c)

def buscarParada(id):
    for parada in listaParadas:
        if(parada.id == id):
            return parada
    return "No existe"