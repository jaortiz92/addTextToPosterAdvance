from typing import Tuple
from PIL import Image, ImageDraw, ImageFont
from PIL.PngImagePlugin import PngImageFile
from PIL.ImageFont import FreeTypeFont
from .constants import Constants
from .utils import Utils

class ImageAdvance:
    def __init__(
            self, name: str, total: str, units: str, 
            advance_value: str, add_advance: bool = True,
            step: int = 1, brand: str = '', season: str = ''
        ) -> None:
        self.name: str = name
        self.total: str = total
        self.units: str = units
        self.advance_value: str = advance_value
        self.add_advance: bool = add_advance
        self.step: int = step
        self.brand: str = brand
        self.season: str = season
        self.open_image()
        self.add_texts()
        Utils.save_image(self.name, self.image)

    def open_image(self) -> None:
        '''
            Open image to use

            Parameters
            ----------
            None

            Returns
            -------
            None
        '''
        if self.step == 2:
            dict_images: dict = Constants.IMAGES.get(
                    self.season,
                    Constants.IMAGES['I24']
            )
            self.image: PngImageFile = Image.open(
                dict_images.get(
                    self.brand,
                    dict_images['DEFAULT']
                )
            )
        else:
            self.image: PngImageFile = Image.open(
                Constants.IMAGES['DEFAULT']
            )

        self.draw: ImageDraw.ImageDraw = ImageDraw.Draw(self.image)

    def add_texts(self) -> None:
        '''
            add all texts to image

            Parameters
            ----------
            None

            Returns
            -------
            None
        '''
        #NAME
        Utils.add_one_text(
            self.draw,
            Constants.FONT_HI_PATH,
            Constants.FONT_NAME_PATH ,
            Constants.SIZE_NAME,
            Constants.TITLE_NAME,
            self.name,
            Constants.Y_NAME,
            Constants.COLOR_NAME
        )

        #UNIT
        Utils.add_one_text(
            self.draw,
            Constants.FONT_TITLE_PATH,
            Constants.FONT_UNIT_PATH,
            Constants.SIZE_UNIT,
            Constants.TITLE_UNIT,
            self.units,
            Constants.Y_UNIT,
            Constants.COLOR_UNIT
        )

        #ORDER_VALUE
        Utils.add_one_text(
            self.draw,
            Constants.FONT_TITLE_PATH,
            Constants.FONT_ORDER_VALUE_PATH,
            Constants.SIZE_ORDER_VALUE,
            Constants.TITLE_ORDER_VALUE,
            self.total,
            Constants.Y_ORDER_VALUE,
            Constants.COLOR_ORDER_VALUE
        )

        #ADVANCE
        if self.add_advance:
            Utils.add_one_text(
                self.draw,
                Constants.FONT_TITLE_PATH,
                Constants.FONT_ADVANCE_PATH,
                Constants.SIZE_ADVANCE,
                Constants.TITLE_ADVANCE,
                self.advance_value,
                Constants.Y_ADVANCE,
                Constants.COLOR_ADVANCE
            )

    