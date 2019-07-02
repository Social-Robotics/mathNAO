# Global imports
import json, os

# Global variables
count = 0
round_count = 0
total_count = 0

exercises_over_tiental, exercises_tien_eenh, exercises_over_tien_eenh = None, None, None
exercises_door_tiental, exercises_wegdenken, exercises_tien_eenh_sub, exercises_door_tien_eenh = None, None, None, None
answers_over_tiental, answers_tien_eenh, answers_over_tien_eenh = None, None, None
answers_door_tiental, answers_wegdenken, answers_tien_eenh_sub, answers_door_tien_eenh = None, None, None, None

current_exercise = None
current_answer = None

redone = False
first_exercise = True


def load_exercises():
    """
    Open the json file containing the exercises for session 1.
    Assign it to the global variable to be used in other methods as well.
    :return: exercises
    """
    with open(os.path.join(os.path.dirname(__file__), 'exercises2.json')) as data:
        data = json.load(data)
        add = data['add']
        global exercises_over_tiental
        exercises_over_tiental = add['over_tiental']['exercises']
        global exercises_tien_eenh
        exercises_tien_eenh = add['tien_eenh']['exercises']
        global exercises_over_tien_eenh
        exercises_over_tien_eenh = add['over_tien_eenh']['exercises']
        sub = data['sub']
        global exercises_door_tiental
        exercises_door_tiental = sub['door_tiental']['exercises']
        global exercises_wegdenken
        exercises_wegdenken = sub['wegdenken']['exercises']
        global exercises_tien_eenh_sub
        exercises_tien_eenh_sub = sub['tien_eenh']['exercises']
        global exercises_door_tien_eenh
        exercises_door_tien_eenh = sub['door_tien_eenh']['exercises']
    print("Add: ")
    print(add)
    print("Sub: ")
    print(sub)


def load_answers():
    """
    Open the json file containing the answers for session 1.
    Assign it to the global variable to be used in other methods as well.
    :return: answers
    """
    with open(os.path.join(os.path.dirname(__file__), 'exercises2.json')) as data:
        data = json.load(data)
        add = data['add']
        global answers_over_tiental
        answers_over_tiental = add['over_tiental']['answers']
        global answers_tien_eenh
        answers_tien_eenh = add['tien_eenh']['answers']
        global answers_over_tien_eenh
        answers_over_tien_eenh = add['over_tien_eenh']['answers']
        sub = data['sub']
        global answers_door_tiental
        answers_door_tiental = sub['door_tiental']['answers']
        global answers_wegdenken
        answers_wegdenken = sub['wegdenken']['answers']
        global answers_tien_eenh_sub
        answers_tien_eenh_sub = sub['tien_eenh']['answers']
        global answers_door_tien_eenh
        answers_door_tien_eenh = sub['door_tien_eenh']['answers']



def get_count():
    """
    Getter for count variable
    :return: count
    """
    return count


def increase_counter():
    global total_count
    total_count += 1
    global count
    if count == 6:
        count = 0
        increase_round()
    else:
        count += 1
    print("Count: " + str(count))


def get_total():
    return total_count


def get_round():
    global round_count
    return round_count


def increase_round():
    global round_count
    round_count += 1


def get_redone():
    return redone


def get_first_exercise():
    return first_exercise


def set_first_exercise():
    global first_exercise
    first_exercise = False


def get_current_exercise():
    """
    Return the current exercise to be provided to the student.
    Increase the counter with 1.
    :return: current_exercise
    """
    print("Get exercise from stack.")
    global current_exercise
    if count == 0:
        current_exercise = exercises_over_tiental.pop(0)
    elif count == 1:
        current_exercise = exercises_tien_eenh.pop(0)
    elif count == 2:
        current_exercise = exercises_over_tien_eenh.pop(0)
    elif count == 3:
        current_exercise = exercises_door_tiental.pop(0)
    elif count == 4:
        current_exercise = exercises_wegdenken.pop(0)
    elif count == 5:
        current_exercise = exercises_tien_eenh_sub.pop(0)
    elif count == 6:
        current_exercise = exercises_door_tien_eenh.pop(0)

    print("Current exercise is: " + current_exercise)
    return current_exercise


def repeat_exercise():
    """
    Provide the exercise that has to be repeated, in order to hear it again.
    :return: repeated_exercise
    """
    if not current_exercise:
        return
    print("Repeating exercise")
    repeated_exercise = current_exercise
    print("Exercise to be repeated: " + repeated_exercise)
    return repeated_exercise


def get_current_answer():
    global current_answer
    if count == 0:
        current_answer = answers_over_tiental.pop(0)
    elif count == 1:
        current_answer = answers_tien_eenh.pop(0)
    elif count == 2:
        current_answer = answers_over_tien_eenh.pop(0)
    elif count == 3:
        current_answer = answers_door_tiental.pop(0)
    elif count == 4:
        current_answer = answers_wegdenken.pop(0)
    elif count == 5:
        current_answer = answers_tien_eenh_sub.pop(0)
    elif count == 6:
        current_answer = answers_door_tien_eenh.pop(0)

    print("Current answer is: " + str(current_answer))
    return current_answer


def check_answer(answer_student):
    """
    Compare the answer to the answer sheet.
     Return whether answer is correct or not.
    :param answer_student: Answer given by the student
    :return: True or False
    """
    print("Checking student answer " + str(answer_student) + " to answer " + str(current_answer))
    if int(answer_student) == int(current_answer):

        return True
    else:
        return False


def redo_exercise():
    global redone
    redone = True
    return current_exercise
