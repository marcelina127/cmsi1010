import math, random, pygame
from dataclasses import dataclass

# Constants
WIDTH, HEIGHT = 1024, 600
GRASS_HEIGHT = 100
GROUND_LEVEL = HEIGHT - (GRASS_HEIGHT // 2.5)
GRASS_TOP = HEIGHT - GRASS_HEIGHT
SKY_TOP = (107, 217, 232)
SKY_BOTTOM = (255, 181, 243)
TREE_SPACING = 100
MAX_PLANE_SPEED = 30
CRUISING_ALTITUDE = 50

# Colors
GRASS_COLOR = (116, 247, 151)
CLOUD_COLOR = (255, 207, 247)
FLOWER_PETAL_COLOR = (242, 99, 130)
FLOWER_CENTER_COLOR = (255, 207, 247)
TREE_LEAF_COLOR = (242, 99, 130)

# Game States
STATE_TITLE = "title"
STATE_RUNNING = "running"
STATE_GAME_OVER = "crashed"
game_state = STATE_TITLE

# Initialize
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Plane Landing")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

@dataclass
class Bird:
    x: int
    y: int
    speed: int = 2
    def move(self): self.x -= self.speed
    def draw(self): pygame.draw.polygon(screen, (60, 60, 60), [(self.x, self.y), (self.x + 10, self.y - 5), (self.x + 20, self.y)])

@dataclass
class Plane:
    x: int
    y: int
    state: str = "flying"
    speed: float = MAX_PLANE_SPEED
    color: tuple = (255, 201, 246)
    vertical_velocity: float = 0
    points: int = 0

    def draw(self):
        center_x = WIDTH // 2
        body_len, body_ht = 80, 10
        nose_radius, tail_ht = 10, 20
        wing_w, wing_h = 60, 10
        nose_x = center_x + body_len // 2
        tail_x = center_x - body_len // 2
        pygame.draw.rect(screen, self.color, (tail_x, self.y - body_ht // 2, body_len, body_ht))
        pygame.draw.circle(screen, self.color, (nose_x, self.y), nose_radius)
        pygame.draw.polygon(screen, self.color, [
            (tail_x, self.y - body_ht // 2),
            (tail_x - 10, self.y - body_ht // 2 - tail_ht),
            (tail_x, self.y + body_ht // 2)
        ])
        pygame.draw.rect(screen, (242, 99, 130), (center_x - wing_w // 2, self.y - wing_h // 2, wing_w, wing_h))

    def move(self):
        if self.state != "crashed":
            self.x += self.speed % TREE_SPACING
            self.y += self.vertical_velocity
            if self.y < CRUISING_ALTITUDE:
                self.y = CRUISING_ALTITUDE
            if self.y >= GROUND_LEVEL:
                self.y = GROUND_LEVEL
                self.state = "crashed"
                self.color = (255, 0, 0)

plane = Plane(0, CRUISING_ALTITUDE)
birds = [Bird(random.randint(WIDTH, WIDTH + 300), random.randint(50, 200)) for _ in range(3)]

def draw_gradient_sky():
    for y in range(HEIGHT):
        r = SKY_TOP[0] + (SKY_BOTTOM[0] - SKY_TOP[0]) * y // HEIGHT
        g = SKY_TOP[1] + (SKY_BOTTOM[1] - SKY_TOP[1]) * y // HEIGHT
        b = SKY_TOP[2] + (SKY_BOTTOM[2] - SKY_TOP[2]) * y // HEIGHT
        pygame.draw.line(screen, (r, g, b), (0, y), (WIDTH, y))

def draw_tree(x, y):
    pygame.draw.rect(screen, (132, 209, 158), (x - 5, y - 60, 10, 60))
    flower_center = (x, y - 85)
    petal_radius = 18
    num_petals = 6
    for i in range(30):
        t = i / 29
        r = int(255 * (1 - t) + TREE_LEAF_COLOR[0] * t)
        g = int(207 * (1 - t) + TREE_LEAF_COLOR[1] * t)
        b = int(247 * (1 - t) + TREE_LEAF_COLOR[2] * t)
        color = (r, g, b)
        for p in range(num_petals):
            angle = 2 * math.pi * p / num_petals
            px = int(flower_center[0] + math.cos(angle) * (petal_radius - i // 2))
            py = int(flower_center[1] + math.sin(angle) * (petal_radius - i // 2))
            pygame.draw.circle(screen, color, (px, py), 12 - i // 3)
    pygame.draw.circle(screen, FLOWER_CENTER_COLOR, flower_center, 7)

def draw_flower(x, y):
    pygame.draw.circle(screen, FLOWER_PETAL_COLOR, (x, y), 6)
    pygame.draw.circle(screen, FLOWER_CENTER_COLOR, (x, y), 3)

def draw_moon():
    pygame.draw.circle(screen, (255, 255, 224), (WIDTH - 90, 90), 40)
    pygame.draw.circle(screen, SKY_TOP, (WIDTH - 70, 90), 40)

def draw_cloud(x, y):
    for dx in (0, 20, 40): pygame.draw.circle(screen, CLOUD_COLOR, (x + dx, y + (dx % 2) * 10), 20)

def draw_landing_strip():
    pygame.draw.rect(screen, (60, 60, 60), (0, GROUND_LEVEL + 10, WIDTH, 10))
    for i in range(0, WIDTH, 80):
        pygame.draw.rect(screen, (255, 255, 255), (i, GROUND_LEVEL + 13, 40, 4))

def draw_game_over():
    text = font.render("GAME OVER - Press R to Restart", True, (255, 0, 0))
    rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text, rect)

def draw_speedometer():
    speed_text = font.render(f"Speed: {int(plane.speed)}", True, (255, 255, 255))
    screen.blit(speed_text, (10, 10))

def draw_points():
    points_text = font.render(f"Points: {plane.points}", True, (255, 255, 255))
    screen.blit(points_text, (WIDTH - 150, 10))

def draw_title_screen():
    screen.fill((0, 0, 0))
    title = font.render("THESE BIRDZ ARE PLANE CRAZY", True, (242, 99, 130))
    prompt = font.render("Press ENTER to Begin", True, (166, 232, 162))
    screen.blit(title, title.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 40)))
    screen.blit(prompt, prompt.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 20)))
    pygame.display.flip()

def draw_stars():
    for _ in range(100):
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT // 2)
        pygame.draw.circle(screen, (255, 255, 255), (x, y), random.randint(1, 3))

def check_bird_collisions():
    for bird in birds:
        if abs(bird.x - WIDTH // 2) < 20 and abs(bird.y - plane.y) < 20:
            plane.points += 1
            plane.color = (255, 0, 0)
            bird.x = random.randint(WIDTH, WIDTH + 300)
            bird.y = random.randint(50, 200)

def draw_scene():
    draw_gradient_sky()
    draw_moon()
    pygame.draw.rect(screen, SKY_TOP, (0, 0, WIDTH, HEIGHT - GRASS_HEIGHT))
    draw_stars()
    draw_cloud(200 - plane.x % WIDTH, 100)
    draw_cloud(500 - plane.x % WIDTH, 80)
    draw_cloud(800 - plane.x % WIDTH, 120)
    pygame.draw.rect(screen, GRASS_COLOR, (0, GRASS_TOP, WIDTH, GRASS_HEIGHT))
    draw_landing_strip()
    for x in range(-plane.x % TREE_SPACING, WIDTH, TREE_SPACING):
        draw_tree(x, GRASS_TOP)
    for x in range(0, WIDTH, 60):
        draw_flower(x + 20, GRASS_TOP + 35)
    for bird in birds:
        bird.draw()
    plane.draw()
    draw_speedometer()
    draw_points()
    if plane.state == "crashed":
        draw_game_over()
    pygame.display.flip()
    clock.tick(60)

def reset_game():
    global plane, birds
    plane = Plane(0, CRUISING_ALTITUDE)
    birds = [Bird(random.randint(WIDTH, WIDTH + 300), random.randint(50, 200)) for _ in range(3)]

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

        if game_state == STATE_TITLE:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                game_state = STATE_RUNNING
                reset_game()

        elif game_state == STATE_RUNNING:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    plane.vertical_velocity = -2
                elif event.key == pygame.K_DOWN:
                    plane.vertical_velocity = 2
                elif event.key == pygame.K_SPACE:
                    plane.speed = min(MAX_PLANE_SPEED, plane.speed + 1)
                elif event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                    plane.speed = max(1, plane.speed - 1)

        elif game_state == STATE_GAME_OVER:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                game_state = STATE_RUNNING
                reset_game()

    if game_state == STATE_RUNNING:
        if plane.state != "crashed":
            for bird in birds:
                bird.move()
            plane.move()
            check_bird_collisions()
            if plane.state == "crashed":
                game_state = STATE_GAME_OVER
        draw_scene()

    elif game_state == STATE_TITLE:
        draw_title_screen()

    elif game_state == STATE_GAME_OVER:
        draw_scene()

    birds[:] = [b for b in birds if b.x > -40]
    for bird in birds:
        bird.move()
        if bird.x < -20:
            bird.x = random.randint(WIDTH, WIDTH + 300)
            bird.y = random.randint(50, 200)
