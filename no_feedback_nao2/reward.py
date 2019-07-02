import almath
import time

current_step = 0
steps = ["Op, je, plaats", "Strek, je, armen", "Vuisten, maken", "Duimen omhoog", "Schouders op", "Hoofd omhoog", "Billen naar achteren", "Voeten naar binnen", "Tong naar buiten"]


def learn_step(tts, motion, posture):
    global current_step
    tts.say("Je mag nu gaan staan.")
    time.sleep(3)
    if current_step == 0:
        tts.say("De eerste stap die ik je ga leren is: ")
        tts.say(steps[current_step])
        tts.say("Dat doe je zo.")
        posture.goToPosture("Stand", 0.5)
        plaats(motion, posture)
        current_step += 1

    if current_step == 1:
        tts.say("De volgende stap is: ")
        tts.say(steps[current_step])
        tts.say("Dat doe je zo.")
        posture.goToPosture("Stand", 0.5)
        armen(motion)
        current_step += 1

    if current_step == 2:
        tts.say("De volgende stap is: ")
        tts.say(steps[current_step])
        tts.say("Dat doe je zo.")
        posture.goToPosture("Stand", 0.5)
        armen(motion)
        vuisten(motion)
        current_step += 1

    if current_step == 3:
        tts.say("De volgende stap is: ")
        tts.say(steps[current_step])
        tts.say("Dat doe je zo.")
        posture.goToPosture("Stand", 0.5)
        armen(motion)
        vuisten(motion)
        duimen(motion)
        current_step += 1

    if current_step == 4:
        tts.say("De volgende stap is: ")
        tts.say(steps[current_step])
        tts.say("Ik kan helaas mijn schouders niet omhoog doen.")
        tts.say("Je moet je schouders helemaal naar boven doen, zodat ze bijna, je oren aanraken!")
        time.sleep(2)
        tts.say("Dat is goed, precies zoals je het nu doet!")
        posture.goToPosture("Stand", 0.5)
        current_step += 1

    if current_step == 5:
        tts.say("De volgende stap is: ")
        tts.say(steps[current_step])
        tts.say("Dat doe je zo.")
        posture.goToPosture("Stand", 0.5)
        hoofd(motion)
        current_step += 1

    if current_step == 6:
        tts.say("De volgende stap is: ")
        tts.say(steps[current_step])
        tts.say("Steek die billen maar helemaal naar achteren!")
        time.sleep(2)
        tts.say("Heel goed!")
        posture.goToPosture("Stand", 0.5)
        tts.say("Ik kan mijn billen niet naar achteren doen, want dan val ik om.")
        current_step += 1

    if current_step == 7:
        tts.say("De volgende stap is: ")
        tts.say(steps[current_step])
        tts.say("Dat doe je door je tenen naar elkaar toe te laten wijzen.")
        time.sleep(2)
        tts.say("Heel goed!")
        posture.goToPosture("Stand", 0.5)
        current_step += 1

    if current_step == 8:
        tts.say("Je weet nu bijna alle, danspasjes.")
        tts.say("De laatste stap is: ")
        tts.say(steps[current_step])
        tts.say("Ik heb helaas geen tong die ik kan uitsteken. Steek je tong maar ver naar buiten!")
        time.sleep(2)
        tts.say("Precies zo, ja!")
        posture.goToPosture("Stand", 0.5)
    posture.goToPosture("Stand", 0.5)
    time.sleep(3)


def plaats(motion, posture):
    # A small step forwards and anti-clockwise with the left foot
    legName = ["LLeg"]
    X       = 0.2
    Y       = 0.1
    Theta   = 0.3
    footSteps = [[X, Y, Theta]]
    fractionMaxSpeed = [1.0]
    clearExisting = False
    motion.setFootStepsWithSpeed(legName, footSteps, fractionMaxSpeed, clearExisting)

    time.sleep(2.0)

    legName = ["RLeg"]
    X = 0.2
    Y = 0.1
    Theta = 0.3
    footSteps = [[X, Y, Theta]]
    fractionMaxSpeed = [1.0]
    clearExisting = False
    motion.setFootStepsWithSpeed(legName, footSteps, fractionMaxSpeed, clearExisting)

    time.sleep(2.0)


def armen(motion):
    motion.post.openHand("RHand")
    motion.post.openHand("LHand")
    names = ["LShoulderPitch", "RShoulderPitch", "LElbowYaw", "RElbowYaw"]
    angle_list = [00.0 * almath.TO_RAD, 00.0 * almath.TO_RAD, 00.0 * almath.TO_RAD, 00.0 * almath.TO_RAD]
    time_list = [1.0, 1.0, 1.0, 1.0]
    is_absolute = True
    motion.angleInterpolation(names, angle_list, time_list, is_absolute)


def vuisten(motion):
    motion.closeHand("RHand")
    motion.closeHand("LHand")


def duimen(motion):
    names = ["LWristYaw", "RWristYaw"]
    angle_list = [-104.0 * almath.TO_RAD, 104.0 * almath.TO_RAD]
    time_list = [1.0, 1.0]
    is_absolute = True
    motion.angleInterpolation(names, angle_list, time_list, is_absolute)


def hoofd(motion):
    names = ["HeadPitch"]
    angle_list = [-38.0 * almath.TO_RAD]
    time_list = [1.0]
    is_absolute = True
    motion.angleInterpolation(names, angle_list, time_list, is_absolute)
