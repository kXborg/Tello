from tello import * 
import threading
import time

def video_pipeline():
    power = get_battery()
    print('Power Level: ', power)
    start_video()


def control_pipeline():
    power = get_battery()
    print('Power Level: ', power)
    takeoff()
    time.sleep(10)
    forward(30)

    
if __name__ == '__main__':
    start()
    
    th1 = threading.Thread(target=video_pipeline)
    th2 = threading.Thread(target=control_pipeline)

    th1.start()
    th2.start()

    th1.join()
    th2.join()

    print('Done!')
