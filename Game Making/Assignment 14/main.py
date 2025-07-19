import arcade
import time
from spaceship import Spaceship
from enemy import Enemy
from heart import Heart


class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=600,height=600,title='Moein Moatali')
        arcade.set_background_color(arcade.color.DARK_BLUE)
        # self.background=arcade.load_texture(":resources:images/backgrounds/stars.png")
        self.background=arcade.load_texture("Images\BG.jpg")
        self.shoot=arcade.load_sound("Audio\shoot.mp3",False)
        self.bang=arcade.load_sound("Audio\Bang.mp3",False)
        self.me=Spaceship(self)
        self.enemy_list=[]
        self.second=time.time()
        self.heart_list=[]
        self.score=0
        for item in range(3):
            herat=Heart(item)
            self.heart_list.append(herat)

 
    
    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0,0,self.width,self.height,self.background)
        arcade.draw_text("Score:"+str(self.score),self.width-100,20,arcade.color.RED,15,12)

        self.me.draw()

        for heart in self.heart_list:
            heart.draw()

        for enemy in self.enemy_list:
            enemy.draw()

        for bullt in self.me.bullet_list:
            bullt.draw()

        if len(self.heart_list)==0:
            arcade.set_background_color(arcade.color.BLACK)
            arcade.draw_text("GAME OVER",self.width/3.5, self.height/2, arcade.color.RED, 36, 20)
            self.background= arcade.load_texture(":resources:images/backgrounds/stars.png")
            print("Your Score:",self.score)



        arcade.finish_render()

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.LEFT or symbol == arcade.key.A:
            self.me.change_x=-1
        elif symbol == arcade.key.RIGHT or symbol == arcade.key.D:
            self.me.change_x=1
        elif symbol == arcade.key.DOWN:
            self.me.change_x=0

        if symbol == arcade.key.SPACE:
            self.me.fire()
            arcade.play_sound(self.shoot,1)
    

    def on_key_release(self, symbol: int, modifiers: int):
        self.me.change_x=0


    def on_update(self, delta_time: float):
        for enemy in self.enemy_list:
            if enemy.center_y <20:
                self.enemy_list.remove(enemy)
                self.heart_list.pop()
    

        self.me.move()
      
        if time.time()-self.second >= 3:
            self.second=time.time() 
            self.new_enemy=Enemy(self.width,self.height)
            self.enemy_list.append(self.new_enemy)

        for enemy in self.enemy_list:
            enemy.move()
        
        for bullet in self.me.bullet_list:
            bullet.move()



        for enemy in self.enemy_list:
            for bullet in self.me.bullet_list:
                if arcade.check_for_collision(enemy,bullet):
                    arcade.play_sound(self.bang,1)
                    self.score+=1
                    self.enemy_list.remove(enemy)
                    self.me.bullet_list.remove(bullet)

        for enemy in self.enemy_list:
            if arcade.check_for_collision(enemy,self.me):
                print("Game over")
                print("Your Score:",self.score)
                exit(0)

        for bullet in self.me.bullet_list:
            if bullet.center_x > self.height:
                self.me.bullet_list.remove(bullet)




window=Game()
arcade.run()