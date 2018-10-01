
import pygame

import game_functions as gf
from settings import Settings
from ball import Ball
from player import Player
from enemy import Enemy
from button import Button
from stats import Stats
from scoreboard import Scoreboard

def run_game():
    pygame.init()
    pygame.display.set_caption('4-Sided Pong')
    settings=Settings()
    screen=pygame.display.set_mode((settings.screenwidth, settings.screenheight))
    ball=Ball(screen)
    player = Player(screen,settings)
    enemy= Enemy(screen,settings,ball)
    play_button=Button(screen,"Pong AI-No Walls: ")
    stats=Stats()
    scoreboard=Scoreboard(screen,settings,stats)



    #ball.start_game()
    while True:
        gf.check_key_events(ball,player,play_button,stats,scoreboard)

        if stats.game_active:

            player.update()
            enemy.update()
            gf.update_ball(screen,settings,ball,player,enemy,stats,scoreboard)
        gf.update_screen(screen,settings,ball,player,enemy,play_button,stats,scoreboard)

run_game()