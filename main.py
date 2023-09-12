# загружаем библиотеки

import cv2
from pyagender import PyAgender
import numpy as np

# создаем объект и загружает изображение

agender = PyAgender()
img = cv2.imread("1.jpg")

# сопределяем характеристики объекта используя метод detect_genders_ages

face_info = agender.detect_genders_ages(img)
