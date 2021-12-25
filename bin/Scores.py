
#Packages
# Standard library imports
from datetime import date
import csv 
import os
import numpy as np
import pandas as pd

# Local library imports
import Juego, logger




class score(object):
    """Esta clase gestiona la escritura y lectura de los resultados"""
    def __init__(self):
        self.file_name = "./scores/partidas.csv"
        self.columnas = ['fecha', 'nombre_P1', 'nombre_P2', 'ganador', 'jugada_P1', 'jugada_P2']
        self.df = None
    


    def _write_row(self,  msg) -> None:
        """Writes a message to the fle_name for a specifc Logger instance"""
        with open(self.file_name, mode ='a',newline ='\n') as csvfile:
            csvwriter = csv.writer(csvfile) 
            csvwriter.writerow(msg)
        return None

    
    # lee resultados, escribe
    # fecha nombre jugador1 nombre jugadore2 ganador jugador1 jugador 2

    def escribir_resultados(self,nombre_jugador_1,nombre_jugador_2,ganador,eleccion_jugador1,eleccion_jugador2)-> None:
        """Escribe el resutlado de una partida en el csv scores"""
        #nombre_jugador_1 ='adry'
        #nombre_jugador_2 ='NPC'
        #ganador = 1
        #eleccion_jugador1 = 'Piedra'
        #eleccion_jugador2 = 'Tijera'
        
        today = date.today()
        hoy = today.strftime("%Y-%m-%d")
        row = [hoy,nombre_jugador_1,nombre_jugador_2,ganador,eleccion_jugador1,eleccion_jugador2 ]
        self._write_row(row)

        return None 
    
    def leer(self)-> None:

        """Lee valores de resultados pasados y los escribe como un dataframe llamado results"""
        results = pd.DataFrame(columns = self.get_columns())
        columnas = self.get_columns()
        with open(self.file_name, mode ='r',newline ='\n') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',')
            
            for row in spamreader:
                aux = np.array(row).reshape(1,len(columnas))
                df_aux = pd.DataFrame(aux, columns=columnas)
                results = pd.concat([results,df_aux])
                self.set_df(results)
        return None       


    def Tops(self)-> pd.DataFrame:
        """calculo de tops: pctge de victorias , numero victorias, numero de partidas """
        df = self.get_df().copy()

        #procesamiento de datos
        dfa = pd.concat([df['nombre_P1'].value_counts().rename('Partidas'),df.groupby('nombre_P1')['ganador'].sum().rename('Victorias')], axis=1)

        dfa['pctge_Victorias'] = dfa['Victorias']/dfa['Partidas']
        dfa.sort_values(by=['pctge_Victorias'], ascending=False,inplace =True)
        dfa = dfa[['pctge_Victorias','Victorias','Partidas']]
        return dfa

    def get_columns(self)-> list:
        return self.columnas

    def get_df(self)-> pd.DataFrame:
        aux =   self.df
        aux['ganador'] = aux['ganador'].astype('int64')
        return aux
    
    def set_df(self,df)-> None:
        self.df = df
        return None

if __name__ == '__main__':
    print("Hellowis")