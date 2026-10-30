import os

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"
os.system("clear")
os.system("alacritty msg config font.size=16")
print("ESHAAN'S ALARM SYSTEM!\n")

import alarm
import lockdown
import typing_test
from faker import Faker

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
os.system("alacritty msg config font.size=11.5")
