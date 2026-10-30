import numpy as np
import threading
import pygame
import time
import math
import os

ring = True

def internal_begin():
    os.system("pactl set-sink-volume @DEFAULT_SINK@ 60%");
    pygame.mixer.pre_init(44100, -16, 2, 512)
    pygame.init()
    SAMPLE_RATE = 44100

    duration = 0.8
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration), False)
    wave = (
        0.65 * np.sin(2 * np.pi * 1200 * t) +
        0.65 * np.sin(2 * np.pi * 1600 * t) +
        0.35 * np.sin(2 * np.pi * 2400 * t)
    )

    wave = np.sign(wave) * np.abs(wave) ** 0.7
    wave = wave / np.max(np.abs(wave)) * 0.85

    audio = np.column_stack((wave, wave))
    audio = (audio * 32767).astype(np.int16)

    alarm = pygame.sndarray.make_sound(audio)

    while ring:
        alarm.play()
        time.sleep(0.85)

    pygame.quit()

def begin():
    threading.Thread(target = internal_begin).start()

def end():
    global ring
    ring = False

