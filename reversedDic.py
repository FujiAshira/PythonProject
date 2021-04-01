TestTrue = True
Time = 1
print("Exit use 'Exit' keys")
print("Check use 'Check' keys")
print("using space bar or ( same key or value ) may get confused")
print("this is in beta so some bugs have in here")
dict1 = {}
ExitOutDict1 = ["exit", "exiT", "exIt", "exIT", "eXit", "eXiT", "eXIt", "eXIT", "Exit", "ExiT", "ExIt", "ExIT", "EXit",
                "EXiT", "EXIt", "EXIT"]
CheckDict1 = ["check", "checK", "cheCk", "cheCK", "chEck", "chEcK", "chECk", "chECK", "cHeck", "cHecK", "cHeCk",
              "cHeCK", "cHEck", "cHEcK", "cHECk", "cHECK", "Check", "ChecK", "CheCk", "CheCK", "ChEck", "ChEcK",
              "ChECk", "ChECK", "CHeck", "CHecK", "CHeCk", "CHeCK", "CHEck", "CHEcK", "CHECk", "CHECK"]
while TestTrue:
    print("Number of Dict : ", Time)
    KeyDict1 = input("List in Dict : ")
    if KeyDict1 in ExitOutDict1:
        TestTrue = False
        continue
    elif KeyDict1 in CheckDict1:
        print(dict1)
        continue
    ValueDict1 = input("Value in Dict : ")
    if KeyDict1 in ExitOutDict1 or ValueDict1 in ExitOutDict1:
        TestTrue = False
    elif KeyDict1 in CheckDict1 or ValueDict1 in CheckDict1:
        print(dict1)
        continue
    else:
        dict1[KeyDict1] = ValueDict1
    Time += 1
dict2 = {}
for i in range(len(dict1)):
    for j in dict1.keys():
        dict2[dict1[j]] = j
print("\nReversed of Dict : ")
print(dict2)
print("\nKey : ")
print(dict2.keys())
print("\nValue : ")
print(dict2.values())
