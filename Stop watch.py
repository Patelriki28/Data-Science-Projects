import time
print("press the ENTER key to start ")
print("press the CTRL+c to exit timer")
while True:
    try:
        input()
        start = time.time()
        print("Started")
    except KeyboardInterrupt:
        print("Stopped")
        end = time.time()
        print("Total Time: ",round(end-start,2),"Seconds")
        break
