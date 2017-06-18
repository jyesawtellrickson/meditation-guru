import win32com.client as wincl
from time import sleep
from os import listdir


class Guru:

    def __init__(self, voice='UK', speed=-3):
        self.speech = wincl.Dispatch("SAPI.SpVoice")
        self.speech.Rate = speed
        self.speech.Voice = self.speech.GetVoices().item(['UK', 'US'].index(voice))
        self.lesson = ''
        self.lesson_length = None
        return

    @staticmethod
    def process_line(line):
        """
        Function to read the special meditation line format
        and create readable script for Guru.
        :param line: (str) line of text file
        :return: (tuple) wait time and text to read
        """
        line = line.replace('\n', '')
        contains_time = False
        try:
            wait_time = int(line.split()[0])
            contains_time = True
        except:
            wait_time = 1
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
        """
        Show the directory of lessons to the user
        and collect a response for the lesson number.
        Sets the lesson file name to the object.
        :return:
        """
        lessons = listdir('lessons')
        print("Lessons:")
        for i in range(0, len(lessons)):
            print("({0}) ".format(i+1)+lessons[i].split(".")[0])
        print("\n")
        choice = input("What would you like to learn today?\n"
                       "Lesson no.: ")
        choice = self.convert_int(choice)
        # Keep asking user for input until they select a lesson
        while choice not in range(1, len(lessons)+1):
            choice = input("Please select a lesson by inputting the corresponding number.\n"
                           "Lesson no.: ")
            choice = self.convert_int(choice)
        self.lesson = lessons[choice-1]
        return

    def see_teachings(self):
        """
        Print list of lessons to the user.
        :return:
        """
        for lesson in listdir('lessons'):
            print(lesson.split(".")[0])
        return

    def enlighten(self, lesson):
        return

    def read_file(self, filename):
        """
        Take a filename and return the lines of text
        as a list.
        Process each line in the standard way.
        Lines starting with # are ignored.
        :param filename: (str) lesson filename
        :return: (list) of tuples for lesson
        """
        file = open('lessons/'+filename, 'r')
        meditation = [self.process_line(l) for l in file.readlines() if l != '\n' and l[0] != '#']
        """
        meditation = []
        for l in file.readlines():
            if l != '\n' and l[0] != '#':
                meditation += [self.process_line(l)]
        """
        file.close()
        return meditation

    def greet(self):
        self.speak("Narmarstay\n")  # incorrect spelling for speech
        return

    def print_and_speak(self, text):
        print(text)
        self.speak(text)
        return

    def speak(self, text):
        self.speech.Speak(text)
        return

    def teach(self):
        """
        Once a lesson is chosen, teach the lesson
        to the user.
        :return:
        """
        if self.lesson == '':
            self.print_and_speak("Please choose a lesson first")
        # get the scale parameter
        scale = 1
        if self.lesson_length:
            scale = self.lesson_length / self.estimate_lesson_length(self.lesson)
        lines = self.read_file(self.lesson)
        for line in lines:
            self.speak(line[1])
            sleep(line[0])
        sleep(5)
        self.print_and_speak("Lesson complete")
        self.lesson = ''
        return

    def tell_me_a_koan(self):
        return

    def estimate_lesson_length(self, lesson):
        """
        Estimate the length of a lesson to expand it out.
        :param lesson:
        :return:
        """
        # length from number of words and pauses
        lines = self.read_file(lesson)
        time = sum([l[0] for l in lines])
        word_count = sum([len(l[1].split()) for l in lines])
        length = time + word_count * 0.5
        return length

