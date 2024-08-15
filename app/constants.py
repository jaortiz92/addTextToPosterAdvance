from typing import Tuple


class Constants:
    # PATH
    IN: str = './in/'
    BASE: str = 'base/'
    OUT: str = './out/'

        # In
    IMAGE_PATH: str = IN + BASE + 'ARTE-SIN-TITULOS.png'
    FONT_HI_PATH: str = IN + BASE + 'Raleway-Regular.ttf'
    FONT_NAME_PATH: str = IN + BASE + 'Raleway-SemiBoldItalic.ttf'
    FONT_TITLE_PATH: str = IN + BASE + 'Raleway-Regular.ttf'
    FONT_UNIT_PATH: str = IN + BASE + 'Century-Gothic-Bold.ttf'
    FONT_ORDER_VALUE_PATH: str = IN + BASE + 'Century-Gothic-Bold.ttf'
    FONT_ADVANCE_PATH: str = IN + BASE + 'Century-Gothic-Bold.ttf'
    FILE_TO_WORK: str = IN + 'Anticipos.xlsx'
        # Out
        
    # Default
    IMAGE_SIZE: Tuple[int] = (1200, 1800)

    # Parameters
        # Axis
    Y_NAME: int = 620
    Y_UNIT: int = 970
    Y_ORDER_VALUE: int = 1064
    Y_ADVANCE: int = 1160
        # Color
    COLOR_NAME: Tuple[int] = (39, 49, 121)
    COLOR_UNIT: Tuple[int] = (39, 49, 121)
    COLOR_ORDER_VALUE: Tuple[int] = (39, 49, 121)
    COLOR_ADVANCE: Tuple[int] = (39, 49, 121)
        # Size
    SIZE_NAME: int = 80
    SIZE_UNIT: int = 70
    SIZE_ORDER_VALUE: int = 70
    SIZE_ADVANCE: int = 70
        # Title
    TITLE_NAME: str = 'Hola '
    TITLE_UNIT: str = 'Unidades: '
    TITLE_ORDER_VALUE: str = 'Total con IVA '
    TITLE_ADVANCE: str = 'Anticipo '
