import paradas as lista
import parada as par
import math
import bbdd as base



def heuristic( coord1, coord2):

    longitud1 = coord1.longitud
    longitud2 = coord2.longitud
    latitud1 = coord1.latitud
    latitud2 = coord2.latitud
    distancia = math.sqrt(pow(longitud2-longitud1,2) + pow(latitud2-latitud1,2))

    return distancia


#define fuction to return neighbor and its distance
#from the passed node
def get_neighbors(parada):
    lista = []
    for x in parada.conexiones:
       lista.append(x)
    return lista




def aStarAlgo(parada_inicio, parada_fin):
    nombre = parada_inicio.nombre
    open_set =[]
    open_set.append(parada_inicio)
    closed_set = set()
    g = {}               #store distance from starting node
    parents = {}         # parents contains an adjacency map of all nodes
    #distance of starting node from itself is zero
    g[parada_inicio] = 0
    #parada_inicio is root node i.e it has no parent nodes
    #so parada_inicio is set to its own parent node
    parents[parada_inicio] = parada_inicio

    while len(open_set) > 0:
        aux = None
        #node with lowest f() is found 
        for indice in open_set:
            if aux == None or  g[indice] + heuristic(parada_inicio,parada_fin) < g[aux] + heuristic(parada_inicio,parada_fin):
                aux = indice

        if aux == parada_fin.nombre:
            pass
        else:
            for (m, weight) in get_neighbors(aux):
              
                #nodes 'm' not in first and last set are added to first
                #aux is set its parent
                if m not in open_set and m not in closed_set:
                    open_set.append(m)
                    parents[m] = aux
                    g[m] = g[aux] + weight
                #for each node m,compare its distance from start i.e g(m) to the
                #from start through aux node
                else:
                    if g[m] > g[aux] + weight:
                        #update g(m)
                        g[m] = g[aux] + weight
                        #change parent of m to aux
                        parents[m] = aux
                        #if m in closed set,remove and add to open
                        if m in closed_set:
                            closed_set.remove(m)
                            open_set.append(m)
        if aux == None:
            print('Path does not exist!')
            return None 
        if aux == parada_fin:
            pass
        else:

            for (m, weight) in get_neighbors(aux):
              
              #  print(m)
                #nodes 'm' not in first and last set are added to first
                #aux is set its parent
                if m not in open_set and m not in closed_set:
                    open_set.append(m)
                    
                    parents[m] = aux
                    g[m] = g[aux] + weight
                #for each node m,compare its distance from start i.e g(m) to the
                #from start through aux node
                else:
                    if g[m] > g[aux] + weight:
                        #update g(m)
                        g[m] = g[aux] + weight
                        #change parent of m to aux
                        parents[m] = aux
                        #if m in closed set,remove and add to open
                        if m in closed_set:
                            closed_set.remove(m)
                            open_set.append(m)
        if aux == None:
            print('Path does not exist!')
            return None
        
        # if the current node is the parada_fin
        # then we begin reconstructin the path from it to the parada_inicio
        if aux == parada_fin:
            path = []

            while parents[aux] != aux:
                path.append(aux)
                aux = parents[aux]
            path.append(parada_inicio)
            path.reverse()
            print('Path found: {}'.format(path))
            return path
        # remove aux from the open_list, and add it to closed_list
        # because all of his neighbors were inspected
        open_set.remove(aux)
        closed_set.add(aux)
    print('Path does not exist!')
    return None

aStarAlgo(base.p301,base.p124)




