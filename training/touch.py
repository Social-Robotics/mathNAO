from naoqi import ALProxy
from naoqi import ALBroker
from naoqi import ALModule

import importlib, time
importlib.import_module("training")
from training import set_touched


# Global variable to store the ReactToTouch module instance
ReactToTouch = None
memory = None

class ReactToTouch(ALModule):
    """ A simple module able to react
        to touch events.
    """
    def __init__(self, name, behavior_manager):
        ALModule.__init__(self, name)
        # No need for IP and port here because
        # we have our Python broker connected to NAOqi broker

        # Create a proxy to ALTextToSpeech for later use
        self.tts = ALProxy("ALTextToSpeech")
        self.behavior_manager = behavior_manager

        # Subscribe to TouchChanged event:
        global memory
        memory = ALProxy("ALMemory")

    def onTouchedTickle(self, strVarName, value):
        """ This will be called each time a touch
        is detected.

        """
        if not value or not strVarName or not self:
            return

        # Unsubscribe to the event when talking,
        # to avoid repetitions


        touched_bodies = []
        for p in value:
            if p[1]:
                touched_bodies.append(p[0])

        if "Head/Touch/Front" in touched_bodies:
            print("Head touched")
            self.launch_stop_behavior("animations/Stand/Emotions/Positive/Laugh_1")
        if "RFoot/Bumper/Left" in touched_bodies or "RFoot/Bumper/Right" in touched_bodies:
            print("Right Foot touched")
            self.launch_stop_behavior("animations/Stand/Emotions/Positive/Laugh_2")
        if "LFoot/Bumper/Left" in touched_bodies or "LFoot/Bumper/Right" in touched_bodies:
            print("Left Foot touched")
            self.launch_stop_behavior("animations/Stand/Emotions/Positive/Laugh_3")

        # Subscribe again to the event
        # memory.subscribeToEvent("TouchChanged",
        #     "ReactToTouch",
        #     "onTouched")
        # self.speech_recognition.pause(False)

    def onTouchedListen(self, strVarName, value):
        if not value or not strVarName or not self:
            return

        print("In listen")

        # Unsubscribe to the event when talking,
        # to avoid repetitions
        # memory.unsubscribeToEvent("TouchChanged",
        #     "ReactToTouch")
        # self.speech_recognition.pause(True)

        touched_bodies = []
        for p in value:
            if p[1]:
                touched_bodies.append(p[0])

        if "RFoot/Bumper/Left" in touched_bodies or "RFoot/Bumper/Right" in touched_bodies:
            print("Right Foot touched")
            set_touched(True)
        if "LFoot/Bumper/Left" in touched_bodies or "LFoot/Bumper/Right" in touched_bodies:
            print("Left Foot touched")
            set_touched(True)

    def launch_stop_behavior(self, behavior_name):
        ''' Launch and stop a behavior, if possible. '''

        # Check that the behavior exists.
        if (self.behavior_manager.isBehaviorInstalled(behavior_name)):

            # Check that it is not already running.
            if (not self.behavior_manager.isBehaviorRunning(behavior_name)):
                # Launch behavior. This is a blocking call, use post if you do not
                # want to wait for the behavior to finish.
                self.behavior_manager.post.runBehavior(behavior_name)
                # time.sleep(5.0)
            else:
                print "Behavior is already running."

        else:
            print "Behavior not found."
            return

        names = self.behavior_manager.getRunningBehaviors()
        print "Running behaviors:"
        print names

        # Stop the behavior.
        if (self.behavior_manager.isBehaviorRunning(behavior_name)):
            self.behavior_manager.stopBehavior(behavior_name)
            time.sleep(1.0)
        else:
            print "Behavior is already stopped."

        names = self.behavior_manager.getRunningBehaviors()
        print "Running behaviors:"
        print names