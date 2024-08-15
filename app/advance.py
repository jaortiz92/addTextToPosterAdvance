import pandas as pd
from pandas.core.frame import DataFrame
from pandas.core.series import Series
from .constants import Constants

class Advance:
    def __init__(self) -> None:
        self.open_files()
        self.clean_file()


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
        self.advance: DataFrame = pd.read_excel(
            Constants.FILE_TO_WORK,
            dtype={
                'CLIENTE': str
            }
        )

    def clean_file(self) -> None:
        '''
        This function clean advance file

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        self.advance = self.advance.assign(
            NOMBRE = lambda df: df['CLIENTE'].str.title() + '!',
            AGREGAR_ANTICIPO = lambda df: df['ANTICIPO'] != 0,
            ANTICIPO = lambda df: df['ANTICIPO'].apply(
                lambda x:'{:.0f}% '.format(x * 100)
            ),
            UNIDADES = lambda df: df['UNIDADES'].apply(
                lambda x:'{:,.0f}'.format(x)
            ).str.replace(',', '.'),
            TOTAL_CON_IVA = lambda df: df['TOTAL CON IVA'].apply(
                lambda x:'${:,.0f}'.format(x)
            ).str.replace(',', '.'),
            VALOR_ANTICIPO = lambda df: df['ANTICIPO'] + df['VALOR ANTICIPO'].apply(
                lambda x:'${:,.0f}'.format(x)
            ).str.replace(',', '.')
        )