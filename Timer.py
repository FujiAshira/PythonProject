import playsound
import time as t

time = input(
    "Write down time, example '1h34m56s' for 1 hour 34 minutes and 56 seconds (Can't read more than 2 number of time) : ")
hour = 0
minute = 0
second = 0
per = 1
tick = 1
if "h" in time:
    count = -1
    for i in time:
        count += 1
        if i == "h":
            count -= 2
            try:
                hour = str(time[count])
                count += 1
                hour = hour + str(time[count])
                hour = int(hour)
            except:
                try:
                    hour = str(time[count])
                except:
                    hour = 0
else:
    hour = 0

if "m" in time:
    count = -1
    for i in time:
        count += 1
        if i == "m":
            count -= 2
            try:
                minute = str(time[count])
                count += 1
                minute = minute + str(time[count])
                minute = int(minute)
            except:
                try:
                    minute = str(time[count])
                    minute = int(minute)
                except:
                    minute = 0
else:
    minute = 0

if "s" in time:
    count = -1
    for i in time:
        count += 1
        if i == "s":
            count -= 2
            try:
                second = str(time[count])
                count += 1
                second = second + str(time[count])
                second = int(second)
            except:
                try:
                    second = str(time[count])
                    second = int(second)
                except:
                    second = 0
else:
    second = 0

if "p" in time:
    count = -1
    for i in time:
        count += 1
        if i == "p":
            count -= 2
            try:
                per = str(time[count])
                count += 1
                per = per + str(time[count])
                per = int(per)
            except:
                try:
                    per = str(time[count])
                    per = int(second)
                except:
                    per = 1
else:
    per = 1

if "t" in time:
    count = -1
    for i in time:
        count += 1
        if i == "t":
            count -= 2
            try:
                tick = str(time[count])
                count += 1
                tick = tick + str(time[count])
                tick = int(tick)
            except:
                try:
                    tick = str(time[count])
                    tick = int(second)
                except:
                    tick = 1
else:
    tick = 1

AT = (int(hour) * 3600) + (int(minute) * 60) + (int(second) * 1)
S = 1 / per * tick
while AT != 0:
    HL = AT // 3600
    HAL = AT // 3600
    ML = (AT % 3600) // 60
    MAL = (AT // 60)
    SL = (AT % 3600) % 60
    print("------------------------",
          "\nHour left :", HL,
          "\nMinute left :", ML,
          "\nSecond left :", SL,
          "\nAll hour left :", HAL,
          "\nAll minute left :", MAL,
          "\nAll second left :", AT)
    t.sleep(S)
    AT -= 1

print("         -------------          ""\n"
      "        /0-----------0\\          ""\n"
      "       /0/00000000000\\0\\         ""\n"
      "      /0/------/-\\/-\\|\\0\\        ""\n"
      "     |0|00/0|-0|0/|0||0|0|       ""\n"
      "     |0|0|00|00|/0|0||0|0|       ""\n"
      "      \\0\\------|0\\\\-/o/0/       ""\n"
      "       \\0\\00000000000/0/        ""\n"
      "        \\0-----------0/         ""\n"
      "         -------------           ")
playsound.playsound('Camera Timer.mp3')
