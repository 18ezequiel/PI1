from fastapi import FastAPI, File, UploadFile                   #### LIBRERIA DE FASTAPI.
from fastapi.responses import HTMLResponse, JSONResponse        #### LIBRERIA DE RESPONSE.
from deta import Deta                                           #### LIBRERIA DE DETA.
import pandas as pd                                             #### PANDAS PARA LEER CSV.
from fastapi.encoders import jsonable_encoder                   #### LIBRERIA PARA EL FORMATO JSON.


app = FastAPI()

##########################################################################
# FUNCIONES PRUEBA.
##########################################################################

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

deta = Deta("e0aqrqk9_y2PEptSrX4pzQghDK9K4x8qUTqLYktWb")  
drive = deta.Drive("myfiles")


@app.get("/render", response_class=HTMLResponse)
def render():
    return '''
    <form action="/upload" enctype="multipart/form-data" method="post">
        <input name="file" type="file">
        <input type="submit">
    </form>'''

##########################################################################
##########################################################################

##########################################################################
# FUNCION UPLOAD, PARA LA CARGA DE ARCHIVOS AL DRIVE DE DETA
##########################################################################

@app.post("/upload")
def upload(file: UploadFile = File(...)):

    '''
    La funcion se encarga de crear un apartado en la api
    para la carga de archivos al drive.
    '''
    
    name = file.filename
    f = file.file
    res = drive.put(name, f)
    return res

##########################################################################
##########################################################################
# FUNCIONES GET
##########################################################################
##########################################################################

@app.get("/get_word_count/{plataforma}/{keyword}")    
def Get_Word_Count(plataforma:str,keyword:str):

    '''
    Esta funcion se encarga de traer la cantidad de veces
    que una palabra se repite en los titulos de las
    distintas plataformas.
    '''

    res = drive.get(f"{plataforma}.csv")
    df = pd.read_csv(res)
    count=0
    for index, i in enumerate(df['title']):
        if keyword in i:
            count+=1
    
    dicc={  'plataforma':plataforma,
            'keyword': keyword,
            'cantidad': count}
    json_compatible_item_data = jsonable_encoder(dicc)
    return JSONResponse(content=json_compatible_item_data)



@app.get("/get_score_count/{plataforma}/{score}/{anio}")    
def Get_Word_Count(plataforma:str,score:int,anio:int):

    '''
    Esta funcion se encarga de traer las peliculas con
    mas score que el indicado, y en determinado año.
    '''

    res = drive.get(f"{plataforma}.csv")
    df = pd.read_csv(res)
    count=0
    tipo='movie'
    for index,i in enumerate(df.title):
        if df['release_year'][index]== anio:
            if df['score'][index]>score:
                if df['type'][index] in tipo:
                    count+=1


    dicc = {'plataforma' : plataforma,
            'score'      : score,
            'anio'        : anio,
            'cantidad'   : count}

    json_compatible_item_data = jsonable_encoder(dicc)
    return JSONResponse(content=json_compatible_item_data)


@app.get("/get_second_score/{plataforma}")   
def Get_second_score(plataforma:str):

    '''
    Esta funcion trae el segundo score mas alto de peliculas
    ordenadas alfabeticamente.
    '''

    res = drive.get(f"{plataforma}.csv")
    df = pd.read_csv(res)
    values=[]
    type='movie'

    for index, i in enumerate(df['title']):
        if df['score'][index]==100:
            if df['type'][index]==type:
                values.append(df['title'][index])

    values.sort()
    result = values[1]
    
    dicc = {'plataforma': plataforma,
            'titulo': result}
            
    json_compatible_item_data = jsonable_encoder(dicc)
    return JSONResponse(content=json_compatible_item_data)



@app.get("/get_longest/{plataforma}/{duration_type}/{release_year}")   
def Get_second_score(plataforma:str,duration_type:str,release_year:int):

    '''
    Esta funcion trae la pelicula con mayor duracion en la
    plataforma y año indicado.
    '''

    res = drive.get(f"{plataforma}.csv")
    df = pd.read_csv(res)
   
    type='movie'
    result=0

    for index, i in enumerate(df['title']):
        if df['duration_type'][index] == duration_type:
            if df['release_year'][index]==release_year:
                if df['type'][index]in type:
                    if df['duration_int'][index]>result:
                        result = df['duration_int'][index]
                        title = df['title'][index]
    
    dicc = {'titulo': title,
            'duracion': result}
            
    json_compatible_item_data = jsonable_encoder(dicc)
    return JSONResponse(content=json_compatible_item_data)



@app.get("/get_rating_count/{rating}")   
def Get_second_score(rating:str):

    '''
    Esta funcion cuenta la cantidad de peliculas en todas
    las plataformas, que tienen el rating indicado.
    '''

    a = drive.get("amazon.csv")
    d = drive.get("disney.csv")
    h = drive.get("hulu.csv")
    n = drive.get("netflix.csv")
    df_a = pd.read_csv(a)
    df_d = pd.read_csv(d)
    df_h = pd.read_csv(h)
    df_n = pd.read_csv(n)

    count = 0
    for index, i in enumerate(df_a['rating']):
        if df_a['rating'][index] == rating:
            count+=1
    for index, i in enumerate(df_d['rating']):
        if df_d['rating'][index] == rating:
            count+=1
    for index, i in enumerate(df_h['rating']):
        if df_h['rating'][index] == rating:
            count+=1
    for index, i in enumerate(df_n['rating']):
        if df_n['rating'][index] == rating:
            count+=1

    dicc = {'rating': rating,
            'cantidad': count}
            
    json_compatible_item_data = jsonable_encoder(dicc)
    return JSONResponse(content=json_compatible_item_data)