import pandas as pd
from pandas.core.frame import DataFrame
from pandas.core.series import Series
from .advance import Advance
from .imageAdvance import ImageAdvance
from .constants import Constants
from .utils import Utils

class App:
    def __init__(self) -> None:
        self.open_files()
        self.fit()


    def open_files(self) -> None:
        '''
            Open files to use

            Parameters
            ----------
            None

            Returns
            -------
            None
        '''
        self.df: DataFrame = Advance().advance


    def fit(self) -> None:
        '''
            Use ORDER_VALUE's data to add texts

            Parameters
            ----------
            None

            Returns
            -------
            None
        '''
        imagens: int = len(self.df)
        print('Se crearan {} imagenes'.format(imagens))
        for i in self.df.index:
            print('Generando imagen {} de {}'.format(i + 1, imagens))
            ImageAdvance(
                self.df.loc[i, 'NOMBRE'],
                self.df.loc[i, 'TOTAL_CON_IVA'],
                self.df.loc[i, 'UNIDADES'],
                self.df.loc[i, 'VALOR_ANTICIPO'],
                self.df.loc[i, 'AGREGAR_ANTICIPO'],
                self.df.loc[i, 'PASO'],
                self.df.loc[i, 'MARCA']
            )
