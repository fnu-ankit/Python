import schedule
import time

def ex():
    print('Hello World!')

schedule.every(7).seconds.do(ex)

while True:
    schedule.run_pending()
    time.sleep(1)
