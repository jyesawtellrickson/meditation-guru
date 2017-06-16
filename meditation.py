import win32com.client as wincl
from time import sleep
from os import listdir


class Guru:

    def __init__(self, voice='UK', speed=-3):
        self.speech = wincl.Dispatch("SAPI.SpVoice")
        self.speech.Rate = speed
        self.speech.Voice = self.speech.GetVoices().item(['UK', 'US'].index(voice))
        self.lesson = ''
        return

    @staticmethod
    def process_line(line):
        line = line.replace('\n','')
        contains_time = False
        try:
            wait_time = int(line.split()[0])
            contains_time = True
        except:
            wait_time = 5
        if contains_time:
            ans = (wait_time, " ".join(line.split()[1:]))
        else:
            ans = (wait_time, line)
        return ans

    @staticmethod
    def convert_int(value):
        try:
            value = int(value)
        except ValueError:
            value = value
        return value

    def choose_teaching(self):
        lessons = listdir('lessons')
        print("Lessons:")
        for i in range(0, len(lessons)):
            print("({0}) ".format(i+1)+lessons[i].split(".")[0])
        choice = input("What would you like to learn today?\n"
                       "Lesson no.: ")
        choice = self.convert_int(choice)
        while choice not in range(1, len(lessons)+1):
            choice = input("Please select a lesson by inputting the corresponding number.\n"
                           "Lesson no.: ")
            choice = self.convert_int(choice)
        self.lesson = lessons[choice-1]
        return

    def see_teachings(self):
        for lesson in listdir('lessons'):
            print(lesson)
        return

    def enlighten(self, lesson):
        return

    def read_file(self, filename):
        file = open('lessons/'+filename, 'r')
        meditation = []
        for l in file.readlines():
            if l[0] == '#':
                a = 1
            elif l != '\n':
                meditation += [self.process_line(l)]
        file.close()
        return meditation

    def greet(self):
        self.speak("Namaste\n")
        return

    def print_and_speek(self, text):
        print(text)
        self.speak(text)
        return

    def speak(self, text):
        self.speech.Speak(text)
        return

    def teach(self):
        lines = self.read_file(self.lesson)
        for line in lines:
            self.speak(line[1])
            sleep(line[0])
        return


Bodhivista = Guru()
Bodhivista.choose_teaching()
Bodhivista.teach()


