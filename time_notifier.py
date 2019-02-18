import datetime
from time import sleep
from pygame import mixer



class TimeNotifier:
    lang_dict={
        "eng" : "eng-emma/"
    }



    def time_count(self):
        while True:
            time_check = datetime.datetime.now()
            print("Present time: {}:{}:{}".format(time_check.hour, time_check.minute, time_check.second))
            if time_check.minute == 0:
                TimeNotifier.notify(hour=time_check.hour)
                sleep(30)
            sleep(30)



    @classmethod
    def notify(cls, folder="mp3/", lang=None, hour=None):
        if hour == None:
            file = "test.mp3"
        else:
            file = "{}.mp3".format(str(hour))

        if lang == None:
            lang = cls.lang_dict["eng"]

        path = "{}{}{}".format(folder, lang, file)

        print(path)

        mixer.init()
        mixer.music.load(path)
        mixer.music.play()



if __name__ == "__main__":
    t = TimeNotifier()
    t.time_count()