from enum import Enum

class Mode(Enum):
    NORMAL = 'NORMAL'
    GTR = 'GTR'
    MIBAND = 'MIBAND'

class Config:
    _mode = Mode.NORMAL
    _image_width = 360
    _image_height = 360

    @staticmethod
    def enableGtrMode():
        Config._mode = Mode.GTR
        Config._image_width = 454
        Config._image_height = 454

    @staticmethod
    def isGtrMode():
        return Config._mode == Mode.GTR

    @staticmethod
    def enableMibandMode():
        Config._mode = Mode.MIBAND
        Config._image_width = 120
        Config._image_height = 240

    @staticmethod
    def isMibandMode():
        return Config._mode == Mode.MIBAND

    @staticmethod
    def getImageHeight():
        return Config._image_height

    @staticmethod
    def getImageWidth():
        return Config._image_width

    @staticmethod
    def getImageWidthHalf():
        return int(Config._image_width / 2)

    @staticmethod
    def getImageHeightHalf():
        return int(Config._image_height / 2)
