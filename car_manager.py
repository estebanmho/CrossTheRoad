COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle
import random


class CarManager:

    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def include_new_car(self):
        aux_car = CarManager.Car(random.choice(COLORS))
        self.cars.append(aux_car)

    def increment_level(self):
        self.speed += MOVE_INCREMENT

    def move_cars(self):
        for car in self.cars:
            car.forward(self.speed)
            if car.xcor() < -300:
                self.cars.remove(car)

    def detect_collision(self, player):
        for car in self.cars:
            if (car.ycor() in range(int(player.ycor()-13), int(player.ycor()+13))) and (car.distance(player) < 25):
                return True
        return False

    class Car(Turtle):
        def __init__(self, colore):
            super().__init__("square")
            self.color(colore)
            self.penup()
            self.setheading(180)
            self.shapesize(stretch_wid=1, stretch_len=2)
            self.goto(x=300, y=random.randint(-240, 240))
            self.speed("fastest")
