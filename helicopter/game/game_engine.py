"""GameEngine: owns the helicopter, obstacles, and game state."""

import random

import pygame

from game.helicopter import Helicopter
from game.obstacle import Obstacle
from game.renderer import WIDTH, HEIGHT

SPAWN_INTERVAL_FRAMES = 90
GAP_HEIGHT = 150
WALL_WIDTH = 60
SCROLL_SPEED = 3


class GameEngine:
    def __init__(self):
        self.reset()

    def reset(self):
        self.helicopter = Helicopter(x=100, y=HEIGHT / 2)
        self.obstacles = []
        self.frames_until_spawn = 0
        self.game_over = False
        self.distance = 0
        self.shield_active = False
        self.ignored_obstacle = None

    def _spawn_obstacle(self):
        margin = 60
        gap_y = random.randint(margin + GAP_HEIGHT // 2, HEIGHT - margin - GAP_HEIGHT // 2)
        self.obstacles.append(Obstacle(
            x=WIDTH, gap_y=gap_y, gap_height=GAP_HEIGHT,
            wall_width=WALL_WIDTH, screen_height=HEIGHT, speed=SCROLL_SPEED,
        ))

    def handle_input(self, keys_pressed):
        if not self.game_over:
            self.helicopter.handle_input(keys_pressed)

    def handle_keydown(self, key):
        if self.game_over and key == pygame.K_r:
            self.reset()
        elif not self.game_over and key == pygame.K_SPACE:
            self.shield_active = True

    def update(self):
        if self.game_over:
            return

        self.helicopter.update(HEIGHT)
        self.distance += SCROLL_SPEED

        self.frames_until_spawn -= 1
        if self.frames_until_spawn <= 0:
            self._spawn_obstacle()
            self.frames_until_spawn = SPAWN_INTERVAL_FRAMES

        for obstacle in self.obstacles:
            obstacle.update()

        self._check_collisions()

        self.obstacles = [o for o in self.obstacles if not o.is_off_screen()]
        if self.ignored_obstacle not in self.obstacles:
            self.ignored_obstacle = None

    def _check_collisions(self):
        helicopter_rect = self.helicopter.get_rect()

        for obstacle in self.obstacles:
            colliding = (
                helicopter_rect.colliderect(obstacle.get_top_rect())
                or helicopter_rect.colliderect(obstacle.get_bottom_rect())
            )

            if obstacle is self.ignored_obstacle:
                if not colliding:
                    self.ignored_obstacle = None
                continue

            if colliding:
                if self.shield_active:
                    self.shield_active = False
                    self.ignored_obstacle = obstacle
                else:
                    self.game_over = True
                break

    def draw(self, surface, font):
        from game import renderer
        renderer.draw_scene(surface, self.helicopter, self.obstacles)
        renderer.draw_text(
            surface, font, f"Distance: {int(self.distance)}", (10, 10)
        )
        if self.shield_active:
            renderer.draw_shield(surface, self.helicopter)
            renderer.draw_text(surface, font, "Shield: ON", (10, 40))
        else:
            renderer.draw_text(
                surface, font, "Shield: OFF (SPACE)", (10, 40)
            )

        if self.game_over:
            renderer.draw_banner(surface, font, "GAME OVER")
            renderer.draw_text(
                surface,
                font,
                f"Final distance: {int(self.distance)}",
                (WIDTH // 2 - 100, HEIGHT // 2 + 35),
            )
            renderer.draw_text(
                surface,
                font,
                "Press R to restart",
                (WIDTH // 2 - 100, HEIGHT // 2 + 65),
            )
