import pygame.font



class Button:

    def __init__(self,screen,msg):

        self.screen=screen

        self.screen_rect=screen.get_rect()



        self.width,self.height =1200,500

        self.button_color=(0,0,0)

        self.text_color=(255,255,255)

        self.font = pygame.font.SysFont(None,48)



        self.rect = pygame.Rect(0,0,self.width, self.height)

        self.rect.center=self.screen_rect.center

        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)

        self.msg_image_rect = self.msg_image.get_rect()

        self.msg_image_2 = self.font.render("Click to Play", True, self.text_color, self.button_color)
        self.msg_image_rect_2 = self.msg_image_2.get_rect()

        self.prep_msg()

    def prep_msg(self):

        self.msg_image_rect.center=self.rect.center
        self.msg_image_rect_2.center=self.screen_rect.center
        self.msg_image_rect_2.bottom=self.screen_rect.bottom- 190


    def draw_button(self):

        self.screen.fill(self.button_color,self.rect)

        self.screen.blit(self.msg_image, self.msg_image_rect)
        self.screen.blit(self.msg_image_2, self.msg_image_rect_2)