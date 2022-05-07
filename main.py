import pygame


class BaseSprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        print(f'BaseSprite\n')


class Character(BaseSprite):
    def __init__(self):
        super().__init__()
        print(f'Character\n')


class Actor(Character):
    def __init__(self):
        super().__init__()
        print(f'Actor\n')


class Protagonist(Actor):
    def __init__(self):
        super().__init__()
        print(f'Protagonist\n')


class Antagonist(Actor):
    def __init__(self):
        super().__init__()
        print(f'Antagonist\n')


class Deuteragonist(Protagonist):
    def __init__(self):
        super().__init__()
        print(f'Deuteragonist\n')


class TertiaryCharacters(Deuteragonist):
    def __init__(self):
        super().__init__()
        print(f'TertiaryCharacters\n')


character = TertiaryCharacters()
