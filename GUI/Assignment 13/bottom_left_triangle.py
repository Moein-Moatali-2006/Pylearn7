import arcade

COLUMN_SPACING = 20
ROW_SPACING = 20
LEFT_MARGIN = 110
BOTTOM_MARGIN = 110

arcade.open_window(400,400,"Complex Loops - Bottom Left Triangle")
arcade.set_background_color(arcade.color.WHITE)

arcade.start_render()

for item in range(10):
    for i in range(10 - item):
        x=i * COLUMN_SPACING + LEFT_MARGIN
        y=item * ROW_SPACING + BOTTOM_MARGIN

        arcade.draw_circle_filled(x,y,7,arcade.color.AO)

arcade.finish_render()
arcade.run()