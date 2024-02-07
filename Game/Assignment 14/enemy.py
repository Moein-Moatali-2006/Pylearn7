import random
import arcade



class Enemy(arcade.Sprite):
    enemies=[]
    def __init__(self,width,height):
        super().__init__(":resources:images/space_shooter/playerShip1_orange.png")
        self.center_x=random.randint(0,width)
        self.center_y=height+24
        self.angle=180
        self.width=48
        self.height=48
        Enemy.enemies.append(self)
        self.speed=len(Enemy.enemies)//2

    def move(self):
        self.center_y-=self.speed