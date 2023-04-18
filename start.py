import turtle

# Скорость анимации
speed = 5


def start():
    """Стартовая позиция и настройка"""

    # Настройка черепашки
    turtle.speed(1000)
    turtle.hideturtle()
    turtle.pencolor("red")
    turtle.pensize(5)

    # Стартовая позиция черепашки
    turtle.up()
    turtle.goto(-200, 0)
    turtle.down()


def first_heart_beat():
    """Первый стук сердца"""

    turtle.forward(50)
    turtle.goto(turtle.pos() + (15, 40))
    turtle.goto(turtle.pos() + (15, -40))
    turtle.forward(10)
    turtle.goto(turtle.pos() + (5, -15))
    turtle.goto(turtle.pos() + (5, 15))
    turtle.forward(5)
    turtle.goto(turtle.pos() + (10, 75))
    turtle.goto(turtle.pos() + (10, -150))
    turtle.goto(turtle.pos() + (10, 100))
    turtle.goto(turtle.pos() + (5, -50))
    turtle.forward(10)
    turtle.goto(turtle.pos() + (5, 25))
    turtle.forward(25)


def second_heart_beat():
    """Второй стук сердца"""

    turtle.forward(50)
    turtle.goto(turtle.pos() + (15, 40))
    turtle.goto(turtle.pos() + (15, -40))
    turtle.forward(10)
    turtle.goto(turtle.pos() + (5, -15))
    turtle.goto(turtle.pos() + (5, 15))
    turtle.forward(5)
    turtle.goto(turtle.pos() + (10, 75))
    turtle.goto(turtle.pos() + (10, -150))
    turtle.goto(turtle.pos() + (10, 100))
    turtle.goto(turtle.pos() + (5, -25))
    turtle.forward(60)


def heart(start_pos: tuple, speed: int):
    """Основа сердца"""

    turtle.pencolor("red")
    turtle.goto(-10, -300)
    turtle.goto(-200, 0)
    turtle.left(120)
    turtle.forward(100)
    rad = (-10 - turtle.xcor()) // 2
    turtle.right(30)
    turtle.speed(speed * 2)
    turtle.circle(-rad, 180)
    turtle.circle(rad, -180)
    turtle.speed(speed)
    turtle.goto(start_pos)


if __name__ == "__main__":
    # Запуск черепашки
    start()

    # Установка скорости
    turtle.speed(speed=speed)

    # Первый стук
    first_heart_beat()

    # Второй стук
    second_heart_beat()

    # Сердце
    heart(start_pos=turtle.pos(), speed=speed)

    # Завершение программы
    turtle.done()
