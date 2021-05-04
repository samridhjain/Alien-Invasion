import sys #module to exit the game when quitting
import pygame #this contains the functionality to create  the game
from pygame.sprite import Group
from settings import Settings 
from ship import Ship
import games_function as gf
from alien import Alien

def run_game():
    #Initialize game and create a screen object. initialize settings()
    pygame.init()
    #screen object is called a surface
    ai_settings = Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height)) 
    #graphical elements are drawn; (1200,800) is a tuple 
    pygame.display.set_caption("Alien Shooter")

    #Make a ship, a group of bullets, and a group of aliens.
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens= Group()
    #NOT OPENING ALIEN IMAGE!

    #Create the fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)

    #Start the main loop for the game.
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)
    
run_game()


# make the aliens move right, pg 276 Making the fleet move
