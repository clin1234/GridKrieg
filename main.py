from direct.showbase.ShowBase import ShowBase
from direct.gui.OnscreenImage import OnscreenImage

from panda3d.core import Texture
from panda3d.core import TransparencyAttrib
from panda3d.core import WindowProperties

import grid


class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        properties = WindowProperties()
        properties.setSize(1000, 750)
        self.win.requestProperties(properties)

        loadGraphics()

    def loadGraphics(self):
        envion = loader.loadModel("models/environment")

        land = OnscreenImage(image="textures/land.png")
        land.setTransparency(TransparencyAttrib.MAlpha)
        water = OnscreenImage(image="textures/water.png")
        water.setTransparency(TransparencyAttrib.MAlpha)

    def camera(self):
        self.camera.setPos(0,0,32)
        self.camera.setP(-90)
