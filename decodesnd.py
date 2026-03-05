import pygame
import time

# if you want to do this with ffmpeg you can use a 1-liner like this:
# ffplay -f s16le -sample_rate 16000 -ch_layout mono S01.snd

def play_snd(file_path):
    pygame.mixer.pre_init(frequency=16000, size=-16, channels=1)
    pygame.init()

    with open(file_path, 'rb') as f:
        raw_data = f.read()

    sound = pygame.mixer.Sound(buffer=raw_data)

    channel = sound.play()
    while channel.get_busy():
        pygame.time.wait(100)

    pygame.quit()

play_snd('S01.snd')
