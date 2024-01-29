import arcade


class SpaceShip(arcade.Sprite):
    def __init__(self,w,h):
        super().__init__(":resources:images/space_shooter/playerShip1_blue.png")
        self.speed=8
        self.center_x=w/2
        self.center_y=80
        self.width=48
        self.height=48