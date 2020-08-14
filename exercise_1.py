from time import sleep

class TrafficLight:
    def __init__(self,):
        self.__color = "color"

    def running(self, color):
        start = None
        while True:
            # start = input("Введите Y, если хотите начать программу светофор.\nВведите Q для выхода.").upper()
            # if start == "Y":
                print("\033[1m\033[31m {}\033[0m".format(color))
                sleep(7)
                print("\033[1m\033[33m {}\033[0m".format(color))
                sleep(2)
                print("\033[1m\033[32m {}\033[0m".format(color))
                sleep(14)
            # else:
            #     break


go = TrafficLight()
go.running('O')

