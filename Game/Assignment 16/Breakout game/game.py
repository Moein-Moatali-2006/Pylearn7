import random
import time
import arcade
from box import Box
from board import Board
from ball import Ball
from hearts import Heart

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=800,height=600,title="Breakout V1")
        arcade.set_background_color(arcade.color.BLACK)
        self.boxes=[]
        self.board=Board(self.width//2,40)
        self.ball=Ball(self)
        self.hearts=[]
        self.end_play=False
        self.end=False
        for item in range(15):
            box=Box(random.randint(0+40,self.width-40),random.randint(self.height//2-40,self.height-40))
            self.boxes.append(box)
        
        for item in range(1,4):
            herat=Heart(item)
            self.hearts.append(herat)
            

    def on_draw(self):
        arcade.start_render()
        arcade.draw_line(0,20,0,self.height-10,arcade.color.YELLOW,line_width=20)
        arcade.draw_line(0,self.height,self.width,self.height,arcade.color.YELLOW,line_width=20)
        arcade.draw_line(self.width,self.height,self.width,20,arcade.color.YELLOW,line_width=20)
        for box in self.boxes:
            box.draw()
        for heart in self.hearts:
            heart.draw()
        self.board.draw()
        self.ball.draw()
        arcade.draw_text(f"Score:{self.board.score}",25,self.height-25,arcade.color.PINK)
        if self.end_play == True:
            arcade.draw_text(f"Game over",self.width//2-20,self.height//2,arcade.color.WHITE,font_size=30)
            self.end=True
        arcade.finish_render()

    
    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.RIGHT:
            self.board.change_x = +1
        if symbol == arcade.key.LEFT:
            self.board.change_x = -1

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        if self.board.center_x < x:
            self.board.center_x=x
        
        if self.board.center_x > x:
            self.board.center_x =x

    def on_update(self, delta_time: float):
        
        self.board.move()
        self.ball.move()

        if self.ball.center_x < 20:
            self.ball.change_x *= -1

        if self.ball.center_x > self.width:
            self.ball.change_x *= -1

        if self.ball.center_y > self.height-20:
            self.ball.change_y *= -1

        if self.ball.center_y < 0:
            self.board.score-=1
            self.hearts.pop()
            del self.ball
            self.ball=Ball(self)

        if len(self.hearts) == 0:
            self.end_play = True

        if self.end == True:
            time.sleep(10)
            exit(0)

        if arcade.check_for_collision(self.board,self.ball):
            self.ball.change_y *= -1

        for item in self.boxes:
            if arcade.check_for_collision(item , self.ball):
                self.board.score+=1
                self.boxes.remove(item)



       
