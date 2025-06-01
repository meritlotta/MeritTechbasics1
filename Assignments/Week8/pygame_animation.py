import sys
import pygame
import random

# constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500
BACKGROUND_COLOR = (143, 175, 66)

# activate pygame library
pygame.init()

# create game surface
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# set pygame window name
pygame.display.set_caption("image")


class Chicken1:
    def __init__(self):
        # set the chicken on screen
        self.img = pygame.image.load("chicken_right.PNG").convert_alpha()
        self.img = pygame.transform.scale(self.img, (100,100))

        # position of the chicken
        self.chicken1_x = -self.img.get_width()
        self.chicken1_y = random.randint(0,SCREEN_HEIGHT - 150)

        # animation variables
        self.speed = random.uniform(0.1, 2)
        self.direction = 1

    def update(self):
        self.chicken1_x += self.speed * self.direction

    def draw(self, screen):
        screen.blit(self.img, (self.chicken1_x, self.chicken1_y))


class Chicken2:
    def __init__(self):
        # set the chicken on screen
        self.img = pygame.image.load("chicken_right.PNG").convert_alpha()
        self.img = pygame.transform.scale(self.img, (150,150))

        # position of the chicken
        self.chicken_x = -self.img.get_width()
        self.chicken_y = random.randint(0,SCREEN_HEIGHT - 150)

        # animation variables
        self.speed = random.uniform(0.1, 2)
        self.direction = 1

    def update(self):
        self.chicken_x += self.speed * self.direction

    def draw(self, screen):
        screen.blit(self.img, (self.chicken_x, self.chicken_y))

class Chicken3:
    def __init__(self):
        # set the chicken on screen
        self.img = pygame.image.load("chicken_left.PNG").convert_alpha()
        self.img = pygame.transform.scale(self.img, (200,200))

        # position of the chicken
        self.chicken3_x = SCREEN_WIDTH
        self.chicken3_y = random.randint(0, SCREEN_HEIGHT - 150)

        # animation variables
        self.speed = random.uniform(0.1, 2)
        self.direction = -1

    def update(self):
        self.chicken3_x += self.speed * self.direction

    def draw(self, screen):
        screen.blit(self.img, (self.chicken3_x, self.chicken3_y))


class Chicken4:
    def __init__(self):
        # set the chicken on screen
        self.img = pygame.image.load("chicken_left_brown.png").convert_alpha()
        self.img = pygame.transform.scale(self.img, (300,300))

        # position of the chicken
        self.chicken4_x = SCREEN_WIDTH
        self.chicken4_y = random.randint(0, SCREEN_HEIGHT - 150)

        # animation variables
        self.speed = random.uniform(0.1, 2)
        self.direction = -1

    def update(self):
        self.chicken4_x += self.speed * self.direction

    def draw(self, screen):
        screen.blit(self.img, (self.chicken4_x, self.chicken4_y))

class Sun:
    def __init__(self):
        #set sun on screen
        self.original_img = pygame.image.load("sun.png").convert_alpha()
        self.original_img = pygame.transform.scale(self.original_img, (200, 200))
        self.img = self.original_img

        #position of the sun
        self.sun_x = 100
        self.sun_y = 100

        #rotation angle
        self.angle = 0

    def update(self):
        self.angle += 0.1
        self.img = pygame.transform.rotate(self.original_img, self.angle)

    def draw(self):
        rect = self.img.get_rect(center=(self.sun_x, self.sun_y))
        screen.blit(self.img, rect)

sun = Sun()
chicken1 = Chicken1()
chicken2 = Chicken2()
chicken3 = Chicken3()
chicken4 = Chicken4()


while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BACKGROUND_COLOR)

    sun.update()
    sun.draw()

    chicken1.update()
    chicken1.draw(screen)

    chicken2.update()
    chicken2.draw(screen)

    chicken3.update()
    chicken3.draw(screen)

    chicken4.update()
    chicken4.draw(screen)


    pygame.display.flip()
