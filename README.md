# PI1
Proyecto individual 1

  Este proyecto tiene como fin el montar una api, mediante Fastapi, con una serie de funciones.
  El deployment esta hecho mediante DETA, y lo que se busca es la carga de data, y que dichas funciones,
  puedan trabajar con esto.
  
  ENV (Entorno Virtual):
  
  El proyecto fue montado en un entorno virtual, para que las librerias que se necesiten no se instalen
  en el equipo.
  
  
  Transformaciones:
  
  Entre las carpetas que se encontraran clonando este repositorio, una de ellas es la de Transformaciones,
  esta carpeta tiene como fin el transformar la data cruda, y dejarla lista para su uso.
  Dentro de esto hay un .py llamado transformaciones.py, que tiene una clase la cual dentro tiene una serie
  de funciones que dejarán los archivos csv colocados en la carpeta Data_cruda, en condiciones. Luego dichos csv, 
  seran subidos a la carpeta Datasets.
  Para la manipulacion de este .py, se hizo un main.ipynb con la clase importada y la mejor visualizacion de los
  dataset.
  
  API:
  
  Por otra parte la carpeta pi_1 es la que contiene la api, esta carpeta tiene consigo las funciones que se
  utilizaran. Se le colocó unas funciones de prueba, luego una función upload para la carga de archivos
  al drive de DETA y por ultimo las funciones get, explicadas dentro del main.py. Los response que tiene dichos get
  son en formato json.
  
  Instalacion del proyecto:
  
  Para la instalacion, solamente se debe clonar el repositorio, y luego mediante terminal siturase en la carpeta
  pi_1 y ejecutar la siguiente linea pip install requirements.py.
  
  

