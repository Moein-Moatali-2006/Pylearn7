import time
import arcade
from fruits import Apple
from fruits import Pear
from fruits import PP
from snake import Snake

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=600,height=600,title="Super Snake 🐍 V1")
        arcade.set_background_color(arcade.color.KHAKI)

        self.food=Apple(self)
        self.new_food=Pear(self)
        self.shit=PP(self)
        self.snake=Snake(self)
        self.game_over="Game Over"
        self.end_play=False
        self.play=True
        

    def on_draw(self):
        arcade.start_render()
        self.food.draw()
        self.snake.draw()
        self.new_food.draw()
        self.shit.draw()
        arcade.draw_text(f"Score:{self.snake.score}", self.width-120, 15, font_size=20, color=arcade.color.RED)
        if self.end_play:
            arcade.draw_text(self.game_over, 100, 100, font_size=50, color=arcade.color.BLACK)
            self.play=False
            
            

        arcade.finish_render()

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.UP:
            self.snake.change_x=0
            self.snake.change_y=1
        elif symbol == arcade.key.DOWN:
            self.snake.change_x=0
            self.snake.change_y=-1
        elif symbol == arcade.key.LEFT:
            self.snake.change_x=-1
            self.snake.change_y=0
        elif symbol == arcade.key.RIGHT:
            self.snake.change_x=1
            self.snake.change_y=0

    def on_update(self, delta_time: float):
        self.snake.move()

        if (self.snake.center_x > self.width) or (self.snake.center_x < 0) or (self.snake.center_y > self.height) or (self.snake.center_y < 0):
            self.end_play=True

        if arcade.check_for_collision(self.food , self.snake):
            self.snake.eat(self.food)
            self.food=Apple(self)

        if arcade.check_for_collision(self.snake , self.new_food):
            self.snake.eat(self.new_food)
            self.new_food=Pear(self)
            self.snake.score += 1

        if arcade.check_for_collision(self.snake ,self.shit):
            self.snake.eat(self.shit)
            self.shit=PP(self)
            self.snake.score = self.snake.score - 2
        
        
        for part in self.snake.body:
            if self.snake.center_x == part["x"] and self.snake.center_y == part["y"]:
                self.end_play=True
        

        if self.snake.score < 0 :
            self.end_play = True

        if self.play ==False:
            time.sleep(5)
            print(f"Your Score:{self.snake.score}")
            print("Thank you,I hope you will be good luck!")
            exit(0)




        

game=Game()
arcade.run()