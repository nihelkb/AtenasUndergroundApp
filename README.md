# AtenasUndergroundApp
Aplicación de busqueda de trayecto óptimo entre dos paradas del metro de Atenas. Asignatura de Inteligencia Artificial, ETSIINF UPM.

## Tabla de Contenidos ##

* [Introducción](#introducción)
  * [Descargar código fuente](#descargar-código-fuente)
  * [Árbol de directorios](#árbol-de-directorios)
  * [Implementación](#implementación)
* [Ejecutar la app](#ejecutar-la-app)
  * [Cómo se usa la app](#cómo-se-usa-la-app)


## Introducción ##

### Descargar código fuente ###

1. Ver el [último lanzamiento](<https://github.com/nihelkb/AtenasUndergroundApp/releases>) de la app
2. [Descargar](<https://github.com/nihelkb/AtenasUndergroundApp/archive/refs/tags/1.0.zip>) el código fuente

### Árbol de directorios ###
``` terminal
AtenasUndergroundApp/
├── app/
│   ├── algoritmo.py
│   ├── bbdd.py
│   ├── gui.py
│   ├── parada.py
│   └── paradas.py
├── build/
│   └── assets/
│       └── frame0/
│           ├── blocked.png
│           ├── end_title.png
│           ├── init_button.png
│           ├── init_button_osc.png
│           ├── line_input.png
│           ├── line_input_blanco.png
│           ├── metro.ico
│           ├── metro_map.png
│           ├── origin_title.png
│           ├── path_icon.png
│           ├── points.png
│           ├── reinit_button.png
│           ├── reinit_button_osc.png
│           └── title.png
└── data/
    ├── CoordenadasMetroAtenas.txt
    └── Costes/
        ├── Linea1.txt
        ├── Linea2.txt
        ├── Linea3.txt
        └── Transbordos.txt
```
### Implementación ###




## Ejecutar la app ##
Se puede ejecutar la aplicación de dos maneras:
* Mediante un ejecutable, que no requiere de instalaciones previas.

1. Ver el [último lanzamiento](<https://github.com/nihelkb/AtenasUndergroundApp/releases>) de la app
2. [Descargar](<https://github.com/nihelkb/AtenasUndergroundApp/releases/download/1.0/App.zip>) el ejecutable de la app
3. Descomprimir el archivo "App.zip"
4. Abrir el archivo ejecutable "Atenas Underground.exe"
  
* Mediante el código fuente, que requiere la instalación previa de Python versión 3.10.7 o posterior.

1. [Instalar Python](<https://www.python.org/downloads/>)
2. [Descargar](#descargar-código-fuente) el código fuente de la app
3. Descomprimir el archivo "AtenasUndergroundApp-1.0.zip"
4. Situarse en el directorio mediante `cd AtenasUndergroundApp/`
5. Ejecutar el mandato `python app/gui.py` para abrir la aplicación

###  Cómo se usa la app ###
El objetivo de la aplicación es encontrar una ruta óptima entre dos paradas del metro de Atenas. Para ello, primero será necesario seleccionar las paradas pulsando en el mapa interativo de la derecha de la ventana. 

#### Pantalla de Inicio ####
La pantalla de inicio solo contiene el campo para seleccionar el origen.

![Pantalla de inicio](/img/PantallaInicio.png "Pantalla de inicio.")

#### Selección primera parada ####
Al pulsar una parada, se marca como seleccionada y aparece el campo para seleccionar la segunda parada.

![Primera parada](/img/PrimeraParada.png "Primera parada seleccionada.")

#### Selección segunda parada ####
Al pulsar otra parada, se marca como seleccionada y aparecen las opciones de iniciar y de reiniciar la búsqueda. 

![Segunda parada](/img/SegundaParada.png "Segunda parada seleccionada.")

##### Caso de error 
Si se seleccionase como destino la misma parada seleccionada para el origen, aparecerá un error que pedirá al usuario cambiar la selección.

![Misma parada](/img/Mismaparada.png "Seleccionada la misma parada.")

#### Inicio de búsqueda ####
Al darle al botón de iniciar, se despliega una nueva ventana en la que se mostrará el trayecto a seguir mediante una animación. La ventana principal quedará bloqueada.

![Trayecto](/img/Trayecto.png "Trayecto óptimo.")

#### Cierre de ventana ####
Antes de cerrar la ventana del trayecto se pedirá al usuario una confirmación que informa de que los resultados se perderán. En caso de aceptar, se cerrará la ventana y se reiniciará la ventana volviendo a la pantalla de inicio.

![Cierre de ventana](/img/Cerrarventana.png "Cierre de ventana emergente.")

#### Cierre de programa ####
Antes de cerrar el programa se pedirá al usuario una confirmación.

![Salir del programa](/img/Cerrarprograma.png "Salir del programa.")

