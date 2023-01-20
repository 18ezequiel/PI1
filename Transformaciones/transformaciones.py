import pandas as pd
import os

class Transformaciones:

    def extract(self, path):

        '''
        Defino el path del csv para extraer la data y
        creo el dataframe.
        '''

        df1 = pd.read_csv(path)

        return df1

    def platform(self, path):

        '''
        Extraigo la data de que platform es.
        '''

        for i in range(len(path)):
            if i == 68:
                platform = path[i]

        return platform


    
    def transform(self, path):

        '''
        Transformo el df
        '''

        df1 = self.extract(path)
        platform = self.platform(path)

        #######################################################################
        # LE INSERTO LA INICIAL DE LA PLATAFORMA EN EL ID.
        #######################################################################
        df1.insert(0, 'id', platform + df1.show_id)

        #######################################################################
        # COLOCO EN LOS STRING VACIOS DEL RATING UNA 'G'.
        #######################################################################

        for i in df1.rating:
            if type(i) != str:
                i = 'G'

        #######################################################################
        # DIVIDO EN DOS COLUMNAS A LA COLUMNA DURATION, UNA COLUMNA INT Y OTRA 
        # STR.
        #######################################################################

        duration = df1["duration"].str.split(expand=True)

        duration.columns = ['duration_int', 'duration_type']

        df1 = pd.concat([df1, duration], axis=1)


        #######################################################################
        # RENOMBRO LA PALABRAS SEASONS DENTRO DE LA COLUMNA DURATION_TYPE A 
        # SEASON.
        #######################################################################

        for index, i in enumerate(df1['duration_type']):
            if df1['duration_type'][index]=='Seasons':
                df1['duration_type'][index] = 'season'

        #######################################################################
        # TRASFORMO TODOS LOS STRINGS EN LETRAS MINUSCULAS.
        #######################################################################

        df1['id'] = df1['id'].str.lower()

        df1['type'] = df1['type'].str.lower()

        df1['title'] = df1['title'].str.lower()

        df1['director'] = df1['director'].str.lower()

        if type(df1['cast']) == str:         
            df1['cast'] = df1['cast'].str.lower()

        df1['country'] = df1['country'].str.lower()

        df1['date_added'] = df1['date_added'].str.lower()

        df1['rating'] = df1['rating'].str.lower()

        df1['listed_in'] = df1['listed_in'].str.lower()

        df1['description'] = df1['description'].str.lower()

        df1['duration_type'] = df1['duration_type'].str.lower()


        #######################################################################
        # EDITO LA NOMENCLATURA DEL DATETIME A AAAA-MM-DD
        #######################################################################

        df1['date_added'] = pd.to_datetime(df1['date_added'])

        df_final = df1


        return df_final

    def load(self, path):

        '''
        Lo bajo de nuevo a un csv
        
        '''

        #######################################################################
        # LLAMO A LAS FUNCIONES
        #######################################################################

        df_final = self.transform(path)

        #######################################################################
        # BUSCO LA PLATAFORMA PARA DARLE EL NOMBRE AL NUEVO CSV
        #######################################################################

        platform = self.platform(path)

        if platform == 'a':
            plataforma = 'amazon'

        if platform == 'd':
            plataforma = 'disney'

        if platform == 'h':
            plataforma = 'hulu'

        if platform == 'n':
            plataforma = 'netflix'


        df_final.drop(['description'], axis='columns', inplace=True)
        
        csv = f"{plataforma}.csv"

        df_final.to_csv(plataforma+'.csv')
        
        return csv


    def complete(self, path):

        csv = self.load(path)

        #######################################################################
        # COMANDO PARA MOVER LA DATA A LA CARPETA DATASETS
        #######################################################################

        command1 = "cd /home/ezequiell/Escritorio/PI1_DETA/PI1"
        command2 = f"mv {csv} /home/ezequiell/Escritorio/PI1_DETA/PI1/Transformaciones/Datasets" 
        
        os.system(command1)
        os.system(command2)
