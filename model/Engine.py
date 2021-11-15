from numpy.core.fromnumeric import size
from Area import Area
from Object import Object
import numpy as np
import random as rd

class Engine:
    # __area = Area
    # __enemy = np.array(type = Object)
    # __main = Object
    # __d_time = 1e-2
    # __radius = 1
    def __init__(self, hight, width, vision, line_speed, angular_speed, count_enemy, max_line_speed_enemy, max_angular_speed_enemy, d_time, gauss_sigma = 10 , gauss_mu = 10) -> None:
        self.__area = Area(hight, width, count_enemy)
        self.__main = Object(line_speed, angular_speed, np.array([width/2, hight/2]))
        self.__vision = vision
        self.__d_time = d_time
        self.__enemy = np.arange(count_enemy)
        random_x = np.random.uniform(0, width, (1, count_enemy))
        random_y = np.random.uniform(0, hight, (1, count_enemy))
        for i in range(count_enemy) :
            self.__enemy[i] = Object(np.random.gauss(gauss_mu, gauss_sigma) * max_line_speed_enemy, rd.random.gauss(gauss_mu, gauss_sigma) * max_angular_speed_enemy)
            self.__enemy[i].set_coord(np.array([random_x[i], random_y[i]]))
        pass
    
    # start model
    # return number of iteration
    def start(self):
        pass
    
    # Generate new enemy and new main object
    def restart(self):
        pass
    

    def __check_colision(self):
        main_coord = self.__main.get_coord()
        for i in range(self.__enemy.shape[1]):
            if np.sum(main_coord ** 2 - self.__enemy[i].get_coord() ** 2) <= 1:
                return True
        return False