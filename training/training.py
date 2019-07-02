# Global imports
import importlib, time, datetime

# Local imports
importlib.import_module("initialize")
from initialize import *

# Initial variables needed for NAO
tts, animated_tts, speech_recognition, memory, tracker, ReactToTouch, speechRecognition = None, None, None, None, None, None, None

# Initial variables
basic_awareness, motion, behavior_manager, event_broker, posture, sound_detection = None, None, None, None, None, None

numbers = []
for x in range(0, 101):
    numbers.append(str(x))

train_numbers = ["37", "98", "7", "11", "42"]
# train_numbers = ["37", "65", "98", "52", "7", "8", "23", "11", "12", "42"]
count = 0

touched = False

def initialize_nao():
    """
    Nao is being initialized by setting up the connection with NaoQi:
    - The speech recognition
    - Memory of saved answers.
    """
    print("Initializing Nao")
    global tts
    tts = init_tts()

    global animated_tts
    animated_tts = init_animated_tts()

    global speech_recognition
    speech_recognition = init_speech_recognition()

    global memory
    memory = init_memory()

    global event_broker
    event_broker = init_event_broker()

    global tracker
    tracker = init_tracker()

    global behavior_manager
    behavior_manager = init_behavior()

    global motion
    motion = init_motion()

    global posture
    posture = init_posture()

    global ReactToTouch
    ReactToTouch = init_touch(behavior_manager)


def explain_training(tts):
    tts.say("Hallo, ik ben Pixel. Ik ben een rekenrobot.")
    print("Hallo, ik ben Pixel. Ik ben een rekenrobot.")
    tts.say("Ik heb wat problemen met horen, ik versta niet altijd goed wat je zegt.")
    print("Ik heb wat problemen met horen, ik versta niet altijd goed wat je zegt.")
    tts.say("Om je goed te kunnen verstaan moet je hard en duidelijk praten.")
    print("Om je goed te kunnen verstaan moet je hard en duidelijk praten.")
    tts.say("Dit gaan we nu even oefenen.")
    print("Dit gaan we nu even oefenen.")
    tts.say("Ik ga 1 voor 1, 5 getallen opnoemen.")
    print("Ik ga 1 voor 1, 5 getallen opnoemen.")
    tts.say("Als jij dan dit getal herhaalt, dan zeg ik wat ik gehoord heb.")
    print("Als jij dan dit getal herhaalt, dan zeg ik wat ik gehoord heb.")
    tts.say("Je kan beginnen met praten, zodra mijn ogen blauw kleuren.")
    print("Je kan beginnen met praten, zodra mijn ogen blauw kleuren.")


def set_touched(is_touched):
    global touched
    print touched
    touched = is_touched


def provide_number(tts):
    global count
    if count == 0:
        tts.say("Het eerste getal is: ")
    else:
        tts.say("Het volgende getal is: ")
    tts.say(train_numbers[count])
    count += 1


def hear_answer():
    speech_recognition.setVocabulary(numbers, False)
    tts.say("")
    answer = ""
    # memory.subscribeToEvent("TouchChanged",
    #                         "ReactToTouch",
    #                         "onTouchedListen")
    while answer == "":
        # global touched
        # if touched:
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
            tts.say("Ik heb je niet gehoord, wil je het nog een keer zeggen?")
        set_touched(False)
    # memory.unsubscribeToEvent("TouchChanged",
    #                           "ReactToTouch")
    return answer


def hear_number():
    speech_recognition.setVocabulary(numbers, False)
    tts.say("")
    answer = ""
    while answer == "":
        speech_recognition.subscribe("GET_ANSWER")
        print('Speech recognition engine started')
        speech_recognition.pause(False)
        time.sleep(3)
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
            tts.say("Ik heb je niet gehoord, wil je het nog een keer zeggen?")
    return answer


def answer_correct(tts, answer):
    tts.say("Volgens mij zei je, " + str(answer))
    print("Volgens mij zei je " + str(answer))


if __name__ == "__main__":
    initialize_nao()

    explain_training(animated_tts)
    global count
    while count != len(train_numbers):
        print("Count = " + str(count))
        provide_number(tts)
        answer = hear_number()
        if int(answer) == int(train_numbers[count-1]):
            answer_correct(animated_tts, answer)
        else:
            answer_correct(animated_tts, answer)
            animated_tts.say("Dat is niet wat ik zei. Probeer nog eens luid en duidelijk te praten.")
            global count
            count -= 1
    animated_tts.say("Dat waren alle getalletjes! We gaan nu oefenen met het aanraken van mijn lichaam.")
    animated_tts.say("Wanneer je de voorkant van mijn voeten of de bovenkant van mijn hoofd aanraakt, kietelt dat en moet ik heel hard lachen.")
    animated_tts.say("Zullen we eens kijken of je mij aan het lachen kan krijgen?")
    animated_tts.say("Ga je gang, probeer het maar!")

    posture.goToPosture("Stand", 1.0)
    memory.subscribeToEvent("TouchChanged",
                            "ReactToTouch",
                            "onTouchedTickle")
    start = datetime.datetime.now()
    print("Starttime is: " + str(start))
    end = datetime.timedelta(minutes=1) + start
    print("Endtime is: " + str(end))

    while datetime.datetime.now() < end:
        pass
    tts.setParameter("speed", 90)
    memory.unsubscribeToEvent("TouchChanged",
                              "ReactToTouch")
    animated_tts.say("Bedankt voor het oefenen! Nu is het tijd om te gaan rekenen.")
    animated_tts.say("We oefenen even 3 makkelijke rekensommetjes, om te kijken of het goed gaat")
    # animated_tts.say("Als je het antwoord op de som weet, raak dan mijn voeten aan. Ik zal dan luisteren naar je antwoord.")
    animated_tts.say("Denk eraan dat je alleen tegen mij kan praten als mijn ogen blauw zijn.")

    tts.say("Hoeveel is " + str(1) + ", erbij, " + str(1))
    answer = hear_answer()
    if int(answer) == 2:
        animated_tts.say("Heel goed!")
    else:
        animated_tts.say("Dat is helaas niet goed.")

    tts.say("Hoeveel is " + str(1) + ", erbij, " + str(2))
    answer = hear_answer()
    if int(answer) == 3:
        animated_tts.say("Alweer goed!")
    else:
        animated_tts.say("Dat is helaas niet goed.")

    tts.say("Hoeveel is " + str(2) + ", erbij, " + str(2))
    answer = hear_answer()
    if int(answer) == 4:
        animated_tts.say("Goed hoor!")
    else:
        animated_tts.say("Dat is helaas niet goed.")

    # memory.unsubscribeToEvent("TouchChanged",
    #                           "ReactToTouch")

    animated_tts.say("Dit was de training. Dankjewel!")
    close_down(tracker, motion, event_broker)
