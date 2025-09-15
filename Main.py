import Painter
import numpy as np
import math
from Eiler import *
from RosslerAttractor import RosslerAttractor
from RungeKutta2 import RungeKutta2
from RungeKutta4 import RungeKutta4
from CD import CD


def solve(metod, time, h, X, a, rossler, name):
    X1 = metod.getAns(time, h, X, a, rossler)
    Painter.draw(X1, h, name)
    Painter.draw_3d(X1, name)


def getDeviation(metod, time, h, X, a, rossler, name):
    X1 = metod.getAns(time, h, X, a, rossler)
    X2 = RungeKutta4().getAns(time, h, X, a, rossler)
    X1_np = np.array(X1)
    X2_np = np.array(X2)

    # Разница между массивами
    difference = X2_np - X1_np
    print(difference)
    Painter.draw(difference, h, name, True)
    #Painter.draw_3d(difference, name)


if __name__ == "__main__":
    rossler = RosslerAttractor()  # Создаем экземпляр класса
    X = [0.1, 0.1, 0.1]
    a = [0.5, 10, 28, 8/3]
    time = 100
    h = 0.00001
    solve(Eiler(), time, h, X, a, rossler, "Метод эйлера")
    solve(RungeKutta2(), time, h, X, a, rossler, "Неявный метод Рунге — Кутты второго порядка")
    solve(CD(), time, h, X, a, rossler, "КД")
    solve(RungeKutta4(), time, h, X, a, rossler, "Классический метод Рунге — Кутты четвёртого порядка")
    getDeviation(Eiler(), time, h, X, a, rossler, "Метод эйлера – ошибка")
    getDeviation(CD(), time, h, X, a, rossler, "КД – ошибка")
    #getDeviation(CD(), time, 0.00001, X, a, rossler, "КД")
    getDeviation(RungeKutta2(), time, 0.00001, X, a, rossler, "Неявный метод Рунге — Кутты второго порядка– ошибка")
    #getDeviation(RungeKutta2(), time, 0.000001, X, a, rossler, "Неявный метод Рунге — Кутты второго порядка– ошибка")
