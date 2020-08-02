import datetime
import time
from pygame import mixer


def Time():
    return datetime.datetime.now()


def Play_music(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break
        else:
            print("Invalid input")


def log_now(msg):
    with open("info_log.txt", "a") as f:
        f.write(f"{msg} {Time()}\n")


if __name__ == '__main__':

    init_water = time.time()
    init_eyes = time.time()
    init_physical = time.time()
    water_time = 60 * 40
    eye_time = 30 * 60
    physical_time = 45 * 60

    while True:
        if time.time() - init_water > water_time:
            print("Please drink water.\nEnter 'drank' to stop.")
            Play_music("water.mp3", "drank")
            init_water = time.time()
            log_now("Drank water at ")

        if time.time() - init_eyes > eye_time:
            print("Please move your eyes from screen for few mins .\nEnter 'done' to stop.")
            Play_music("water.mp3", "done")
            init_eyes = time.time()
            log_now("Eyes relaxed at ")

        if time.time() - init_physical > physical_time:
            print("Please do some physical work.\nEnter 'done' to stop.")
            Play_music("water.mp3", "done")
            init_physical = time.time()
            log_now("Exercise done at ")

        print("Press q if you want to quit: ")
        code_stop = input()
        if code_stop == "q" or code_stop == "Q":
            quit()
        else:
            print("Invalid input")
