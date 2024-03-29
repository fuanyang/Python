import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """ a class to represent a single alien in the fleet """

    def __init__(self, ai_settings, screen):
        """ initialize the alien and set its starting position """
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        # load alien image and get its rect attribute
        self.image = pygame.image.load(r"C:\Users\soda0\OneDrive\Documents\GitHub\msitm6341-yangf\alien_invasion\images\alien.png").convert_alpha()
        self.rect = self.image.get_rect()
        # start each new alien near the top left of the screen
        self.rect.x = self.rect.width 
        self.rect.y = self.rect.height 
        # store the alien's exact position
        self.x= float(self.rect.x)
    
    def blitme(self):
        """ draw the alien at its current location """
        self.screen.blit(self.image, self.rect)

    def update(self):
        """ move the alien right or left"""
        self.x += (self.ai_settings.alien_speed_factor*self.ai_settings.fleet_direction)
        self.rect.x= self.x

    
    def check_edges(self):
        """ return true if alien is at edge of screen """
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True