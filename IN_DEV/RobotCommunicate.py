import requests
import time
import os


print("Для запуска введите 2 последние цифры IP")
ipBytes = [input("Первое число: "), input("Второе число: ")]
ip = f"192.168.{ipBytes[0]}.{ipBytes[1]}"


def Timer(timerTime, deltaTime):
    while(timerTime>0):
        timerTime -= deltaTime
        print(".")
        time.sleep(deltaTime)

def MoveForward():
    response = requests.get(f"http://{ip}/f")
    print(f"Вперёд")

def MoveBack():
    response = requests.get(f"http://{ip}/b")
    print(f"Назад")

def MoveRight():
    response = requests.get(f"http://{ip}/r")
    print(f"Вправо")

def MoveLeft():
    response = requests.get(f"http://{ip}/l")
    print(f"Влево")

def MoveStop():
    response = requests.get(f"http://{ip}/s")
    print(f"Стоп")


def standartTest():
    while True:
        response = requests.get(f"http://{ip}/f")
        print(f"http://{ip}/f")
        Timer(2, 0.5)

        response = requests.get(f"http://{ip}/b")
        print(f"http://{ip}/b")
        Timer(2, 0.5)

        response = requests.get(f"http://{ip}/r")
        print(f"http://{ip}/r")
        Timer(2, 0.5)

        response = requests.get(f"http://{ip}/l")
        print(f"http://{ip}/l")
        Timer(2, 0.5)

        response = requests.get(f"http://{ip}/s")
        print(f"http://{ip}/s")
        Timer(2, 0.5)

def manualControl():
    while True:
        direction = input()

        if(direction == "в"):
            MoveForward()
        elif(direction == "н"):
            MoveBack()
        elif(direction == "п"):
            MoveRight()
        elif(direction == "л"):
            MoveLeft()
        elif(direction == "с"):
            MoveStop()
        else:
            continue


def main():
    os.run("cls")
    print("=== Д/У - En24 - byRitme ===")
    mode = int(input("Выбор режима (0 - Тест моторов, 1 - Ручное Д/У, -1 - Выход): "))
    
    if(mode == 0):
        standartTest()
    elif(mode == 1):
        ()
    elif(mode == -1):
        exit()
    else:
        return


while(__name__ == "__main__"):
    main()