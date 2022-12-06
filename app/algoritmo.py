import paradas as lista
import parada as par
import math
import bbdd as base

# calcula la heuristica
def heuristica( coord1, coord2):

    longitud1 = coord1.longitud
    longitud2 = coord2.longitud
    latitud1 = coord1.latitud
    latitud2 = coord2.latitud
    distancia = math.sqrt(pow(longitud2-longitud1,2) + pow(latitud2-latitud1,2))

    return distancia


# funcion que te devuelve las conexiones que tiene un parada
def getVecinos(parada):
    lista = []
    for x in parada.conexiones:
       lista.append(x)
    return lista

def aStarAlgo(parada_inicio, parada_fin):
    open_set =[]
    open_set.append(parada_inicio)
    closed_set = set()
    distancia = {}       # Almacena la distancia desde el nodo inicial
    padres = {}         # parents tiene el mapa de adayacencia
    # La distancia desde el nodo raiz a si mismo es cero
    distancia[parada_inicio] = 0
    #parada_inicio es el nodo raiz por lo que no tiene padres
    #parada_inicio es añadido con su propio nodo padre 
    padres[parada_inicio] = parada_inicio

    while len(open_set) > 0:
        aux = None
        # Nodo con el menor f() 
        for indice in open_set:
            if aux == None or  distancia[indice] + heuristica(parada_inicio,parada_fin) < distancia[aux] + heuristica(parada_inicio,parada_fin):
                aux = indice

        if aux == parada_fin.nombre:
            pass
        else:
            for (valor, peso) in getVecinos(aux):
              
                #nodos 'valor' que no esten en el primer y ultimo set son añadido al primero
                #aux se establece su padres
                if valor not in open_set and valor not in closed_set:
                    open_set.append(valor)
                    padres[valor] = aux
                    distancia[valor] = distancia[aux] + peso
                #Para cada nodo valor comparamos la distancia desde el inicio
                else:
                    if distancia[valor] > distancia[aux] + peso:
                        #Se actualiza distancia(m)
                        distancia[valor] = distancia[aux] + peso
                        #Se cambia el padre de valor a aux
                        padres[valor] = aux
                        #Si valor esta en closed set, se elimina de y se añade a open
                        if valor in closed_set:
                            closed_set.remove(valor)
                            open_set.append(valor)
        if aux == None:
            print('Path no existe!')
            return None 
        if aux == parada_fin:
            pass
        else:

            for (valor, peso) in getVecinos(aux):
              
              # print(valor)
                #nodos 'valor' que no esten en el primer set y ultimo set son añados que no esten en el first and last set son añadidos al set first
                #Aux se estable su padre
                if valor not in open_set and valor not in closed_set:
                    open_set.append(valor)
                    
                    padres[valor] = aux
                    distancia[valor] = distancia[aux] + peso
                #Para cada nodo valor comparamos la distancia desde el inicio
                else:
                    if distancia[valor] > distancia[aux] + peso:
                        #Se actualiza distancia(m)
                        distancia[valor] = distancia[aux] + peso
                        #Se cambia el padre de valor a aux
                        padres[valor] = aux
                         #Si valor esta en closed set, se elimina de y se añade a open
                        if valor in closed_set:
                            closed_set.remove(valor)
                            open_set.append(valor)
        if aux == None:
            print('Path no existe!')
            return None
        
        # Si el nodo es parada_fin
        # Empezamos a reconstruir hasta parada_inicio y posteriormente lo invertimo para obtener el camino
        if aux == parada_fin:
            path = []
            aux2 = aux
            i = 0 
            while padres[aux] != aux:
                if  aux.id != aux2.id or i != 1:
                    path.append(aux)
                    i = 1
                elif aux.id == aux2.id:
                    path.remove(aux2)
                    path.append(aux)
                aux2 = aux
                aux = padres[aux]
            path.append(parada_inicio)
            path.reverse()
            print('Path encontrado: {}'.format(path))
            return path
        # Eliminamos aux de open_list, y lo añadimos a closed_list
        # porque todos los vecinos se han inspecionado
        open_set.remove(aux)
        closed_set.add(aux)
    print('Path no existe!')
    return None