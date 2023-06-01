import datetime
import time
import winsound
def set_alarm(alarm_time):
    """function of the alarm"""
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == alarm_time:
            print("wake up")
            #play a sound (windows-specific)
            winsound.Playsound("sound.wav",winsound.SND_ASYNC)
            break
        time.sleep(1)

    alarm_time = input("Enter the alarm time in HH:MM:S S format: ")
    set_alarm(alarm_time)
