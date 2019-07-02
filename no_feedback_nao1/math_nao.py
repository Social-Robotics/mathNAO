def mistakes_rijgen(a, b, operator):
    rijg = []
    digits_a = [int(x) for x in str(a)]
    print("Digits from first number are: " + str(digits_a))
    digits_b = [int(x) for x in str(b)]
    print("Digits from second number are: " + str(digits_b))
    if operator == "erbij":
        units = int(digits_a[len(digits_a)-1]) + int(digits_b[len(digits_b)-1])
        if units > 10:
            units -= 10
            rijg.append(int(a) + int(b) - int(units))
            print(str(rijg))
    elif operator == "eraf":
        units = int(digits_a[len(digits_a) - 1]) - int(digits_b[len(digits_b) - 1])
        if units < 0:
            units = abs(units)
            rijg.append(int(a) - int(b) + int(units))
            print(str(rijg))
    return rijg


def mistakes_tussenstap(a, b, operator):
    fault = []



def mistakes_operator(a, b, operator):
    fault = []
    if operator == "erbij":
        fault.append(int(a) - int(b))
    elif operator == "eraf":
        fault.append(int(a) + int(b))
    return fault


def mistakes_splitsen(a, b, operator):
    split = []
    digits_a = [int(x) for x in str(a)]
    # print("Digits from first number are: " + str(digits_a))
    digits_b = [int(x) for x in str(b)]
    # print("Digits from second number are: " + str(digits_b))
    if operator == "erbij":
        if len(digits_a) is 2 and len(digits_b) is 2:
            tens = int(digits_a[0] + digits_b[0])
            print("Tens added: " + str(tens))
            units = int(digits_a[1] + digits_b[1])
            print("Units added: " + str(units))
    elif operator == "eraf":
        if len(digits_a) == 2 and len(digits_b) == 2:
            tens = int(digits_a[0] - digits_b[0])
            print("Tens subtracted: " + str(tens))
            units = (int(digits_a[1] - digits_b[1]))
            print("Units subtracted: " + str(units))
            if units < 0:
                units = abs(units)
                split.append(int(str(tens) + str(units)))
                print split
    return split


def mistakes_switched(a, b, operator):
    switch = []
    digits_a = [int(x) for x in str(a)]
    # print("Digits from first number are: " + str(digits_a))
    digits_b = [int(x) for x in str(b)]
    # print("Digits from second number are: " + str(digits_b))

    if len(digits_a) > 1:
        new_a = int(str(digits_a[1]) + str(digits_a[0]))
    else:
        new_a = 0
    if len(digits_b) > 1:
        new_b = int(str(digits_b[1]) + str(digits_b[0]))
    else:
        new_b = 0

    if operator == "erbij":
        switch = [int(new_a) + int(b), int(new_b) + int(a), int(new_a) + int(new_b)]
        print("Possible switched answers: " + str(switch))
    elif operator == "eraf":
        switch = [int(new_a) - int(b), int(new_b) - int(a), int(new_a) - int(new_b)]
        print("Possible switched answers: " + str(switch))
    return switch


def rijgen(tts, a, b, operator):
    digits_a = [int(x) for x in str(a)]
    print("Digits from first number are: " + str(digits_a))
    digits_b = [int(x) for x in str(b)]
    print("Digits from second number are: " + str(digits_b))

    if operator == "erbij":
        if int(a) > 10 and int(b) > 10:
            tts.say("We tellen eerst de tientallen van het tweede getal bij het eerste getal op.")
            tientallen = int(digits_b[0])*10 + int(a)
            tts.say(str(a) + ", erbij " + str(int(digits_b[0])*10) + ", is " + str(tientallen))
            print("Tientallen: " + str(a) + " erbij " + str(int(digits_b[0])*10) + " is " + str(tientallen))
        else:
            tientallen = int(a)

        units = int(digits_a[len(digits_a) - 1]) + int(digits_b[len(digits_b) - 1])
        tts.say("We kijken of de eenheden bij elkaar opgeteld meer dan 10 zijn")
        if units > 10:
            tts.say("In dit geval, is dat zo.")
            tts.say(str(digits_a[len(digits_a) - 1]) + ", erbij " + str(digits_b[len(digits_b) - 1]))

            tts.say("Is meer dan 10. We tellen eerst door tot een heel tiental.")
            over_tiental = 10 - int(digits_a[len(digits_a) - 1])
            tussenstop = int(tientallen) + int(over_tiental)
            tts.say(str(tientallen) + ", erbij " + str(over_tiental) + ", is " + str(tussenstop))
            print("Eenheden>10: " + str(tientallen) + " erbij " + str(over_tiental) + " is " + str(tussenstop))

            tts.say("Daarna tellen we de rest erbij op.")
            rest = int(digits_b[len(digits_b) - 1]) - over_tiental
            uitkomst = int(a) + int(b)
            tts.say(str(tussenstop) + ", erbij " + str(rest) + ", is " + str(uitkomst))
            print("Rest: " + str(tussenstop) + " erbij " + str(rest) + " is " + str(uitkomst))
        else:
            tts.say("In dit geval is dat niet zo. We kunnen dus de eenheden gemakkelijk bij elkaar optellen.")
            uitkomst = tientallen + int(digits_b[len(digits_b) - 1])
            tts.say(str(tientallen) + ", erbij " + str(digits_b[len(digits_b) - 1]) + ", is " + str(uitkomst))
            print("Eenheden<10: " + str(tientallen) + " erbij " + str(digits_b[len(digits_b) - 1]) + " is " + str(uitkomst))

    elif operator == "eraf":
        if int(a) > 10 and int(b) > 10:
            tts.say("We trekken eerst de tientallen van het tweede getal af van het eerste getal.")
            tientallen = int(a) - int(digits_b[0])*10
            tts.say(str(a) + ", eraf " + str(int(digits_b[0])*10) + ", is " + str(tientallen))
            print("Tientallen: " + str(a) + " eraf " + str(int(digits_b[0])*10) + " is " + str(tientallen))

        else:
            tientallen = int(a)

        units = int(digits_a[len(digits_a) - 1]) - int(digits_b[len(digits_b) - 1])
        tts.say("We trekken de eenheden van elkaar af.")
        if units < 0 and int(tientallen) > 20:
            tts.say("In dit geval kunnen we niet zomaar de eenheden van elkaar aftrekken.")
            tts.say(str(digits_a[len(digits_a) - 1]) + ", eraf " + str(digits_b[len(digits_b) - 1]))
            tts.say("Dat kan niet.")
            tts.say("We moeten dus even een tiental lenen. Dit trekken we van " + str(int(digits_a[0])*10) + " af.")
            tts.say(str(int(digits_a[0])*10) + " wordt dan, " + str(int(digits_a[0])*10-10))
            print("Lenen: " + str(int(digits_a[0])*10) + " eraf " + str(10) + " is " + str(int(digits_a[0])*10-10))

            tts.say("Nu kunnen we de som wel uitrekenen.")
            door_tiental = int(digits_a[len(digits_a) - 1]) + 10
            tussenstop = int(door_tiental) - (digits_b[len(digits_b) - 1])
            tts.say(str(door_tiental) + ", eraf " + str(digits_b[len(digits_b) - 1]) + ", is " + str(tussenstop))
            print("Tientallen: " + str(door_tiental) + " eraf " + str(digits_b[len(digits_b) - 1]) + " is " + str(tussenstop))

            tts.say("Nu tellen we de twee stappen bij elkaar op, om tot het antwoord te, komen")
            uitkomst = int(a) - int(b)

            tts.say(str(int(tientallen)-10) + ", erbij " + str(tussenstop) + ", is " + str(uitkomst))
            print("Rest: " + str(int(tientallen)-10) + " eraf " + str(tussenstop) + " is " + str(uitkomst))

        elif units < 0 and int(tientallen) < 20:
            tts.say("In dit geval kunnen we niet zomaar de eenheden van elkaar aftrekken.")
            tts.say(str(digits_a[len(digits_a) - 1]) + ", eraf " + str(digits_b[len(digits_b) - 1]))
            tts.say("Dat kan niet.")
            tts.say("We gaan eerst aftrekken, tot een heel tiental.")
            tussenstop = int(tientallen) - digits_a[len(digits_a) - 1]
            tts.say(str(tientallen) + ", eraf " + str(digits_a[len(digits_a) - 1]) + ", is " + str(tussenstop))

            tts.say("Nu nog de rest eraf halen")
            rest = abs(int(units))
            uitkomst = int(a) - int(b)
            tts.say(str(tussenstop) + ", eraf " + str(rest) + ", is " + str(uitkomst))
        else:
            uitkomst = int(tientallen) - int(digits_b[len(digits_b) - 1])
            tts.say(str(tientallen) + ", eraf " + str(digits_b[len(digits_b) - 1]) + ", is " + str(uitkomst))
            print("Rest: " + str(int(tientallen)) + " eraf " + str(str(digits_b[len(digits_b) - 1])) + " is " + str(uitkomst))

    tts.say("Het antwoord is dus: " + str(uitkomst))
