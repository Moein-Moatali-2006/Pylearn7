import arcade


class Heart(arcade.Sprite):
    def __init__(self,x):
        super().__init__("pictures\heart.png")
        self.width=20
        self.height=20
        self.center_x= x*25+20
        self.center_y=15
        
