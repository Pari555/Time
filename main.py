import time
#Function: time()
print("Seconds since epoch = " + str(time.time()))

countdown = 3
while (countdown >= 0):
  print(countdown)
  countdown -= 1
  time.sleep(1)
print("VROOOOOOOOOOM!")

startTime = time.time()
userName = input("Type your Name:")
endTime = time.time()
print("Elapsed Time: " + str(endTime-startTime))