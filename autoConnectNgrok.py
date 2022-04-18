import os
import time

time.sleep(40)
#print(os.system("cd .. ; ls -a"))
process = os.system("cd /home/pi; ./ngrok tcp 5900")
