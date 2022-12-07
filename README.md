# AtenasUndergroundApp
Aplicación de busqueda de trayecto óptimo entre dos paradas del metro de Atenas. Asignatura de Inteligencia Artificial, ETSIINF UPM.

## Table of Contents ##

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
2. [Descargar](<https://github.com/nihelkb/AtenasUndergroundApp/archive/refs/tags/1.0.zip>) el código fuente de la app
3. Descomprimir el archivo "AtenasUndergroundApp-1.0.zip"
4. Situarse en el directorio mediante `cd AtenasUndergroundApp/`
5. Ejecutar el mandato `python app/gui.py` para abrir la aplicación

###  Cómo se usa la app ###
El objetivo de la aplicación es encontrar una ruta óptima entre dos paradas del metro de Atenas. Para ello, habrá que elegir las paradas.

La selección de las paradas se hace pulsando en el mapa interativo de la derecha de la ventana. 
