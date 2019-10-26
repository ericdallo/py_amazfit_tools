from watchFaceParser.models.elements.watchFace import WatchFace
from watchFaceParser.config import Config
from PIL import Image, ImageDraw

class PreviewGenerator:

    @staticmethod
    def createAnimation(descriptor, images, states):
        previewWatchFace = WatchFace(descriptor)
        for watchState in states:
            image = PreviewGenerator.createFrame(previewWatchFace, images, watchState)
            yield image


    @staticmethod
    def createImage(descriptor, images, state):
        previewWatchFace = WatchFace(descriptor)
        return PreviewGenerator.createFrame(previewWatchFace, images, state)


    @staticmethod
    def createFrame(watchFace, resources, state):
        graphics = Image.new('RGBA', (Config.getImageWidth(), Config.getImageHeight()))
        watchFace.draw3(graphics, resources, state)
        return graphics
