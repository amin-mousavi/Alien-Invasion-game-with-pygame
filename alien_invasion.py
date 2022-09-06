import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet


class AlienInvasion:
    """overall class to manage game assets and behavior."""

    def __init__(self) -> None:
        """Initializing the game, and create game resource"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )

        #for full screen mode
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """start the main loop for the game."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()

            # make the most recently drawn screen visible
            pygame.display.flip()

    def _check_events(self):
        # watch for keyboard and mouse events.
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
               
    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_q:
            sys.exit()
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        # if event.key == pygame.K_DOWN:
        #     self.ship.moving_down = True
        # if event.key == pygame.K_UP:
        #     self.ship.moving_up = True

    def _check_keyup_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        # if event.key == pygame.K_DOWN:
        #     self.ship.moving_down = False
        # if event.key == pygame.K_UP:
        #     self.ship.moving_up = False

    def _fire_bullet(self):
        """Create a new bullet and add it to bullet group"""
        if len(self.bullets) < self.settings.allowed_bullet:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_screen(self):
        # redraw the screen during each pass through the loop
        self.screen.fill(self.settings.bg_color)            
        self.ship.blitem()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

    def _update_bullets(self):
        """Update position of bullets and get rid from old bullets."""
        # Update bullets position
        self.bullets.update()
        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        # print(len(self.bullets))

if __name__ == '__main__':
    # make a game instance and run the game.
    ai = AlienInvasion()
    ai.run_game()
