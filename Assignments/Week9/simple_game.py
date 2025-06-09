import pygame
import sys
import random

pygame.init()

# Load images
sunflower_img = pygame.transform.scale(pygame.image.load("sunflower.PNG"), (100, 150))
tomato_img = pygame.transform.scale(pygame.image.load("tomato.PNG"), (150, 150))
sun_icon = pygame.transform.scale(pygame.image.load("sun.PNG"), (100, 100))
water_icon = pygame.transform.scale(pygame.image.load("rain.PNG"), (100, 100))
plant_icon = pygame.transform.scale(pygame.image.load("plant.PNG"), (100, 100))

# Screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = (110, 150, 30)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Buttons
font = pygame.font.SysFont(None, 36)
sunflower_button = pygame.Rect(200, 250, 200, 80)
tomato_button = pygame.Rect(400, 250, 200, 80)

sun_rect = sun_icon.get_rect(topleft=(325, 500))
water_rect = water_icon.get_rect(topleft=(150, 500))
plant_rect = plant_icon.get_rect(topleft=(500, 500))

# Fonts
text1 = font.render("sunflower", True, (0, 0, 0))
text2 = font.render("tomato", True, (0, 0, 0))
text3 = font.render("What plant do you want to plant?", True, (0, 0, 0))

# Game state
selected_plant = None
plants = []
GARDEN_RECT = pygame.Rect(50, 50, SCREEN_WIDTH - 100, SCREEN_HEIGHT - 200)

#Plant class
class Plant:
    def __init__(self, x, y, width, height):
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._watered = False
        self._sunlight = False

    def get_position(self):
        return self._x, self._y

    def get_size(self):
        return self._width, self._height

    def set_watered(self):
        self._watered = True

    def set_sunlight(self):
        self._sunlight = True

    def is_watered(self):
        return self._watered

    def is_sunlit(self):
        return self._sunlight

    def draw(self, screen):
        raise NotImplementedError("Subclass must implement draw method")

# Sunflower subclass
class Sunflower(Plant):
    def __init__(self, x, y):
        super().__init__(x, y, 100, 150)

    def draw(self, screen):
        screen.blit(sunflower_img, (self._x, self._y))

# Tomato subclass
class Tomato(Plant):
    def __init__(self, x, y):
        super().__init__(x, y, 150, 150)

    def draw(self, screen):
        screen.blit(tomato_img, (self._x, self._y))

# Helper function
def get_random_position(width, height):
    x = random.randint(GARDEN_RECT.left, GARDEN_RECT.right - width)
    y = random.randint(GARDEN_RECT.top, GARDEN_RECT.bottom - height)
    return x, y

# Main loop
while True:
    screen.fill(BACKGROUND_COLOR)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos

            if selected_plant is None:
                if sunflower_button.collidepoint(mouse_pos):
                    selected_plant = "sunflower"
                    x, y = get_random_position(100, 150)
                    plants.append(Sunflower(x, y))
                    print("Sunflower planted at", x, y)
                elif tomato_button.collidepoint(mouse_pos):
                    selected_plant = "tomato"
                    x, y = get_random_position(150, 150)
                    plants.append(Tomato(x, y))
                    print("Tomato planted at", x, y)

            else:
                if water_rect.collidepoint(mouse_pos) and plants:
                    plants[-1].set_watered()
                    print("Last plant watered")
                elif sun_rect.collidepoint(mouse_pos) and plants:
                    plants[-1].set_sunlight()
                    print("Last plant got sunlight")
                elif plant_rect.collidepoint(mouse_pos):
                    selected_plant = None
                    print("Select another plant")

    # Draw UI
    if selected_plant is None:
        screen.blit(text3, (SCREEN_WIDTH // 2 - text3.get_width() // 2, 200))
        pygame.draw.rect(screen, (255, 223, 0), sunflower_button)
        pygame.draw.rect(screen, (255, 99, 71), tomato_button)
        screen.blit(text1, (sunflower_button.x + 34, sunflower_button.y + 28))
        screen.blit(text2, (tomato_button.x + 55, tomato_button.y + 28))
    else:
        garden_text = font.render("Your garden", True, (0, 0, 0))
        screen.blit(garden_text, (SCREEN_WIDTH // 2 - garden_text.get_width() // 2, 30))

        for plant in plants:
            plant.draw(screen)

        screen.blit(water_icon, (170, 500))
        screen.blit(sun_icon, (325, 500))
        screen.blit(plant_icon, (490, 500))

        water_text = font.render("Water", True, (0, 0, 0))
        sun_text = font.render("Sunlight", True, (0, 0, 0))
        another_text = font.render("Another", True, (0, 0, 0))

        screen.blit(water_text, (190, 470))
        screen.blit(sun_text, (325, 470))
        screen.blit(another_text, (490, 470))

    pygame.display.flip()
