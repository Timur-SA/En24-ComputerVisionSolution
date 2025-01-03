import cv2 as cv
#import numpy as np
import os
from InitConfig import *
from RobotCommunicate import NetControl
from ImageProcessing import ImageProcessor
from CameraInput import CaptureImage
import time


class PIDController:
    def __init__(self, Kp, Ki, Kd):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.previous_error = 0
        self.integral = 0
        self.last_time = time.time()

    def update(self, error):
        current_time = time.time()
        dt = current_time - self.last_time
        self.last_time = current_time

        p_term = self.Kp * error
        i_term = self.Ki * self.integral
        d_term = self.Kd * (error - self.previous_error) / dt
        self.integral += error * dt
        self.previous_error = error

        output = p_term + i_term + d_term
        return output


# Настройки PID-контроллера
Kp = 0.5  # Пропорциональный коэффициент
Ki = 0.001  # Интегральный коэффициент
Kd = 0.05  # Дифференциальный коэффициент

pid_controller = PIDController(Kp, Ki, Kd)
robot_controller = NetControl()
camera_capture = CaptureImage()

while True:
    # Захватываем кадр с камеры
    frame = camera_capture.GetImage()

    # Находим направление линии
    direction = ImageProcessor().find_direction_of_line(frame)

    if direction is not None:
        # Направление найдено, корректируем движение робота
        error = direction - 0  # Предполагаем, что идеальное направление - 0 градусов
        correction = pid_controller.update(error)

        # Скорректированное движение робота
        if correction > 0:
            robot_controller.MoveLeft()
        elif correction < 0:
            robot_controller.MoveRight()
        else:
            robot_controller.MoveForward()
    else:
        # Линия не найдена, останавливаемся
        robot_controller.MoveStop()
