import sys
import pygame

#############################KeyEvents###################################################
def check_key_events(ball,player,play_button,stats,scoreboard):
    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            sys.exit()

        elif event.type == pygame.KEYDOWN:

            check_keydown(event,player)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event,player)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            match_start( ball, play_button, stats,scoreboard, mouse_x, mouse_y)



def check_keydown(event,player,):
    if event.key == pygame.K_RIGHT:

        player.movingright = True

    elif event.key == pygame.K_LEFT:

        player.movingleft = True

    elif event.key== pygame.K_UP:

        player.movingup=True

    elif event.key== pygame.K_DOWN:

        player.movingdown=True


    elif event.key == pygame.K_q:

        sys.exit()
def match_start(ball,play_button,stats,scoreboard,mouse_x,mouse_y):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)

    if button_clicked and not stats.game_active:

        stats.reset_stats()
        scoreboard.prep_score()

        stats.game_active = True
        ball.ball_reset()
        ball.start_game()





def check_keyup_events(event,player):
    if event.key == pygame.K_RIGHT:

        player.movingright = False

    elif event.key == pygame.K_LEFT:

        player.movingleft = False

    elif event.key == pygame.K_UP:

        player.movingup = False

    elif event.key == pygame.K_DOWN:

        player.movingdown = False


#########################Updates################################################
def update_ball(screen,settings,ball,player,enemy,stats,scoreboard):
    ball.update()
    collision_check(ball,player,enemy)
    keep_score(screen,settings,ball,stats,scoreboard)

def keep_score(screen,settings,ball,stats,scoreboard):
    screen_rect=screen.get_rect()

    #Player scores
    if ball.rect.right >= settings.screenwidth/2:
        if ball.rect.right >= screen_rect.right:
            stats.player_score+=1

        if ball.rect.top > screen_rect.top:
            stats.player_score+=1

        if ball.rect.bottom < screen_rect.bottom:
            stats.player_score+=1

    elif ball.rect.left < settings.screenwidth/2:
        if ball.rect.left< screen_rect.left:
            stats.enemy_score+=1

        if ball.rect.top < screen_rect.top:
            stats.enemy_score+=1
            ball.start_game()
        if ball.rect.bottom<screen_rect.bottom:
            stats.enemy_score+=1

    scoreboard.show_score()
def collision_check(ball,player,enemy):
    hit=pygame.mixer.Sound("hit.wav")
    #Update when player hits
    if ball.rect.colliderect(player.main_paddle):
        ball.x_velocity*= -1.2
        ball.rect.centerx += ball.x_velocity
        ball.rect.centery += ball.x_velocity/2
        hit.play()
    if ball.rect.colliderect(player.top_paddle):
        ball.y_velocity *=-1
        ball.rect.centery += ball.y_velocity
        hit.play()
    if ball.rect.colliderect(player.bottom_paddle):
        ball.y_velocity *=-1
        ball.rect.centery += ball.y_velocity
        hit.play()

    #Update when enemy hits
    if ball.rect.colliderect(enemy.main_paddle):
        ball.x_velocity*= -1.2
        ball.rect.centerx += ball.x_velocity
        ball.rect.centery += ball.x_velocity/2
        hit.play()
    if ball.rect.colliderect(enemy.top_paddle):
        ball.y_velocity *=-1
        ball.rect.centery += ball.y_velocity
        hit.play()
    if ball.rect.colliderect(enemy.bottom_paddle):
        ball.y_velocity *=-1
        ball.rect.centery += ball.y_velocity
        hit.play()
        

def update_screen(screen,settings,ball,player,enemy,play_button,stats,scoreboard):
    screen.fill(settings.color_bg)
    player.drawmidfield()
    player.drawplayer()
    enemy.drawplayer()
    ball.blit_ball()
    scoreboard.show_score()

    if not stats.game_active:
        play_button.draw_button()
    pygame.display.flip()