import pygame
import numpy as np
pygame.mixer.init()


def play_sound(value, max_value):
    pygame.mixer.Sound(buffer=generate_sound(value, max_value)).play()


def generate_sound(value, max_value):
    sample_rate = 44100
    duration = 0.2
    frequency = 100 + 200 * value / max_value
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    note = np.sin(frequency * t * 2 * np.pi)
    audio = note * (2**15 - 1) / np.max(np.abs(note))
    audio = audio.astype(np.int16)
    return audio
