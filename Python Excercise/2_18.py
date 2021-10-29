#Current time
GMT_Offset = eval(input("Enter the time zone offset to GMT"))

import time

currentTime = time.time()

totalSeconds = int(currentTime)
currentSeconds = totalSeconds % 60

totalMinutes = totalSeconds // 60
currentMinutes = totalMinutes % 60

totalHours = totalMinutes // 60
currentHour = totalHours % 24 + GMT_Offset

print(currentHour, ":", currentMinutes, ":", currentSeconds)

