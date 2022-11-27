import pygame
from pygame import mixer

import random
from time import sleep

class SchoolRace:

    def __init__(self):
        pygame.init()
        self.display_width = 800
        self.display_height = 600
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.clock = pygame.time.Clock()
        self.initialize()


    def initialize(self):
        self.crashed = False

        self.pencilImg = pygame.image.load("pencil.png")
        self.pencil_x_coordinate = (self.display_width * 0.45)
        self.pencil_y_coordinate = (self.display_height * 0.8)
        self.pencil_width = 40

        self.sharpener = pygame.image.load("sharpener.png")
        self.sharpener_startx = random.randrange(325, 420)
        self.sharpener_starty = -600
        self.sharpener_speed = 5
        self.sharpener_width = 40
        self.sharpener_height = 50

        self.point = pygame.image.load("a-mark.png")
        self.point_startx = random.randrange(325, 420)
        self.point_starty = -600
        self.point_speed = 5
        self.point_width = 32
        self.point_height = 32
        self.value = 0

        icon = pygame.image.load("school.png")
        pygame.display.set_icon(icon)

        self.bgImg = pygame.image.load("background.jpg")
        self.bg_x1 = (self.display_width / 2) - (360 / 2)
        self.bg_x2 = (self.display_width / 2) - (360 / 2)
        self.bg_y1 = 0
        self.bg_y2 = -600
        self.bg_speed = 3
        self.count = 0

        mixer.music.load("engine.wav")
        mixer.music.play(-1)

    def game_window(self):
        self.gameDisplay = pygame.display.set_mode((self.display_width, self.display_height))
        pygame.display.set_caption('School Race')
        self.run_pencil()

    def display_message(self, msg):
        font = pygame.font.Font("KGHolocene.ttf", 72)
        text = font.render(msg, True, (255, 255, 255))
        self.gameDisplay.blit(text, (400 - text.get_width() // 2, 240 - text.get_height() // 2))
        self.display_end()
        pygame.display.update()
        self.clock.tick(60)
        sleep(1.5)
        school_race.initialize()
        school_race.game_window()

    def background(self):
        self.gameDisplay.blit(self.bgImg, (self.bg_x1, self.bg_y1))
        self.gameDisplay.blit(self.bgImg, (self.bg_x2, self.bg_y2))

        self.bg_y1 += self.bg_speed
        self.bg_y2 += self.bg_speed

        if self.bg_y1 >= self.display_height:
            self.bg_y1 = -600

        if self.bg_y2 >= self.display_height:
            self.bg_y2 = -600

    def distance(self, count):
        font = pygame.font.Font("KGHolocene.ttf", 20)
        text = font.render("Distance : " + str(count), True, self.white)
        self.gameDisplay.blit(text, (0, 0))

    def score(self, value):
        font = pygame.font.Font("KGHolocene.ttf", 20)
        text = font.render("Score : " + str(value), True, self.white)
        self.gameDisplay.blit(text, (0, 30))

    def display_end(self):
        font = pygame.font.Font("KGHolocene.ttf", 14)
        text = font.render("Thanks for playing!", True, self.white)
        self.gameDisplay.blit(text, (600, 520))

    def pencil(self, pencil_x_coordinate, pencil_y_coordinate):
        self.gameDisplay.blit(self.pencilImg, (pencil_x_coordinate, pencil_y_coordinate))

    def run_sharpener(self, thinga, thingb):
        self.gameDisplay.blit(self.sharpener, (thinga, thingb))

    def run_point(self, thingc, thingd):
        self.gameDisplay.blit(self.point, (thingc, thingd))

    def run_pencil(self):

        while not self.crashed:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.crashed = True

                if (event.type == pygame.KEYDOWN):
                    if (event.key == pygame.K_LEFT):
                        self.pencil_x_coordinate -= 50
                    if (event.key == pygame.K_RIGHT):
                        self.pencil_x_coordinate += 50

            self.gameDisplay.fill(self.black)
            self.background()

            self.run_sharpener(self.sharpener_startx, self.sharpener_starty)
            self.sharpener_starty += self.sharpener_speed

            if self.sharpener_starty > self.display_height:
                self.sharpener_starty = 0 - self.sharpener_height
                self.sharpener_startx = random.randrange(310, 450)

            self.run_point(self.point_startx, self.point_starty)
            self.point_starty += self.point_speed

            if self.point_starty > self.display_height:
                self.point_starty = 0 - self.point_height
                self.point_startx = random.randrange(320, 440)

            self.pencil(self.pencil_x_coordinate, self.pencil_y_coordinate)
            self.distance(self.count)
            self.count += 1
            if (self.count % 100 == 0):
                self.sharpener_speed += 0.5
                self.bg_speed += 1

            if self.pencil_y_coordinate < self.sharpener_starty + self.sharpener_height:
                if self.pencil_x_coordinate > self.sharpener_startx and self.pencil_x_coordinate < self.sharpener_startx + self.sharpener_width or self.pencil_x_coordinate + self.pencil_width > self.sharpener_startx and self.pencil_x_coordinate + self.pencil_width < self.sharpener_startx + self.sharpener_width:
                    self.crashed = True
                    crash_sound = mixer.Sound("crash.wav")
                    crash_sound.play()
                    self.display_message("Game Over!")

            if self.pencil_x_coordinate < 310 or self.pencil_x_coordinate > 420:
                self.crashed = True
                crash_sound = mixer.Sound("crash.wav")
                crash_sound.play()
                self.display_message("Game Over!")

            self.score(self.value)
            if self.pencil_y_coordinate < self.point_starty + self.point_height:
                if self.pencil_x_coordinate > self.point_startx and self.pencil_x_coordinate < self.point_startx + self.point_width or self.pencil_x_coordinate + self.pencil_width > self.point_startx and self.pencil_x_coordinate + self.pencil_width < self.point_startx + self.point_width:
                    self.value += 1
                    point_sound = mixer.Sound("point.wav")
                    point_sound.play()

            pygame.display.update()
            self.clock.tick(60)

if __name__ == '__main__':
    school_race = SchoolRace()
    school_race.game_window()