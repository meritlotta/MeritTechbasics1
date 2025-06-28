import pygame
import random
import time

pygame.init()

screen_width, screen_height = 600, 600
screen_size = (screen_width, screen_height)
display = pygame.display.set_mode((screen_width, screen_height))


# timer

# set box
box = pygame.image.load("box.png").convert_alpha()
box = pygame.transform.scale(box, (150, 150))

box_rect = box.get_rect()
box_rect.center = (screen_width // 2, screen_height // 2)

# set random objects
class Object:
    def __init__(self, image_path, size, screen_size, flip_x=False, flip_y=False):
        self.visible = True
        original_image = pygame.image.load(image_path).convert_alpha()
        original_image = pygame.transform.scale(original_image, size)
        original_image = pygame.transform.flip(original_image, flip_x, flip_y)

        # random rotation
        rotation_angle = random.randint(-10, 10)
        rotated_image = pygame.transform.rotate(original_image, rotation_angle)

        # Set image
        self.image = rotated_image
        self.rect = self.image.get_rect()

        # random position
        self.rect.topleft = (
            random.randint(0, screen_size[0] - self.rect.width),
            random.randint(0, screen_size[1] - self.rect.height)
        )

        self.dragging = False
        self.offset_x = 0
        self.offset_y = 0

    def draw(self, screen):
        if self.visible:
            screen.blit(self.image, self.rect.topleft)

    def handle_mouse_down(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.dragging = True
            mouse_x, mouse_y = mouse_pos
            self.offset_x = self.rect.x - mouse_x
            self.offset_y = self.rect.y - mouse_y
            return True
        return False

    def handle_mouse_up(self, box_rect, mouse_pos):
        self.dragging = False
        if box_rect.collidepoint(mouse_pos):
            self.visible = False

    def handle_mouse_motion(self, mouse_pos):
        if self.dragging:
            mouse_x, mouse_y = mouse_pos
            self.rect.x = mouse_x + self.offset_x
            self.rect.y = mouse_y + self.offset_y


def reset_objects():
    items = []

    def add_items(image_path, size, count):
        for _ in range(count):
            flip_x = random.choice([True, False])
            flip_y = False
            items.append(Object(image_path, size, screen_size, flip_x, flip_y))

    add_items("sock.WEBP", (80, 100), random.randint(1, 5))
    add_items("banana.PNG", (100, 50), random.randint(1, 5))
    add_items("mug.png", (100, 100), random.randint(1, 5))
    add_items("football.PNG", (90, 90), random.randint(1, 5))
    add_items("umbrella.PNG", (150, 150), random.randint(1, 5))
    add_items("sunglasses.PNG", (120, 70), random.randint(1, 5))
    add_items("cd.PNG", (70, 70), random.randint(1, 5))
    add_items("toiletpaper.png", (100, 100), random.randint(1, 5))
    add_items("money.png", (100, 100), random.randint(1, 5))
    add_items("beer.PNG", (100, 120), random.randint(1, 5))
    add_items("plant.WEBP", (200, 200), random.randint(1, 5))
    add_items("brokkoli.png", (200, 200), random.randint(1, 5))
    add_items("clock.PNG", (80, 75), random.randint(1, 5))

    return items


# play again
class Button:
    def __init__(self, text, position, size):
        self.font = pygame.font.SysFont("comicsans", 30)
        self.text = text
        self.position = position
        self.size = size

        self.rect = pygame.Rect(position, size)
        self.text_surf = self.font.render(text, True, (255, 255, 255))
        self.text_rect = self.text_surf.get_rect(center=self.rect.center)

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 128, 0), self.rect, border_radius=10)
        screen.blit(self.text_surf, self.text_rect)

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)


def all_cleaned(objects):
    return all(not obj.visible for obj in reversed(objects))


objects = reset_objects()
game_started = False
game_finished = False

button_width, button_height = 200, 50
button_x = screen_width // 2 - button_width // 2
button_y = screen_height // 2 + 80

restart_button = Button("Play Again?", (button_x, 450), (button_width, button_height))
start_button = Button("Got it", (screen_width // 2 - 75, screen_height // 2 + 80), (150, 60))

dragged_object = None
game_started = False

start_time = 0
elapsed_time = 0
game_finished = False


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


        elif event.type == pygame.MOUSEBUTTONDOWN:
            if not game_started:
                if start_button.is_clicked(event.pos):
                    game_started = True
                    start_time = time.time()
                    game_finished = False

            else:
                if game_finished and restart_button.is_clicked(event.pos):
                    objects = reset_objects()
                    start_time = time.time()
                    game_finished = False
                    dragged_object = None

                else:
                    for obj in reversed(objects):
                        if obj.visible and obj.handle_mouse_down(event.pos):
                            dragged_object = obj
                            objects.remove(obj)
                            objects.append(obj)
                            break

        elif event.type == pygame.MOUSEBUTTONUP:
            if dragged_object:
                dragged_object.handle_mouse_up(box_rect, event.pos)
                dragged_object.dragging = False
                dragged_object = None

        elif event.type == pygame.MOUSEMOTION:
            if dragged_object:
                dragged_object.handle_mouse_motion(event.pos)

    display.fill((220, 220, 220))

    if not game_started:
        font = pygame.font.SysFont("comicsans", 28)
        msg = "Clean up the items and put them in the box"
        text_surf = font.render(msg, True, (0, 0, 0))
        text_rect = text_surf.get_rect(center=(screen_width // 2, screen_height // 2 - 40))
        display.blit(text_surf, text_rect)
        start_button.draw(display)

    else:
        display.blit(box, box_rect.topleft)

        for obj in reversed(objects):
            obj.draw(display)

        if all_cleaned(objects):
            font = pygame.font.SysFont("comicsans", 30)
            line1 = font.render("All cleaned up!", True, (0, 128, 0))
            line2 = font.render(f"This took you {elapsed_time:.2f} seconds", True, (0, 128, 0))
            line1_rect = line1.get_rect(center=(screen_width // 2, 180))
            line2_rect = line2.get_rect(center=(screen_width // 2, 400))  # slightly below line1
            display.blit(line1, line1_rect)
            display.blit(line2, line2_rect)

            restart_button.draw(display)

            if not game_finished:
                elapsed_time = time.time() - start_time  # Current time minus start time
                game_finished = True  # Mark that game is done

    pygame.display.flip()
