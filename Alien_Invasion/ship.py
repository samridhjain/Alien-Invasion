import pygame

class Ship():
    
    def __init__(self, ai_settings, screen):
        """Initialize the ship and set its starting position."""
        self.screen = screen
        self.ai_settings = ai_settings

        #Load the ship image and get its rect.
        self.image = pygame.image.load('/Users/samridhjain/Desktop/Python/Alien_Invasion/images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #Store a decimal value for the ship's center.
        self.center = float(self.rect.centerx)

        #movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update ship's position based on the movement flag."""
        #Update the ship's center value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= self.ai_settings.ship_speed_factor


    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)