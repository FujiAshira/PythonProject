Word = input("Input word to reversed : ")
LenWord = len(Word)
Reversed = ""
for i in range(1,LenWord + 1):
    Reversed += Word[LenWord - i]
print(Reversed)
