import arcade
from ball import Ball
from rocket import Rocket


class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=800,height=600,title="Pong V1")
        arcade.set_background_color(arcade.color.BLACK)
        self.ball = Ball(self)
        self.player_1 = Rocket(35,self.height//2,arcade.color.BLUE,"User")
        self.player_2 = Rocket(self.width-35 , self.height//2 ,arcade.color.RED ,"AI")

    
    def on_draw(self):
        arcade.start_render()
        self.player_1.draw()
        self.player_2.draw()
        arcade.draw_rectangle_outline(self.width//2,self.height//2,self.width-30,self.height-30,arcade.color.WHITE,10)
        arcade.draw_line(self.width//2,30,self.width//2,self.height-30,arcade.color.WHITE,line_width=10)
        self.ball.draw()
        arcade.draw_text(f"Score:{self.player_1.score}",self.width//2 -100 ,40,arcade.color.BLUE,15)
        arcade.draw_text(f"Score:{self.player_2.score}",self.width//2 +30 ,40,arcade.color.RED,15)
        arcade.finish_render()

    def on_key_release(self, symbol: int, modifiers: int):
        super().on_key_release(symbol, modifiers)
        if symbol == arcade.key.UP:
            self.player_1.change_y = +1
            self.player_1.center_y += self.player_1.change_y * self.player_1.speed*3
        
        if symbol == arcade.key.DOWN:
            self.player_1.change_y = -1
            self.player_1.center_y += self.player_1.change_y * self.player_1.speed*3

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        if self.player_1.center_y < y < self.height-70:
            self.player_1.center_y = y

        if self.player_1.center_y > y > 70:
            self.player_1.center_y = y

    def on_update(self, delta_time: float):
        self.ball.move()
       
        self.player_2.move(self,self.ball)
        

        if self.ball.center_y < 30 or self.ball.center_y > self.height -30 :
            self.ball.change_y *= -1

        if (arcade.check_for_collision(self.player_1,self.ball)) or (arcade.check_for_collision(self.player_2,self.ball)):
            self.ball.change_x *= -1

        if self.ball.center_x < 0 :
            self.player_2.score+=1
            del self.ball
            self.ball=Ball(self)

        if self.ball.center_x > self.width :
            self.player_1.score+=1
            del self.ball
            self.ball=Ball(self)


game=Game()
arcade.run()