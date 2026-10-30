import os

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"
os.system("clear")
os.system("alacritty msg config font.size=16")
os.system("pkill polybar")
print("ESHAAN'S ALARM SYSTEM!\n")

import alarm
import lockdown
import typing_test
from faker import Faker
import sys
from datetime import datetime

wake_up_time = datetime.strptime(sys.argv[1], "%I:%M %p")
while (datetime.now().strftime("%I:%M %p") != wake_up_time):
    time.sleep(10)

def verifyF(inp):
    if len(inp) > 131:
        return verifyF(Faker().paragraph(nb_sentences=5))
    else:
        return inp

alarm.begin()
lockdown.begin()

for i in range(5):
    while (not typing_test.typing_test(verifyF(Faker().paragraph(nb_sentences=5)))):
        pass

lockdown.end()
alarm.end()
os.system("polybar&disown")
os.system("alacritty msg config font.size=11.5")
