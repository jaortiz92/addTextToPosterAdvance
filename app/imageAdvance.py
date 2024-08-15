from typing import Tuple
from PIL import Image, ImageDraw, ImageFont
from PIL.PngImagePlugin import PngImageFile
from PIL.ImageFont import FreeTypeFont
from .constants import Constants
from .utils import Utils

class ImageAdvance:
    def __init__(
            self, name: str, total: str, units: str, 
            advance_value: str, add_advance: bool = True
        ) -> None:
        self.name: str = name
        self.total: str = total
        self.units: str = units
        self.advance_value: str = advance_value
        self.add_advance: bool = add_advance
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
        self.image: PngImageFile = Image.open(Constants.IMAGE_PATH)
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
        self.add_one_text(
            Constants.FONT_HI_PATH,
            Constants.FONT_NAME_PATH ,
            Constants.SIZE_NAME,
            Constants.TITLE_NAME,
            self.name,
            Constants.Y_NAME,
            Constants.COLOR_NAME
        )

        #UNIT
        self.add_one_text(
            Constants.FONT_TITLE_PATH,
            Constants.FONT_UNIT_PATH,
            Constants.SIZE_UNIT,
            Constants.TITLE_UNIT,
            self.total,
            Constants.Y_UNIT,
            Constants.COLOR_UNIT
        )

        #ORDER_VALUE
        self.add_one_text(
            Constants.FONT_TITLE_PATH,
            Constants.FONT_ORDER_VALUE_PATH,
            Constants.SIZE_ORDER_VALUE,
            Constants.TITLE_ORDER_VALUE,
            self.units,
            Constants.Y_ORDER_VALUE,
            Constants.COLOR_ORDER_VALUE
        )

        #ADVANCE
        if self.add_advance:
            self.add_one_text(
                Constants.FONT_TITLE_PATH,
                Constants.FONT_ADVANCE_PATH,
                Constants.SIZE_ADVANCE,
                Constants.TITLE_ADVANCE,
                self.advance_value,
                Constants.Y_ADVANCE,
                Constants.COLOR_ADVANCE
            )

    def add_one_text(
            self, font_path_one: str, font_path_two: str,
            size: int, text_one: str, text_two: str,
            y_value: int, color: Tuple[int]
        ) -> None:
        '''
            font_path_one: str
                Path to text one's font
            font_path_two: str
                Path to text two's font
            size: int
                Size to text's font
            text_one: str
                Text one
            text_two: str
                Text two
            y_value: int
                Position to y in the image
            color: Tuple[int]
                Color to use in the text

            Parameters
            ----------
            None

            Returns
            -------
            None
        '''

        font_one: FreeTypeFont = ImageFont.truetype(font_path_one, size)
        
        font_two: FreeTypeFont = ImageFont.truetype(font_path_two, size)
        
        sizes: Tuple[int] = Utils.generate_size(
            text_one, text_two,
            font_one, font_two,
        )

        x_name: int = Utils.generate_center_value(sizes[0])

        self.draw.text(
            (x_name, y_value),
            text_one,
            font=font_one,
            fill=color
        )

        self.draw.text(
            (x_name + sizes[2], y_value),
            text_two,
            font=font_two,
            fill=color
        )