#Moein Moatali
import turtle

# تنظیمات اولیه
wn = turtle.Screen()
wn.title("Moein Moatali")
wn.bgcolor("white")

pen = turtle.Turtle()
pen.speed(15)
pen.color("black")

# تعداد اضلاع شکل اولیه
num_sides = 3
length = 100  # طول هر ضلع

# تابع برای رسم یک چندضلعی
def draw_shape(sides, len):
    angle = 360 / sides
    for _ in range(sides):
        pen.forward(len)
        pen.right(angle)

# تابع برای تغییر تعداد ضلع‌ها و رسم شکل
def draw_tour(iterations):
    global num_sides
    for _ in range(iterations):
        draw_shape(num_sides, length)
        num_sides += 1  # افزایش تعداد اضلاع برای دور بعدی

# رسم اولین چندضلعی
draw_shape(num_sides, length)

# انجام تور با افزایش تعداد ضلع‌ها
draw_tour(10)

# پایان برنامه در صورت کلیک بر روی صفحه
wn.mainloop()







