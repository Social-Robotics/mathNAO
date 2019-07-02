from naoqi import ALProxy
from naoqi import ALBroker
from naoqi import ALModule

import importlib
importlib.import_module("exercise")
from exercise import repeat_exercise

importlib.import_module("student")
from student import set_touched, increase_foot_counter, increase_head_counter

# Global variable to store the ReactToTouch module instance
ReactToTouch = None
memory = None

class ReactToTouch(ALModule):
    """ A simple module able to react
        to touch events.
    """
    def __init__(self, name, speech_recognition):
        ALModule.__init__(self, name)
        # No need for IP and port here because
        # we have our Python broker connected to NAOqi broker

        # Create a proxy to ALTextToSpeech for later use
        self.tts = ALProxy("ALTextToSpeech")
        self.speech_recognition = speech_recognition

        # Subscribe to TouchChanged event:
        global memory
        memory = ALProxy("ALMemory")
        # memory.subscribeToEvent("TouchChanged",
        #     "ReactToTouch",
        #     "onTouched")

    def onTouched(self, strVarName, value):
        """ This will be called each time a touch
        is detected.

        """
        if not value or not strVarName or not self:
            return

        # Unsubscribe to the event when talking,
        # to avoid repetitions
        # memory.unsubscribeToEvent("TouchChanged",
        #     "ReactToTouch")
        # self.speech_recognition.pause(True)

        touched_bodies = []
        for p in value:
            if p[1]:
                touched_bodies.append(p[0])

        if "Head/Touch/Front" in touched_bodies:
            # self.speech_recognition.pause(True)
            repeated_exercise = repeat_exercise()
            print(repeat_exercise())
            self.tts.say("Hoeveel is: ")
            self.tts.say(str(repeated_exercise))
            increase_head_counter()
            # self.speech_recognition.pause(False)

        if "RFoot/Bumper/Left" in touched_bodies or "RFoot/Bumper/Right" in touched_bodies:
            print("Right Foot touched")
            set_touched(True)
            increase_foot_counter()
        if "LFoot/Bumper/Left" in touched_bodies or "LFoot/Bumper/Right" in touched_bodies:
            print("Left Foot touched")
            set_touched(True)
            increase_foot_counter()

        # Subscribe again to the event
        # memory.subscribeToEvent("TouchChanged",
        #     "ReactToTouch",
        #     "onTouched")
        # self.speech_recognition.pause(False)
