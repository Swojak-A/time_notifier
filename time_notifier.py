import datetime
from time import sleep
from pygame import mixer

class TimeNotifier:
    def __init__(self):
        pass

    def time_count(self, func):
        while True:
            time_check = datetime.datetime.now()
            print("Present time: {}, {}, {}".format(time_check.hour, time_check.minute, time_check.second))
            if time_check.minute == 00:
                func
                sleep(60)
            sleep(30)

    def notify(self):
        mixer.init()
        mixer.music.load("mp3/test.mp3")
        mixer.music.play()

if __name__ == "__main__":
    t = TimeNotifier()
    t.time_count(t.notify())