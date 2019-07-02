
def explain_session(tts):
    tts.say("Hallo! Leuk dat je weer met mij sommetjes wil maken.")
    tts.say("Ik zal je even uitleggen wat we gaan doen. ")
    # tts.say("Vorig jaar heb je geleerd hoe je erbij en eraf sommen moet maken die tot 100 gaan.")
    tts.say("Wij gaan weer 20 minuten lang rekensommetjes oefenen, die jij de vorige keer fout gedaan hebt.")
    tts.say("Maak je een foutje tijdens het rekenen, dan mag je het nog een keer proberen.")
    tts.say("Aan het eind dansen we weer samen het dansje.")
    # print("Ik zal je even uitleggen wat we gaan doen. " +
    #         "Vorig jaar heb je geleerd hoe je erbij en eraf sommen moet maken die tot 100 gaan." +
    #         "Wij gaan 20 minuten lang rekensommetjes oefenen, die jij uit je hoofd moet proberen uit te rekenen." +
    #         "Gaat dit goed, dan leer ik jou een dansje." +
    #         "Maak je een foutje, dan probeer ik je uit te leggen, hoe het wel moet.")


def explain_matter(tts):
    tts.say("Vorig jaar heb je veel geoefend met het rekenen, vooral met erbij, en eraf sommetjes die tot 100 gaan.")
    tts.say("Je hebt geleerd hoe je over het tiental moet heenrekenen, zoals bijvoorbeeld bij 18, erbij 3, en wat er moet gebeuren als je 12, eraf 4, moet uitrekenen.")
    tts.say("Vandaag gaan we verder met oefenen van deze sommetjes.")
    # print("Vorig jaar heb je veel geoefend met het rekenen, vooral met erbij en eraf sommetjes die tot 100 gaan." +
    #         "Je hebt geleerd hoe je over het tiental moet heenrekenen, zoals bijvoorbeeld bij 18 erbij 3, en wat er moet gebeuren als je 12 eraf 4 moet uitrekenen." +
    #         "Vandaag gaan we verder met oefenen van deze sommetjes.")


def explain_working(tts):
    tts.say("Als je de som niet goed verstaan hebt, of je wil hem tijdens het rekenen nog een keer horen, druk dan zachtjes op mijn hoofd.")
    # print("Als je de som niet goed verstaan hebt, of je wil hem tijdens het rekenen nog een keer horen, druk dan zachtjes op mijn hoofd.")

    tts.say("Als je denkt dat je het antwoord op de som weet, druk dan tegen een van mijn voeten aan, dan zal ik luisteren naar je antwoord.")
    # print("Als je denkt dat je het antwoord op de som weet, druk dan tegen een van mijn voeten aan, dan zal ik luisteren naar je antwoord.")

    tts.say("Denk eraan dat je alleen tegen mij kan praten als mijn ogen blauw kleuren.")
    # print("Denk eraan dat je alleen tegen mij kan praten als mijn ogen blauw kleuren.")


def explain_switch(tts, number, digit1, digit2):
    tts.say(str(number))
    tts.say("Schrijf je als ")
    tts.say(str(digit1))
    tts.say(", en, ")
    tts.say(str(digit2))


def explain_split(tts):
    tts.say("Jammer, bijna goed! Ik denk dat je een fout gemaakt hebt bij het splitsen.")
    tts.say("Hou er rekeneing mee dat je altijd het eerste getal, eraf, het tweede getal moet doen.")
    tts.say("Als dat niet kan, moet je gaan lenen.")
    tts.say("Probeer het nog eens een keer.")


def explain_operator(tts, operator):
    tts.say("Het rekenen ging bijna goed!")
    tts.say("Je hebt een foutje gemaakt bij erbij en eraf.")
    if operator == "erbij":
        tts.say("Erbij betekent dat je het tweede getal bij het eerste getal optelt.")
    elif operator == "eraf":
        tts.say("Eraf betekent dat je het tweede getal van het eerste getal aftrekt.")
    tts.say("Probeer het nog eens een keer.")


def cheer_correct(tts, leds, count):
    leds.post.randomEyes(2)
    if count == 0:
        tts.say("Goed gedaan! Dat is inderdaad het goede antwoord!")
    elif count == 1:
        tts.say("Alweer goed! Je bent goed bezig!")
    elif count == 2:
        tts.say("Je bent een kanjer! Dat is het goede antwoord!")
    elif count == 3:
        tts.say("Ja, helemaal goed! Op naar de volgende!")
    elif count == 4:
        tts.say("Perfect! Precies het goede antwoord!")
    elif count == 5:
        tts.say("Goed zo! Je bent een reken wonder!")
    elif count == 6:
        tts.say("Wat goed! Deze had ik de eerste keer fout!")
    elif count == 7:
        tts.say("Ja! Dat klopt inderdaad!")
    elif count == 8:
        tts.say("Heel goed! Ik ben trots op je!")
    leds.post.reset("FaceLeds")


def wrong_answer(tts, count):
    if count == 0:
        tts.say("Helaas, dat is niet het goede antwoord.")
    elif count == 1:
        tts.say("Je had het bijna goed!")
    elif count == 2:
        tts.say("jammer, niet goed.")
    elif count == 3:
        tts.say("Ik denk dat dat niet klopt.")
    elif count == 4:
        tts.say("Helaas, ik vond deze ook heel lastig.")
    elif count == 5:
        tts.say("Dat is fout. De volgende keer gaat het vast beter.")


def no_answer(tts, count):
    if count == 0:
        tts.say("Ik heb je antwoord niet goed gehoord, wil je dit nog een keer herhalen?")
    elif count == 1:
        tts.say("Ik kon je niet verstaan. Probeer hard en op normaal tempo te praten.")
    elif count == 2:
        tts.say("Sorry, ik verstond niet wat je zei. Zeg het nog eens luid en duidelijk.")
    elif count == 3:
        tts.say("Wat zei je? Ik kon je helaas niet goed horen.")
