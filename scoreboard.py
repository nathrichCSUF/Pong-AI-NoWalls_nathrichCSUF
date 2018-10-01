import pygame.font


class Scoreboard:
    def __init__(self,screen,settings,stats):
        self.screen=screen
        self.screen_rect=screen.get_rect()
        self.settings=settings
        self.stats=stats

        self.player_textcolor=(0,0,255)
        self.enemy_textcolor=(255,0,0)
        self.font = pygame.font.SysFont(None, 48)

        player_str = "Player " + str(self.stats.player_score) + "/" + str(self.stats.max_score)
        enemy_str = "Enemy " + str(self.stats.enemy_score) + "/" + str(self.stats.max_score)

        self.player_score_image = self.font.render(player_str, True, self.player_textcolor,

                                                   self.settings.color_bg)
        self.enemy_score_image = self.font.render(enemy_str, True, self.enemy_textcolor,

                                                  self.settings.color_bg)

        self.player_rect = self.player_score_image.get_rect()
        self.enemy_rect = self.enemy_score_image.get_rect()
        self.prep_score()

    def prep_score(self):

        self.enemy_rect.left = self.settings.screenwidth/2 + 20

        self.enemy_rect.top = 20

        self.player_rect.right=self.settings.screenwidth/2  - 20

        self.player_rect.top = 20

    def show_score(self):
        self.screen.blit(self.player_score_image, self.player_rect)
        self.screen.blit(self.enemy_score_image,self.enemy_rect)
