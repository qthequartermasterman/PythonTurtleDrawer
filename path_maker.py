import turtle
import random
import io
from PIL import Image
from pathlib import Path


def forward(t, dis=100):
    t.forward(dis)


def backward(t, dis=100):
    t.backward(dis)


def left(t, angle=90):
    t.left(angle)


def right(t, angle=90):
    t.right(angle)


def none(t=None):
    return


def write(t, text):
    t.write(text, font=("Arial", 24, "normal"))


def save(s, filename):
    ps = s.getcanvas().postscript()
    img = Image.open(io.BytesIO(ps.encode('utf-8')))
    img.save(filename)


def draw(number_of_forward_steps=4, filename=Path('./tmp/path.jpg')):
    s = turtle.Screen()
    s.reset()
    t = turtle.Turtle()
    t.speed(0)
    t.pensize(5)
    directions = [left, right]*5 + [none]  # We want left and right turns to be more common than not turning

    write(t, 'Start')  # Place the word 'Start' at the beginning of the path

    for _ in range(number_of_forward_steps):  # We want it to move forward a number of times, defined above
        move_function = random.choice(directions)
        move_function(t)
        forward(t)

    write(t, 'End')  # Place the word 'End' at the end of the path
    save(s, filename)


if __name__ == "__main__":
    type_of_paths = {'Beginner': 3,
                   'Intermediate': 4,
                   'Advanced': 5}
    number_of_each_type = 20

    for type in type_of_paths.keys():
        filedir = Path(f'./{type}')
        filedir.mkdir(parents=True, exist_ok=True)
        for i in range(number_of_each_type):
            filename = filedir / f'path{i}.jpg'
            number_of_moves = type_of_paths[type]
            draw(number_of_forward_steps=number_of_moves, filename=filename)