import requests
import time

print("Для запуска введите 2 последние цифры IP")
ipBytes = [input("Первое число: "), input("Второе число: ")]
ip = f"192.168.{ipBytes[0]}.{ipBytes[1]}"

def Timer(timerTime, deltaTime):
    while(timerTime>0):
        timerTime -= deltaTime
        print(".")
        time.sleep(deltaTime)

def standartTest():
    while True:
        response = requests.get("http://192.168.201.188/f")
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

def main():
    standartTest()


main()


"""def standartTest():
    while True:
        response = requests.get(f"http://{ip}/f")
        print(f"http://{ip}/f")
        print("Пуск моторов")
        Timer(2, 0.5)

        response = requests.get(f"http://{ip}/gpio/0")
        print(f"http://{ip}/gpio/0")
        print("Стоп")
        Timer(2, 0.5)"""