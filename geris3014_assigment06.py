#1
# a) ABDGHEICFJ

#2
class QuizGift:
    def __init__(self, questions):
        self.questions = questions
        self.time_limit = 100
        # lage sånn dynamic program med sånn 2d diagram ting
        self.dp = [[0 for i in range(self.time_limit + 1)] for i in range(len(questions) + 1)]

    def compute_result(self):
        for i in range(1, len(self.questions) + 1):
            for t in range(self.time_limit + 1):
                if self.questions[i-1][1] <= t:
                    self.dp[i][t] = max(self.dp[i-1][t], self.questions[i-1][0] + self.dp[i-1][t - self.questions[i-1][1]])
                else:
                    # Carryon poeng
                    self.dp[i][t] = self.dp[i-1][t]

        # FInne max
        max_points = max(self.dp[-1])
        return max_points

    def print_result(self, max_points):
        if max_points <= 250:
            gift = "a watch"
        elif max_points <= 750:
            gift = "a smartphone"
        else:
            gift = "a laptop"

        print(f"Max points:{max_points}")
        print(f"Gift: {gift} ")

#eksempel
questions = [
    (120, 15), # Question 1
    (200, 20), # Question 2
    (150, 40), # Question 3
    (350, 50), # Question 4
    (100, 20), # Question 5
    (90, 10)   # Question 6
]

quiz = QuizGift(questions)
max_points = quiz.compute_result()
quiz.print_result(max_points)

#3
from abc import ABC, abstractmethod
from math import sqrt


class Shape(ABC):
    @abstractmethod
    def compute_area(self):
        pass


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def compute_area(self):
        area = self.side*self.side
        print(f"{area}")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def compute_area(self):
        area = 3.14 * self.radius * self.radius
        print(f"{area}")


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def compute_area(self):
        s = (self.a+self.b+self.c)/2
        area = sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))
        print(f"{area}")


my_square = Square(2)
my_circle = Circle(2)
my_triangle = Triangle(5, 4, 3)
print('Area of square:', end=' ')
my_square.compute_area()
print('Area of circle:', end=' ')
my_circle.compute_area()
print('Area of triangle:', end=' ')
my_triangle.compute_area()


#4
class House:
    count = 0

    def __init__(self, owner, condition, price):
        self.owner = owner
        self.condition = condition
        self.price = price
        self.cost = 0
        self.sold = False
        House.count += 1

    def sell(self, new_owner):
        self.owner = new_owner
        self.sold = True
        print('House sold! Profit: ', self.price - self.cost)

    def change_price(self, new_price):
        if self.sold:
            print('House has been sold!')
        else:
            self.price = new_price

    def renovate(self, expense, new_condition):
        self.cost += expense
        self.condition = new_condition
        print('House renovated!')

    def print_info(self):
        print('Owner: ', self.owner, ', Condition: ', self.condition, ', Price: ', self.price)

house1 = House('John', 'Good', 100000)
house2 = House('Mary', 'Bad', 250000)

house1.print_info()
house2.print_info()
house1.renovate(50000, 'Great')
house1.sell('Leo')
house1.print_info()
print('Total number of houses: ', House.count)
