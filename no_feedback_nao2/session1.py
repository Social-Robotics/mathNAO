# Global imports
import importlib, datetime
from random import randint

# Local imports
importlib.import_module("initialize")
from initialize import *

importlib.import_module("converse")
from converse import *

importlib.import_module("student")
from student import *

importlib.import_module("exercise")
from exercise import *

importlib.import_module("reward")
from reward import *

importlib.import_module("math_nao")
from math_nao import *

# Initial variables needed for NAO
tts, animated_tts, speech_recognition, memory, tracker, ReactToTouch, speechRecognition = None, None, None, None, None, None, None

# Initial variables
motion, event_broker, posture, behavior_manager, leds = None, None, None, None, None
provided_exercises = {}
provided_exercise = None
exercise_done = None
start = None
total_count = 0
number_categories = []


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
    tracker = init_tracker()

    global motion
    motion = init_motion()

    global leds
    leds = init_leds()

    global behavior_manager
    behavior_manager = init_behavior()

    global posture
    posture = init_posture()

    global ReactToTouch
    ReactToTouch = init_touch(speech_recognition)


def provide_exercise():
    global provided_exercise
    provided_exercise = get_current_exercise(number_categories)
    global exercise_done
    exercise_done = provided_exercise
    if get_first_exercise():
        animated_tts.say("De eerste rekensom: Hoeveel is")
        set_first_exercise()
    else:
        animated_tts.say("De volgende som: Hoeveel is:")
    animated_tts.say(str(provided_exercise))
    provided_exercise = provided_exercise.split(" ")
    for i in range(0, len(provided_exercise)):
        provided_exercise[i] = provided_exercise[i].replace(",", "")
    return provided_exercise


def calculate_correct_answers():
    answers = 0
    for category, list in provided_exercises.iteritems():
        if 0 in list:
            answers += 1
    return answers


def answers_per_category():
    answers = {}
    for category, list in provided_exercises.iteritems():
        answers[category % 10] = {0 : 0, 1 : 0, 2 : 0}
    for category, list in provided_exercises.iteritems():
        if 0 in list:
            answers[category % 10][0] += 1
        elif 1 in list:
            answers[category % 10][1] += 1
        elif 2 in list:
            answers[category % 10][2] += 1

    print answers
    return answers


if __name__ == "__main__":
    for arg in sys.argv[1:]:
        number_categories.append(arg)
    print("Categories used: " + str(number_categories))

    initialize_nao()
    load_exercises(number_categories)
    load_answers(number_categories)
    explain_session(animated_tts)
    explain_working(animated_tts)

    global start
    start = datetime.datetime.now()
    print("Starttime is: " + str(start))
    end = datetime.timedelta(minutes=20) + start
    print("Endtime will be: " + str(end))
    # Entire loop of exercises
    while datetime.datetime.now() < end:
        print("\n")
        print("Current time is: " + str(datetime.datetime.now()))
        exercise = provide_exercise()
        get_current_answer(number_categories)
        posture.post.goToPosture("Stand", 2)
        answer = hear_answer(tts, speech_recognition, memory, datetime.datetime.now())

        if check_answer(answer):
            cheer_correct(animated_tts, leds, randint(0, 8))
            provided_exercises[get_count()+(get_round()*10)] = [exercise_done, 0]
        else:
            leds.post.rotateEyes(0xFF0000, 0.5, 5)
            wrong_answer(animated_tts, randint(0, 5))
            animated_tts.say("Probeer het nog eens een keer.")
            leds.post.reset("FaceLeds")

            posture.post.goToPosture("Stand", 2)
            answer = hear_answer(tts, speech_recognition, memory, datetime.datetime.now())

            if check_answer(answer):
                cheer_correct(animated_tts, leds, randint(0, 8))
                provided_exercises[get_count()+(get_round()*10)] = [exercise_done, 1]
            else:
                wrong_answer(animated_tts, randint(0, 5))
                provided_exercises[get_count()+(get_round()*10)] = [exercise_done, 2]
        increase_counter(number_categories)
        print(provided_exercises)
        time.sleep(1)
    animated_tts.say("De tijd zit erop. Dat was leuk toch?")

    answers_per_category()
    print("Total foot count: " + str(get_counter_foot()))
    print("Total head count: " + str(get_counter_head()))
    print("Total exercises done: " + str(get_total()))
    correct_answers = calculate_correct_answers()
    if correct_answers == 0:
        animated_tts.say("Je hebt heel hard gewerkt, de volgende keer gaat het vast beter!")
    else:
        animated_tts.say("Je had maar liefst " + str(correct_answers) + " sommen in 1 keer goed! Knap hoor!")
        print("Je had maar liefst " + str(correct_answers) + " sommen in 1 keer goed! Knap hoor!")

    animated_tts.say("Tijd om te dansen. Dans je met me mee?")
    if behavior_manager.isBehaviorRunning("tsjoetsjoewa-efad64/tsjoetsjoewa"):
        behavior_manager.stopAllBehaviors()
    behavior_manager.startBehavior("tsjoetsjoewa-efad64/tsjoetsjoewa")
    time.sleep(180)
    behavior_manager.stopBehavior("tsjoetsjoewa-efad64/tsjoetsjoewa")
    animated_tts.say("Ik hoop dat je het leuk gevonden hebt om met mij te rekenen. Ik in ieder geval wel!")
    animated_tts.say("Dankjewel voor al het harde werk! Misschien tot een volgende keer.")
    close_down(tracker, motion, event_broker)
