# Global imports
import time, importlib, datetime
from random import randint
importlib.import_module("converse")
from converse import no_answer

# Global variables
speech_detected = False
touched = False
warned = False
counter_foot, counter_head = 0, 0

names = ["Sander", "Koen"]
numbers = []
for x in range(0, 101):
    numbers.append(str(x))


def set_touched(is_touched):
    global touched
    touched = is_touched


def increase_foot_counter():
    global counter_foot
    counter_foot += 1


def increase_head_counter():
    global counter_head
    counter_head += 1


def get_counter_head():
    global counter_head
    return counter_head


def get_counter_foot():
    global counter_foot
    return counter_foot


def initialize_student(tts, speech_recognition, memory):
    """
    Initialize the student, retrieving its name.
    :param tts: TextToSpeech engine
    :param speech_recognition: SpeechRecognition engine
    :param memory: Memory engine
    :return: name of the student
    """
    # Set the vocabulary to recognise all the names
    speech_recognition.setVocabulary(names, False)
    # Start the speech recognition engine with user Test_ASR
    tts.say("")
    speech_recognition.subscribe("GET_NAME")
    print('Speech recognition engine started')
    speech_recognition.pause(False)
    time.sleep(3.0)
    speech_recognition.pause(True)
    name = memory.getData("WordRecognized")
    speech_recognition.unsubscribe("GET_NAME")


def hear_answer(tts, speech_recognition, memory, cur_time):
    """
    Retrieve the answer to an exercise.
    :param tts: TextToSpeech engine
    :param speech_recognition: SpeechRecognition engine
    :param memory: Memory engine
    :return: answer
    """
    speech_recognition.setVocabulary(numbers, False)
    tts.say("")
    answer = ""
    memory.subscribeToEvent("TouchChanged",
                            "ReactToTouch",
                            "onTouched")
    while answer == "":
        if touched:
            speech_recognition.subscribe("GET_ANSWER")
            print('Speech recognition engine started')
            speech_recognition.pause(False)
            time.sleep(3.0)
            speech_recognition.pause(True)
            answer = memory.getData("WordRecognized")
            print("data: %s" % answer)
            # Confidence must be bigger than 0.5 in order to continue
            if answer[1] < 0.45:
                answer = ""
            else:
                answer = str(answer[0])
            speech_recognition.unsubscribe("GET_ANSWER")
            if answer == "":
                no_answer(tts, randint(0, 3))
            set_touched(False)
        elif not warned and datetime.datetime.now() > (cur_time + datetime.timedelta(minutes=3)):
            global warned
            warned = True
            tts.say("Je werkt nu 3 minuten aan deze som. Fouten maken mag. Het is niet erg als je het antwoord niet weet. Zeg maar gewoon wat je denkt.")
    memory.unsubscribeToEvent("TouchChanged",
                              "ReactToTouch")
    global warned
    warned = False
    return answer
