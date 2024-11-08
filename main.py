import json as js
import cv2 as cv
import numpy as np

with open('config.json', 'r', encoding='utf-8') as config_file:
    cf = js.load(config_file)

print("Проект для En+ 24/25. Версия: " + cf["version"])
print("Нижняя граница: " + str(cf["RED"][0]))