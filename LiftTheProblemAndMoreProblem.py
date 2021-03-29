import random

def Check(NameLift, Number):
    global level
    global NearDict
    NameLift = int(NameLift)
    morethan = NameLift - level
    lessthan = level - NameLift
    if morethan > lessthan:
        NearDict[Number] = morethan
    elif lessthan > morethan:
        NearDict[Number] = lessthan
    elif morethan == lessthan:
        NearDict[Number] = morethan or lessthan
    else:
        print("Error")
    # print(Number)
    # print(NearDict[Number])
    # print(NearDict)
    # print(NameLift)
    # print("------")
    return NearDict
Lift1 = random.randint(1, 25)
Lift2 = random.randint(1, 25)
Lift3 = random.randint(1, 25)
Lift4 = random.randint(1, 25)
Lift5 = random.randint(1, 25)
a = True
while True:
    Near1 = 0
    Near2 = 0
    Near3 = 0
    Near4 = 0
    Near5 = 0
    LiftDict = {1: Lift1, 2: Lift2, 3: Lift3, 4: Lift4, 5: Lift5}
    NearDict = {1: Near1, 2: Near2, 3: Near3, 4: Near4, 5: Near5}
    while a:
        level = input("Insert floor that you are there (1-25) = ")
        try:
            level = int(level)
            if level > 25 or level < 1:
                print("Out of index")
                continue
            a = False
        except:
            print("try again")
    for i in range(1, (len(LiftDict)+1)):
        Check(LiftDict[i], i)
    LeastNearLift = min(NearDict.values())
    #print(LeastNearLift)
    DictOfLiftComing: list[int] = []  #3,5
    n = 0
    print("Lift 1 =", Lift1)
    print("Lift 2 =", Lift2)
    print("Lift 3 =", Lift3)
    print("Lift 4 =", Lift4)
    print("Lift 5 =", Lift5)
    for i in range(1, (len(NearDict)+1)):
        n += 1
        if NearDict[i] == LeastNearLift:
            DictOfLiftComing.append(n)
    if len(DictOfLiftComing) == 1:
        print("Lift number", DictOfLiftComing[0], "are coming")
    elif len(DictOfLiftComing) == 2:
        print("lift number", DictOfLiftComing[0], "or", DictOfLiftComing[1], "are coming")
    elif len(DictOfLiftComing) == 3:
        print("lift number", DictOfLiftComing[0], "or", DictOfLiftComing[1], "or", DictOfLiftComing[2], "are coming")
    elif len(DictOfLiftComing) == 4:
        print("lift number", DictOfLiftComing[0], "or",  DictOfLiftComing[1], "or", DictOfLiftComing[2], "or", DictOfLiftComing[3], "are coming")
    elif len(DictOfLiftComing) == 5:
        print("lift number", DictOfLiftComing[0], "or", DictOfLiftComing[1], "or", DictOfLiftComing[2], "or", DictOfLiftComing[3], "or", DictOfLiftComing[4], "are coming")
        stop = input()
    else:
        print("Error")
    if len(DictOfLiftComing) == 1:
        i = DictOfLiftComing[0]
        i = int(i)
        if i == 1:
            Lift1 = level
        elif i == 2:
            Lift2 = level
        elif i == 3:
            Lift3 = level
        elif i == 4:
            Lift4 = level
        elif i == 5:
            Lift5 = level
        else:
            print("Error")
    elif len(DictOfLiftComing) > 1:
        try:
            iChoose = random.choice(DictOfLiftComing[0], DictOfLiftComing[1], DictOfLiftComing[2], DictOfLiftComing[3], DictOfLiftComing[4])
        except:
            try:
                iChoose = random.choice(DictOfLiftComing[0], DictOfLiftComing[1], DictOfLiftComing[2], DictOfLiftComing[3])
            except:
                try:
                    iChoose = random.choice(DictOfLiftComing[0], DictOfLiftComing[1], DictOfLiftComing[2])
                except:
                    try:
                        iChoose = random.choice(DictOfLiftComing[0], DictOfLiftComing[1])
                    except:
                        try:
                            iChoose = DictOfLiftComing[0]
                        except:
                            None
        if iChoose == 1:
            Lift1 = level
        elif iChoose == 2:
            Lift2 = level
        elif iChoose == 3:
            Lift3 = level
        elif iChoose == 4:
            Lift4 = level
        elif iChoose == 5:
            Lift5 = level
        else:
            print("Error")
    a = True

