# Global imports
import sys, importlib

# Local imports
importlib.import_module("touch")
from touch import ReactToTouch

# NAO imports
from naoqi import ALProxy, ALBroker

# NAO initial variables
NAO_ip = "localhost"
NAO_port = 9559


def init_tts():
    """
    Initialise the TextToSpeech engine of NAO.
    Set the language to Dutch and the speed to a relatively understandable pace.
    :return: tts instance
    """
    try:
        tts = ALProxy("ALTextToSpeech", NAO_ip, NAO_port)
        tts.setLanguage("Dutch")
        # tts.setParameter("speed", 105)
        tts.setParameter("speed", 90)
        return tts
    except Exception, e:
        print("Could not create proxy to ALTextToSpeech")
        print("Error was: ", e)
        sys.exit(1)


def init_animated_tts():
    """
    Initialise the TextToSpeech engine of NAO.
    Set the language to Dutch and the speed to a relatively understandable pace.
    :return: tts instance
    """
    try:
        animated_tts = ALProxy("ALAnimatedSpeech", NAO_ip, NAO_port)
        return animated_tts
    except Exception, e:
        print("Could not create proxy to ALAnimatedSpeech")
        print("Error was: ", e)
        sys.exit(1)


def init_speech_recognition():
    """
    Initialise the SpeechRecognition engine of NAO.
    Set the language to Dutch and pause the engine for later use.
    :return: speech_recognition instance
    """
    try:
        speech_recognition = ALProxy("ALSpeechRecognition", NAO_ip, NAO_port)
        speech_recognition.setLanguage("Dutch")
        speech_recognition.setAudioExpression(False)
        speech_recognition.pause(True)
        return speech_recognition
    except Exception, e:
        print("Could not create proxy to ALSpeechRecognition")
        print("Error was: ", e)
        sys.exit(1)


def init_memory():
    """
    Initialise the Memory engine of NAO.
    :return: memory instance
    """
    try:
        memory = ALProxy("ALMemory", NAO_ip, NAO_port)
        return memory
    except Exception, e:
        print("Could not create proxy to ALMemory")
        print("Error was: ", e)
        sys.exit(1)


def init_motion():
    """
    Initialise the Motion engine of NAO.
    Wake-up NAO to be in an active state.
    :return: motion instance
    """
    try:
        motion = ALProxy("ALMotion", NAO_ip, NAO_port)
        motion.wakeUp()
        return motion
    except Exception, e:
        print("Could not create proxy to ALMotion")
        print("Error was: ", e)
        sys.exit(1)


def init_tracker():
    """
    Initialise the Tracker engine of NAO, able to track the face of the person in front of it.
    :return: tracker instance
    """
    try:
        tracker = ALProxy("ALTracker", NAO_ip, NAO_port)
        # Add target to track.
        targetName = "Face"
        faceWidth = 0.1
        tracker.registerTarget(targetName, faceWidth)
        # Then, start tracker.
        tracker.track(targetName)
        return tracker
    except Exception, e:
        print("Could not create proxy to ALTracker")
        print("Error was: ", e)
        sys.exit(1)


def init_posture():
    """
    Initialise the RobotPosture engine of NAO.
    :return: posture instance
    """
    posture = ALProxy("ALRobotPosture", NAO_ip,NAO_port)
    return posture


def init_behavior():
    behavior_manager = ALProxy("ALBehaviorManager", NAO_ip, NAO_port)
    return behavior_manager


def init_event_broker():
    """
    Initialise an event broker, to work with the event changes of NAO.
    :return: event_broker instance
    """
    try:
        event_broker = ALBroker("event_broker", "0.0.0.0", 0,
                                NAO_ip, NAO_port)
        return event_broker
    except Exception, e:
        print("Could not create event_broker")
        print("Error was: ", e)
        sys.exit(1)


def init_touch(behavior_manager):
    """
    Initialise the ReactToTouch event watcher, to be able to react to touches on NAO
    :return: ReactToTouch instance
    """
    global ReactToTouch
    ReactToTouch = ReactToTouch("ReactToTouch", behavior_manager)
    return ReactToTouch


def close_down(tracker, motion, event_broker):
    """
    Put Nao to a resting position.
    Stop the awareness of humans.
    Stop the broker, no more event watchers are needed.
    Then shut down the software.
    :param tracker: The tracker instance
    :param motion: The motion instance
    :param event_broker: The event_broker
    :return:
    """
    print "Finished training, shutting down"
    # Stop tracker.
    tracker.stopTracker()
    tracker.unregisterAllTargets()
    motion.rest()
    event_broker.shutdown()
    sys.exit(0)
