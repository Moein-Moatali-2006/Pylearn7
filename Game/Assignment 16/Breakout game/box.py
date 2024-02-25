import arcade


class Box(arcade.Sprite):
    def __init__(self,center_x,center_y):
        super().__init__("pictures\Box.png")
        self.width = 38
        self.height = 38
        self.center_x = center_x
        self.center_y = center_y
        self.change_x = 0
        self.change_y = 0

