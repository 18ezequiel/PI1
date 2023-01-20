# PI1
Proyecto individual 1

  Este proyecto tiene como fin el montar una api, mediante Fastapi, con una serie de funciones.
  El deployment esta hecho mediante DETA, lo que se busca es la carga de data y que dichas funciones
  puedan trabajar con esto.
  
  ENV (Entorno Virtual): /PI1-env
  
  El proyecto fue montado en un entorno virtual, para que las librerias que se necesiten no sean instaladas
  en el equipo.
  
  
  Transformaciones: /Transformaciones
  
  Entre las carpetas del repositorio, podremos hallar una denominada Transformaciones,
  esta tiene como fin el transformar la data cruda, y dejarla lista para su uso.
  Dentro se encuentra un archivo nombrado transformaciones.py, en el cual se encuentra una clase con funciones
  que dejarán los archivos csv colocados en /Data_cruda, aptos para su uso. Luego dichos csv, 
  seran subidos a /Datasets.
  Para la manipulación de este .py, se hizo un main.ipynb con la clase importada.
  
  API: /pi_1
  
  Por otra parte la carpeta pi_1 es la que contiene la API, esta tiene consigo las funciones que se
  utilizarán. Se le colocó unas funciones de prueba, luego una función upload para la carga de archivos
  al drive de DETA y por último las funciones get, explicadas dentro del main.py. Los response que tiene dichos get
  son en formato json.
  
  Instalacion del proyecto:
  
  Para la instalación, sólamente se debe clonar el repositorio, y luego mediante terminal siturase en la carpeta
  /pi_1 y ejecutar la siguiente linea de código -pip install requirements.txt-.
  
  

