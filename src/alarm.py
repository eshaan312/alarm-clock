import numpy as np
import threading
import pygame
import time
import math
import os

ring = True

def internal_begin():
    os.system("pactl set-sink-volume @DEFAULT_SINK@ 67%");
    pygame.mixer.pre_init(44100, -16, 2, 512)
    pygame.init()
    SAMPLE_RATE = 44100

    duration = 1.2
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration), False)
    base_wave = (
        0.6 * np.sin(2 * np.pi * 587.33 * t) +  
        0.4 * np.sin(2 * np.pi * 880.00 * t)   
    )

    pulse_frequency = 4.0 
    pulse_envelope = 0.5 * (1 + np.sin(2 * np.pi * pulse_frequency * t))

    wave = base_wave * pulse_envelope

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

