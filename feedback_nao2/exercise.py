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
exercises = {}
answers = {}

redone = False
first_exercise = True


def load_exercises(number_categories):
    """
    Open the json file containing the exercises for session 1.
    Assign it to the global variable to be used in other methods as well.
    :return: exercises
    """
    with open(os.path.join(os.path.dirname(__file__), 'exercises2.json')) as data:
        data = json.load(data)
        add = data['add']
        if "0" in number_categories:
            global exercises_over_tiental
            exercises_over_tiental = add['over_tiental']['exercises']
            exercises[0] = exercises_over_tiental
        if "1" in number_categories:
            global exercises_tien_eenh
            exercises_tien_eenh = add['tien_eenh']['exercises']
            exercises[1] = exercises_tien_eenh
        if "2" in number_categories:
            global exercises_over_tien_eenh
            exercises_over_tien_eenh = add['over_tien_eenh']['exercises']
            exercises[2] = exercises_over_tien_eenh
        sub = data['sub']
        if "3" in number_categories:
            global exercises_door_tiental
            exercises_door_tiental = sub['door_tiental']['exercises']
            exercises[3] = exercises_door_tiental
        if "4" in number_categories:
            global exercises_wegdenken
            exercises_wegdenken = sub['wegdenken']['exercises']
            exercises[4] = exercises_wegdenken
        if "5" in number_categories:
            global exercises_tien_eenh_sub
            exercises_tien_eenh_sub = sub['tien_eenh']['exercises']
            exercises[5] = exercises_tien_eenh_sub
        if "6" in number_categories:
            global exercises_door_tien_eenh
            exercises_door_tien_eenh = sub['door_tien_eenh']['exercises']
            exercises[6] = exercises_door_tien_eenh
    print("Exercises: ")
    print(str(exercises))


def load_answers(number_categories):
    """
    Open the json file containing the answers for session 1.
    Assign it to the global variable to be used in other methods as well.
    :return: answers
    """
    with open(os.path.join(os.path.dirname(__file__), 'exercises2.json')) as data:
        data = json.load(data)
        add = data['add']
        if "0" in number_categories:
            global answers_over_tiental
            answers_over_tiental = add['over_tiental']['answers']
            answers[0] = answers_over_tiental
        if "1" in number_categories:
            global answers_tien_eenh
            answers_tien_eenh = add['tien_eenh']['answers']
            answers[1] = answers_tien_eenh
        if "2" in number_categories:
            global answers_over_tien_eenh
            answers_over_tien_eenh = add['over_tien_eenh']['answers']
            answers[2] = answers_over_tien_eenh
        sub = data['sub']
        if "3" in number_categories:
            global answers_door_tiental
            answers_door_tiental = sub['door_tiental']['answers']
            answers[3] = answers_door_tiental
        if "4" in number_categories:
            global answers_wegdenken
            answers_wegdenken = sub['wegdenken']['answers']
            answers[4] = answers_wegdenken
        if "5" in number_categories:
            global answers_tien_eenh_sub
            answers_tien_eenh_sub = sub['tien_eenh']['answers']
            answers[5] = answers_tien_eenh_sub
        if "6" in number_categories:
            global answers_door_tien_eenh
            answers_door_tien_eenh = sub['door_tien_eenh']['answers']
            answers[6] = answers_door_tien_eenh


def get_count():
    """
    Getter for count variable
    :return: count
    """
    return count


def increase_counter(number_categories):
    max_count = len(number_categories)-1
    global total_count
    total_count += 1
    global count
    if count == max_count:
        count = 0
        increase_round()
    else:
        count += 1
    print("Count: " + str(count))


def get_round():
    global round_count
    return round_count


def get_total():
    return total_count


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


def get_current_exercise(number_categories):
    """
    Return the current exercise to be provided to the student.
    Increase the counter with 1.
    :return: current_exercise
    """
    print("Get exercise from stack.")
    global current_exercise
    if count == 0:
        current_exercise = exercises[int(number_categories[0])].pop(0)
    elif count == 1:
        current_exercise = exercises[int(number_categories[1])].pop(0)
    elif count == 2:
        current_exercise = exercises[int(number_categories[2])].pop(0)

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


def get_current_answer(number_categories):
    global current_answer
    if count == 0:
        current_answer = answers[int(number_categories[0])].pop(0)
    elif count == 1:
        current_answer = answers[int(number_categories[1])].pop(0)
    elif count == 2:
        current_answer = answers[int(number_categories[2])].pop(0)

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
