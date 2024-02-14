import random
import arcade


class Snake(arcade.Sprite):
    def __init__(self,game):
        super().__init__()
        self.width=32
        self.height=32
        self.center_x=game.width//2
        self.center_y=game.height//2
        self.speed=4
        self.change_x=0
        self.change_y=0
        self.body=[]
        self.score=0
        self.color=arcade.color.BLACK
        self.colors=[arcade.color.RED,arcade.color.GREEN,arcade.color.ORANGE,arcade.color.PURPLE,arcade.color.YELLOW,arcade.color.BROWN,arcade.color.PINK,arcade.color.CRIMSON,arcade.color.GRAY]

    
    def draw(self):
        arcade.draw_rectangle_filled(self.center_x,self.center_y,self.width,self.height,self.color)

        for part in self.body:
            arcade.draw_rectangle_filled(part['x'],part['y'],self.width,self.height,random.choice(self.colors))

    def eat(self,food):
        del food
        self.score += 1
        

    def move(self):
        self.body.append({"x":self.center_x,"y":self.center_y})

        if len(self.body) > self.score:
            self.body.pop(0)
        
        self.center_x += self.change_x * self.speed
        self.center_y += self.change_y * self.speed


    def move_ai(self,center_x,center_y):
        self.body.append({"x" : self.center_x , "y" : self.center_y})
        if len(self.body) > self.score :
            self.body.pop(0)

        if self.center_y > center_y:
            self.center_y -= self.speed

        if self.center_y < center_y:
            self.center_y += self.speed

        if self.center_x < center_x:
            self.center_x += self.speed
            
        if self.center_x > center_x:
            self.center_x -= self.speed

        


