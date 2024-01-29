import arcade


class Draw(arcade.Window):
    def __init__(self):
        super().__init__(600,600,"Complex Loops-Box")
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        arcade.start_render()
        center_x = 400
        center_y = 200
        counter_1 = 0
        counter_2 = 0
        for item in range(10):
            if item % 2 == 0:
                counter_2 = 0
                for j in range(10):
                    if j % 2 == 0:
                        arcade.draw_rectangle_filled(center_x-counter_1, center_y+ counter_2, 10, 10, arcade.color.BLUE, 45)
                        counter_2 += 25
                    elif j % 2 == 1 :
                        arcade.draw_rectangle_filled(center_x-counter_1, center_y+ counter_2, 10, 10, arcade.color.RED, 45)
                        counter_2 += 25
            elif item % 2 == 1:
                counter_2 = 0
                for j in range(10):
                    if j % 2 == 0:
                        arcade.draw_rectangle_filled(center_x-counter_1, center_y+ counter_2, 10, 10, arcade.color.RED, 45)
                        counter_2 += 25
                    elif j % 2 == 1 :
                        arcade.draw_rectangle_filled(center_x-counter_1, center_y+ counter_2, 10, 10, arcade.color.BLUE, 45)
                        counter_2 += 25
            counter_1 += 25
        arcade.finish_render
                

Square=Draw()
arcade.run()













