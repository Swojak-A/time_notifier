import datetime
from time import sleep

class TimeNotifier:
    def __init__(self):
        pass

    def time_count(self):
        while True:
            time_check = datetime.datetime.now()
            print("Present time: {}, {}, {}".format(time_check.hour, time_check.minute, time_check.second))
            if time_check.minute == 0:
                print("New hour")
                sleep(60)
            sleep(30)


if __name__ == "__main__":
    t = TimeNotifier()
    t.time_count()