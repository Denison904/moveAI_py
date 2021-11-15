import math

import numpy as np
class Object:
    def __init__(self, line_speed: float, angular_speed: float, coord) -> None:
        self.__line_speed = line_speed
        self.__angular_speed = angular_speed
        self.__coord = coord
        self.__cource = 0
        pass

    def set_cource(self, cource: float) -> None:
        self.__cource = cource
        pass
    
    def set_line_speed(self, speed: float) -> None:
        self.__line_speed = speed
        pass
    
    def set_angular_speed(self, speed: float) -> None:
        self.__angular_speed = speed
        pass

    def set_vision(self, vision: float) -> None:
        self.__vision = vision
        pass
    
    def set_coord(self, coord: np.ndarray) -> None:
        self.__coord = coord
        pass

    def set_X(self, x: float) -> None:
        self.__coord[0] = x
        pass

    def set_Y(self, y: float) -> None:
        self.__coord[1] = y
        pass

    def move(self, d_time) -> None: # TODO!
        self.__coord[0] -= d_time * math.sin(self.__angular_speed * d_time) * self.__line_speed
        self.__coord[1] += d_time * math.cos(self.__angular_speed * d_time) * self.__line_speed
        pass

    def get_coord(self):
        return self.__coord