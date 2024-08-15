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
        self.advances: DataFrame = Advance().advance

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
        imagens: int = len(self.advances)
        print('Se crearan {} imagenes'.format(imagens))
        for i in self.advances.index:
            print('Generando imagen {} de {}'.format(i + 1, imagens))
            ImageAdvance(
                self.advances.loc[i, 'NOMBRE'],
                self.advances.loc[i, 'TOTAL_CON_IVA'],
                self.advances.loc[i, 'UNIDADES'],
                self.advances.loc[i, 'VALOR_ANTICIPO'],
                self.advances.loc[i, 'AGREGAR_ANTICIPO'],
            )
        print('Proceso Completado')


